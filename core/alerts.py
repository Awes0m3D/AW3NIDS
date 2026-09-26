from PySide6.QtCore import QObject, Signal
from datetime import datetime
from dataclasses import dataclass

class AlertManager(QObject):

    alert_created = Signal(dict)

    def __init__(self):
        super().__init__()

    def create_alert(self, alert):
        
            formatted_alert = {
                "time": alert.get("time", datetime.now().strftime("%H:%M:%S")),
                "threat": alert.get("threat", "Unknown"),
                "source_ip": alert.get("source_ip", "-"),
                "severity": alert.get("severity", "Medium"),
                "details": alert.get("details", ""),
                "status": "Active"
            }
            print("AlertManager received:", alert)

            self.alert_created.emit(formatted_alert)