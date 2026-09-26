from collections import defaultdict
from datetime import datetime, timedelta

from scapy.layers.inet import IP, TCP


class PortScanDetector:
    """
    Detects TCP port scans by tracking the number of unique
    destination ports contacted by each source IP within
    a configurable time window.
    """

    def __init__(self,config):

        # src_ip -> {"ports": set(), "first_seen": datetime}
        self.config = config 
        self.scans = defaultdict(
            lambda: {
                "ports": set(),
                "first_seen": datetime.now()
            }
        )

        # Cooldown to avoid alert spam
        self.last_alert = {}

        self.threshold = self.config.get("port_scan_threshold", 20)         # ports
        self.window =  self.config.get("port_scan_window", 5)           # seconds
        self.cooldown = self.config.get("alert_cooldown", 30)  # seconds

    def inspect(self, packet):

        if not packet.haslayer(IP):
            return None

        if not packet.haslayer(TCP):
            return None

        src = packet[IP].src
        dst_port = packet[TCP].dport

        flags = packet[TCP].flags

        # Only count SYN packets without ACK
        if not (flags & 0x02):
            return None

        if flags & 0x10:
            return None

        print(f"{src} -> {dst_port}")

        now = datetime.now()

        record = self.scans[src]

        # Reset if outside the time window
        if (now - record["first_seen"]).total_seconds() > self.window:

            record["ports"].clear()
            record["first_seen"] = now

        record["ports"].add(dst_port)
        print("Ports:", record["ports"])
        print("Count:", len(record["ports"]))

        ports_seen = len(record["ports"])

        if ports_seen < self.threshold:
            return None

        # Cooldown
        if src in self.last_alert:

            if (now - self.last_alert[src]).total_seconds() < self.cooldown:
                return None

        self.last_alert[src] = now
        
        # Reset after alert
        self.scans[src]["ports"].clear()
        self.scans[src]["first_seen"] = now

        severity = self.calculate_severity(ports_seen)
        
        print("=" * 50)
        print("PORT SCAN DETECTED")
        print(f"Source: {src}")
        print(f"Ports: {ports_seen}")
        print(f"Severity: {severity}")
        print("=" * 50)
        
        return {
            "time": now.strftime("%H:%M:%S"),
            "threat": "Port Scan",
            "source_ip": src,
            "severity": severity,
            "details": f"{ports_seen} unique ports in {self.window} seconds",
            "status": "Active"  
        }

    def calculate_severity(self, ports):

        if ports > 50:
            return "Critical"

        elif ports > 20:
            return "High"

        return "Medium"