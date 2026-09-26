from PySide6.QtCore import QObject, Signal
from scapy.all import AsyncSniffer, conf


class PacketCapture(QObject):

    packet_received = Signal(object)
    packet_count_changed = Signal(int)
    status_changed = Signal(str)
    packet_processed = Signal(object)

    def __init__(self):
        super().__init__()

        self.packet_count = 0
        self.sniffer = None
        self.running = False

    def get_interfaces(self):
        return list(conf.ifaces.values())

    def process_packet(self, packet):
        print(packet.summary())

        self.packet_count += 1
        print("Packet Count:", self.packet_count)

        self.packet_received.emit(packet)
        self.packet_count_changed.emit(self.packet_count)

        self.packet_processed.emit(packet)



    def start_capture(self, interface):

        print("Starting capture on:", interface)
        print(type(interface), interface) 
        if self.running:
            return

        self.packet_count = 0
        self.running = True

        self.sniffer = AsyncSniffer(
            iface=interface,
            prn=self.process_packet,
            store=False
        )

        self.sniffer.start()

        self.status_changed.emit("Monitoring")


    def stop_capture(self):
    
        if not self.running:
            return

        self.running = False

        if self.sniffer is not None:

            try:
                if self.sniffer.running:
                    self.sniffer.stop()

            except Exception as e:
                print("Stop warning:", e)

            finally:
                self.sniffer = None

        self.status_changed.emit("Stopped")