from PySide6.QtCore import QObject, Signal
from detectors.port_scan import PortScanDetector
from detectors.syn_flood import SynFloodDetector


class Detector(QObject):

    alert_detected = Signal(dict)

    def __init__(self,config):
        super().__init__()

        self.detectors = [
            PortScanDetector(config),
            SynFloodDetector(config),
        ]

    def inspect_packet(self, packet):
    
        for detector in self.detectors:

            alert = detector.inspect(packet)

            if alert:
                self.alert_detected.emit(alert)
                return alert

        return None