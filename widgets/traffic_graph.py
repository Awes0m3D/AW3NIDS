import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout


class TrafficGraph(QWidget):

    def __init__(self, graph_type="traffic"):
        super().__init__()

        self.graph_type = graph_type

        layout = QVBoxLayout(self)

        self.plot = pg.PlotWidget()

        layout.addWidget(self.plot)

        # Graph title and labels
        if self.graph_type == "threat":
            self.plot.setTitle("Threat Activity")
            self.plot.setLabel("left", "Threats / Second")
        else:
            self.plot.setTitle("Network Traffic")
            self.plot.setLabel("left", "Packets / Second")

        self.plot.setLabel("bottom", "Time")

        self.plot.showGrid(x=True, y=True)

        # Network traffic data
        self.x = list(range(60))
        self.y = [0] * 60

        self.curve = self.plot.plot(self.x, self.y)

        # Threat activity data
        self.threat_count = 0
        self.threat_history = []

    # ---------------------------------
    # Threat Activity
    # ---------------------------------

    def add_threat(self):
        self.threat_count += 1

        print("THREAT GRAPH RECEIVED:", self.threat_count)

    def update_threat_graph(self):
        print(">>> THREAT GRAPH UPDATE:")

        self.threat_history.append(self.threat_count)

        # Reset for the next second
        self.threat_count = 0

        if len(self.threat_history) > 60:
            self.threat_history.pop(0)

        x = list(range(len(self.threat_history)))

        self.curve.setData(
            x,
            self.threat_history
        )

    # ---------------------------------
    # Network Traffic
    # ---------------------------------

    def update_graph(self, packets):

        self.y.append(packets)
        self.y.pop(0)

        self.curve.setData(
            self.x,
            self.y
        )