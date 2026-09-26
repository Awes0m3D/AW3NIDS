from collections import Counter
from datetime import datetime



class Analytics:

    def __init__(self):

        self.start_time = datetime.now()

        self.total_packets = 0
        self.total_alerts = 0

        self.protocols = Counter()
        self.threats = Counter()
        self.sources = Counter()
        self.active_hosts = set()


    # ----------------------------
    # Packet Statistics
    # ----------------------------

    def add_packet(self, packet, protocol):

        self.total_packets += 1

        src = packet["src"]

        self.protocols[protocol] += 1
        self.sources[src] += 1

        self.active_hosts.add(src)

    # ----------------------------
    # Alert Statistics
    # ----------------------------

    def add_alert(self, alert):
        
        print("ANALYTICS ALERT:", alert)

        self.total_alerts += 1
        self.threats[alert["threat"]] += 1

    # ----------------------------
    # Dashboard Values
    # ----------------------------

    def get_total_packets(self):
        return self.total_packets

    def get_total_alerts(self):
        return self.total_alerts

    def get_active_hosts(self):
        return len(self.active_hosts)

    # ----------------------------
    # Chart Data
    # ----------------------------

    def get_protocol_stats(self):
        return dict(self.protocols)

    def get_threat_stats(self):
        return dict(self.threats)

    def get_top_sources(self, limit=5):

        return dict(
            self.sources.most_common(limit)
        )