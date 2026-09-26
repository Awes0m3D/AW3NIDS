import sqlite3
from pathlib import Path


class DatabaseManager:

    def __init__(self):

        db_path = Path(__file__).parent / "aw3nids.db"

        self.connection = sqlite3.connect(db_path)

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS alerts(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            time TEXT,

            threat TEXT,

            source_ip TEXT,

            severity TEXT,

            status TEXT,

            details TEXT

        )

        """)

        self.connection.commit()

    def commit(self):

        self.connection.commit()

    def close(self):

        self.connection.close()