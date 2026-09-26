from collections import defaultdict
from datetime import datetime
from scapy.layers.inet import IP, TCP


class SynFloodDetector:

    def __init__(self, config):
        
        self.config = config
        self.sources = defaultdict(
            lambda: {
                "count": 0,
                "ports": set(),
                "first_seen": datetime.now()
            }
        )

        self.last_alert = {}

        # Configuration
        self.threshold = self.config.get("syn_flood_threshold", 20)     # SYN packets
        self.window = self.config.get("syn_window",5)         # seconds
        self.cooldown = self.config.get("alert_cooldown", 30)        # seconds

    def inspect(self, packet):
    
        print("----- NEW PACKET -----")

        if not packet.haslayer(IP):
            print("No IP")
            return None

        print("Has IP")

        if not packet.haslayer(TCP):
            print("No TCP")
            return None

        print("Has TCP")
        
        src = packet[IP].src
        flags = packet[TCP].flags

        print("=" * 40)
        print("SRC :", packet[IP].src)
        print("DST :", packet[IP].dst)
        print("SPORT :", packet[TCP].sport)
        print("DPORT :", packet[TCP].dport)
        print("FLAGS :", flags)
        print("=" * 40)

        if not (flags & 0x02):
            print("Rejected: Not a SYN")
            return None

        if flags & 0x10:
            print("Rejected: ACK flag set")
            return None

        print("Accepted SYN packet")

        now = datetime.now()

        record = self.sources[src]

        # Reset time window
        elapsed = (now - record["first_seen"]).total_seconds()

        if elapsed > self.window:
            record["count"] = 0
            record["first_seen"] = now

        record["count"] += 1
        record["ports"].add(packet[TCP].dport)

        print(f"SYN count: {record['count']}")
        print(f"Unique ports: {len(record['ports'])}")

        count = record["count"]

        unique_ports = len(record["ports"])

        if count < self.threshold:
            return None

        if unique_ports > 5:
            return None

        # Cooldown
        if src in self.last_alert:

            elapsed = (now - self.last_alert[src]).total_seconds()

            if elapsed < self.cooldown:
                return None

        self.last_alert[src] = now

        # Reset after alert
        record["count"] = 0
        record["first_seen"] = now

        severity = self.calculate_severity(count)

        print(f"SYN Flood detected from {src}")

        return {
            "time": now.strftime("%H:%M:%S"),
            "threat": "SYN Flood",
            "source_ip": src,
            "severity": severity,
            "details": f"{count} SYN packets in {self.window} seconds",
            "status": "Active"
        }

    def calculate_severity(self, count):

        if count >= 500:
            return "Critical"

        elif count >= 250:
            return "High"

        return "Medium"