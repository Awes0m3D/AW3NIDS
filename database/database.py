
import sqlite3
import sys
from pathlib import Path
from datetime import datetime


class DatabaseManager:

    def __init__(self):
        if getattr(sys, "frozen", False):
            # Packaged application: store the database
            # in a writable directory beside the executable
            app_dir = \
    Path(sys.executable).resolve().parent
        else:
        # Normal Python execution
            app_dir = Path(__file__).resolve().parent

        app_dir.mkdir(parents=True, exist_ok=True)
        db_path = app_dir / "aw3nids.db"

        self.connection = sqlite3.connect(str(db_path))
        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        # Alerts table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TEXT,
                threat TEXT,
                source_ip TEXT,
                severity TEXT,
                status TEXT,
                details TEXT
            )
        """)

        # Add new columns safely to existing databases.
        existing_columns = {
            row["name"]
            for row in self.cursor.execute(
                "PRAGMA table_info(alerts)"
            ).fetchall()
        }

        new_columns = {
            "destination_ip": "TEXT",
            "protocol": "TEXT",
        }

        for column, data_type in new_columns.items():
            if column not in existing_columns:
                self.cursor.execute(
                    f"ALTER TABLE alerts ADD COLUMN {column} {data_type}"
                )

        # System and activity logs table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time TEXT,
                event TEXT,
                level TEXT,
                details TEXT,
                source_ip TEXT
            )
        """)

        self.connection.commit()

    # ---------------- ALERTS ----------------

    def save_alert(self, alert):
        """Save an alert dictionary to the database."""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute("""
            INSERT INTO alerts (
                time, threat, source_ip, destination_ip,
                protocol, severity, status, details
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            alert.get("time") or alert.get("timestamp") or now,
            alert.get("threat", "Unknown"),
            alert.get("source_ip") or alert.get("source", "-"),
            alert.get("destination_ip") or alert.get("destination", "-"),
            alert.get("protocol", "-"),
            alert.get("severity", "Medium"),
            alert.get("status", "Active"),
            alert.get("details", "")
        ))

        self.connection.commit()

    def get_alerts(self, limit=None):
        """Retrieve saved alerts, newest first."""
        query = "SELECT * FROM alerts ORDER BY id DESC"
        params = ()

        if limit is not None:
            query += " LIMIT ?"
            params = (max(0, int(limit)),)

        return self.cursor.execute(query, params).fetchall()

    def clear_alerts(self):
        """Delete all saved alerts."""
        self.cursor.execute("DELETE FROM alerts")
        self.connection.commit()

    # ---------------- LOGS ----------------

    def save_log(
        self,
        event,
        level="INFO",
        details="",
        source_ip="-"
    ):
        """Save a system activity or detection log."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.cursor.execute("""
            INSERT INTO logs (
                time, event, level, details, source_ip
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            timestamp,
            event,
            level,
            details,
            source_ip
        ))

        self.connection.commit()

    def get_logs(self, limit=None):
        """Retrieve saved logs, newest first."""
        query = "SELECT * FROM logs ORDER BY id DESC"
        params = ()

        if limit is not None:
            query += " LIMIT ?"
            params = (max(0, int(limit)),)

        return self.cursor.execute(query, params).fetchall()

    def clear_logs(self):
        """Delete all saved logs."""
        self.cursor.execute("DELETE FROM logs")
        self.connection.commit()

    # ---------------- CONNECTION ----------------

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()