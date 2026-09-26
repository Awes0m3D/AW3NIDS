from database.database import DatabaseManager


class AlertRepository:

    def __init__(self, database):
        self.db = database
    

    def save(self, alert):
    
        self.db.cursor.execute("""

            INSERT INTO alerts(

                time,

                threat,

                source_ip,

                severity,

                status,

                details

            )

            VALUES(?,?,?,?,?,?)

        """, (

            alert["time"],

            alert["threat"],

            alert["source_ip"],

            alert["severity"],

            alert["status"],

            alert["details"]

        ))

        self.db.commit()
    
    
    def all(self):
        
        self.db.cursor.execute("""

            SELECT
                time,
                threat,
                source_ip,
                severity,
                status,
                details

            FROM alerts

            ORDER BY id DESC

        """)

        rows = self.db.cursor.fetchall()

        alerts = []

        for row in rows:

            alerts.append({

                "time": row[0],
                "threat": row[1],
                "source_ip": row[2],
                "severity": row[3],
                "status": row[4],
                "details": row[5]

            })

        return alerts
    

    def delete(self, alert_id):
    
        self.db.cursor.execute(

            "DELETE FROM alerts WHERE id=?",

            (alert_id,)

        )

        self.db.commit()


    def clear(self):
    
        self.db.cursor.execute(

            "DELETE FROM alerts"

        )

        self.db.commit()