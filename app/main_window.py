import os
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from PySide6.QtCore import Qt, QTimer
from app.ui_main_window import Ui_MainWindow
from core.capture import PacketCapture
from datetime import datetime
import csv
import logging
from scapy.layers.inet import IP, TCP, UDP, ICMP
from core.alerts import AlertManager
from core.detector import Detector
from PySide6.QtGui import QColor
from widgets.traffic_graph import TrafficGraph
from PySide6.QtWidgets import QTableWidget,QHeaderView,QAbstractItemView
from simulator.attack_simulator import AttackSimulator
from core.analytics import Analytics
from app.about_dialog import AboutDialog
from database.alerts import AlertRepository
from settings.config import ConfigManager
from database.database import DatabaseManager
from core.firewall import FirewallManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_logging()
        self.config = ConfigManager()
        print(type(self.config))
        print(hasattr(self.config, "get"))
        print(dir(self.config))
        self.database = DatabaseManager()
        self.analytics = Analytics()
        self.alert_repo = AlertRepository(self.database)

        self.traffic_graph = TrafficGraph("threat")
        self.ui.LayoutGraphAnalytics.layout().addWidget(self.traffic_graph)
        #self.ui.verticalLayout_55.layout().addWidget(self.traffic_graph)

        self.alerts = AlertManager()
        self.detector = Detector(self.config)

# Alerts Page
        self.firewall_manager = FirewallManager()
        self.ui.btnBlockIP.clicked.connect(self.block_ip)
        self.ui.btnUnblockIP.clicked.connect(self.unblock_ip)

        self.detector.alert_detected.connect(
            self.alerts.create_alert
        )
        self.alerts.alert_created.connect(
            self.analytics.add_alert
        )

        self.load_settings()
        self.load_saved_alerts()

        print("Alert columns:", self.ui.tableRecentAlerts.columnCount())

        # Store recently captured packets for the Packet Details panel
        self.packet_history = []

        # Used for the traffic graph
        self.packets_this_second = 0

        # Create the packet capture engine
        self.capture = PacketCapture()

        # Connect alert signals

        self.alerts.alert_created.connect(
            self.display_alert
        )

        self.alerts.alert_created.connect(
            self.update_alerts_page
        )

        self.alerts.alert_created.connect(
            self.record_alert_analytics
        )

        self.alerts.alert_created.connect(
            self.update_threat_graph
        )

        # Connect signals from capture engine
        self.capture.packet_count_changed.connect(
            self.update_packet_count
        )

        self.capture.status_changed.connect(
            self.update_status
        )
        
        self.capture.packet_received.connect(
            self.display_packet
        )

        self.ui.btnStartCapture.clicked.connect(
            self.start_monitoring
        )

        self.ui.btnSaveSettings.clicked.connect(
            self.save_settings
        )

        self.ui.tableLivePackets_2.itemSelectionChanged.connect(
            self.show_packet_details
        )

        table = self.ui.tableLivePackets_2

        table.setColumnCount(5)
        table.setHorizontalHeaderLabels([
            "Time",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Length"
        ])

        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.setAlternatingRowColors(True)
        table.setSortingEnabled(False)
        table.horizontalHeader().setStretchLastSection(True)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        header = table.horizontalHeader()

        # Resize behaviour
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)   # Time
        header.setSectionResizeMode(1, QHeaderView.Stretch)            # Source
        header.setSectionResizeMode(2, QHeaderView.Stretch)            # Destination
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)   # Protocol
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)   # Length

        # Appearance
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        table.setSelectionMode(QAbstractItemView.SingleSelection)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setShowGrid(False)

        # Hide row numbers
        table.verticalHeader().setVisible(False)

        # Stretch the last column
        header.setStretchLastSection(True)

        # ---------------
        # Graph
        # ---------------

        self.graph = TrafficGraph()

        self.ui.graphContainer.layout().addWidget(self.graph)
        self.packets_this_second = 0

        self.graph_timer = QTimer()

        self.graph_timer.timeout.connect(
        self.update_graph
        )

        self.graph_timer.start(1000)

        # Setup the application
        self.setup_navigation()
        self.setup_toolbar()
        self.setup_reports()
        self.setup_logs_page()

        self.load_interfaces()

        self.capture.packet_processed.connect(
            self.detector.inspect_packet
        )

        self.simulator = AttackSimulator()

        self.ui.cmbAttackType.addItems([
            "Port Scan",
            "SYN Flood"
        ])
        # connect button for simulator

        self.ui.btnRunSimulation.clicked.connect(
            self.run_simulation
        )

        self.ui.lblPacketCount.setText(
            str(self.analytics.get_total_packets())
        )

        self.ui.lblThreatCount.setText(
            str(self.analytics.get_total_alerts())
        )

        self.ui.lblHostCount.setText(
            str(self.analytics.get_active_hosts())
        )

        self.analytics_timer = QTimer()

        self.analytics_timer.timeout.connect(
            self.update_analytics_dashboard
        )

        self.analytics_timer.timeout.connect(
            self.traffic_graph.update_threat_graph
        )

        self.analytics_timer.start(1000)

    # -----------------------------------------
    # Navigation
    # -----------------------------------------
    def setup_navigation(self):
        
        self.ui.btnDashboard.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageDashboard
            )
        )
        self.ui.btnLiveCapture.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageCapture
            )
        )

        self.ui.btnAlerts.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageAlerts
            )
        )

        self.ui.btnLogs.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageLogs
            )
        )

        self.ui.btnAnalytics.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageAnalytics
            )
        )

        self.ui.btnReports.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageReports
            )
        )

        self.ui.btnSimulator.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageSimulator
            )
        )
        
        self.ui.btnDatabase.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageDatabase
            )
        )

        self.ui.btnSettings.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(
                self.ui.pageSettings
            )
        )
    
    # -----------------------------------------
    # Reports
    # -----------------------------------------
    def setup_reports(self):

        # Connect report buttons
        self.ui.btnGenerateReport.clicked.connect(
            self.generate_report
        )

        #self.ui.btnExportReport.clicked.connect(
         #   self.export_report
        #)

    # -----------------------------------------
    # Toolbar
    # -----------------------------------------

    def setup_toolbar(self):

        self.ui.actionStartMonitoring.triggered.connect(
            self.start_monitoring
        )

        self.ui.actionStopMonitoring.triggered.connect(
            self.stop_monitoring
        )

        self.ui.actionClearAlerts.triggered.connect(
            self.clear_alerts
        )

        self.ui.actionExportReport.triggered.connect(
            self.export_report
        )
        
        self.ui.btnRefreshInterfaces.clicked.connect(
            self.load_interfaces
        )
        
        self.ui.btnStopCapture.clicked.connect(
           self.stop_monitoring
        )

        self.ui.actionAbout.triggered.connect(
            self.show_about
        )

    # -----------------------------------------
    # Packet Counter
    # -----------------------------------------

    def update_packet_count(self, count):
        self.ui.lblPacketCount.setText(str(count))
    

    
    def display_packet(self, packet):

        table = self.ui.tableLivePackets_2

        if not packet.haslayer(IP):
            return

        protocol = "OTHER"

        self.analytics.add_packet(
            {
                "src": packet[IP].src
            },
            protocol
        )

        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        self.packets_this_second += 1


        row = table.rowCount()
        table.insertRow(row)

        table.setVerticalHeaderItem(
            row,
            QTableWidgetItem(str(row))
        )

        table.setItem(row, 0, QTableWidgetItem(datetime.now().strftime("%H:%M:%S")))
        table.setItem(row, 1, QTableWidgetItem(packet[IP].src))
        table.setItem(row, 2, QTableWidgetItem(packet[IP].dst))
        table.setItem(row, 3, QTableWidgetItem(protocol))
        table.setItem(row, 4, QTableWidgetItem(str(len(packet))))

        # Keep only the most recent 500 packets
        while table.rowCount() > 500:
            table.removeRow(0)

        table.scrollToBottom()

        table.setUpdatesEnabled(False)

        # Insert row and populate it

        table.setUpdatesEnabled(True)

        item = QTableWidgetItem(protocol)

        if protocol == "TCP":
            item.setForeground(QColor("blue"))

        elif protocol == "UDP":
            item.setForeground(QColor("darkgreen"))

        table.setItem(row, 3, item)

        self.packet_history.append({
            "time": datetime.now(),
            "packet": packet
        })


        print("Updating dashboard...")
        self.update_dashboard_table(packet)


    def update_dashboard_table(self, packet):
        
        if not packet.haslayer(IP):
            return

        table = self.ui.tableLivePackets

        row = table.rowCount()
        table.insertRow(row)

        protocol = "OTHER"

        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        table.setItem(row, 0, QTableWidgetItem(datetime.now().strftime("%H:%M:%S")))
        table.setItem(row, 1, QTableWidgetItem(packet[IP].src))
        table.setItem(row, 2, QTableWidgetItem(packet[IP].dst))
        table.setItem(row, 3, QTableWidgetItem(protocol))
        table.setItem(row, 4, QTableWidgetItem(str(len(packet))))

        while table.rowCount() > 10:
            table.removeRow(0)

        table.scrollToBottom()


        # Update the dashboard counter
        self.update_threat_count()


    
    def display_alert(self, alert):
                
        table = self.ui.tableRecentAlerts

        row = table.rowCount()
        table.insertRow(row)

        table.setItem(
            row, 0,
            QTableWidgetItem(alert["time"])
        )

        table.setItem(
            row, 1,
            QTableWidgetItem(alert["threat"])
        )

        table.setItem(
            row, 2,
            QTableWidgetItem(alert["source_ip"])
        )

        severity_item = QTableWidgetItem(alert["severity"])

        if alert["severity"] == "Medium":
            severity_item.setForeground(QColor("orange"))

        elif alert["severity"] == "High":
            severity_item.setForeground(QColor("red"))

        elif alert["severity"] == "Critical":
            severity_item.setForeground(QColor("darkRed"))

        table.setItem(row, 3, severity_item)

        table.setItem(
            row, 4,
            QTableWidgetItem(alert["details"])
        )

        table.setItem(
            row, 5,
            QTableWidgetItem(alert["status"])
        )

        table.scrollToBottom()

        header = self.ui.tableRecentAlerts.horizontalHeader()

        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)


        self.alert_repo.save(alert)

        # this is to record the security alert in the application log
        self.app_logger.warning(
            "Security alert | Threat: %s | Source IP: %s | Severity: %s | Details: %s",
            alert.get("threat", "Unknown"),
            alert.get("source_ip", "-"),
            alert.get("severity", "Medium"),
            alert.get("details", "")
        )

        alerts = self.alert_repo.all()
        # -----------------------------------------
    # Toolbar Functions
    # -----------------------------------------
    def start_monitoring(self):
        
            iface = self.ui.cmbInterface.currentData()

            if iface is None:
                QMessageBox.warning(
                    self,
                    "AW3NIDS",
                    "Please select a network interface."
                    )
                return

            self.capture.start_capture(iface)
            
            self.app_logger.info(
                "Packet monitoring started on interface: %s",iface
            )

            self.ui.lblNetworkStatus.setText("🟢 Monitoring")
            self.ui.lblStatusDetail.setText("🟢 Monitoring")



            QMessageBox.information(
                self,
                "AW3NIDS",
                "Monitoring Started"
            )
            self.ui.btnStartCapture.setEnabled(False)
            self.ui.btnStopCapture.setEnabled(True)
            self.ui.cmbInterface.setEnabled(False)

    
    def stop_monitoring(self):
        try:
            self.capture.stop_capture()
            self.app_logger.info("Packet monitoring stopped successfully")
            self.ui.lblNetworkStatus.setText("🔴 Not Monitoring")

        except Exception as e:
            self.app_logger.exception("Failed to stop packet monitoring")
            print("Stop error:", e)

            QMessageBox.warning(
                self,
                "AW3NIDS",
                f"Failed to stop monitoring: \n{e}"
            )
            return

        QMessageBox.information(
            self,
            "AW3NIDS",
            "Monitoring Stopped"
        )

        self.ui.btnStartCapture.setEnabled(True)
        self.ui.btnStopCapture.setEnabled(False)

        self.ui.cmbInterface.setEnabled(True)

        self.ui.lblStatusDetail.setText("🔴 Not Monitoring")


    def clear_alerts(self):
    
        self.ui.tableRecentAlerts.setRowCount(0)
        self.ui.tableLivePackets.setRowCount(0)
    
    def generate_report(self):


        try:
            alerts = self.alert_repo.all()

            table = self.ui.tabeReports

            # Clear previous report
            table.setRowCount(0)

            # Add alerts to report table
            for alert in alerts:

                row = table.rowCount()
                table.insertRow(row)

                table.setItem(
                    row,
                    0,
                    QTableWidgetItem(
                        alert.get("time", "-")
                    )
                )

                table.setItem(
                    row,
                    1,
                    QTableWidgetItem(
                        alert.get("threat", "-")
                    )
                )

                table.setItem(
                    row,
                    2,
                    QTableWidgetItem(
                        alert.get("source_ip", "-")
                    )
                )

                table.setItem(
                    row,
                    3,
                    QTableWidgetItem(
                        alert.get("severity", "-")
                    )
                )

                table.setItem(
                    row,
                    4,
                    QTableWidgetItem(
                        alert.get("status", "-")
                    )
                )

            QMessageBox.information(
                self,
                "AW3NIDS",
                f"Report generated successfully.\n\n"
                f"Total alerts: {len(alerts)}"
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Report Error",
                f"Failed to generate report:\n\n{str(e)}"
            )

    
    def generate_report(self):
    
        try:
            alerts = self.alert_repo.all()

            # Clear existing report table
            self.ui.tableReports.setRowCount(0)

            # Display alerts
            for alert in alerts:

                row = self.ui.tableReports.rowCount()
                self.ui.tableReports.insertRow(row)

                self.ui.tableReports.setItem(
                    row,
                    0,
                    QTableWidgetItem(
                        alert.get("time", "-")
                    )
                )

                self.ui.tableReports.setItem(
                    row,
                    1,
                    QTableWidgetItem(
                        alert.get("threat", "-")
                    )
                )

                self.ui.tableReports.setItem(
                    row,
                    2,
                    QTableWidgetItem(
                        alert.get("source_ip", "-")
                    )
                )

                self.ui.tableReports.setItem(
                    row,
                    3,
                    QTableWidgetItem(
                        alert.get("severity", "-")
                    )
                )

                self.ui.tableReports.setItem(
                    row,
                    4,
                    QTableWidgetItem(
                        alert.get("status", "-")
                    )
                )

            QMessageBox.information(
                self,
                "AW3NIDS",
                f"Report generated successfully.\n\n"
                f"Total alerts: {len(alerts)}"
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Report Error",
                f"Failed to generate report:\n\n{str(e)}"
            )
        
    def export_report(self):

        #QMessageBox.information(
         #   self,
          #  "AW3NIDS",
           # "Report Export Coming Soon"
       # )
    
        table = self.ui.tableReports

        if table.rowCount() == 0:
            QMessageBox.warning(
                self,
                "AW3NIDS",
                "Please generate a report first."
            ) 
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export AW3NIDS Report",
            "AW3NIDS_Report.csv",
            "CSV Files (*.csv)"
        )

        if not file_path:
            return

        try:
            with open(
                file_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                # Write column headers
                headers = []

                for column in range(table.columnCount()):
                    header = table.horizontalHeaderItem(column)

                    if header:
                        headers.append(header.text())
                    else:
                        headers.append(f"Column {column + 1}")

                writer.writerow(headers)

                # Write table data
                for row in range(table.rowCount()):

                    row_data = []

                    for column in range(table.columnCount()):

                        item = table.item(row, column)

                        if item:
                            row_data.append(item.text())
                        else:
                            row_data.append("")

                    writer.writerow(row_data)

            QMessageBox.information(
                self,
                "AW3NIDS",
                "Report exported successfully."
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Export Error",
                f"Failed to export report:\n\n{str(e)}"
            )

       
    def update_status(self, status):

        if status == "Monitoring":
            self.ui.lblNetworkStatus.setText("🟢 Monitoring")
        else:
            self.ui.lblNetworkStatus.setText("🔴 Not Monitoring")


    #---------------------------
    # Load Interface
    # -------------------------

    def load_interfaces(self):
    
        self.ui.cmbInterface.clear()
        self.ui.cmbSetInterface.clear()

        interfaces = self.capture.get_interfaces()
        

        for iface in interfaces:

            self.ui.cmbInterface.addItem(
                iface.description,
                iface
            )
            
            self.ui.cmbSetInterface.addItem(
                iface.description, iface
            )



    def record_alert_analytics(self, alert):
        self.analytics.add_alert(alert)

    def update_threat_graph(self, alert):
        self.traffic_graph.add_threat()

    def update_alerts_page(self, alert):
        table = self.ui.tableAlerts

        row = table.rowCount()
        table.insertRow(row)

        table.setItem(row, 0, QTableWidgetItem(alert.get("time", "-")))
        table.setItem(row, 1, QTableWidgetItem(alert.get("severity", "-")))
        table.setItem(row, 2, QTableWidgetItem(alert.get("threat", "-")))
        table.setItem(row, 3, QTableWidgetItem(alert.get("source_ip", "-")))
        table.setItem(row, 4, QTableWidgetItem(alert.get("destination_ip" , "-")))
        table.setItem(row, 5, QTableWidgetItem(alert.get("protocol" ,"-")))
        table.setItem(row, 6, QTableWidgetItem(alert.get("details", "")))

        self.update_alert_counters(alert)
        self.style_alert_row(row,alert)


    def update_threat_count(self):
           
            """
        Updates the threat count displayed on the dashboard.
        it currently counts the number of rows in the Recent Alerts table.
        """

            threat_count = self.ui.tableRecentAlerts.rowCount()

            self.ui.lblThreatCount.setText(str(threat_count))
        
    
    def show_packet_details(self):

        row = self.ui.tableLivePackets_2.currentRow()

        if row < 0 or row >= len(self.packet_history):
            return

        entry = self.packet_history[row]

        packet = entry["packet"]
        
        # Time
        self.ui.lblDetailTime.setText(
            entry["time"].strftime("%H:%M:%S")
        )

        # IP Information
        if packet.haslayer(IP):
            self.ui.lblDetailSrc.setText(packet[IP].src)
            self.ui.lblDetailDst.setText(packet[IP].dst)
            self.ui.lblDetailTTL.setText(str(packet[IP].ttl))
        else:
            self.ui.lblDetailSrc.setText("-")
            self.ui.lblDetailDst.setText("-")
            self.ui.lblDetailTTL.setText("-")

        # Length
        self.ui.lblDetailLength.setText(str(len(packet)))

        # TCP
        if packet.haslayer(TCP):
            self.ui.lblDetailProtocol.setText("TCP")
            self.ui.lblDetailSrcPort.setText(str(packet[TCP].sport))
            self.ui.lblDetailDstPort.setText(str(packet[TCP].dport))
            self.ui.lblDetailFlags.setText(str(packet[TCP].flags))

        # UDP
        elif packet.haslayer(UDP):
            self.ui.lblDetailProtocol.setText("UDP")
            self.ui.lblDetailSrcPort.setText(str(packet[UDP].sport))
            self.ui.lblDetailDstPort.setText(str(packet[UDP].dport))
            self.ui.lblDetailFlags.setText("N/A")

        # Other Protocols
        else:
            self.ui.lblDetailProtocol.setText("Other")
            self.ui.lblDetailSrcPort.setText("-")
            self.ui.lblDetailDstPort.setText("-")
            self.ui.lblDetailFlags.setText("-")

        
        entry = self.packet_history[row]

        packet = entry["packet"]

        self.ui.lblDetailTime.setText(
            entry["time"].strftime("%H:%M:%S")
        )


    def update_graph(self):

        self.graph.update_graph(
            self.packets_this_second
        )

        self.packets_this_second = 0

    
    def run_simulation(self):
    
        attack = self.ui.cmbAttackType.currentText()

        packets = self.ui.spinSimPacketCount.value()

        self.ui.txtSimulationLog.append(
            f"Running {attack} simulation..."
        )

        if attack == "Port Scan":

            self.simulator.port_scan(
                self.detector,
                packets
            )

        elif attack == "SYN Flood":

            self.simulator.syn_flood(
                self.detector,
                packets
            )

        self.ui.txtSimulationLog.append(
            "Simulation completed.\n"
        )
    

    def update_analytics_dashboard(self):
    
        self.ui.lblTotalPackets.setText(
            str(self.analytics.get_total_packets())
        )

        self.ui.lblTotalThreats.setText(
            str(self.analytics.get_total_alerts())
        )

        self.ui.lblActiveHosts.setText(
            str(self.analytics.get_active_hosts())
        )
        self.ui.lblHostCount.setText(
            str(self.analytics.get_active_hosts())
        )

        uptime = datetime.now() - self.analytics.start_time

        self.ui.lblUptime.setText(str(uptime).split(".")[0])

        # Attack breakdown
        threats = self.analytics.get_threat_stats()

        self.ui.lblPortScanCount.setText(
            str(threats.get("Port Scan", 0))
        )

        self.ui.lblSynFloodCount.setText(
            str(threats.get("SYN Flood", 0))
        )

        self.ui.lblIcmpFloodCount.setText(
            str(threats.get("ICMP Flood", 0))
        )

        self.ui.lblArpSpoofCount.setText(
            str(threats.get("ARP Spoof", 0))
        )

    def load_saved_alerts(self):

        table = self.ui.tableAlerts

        table.setRowCount(0)

        alerts = self.alert_repo.all()

        for alert in alerts:

            row = table.rowCount()
            table.insertRow(row)

            table.setItem(row, 0, QTableWidgetItem(alert["time"]))
            table.setItem(row, 1, QTableWidgetItem(alert["threat"]))
            table.setItem(row, 2, QTableWidgetItem(alert["source_ip"]))
            table.setItem(row, 3, QTableWidgetItem(alert["severity"]))
            table.setItem(row, 4, QTableWidgetItem(alert["status"]))
            table.setItem(row, 5, QTableWidgetItem(alert["details"]))

    def load_saved_alerts_database(self):

        table = self.ui.tableDatabase

        table.setRowCount(0)

        alerts = self.alert_repo.all()

        for alert in alerts:
            row = table.rowCount()
            table.insertRow(row)

            table.setItem(row, 0, QTableWidgetItem(alert["time"]))
            table.setItem(row, 1, QTableWidgetItem(alert["threat"]))
            table.setItem(row, 2, QTableWidgetItem(alert["source_ip"]))
            table.setItem(row, 3, QTableWidgetItem(alert["severity"]))
            table.setItem(row, 4, QTableWidgetItem(alert["status"]))
            table.setItem(row, 5, QTableWidgetItem(alert["details"]))

    def show_about(self):
        dialog = AboutDialog()
        dialog.exec()
    
    def load_settings(self):
    
        self.ui.spinPacketHistory.setValue(
            self.config.get("packet_history")
        )

        self.ui.spinRefreshRate.setValue(
            self.config.get("refresh_rate")
        )

        self.ui.spinPortScanThreshold.setValue(
            self.config.get("port_scan_threshold")
        )

        self.ui.spinSynThreshold.setValue(
            self.config.get("syn_flood_threshold")
        )

        self.ui.spinSynWindow.setValue(
            self.config.get("syn_window")
        )

        self.ui.spinCooldown.setValue(
            self.config.get("alert_cooldown")
        )

        self.ui.chkSaveDatabase.setChecked(
            self.config.get("save_database")
        )

        self.ui.chkWriteLog.setChecked(
            self.config.get("write_log")
        )

        self.ui.chkPopup.setChecked(
            self.config.get("popup_notifications")
        )

        self.ui.chkPlaySound.setChecked(
            self.config.get("play_sound")
        )

        self.ui.cmbTheme.setCurrentText(
            self.config.get("theme")
        )

        self.ui.cmbAccent.setCurrentText(
            self.config.get("accent")
        )
    
    def save_settings(self):
    
        self.config.set(
            "packet_history",
            self.ui.spinPacketHistory.value()
        )

        self.config.set(
            "refresh_rate",
            self.ui.spinRefreshRate.value()
        )

        self.config.set(
            "port_scan_threshold",
            self.ui.spinPortScanThreshold.value()
        )

        self.config.set(
            "syn_flood_threshold",
            self.ui.spinSynThreshold.value()
        )

        self.config.set(
            "syn_window",
            self.ui.spinSynWindow.value()
        )

        self.config.set(
            "alert_cooldown",
            self.ui.spinCooldown.value()
        )

        self.config.set(
            "save_database",
            self.ui.chkSaveDatabase.isChecked()
        )

        self.config.set(
            "write_log",
            self.ui.chkWriteLog.isChecked()
        )

        self.config.set(
            "popup_notifications",
            self.ui.chkPopup.isChecked()
        )

        self.config.set(
            "play_sound",
            self.ui.chkPlaySound.isChecked()
        )

        self.config.set(
            "theme",
            self.ui.cmbTheme.currentText()
        )

        self.config.set(
            "accent",
            self.ui.cmbAccent.currentText()
        )

        self.config.save()

        self.statusBar().showMessage(
            "Settings saved successfully.",
            3000
        )

    def reset_settings(self):
    
        self.config.data = {

                "interface": "",

                "packet_history": 500,

                "refresh_rate": 1000,

                "port_scan_threshold": 15,

                "syn_flood_threshold": 20,

                "syn_window": 5,

                "alert_cooldown": 30,

                "save_database": True,

                "write_log": True,

                "popup_notifications": True,

                "play_sound": False,

                "theme": "Dark",

                "accent": "Blue"
            }

        self.config.save()

        self.load_settings()

# Alerts IP Blocking
    def block_ip(self):
        ip = self.ui.txtIPAddress.text().strip()

        if not ip:
            QMessageBox.warning(
                self,
                "IP Address Required",
                "Please enter an IP address."
            )
            return

        success, message = self.firewall_manager.block_ip(ip)

        if success:
            QMessageBox.information(
                self,
                "IP Blocked",
                message
            )

            self.add_blocked_ip(ip, "Manual Block")

            self.ui.txtIPAddress.clear()

        else:
            QMessageBox.critical(
                self,
                "Block Failed",
                message
            )

    def unblock_ip(self):
        ip = self.ui.txtIPAddress.text().strip()

        if not ip:
            QMessageBox.warning(
                self,
                "IP Address Required",
                "Please enter an IP address."
            )
            return

        success, message = self.firewall_manager.unblock_ip(ip)

        if success:
            QMessageBox.information(
                self,
                "IP Unblocked",
                message
            )

            self.remove_blocked_ip(ip)

            self.ui.txtIPAddress.clear()

        else:
            QMessageBox.critical(
                self,
                "Unblock Failed",
                message
            )

    def add_blocked_ip(self, ip, reason):
        table = self.ui.tableBlockedIPs

        row = table.rowCount()
        table.insertRow(row)

        table.setItem(row, 0, QTableWidgetItem(ip))
        table.setItem(
            row,
            1,
            QTableWidgetItem(datetime.now().strftime("%H:%M:%S"))
        )
        table.setItem(row, 2, QTableWidgetItem(reason))
        table.setItem(row, 3, QTableWidgetItem("BLOCKED"))

    def remove_blocked_ip(self, ip):
        table = self.ui.tableBlockedIPs

        for row in range(table.rowCount()):
            item = table.item(row, 0)

            if item and item.text() == ip:
                table.removeRow(row)
                break

    def update_alert_counters(self, alert):
        severity = alert.get("severity", "Medium").lower()

        total = int(self.ui.lblTotalAlerts.text() or 0)
        self.ui.lblTotalAlerts.setText(str(total + 1))

        if severity == "critical":
            count = int(self.ui.lblCriticalAlerts.text() or 0)
            self.ui.lblCriticalAlerts.setText(str(count + 1))

        elif severity == "high":
            count = int(self.ui.lblHighAlerts.text() or 0)
            self.ui.lblHighAlerts.setText(str(count + 1))

        elif severity == "medium":
            count = int(self.ui.lblMediumAlerts.text() or 0)
            self.ui.lblMediumAlerts.setText(str(count + 1))

    def style_alert_row(self, row, alert):
        severity = alert.get("severity", "").lower()

        if severity == "critical":
            text = "CRITICAL"

        elif severity == "high":
            text = "HIGH"

        elif severity == "medium":
            text = "MEDIUM"

        elif severity == "low":
            text = "LOW"

        else:
            return

        item = self.ui.tableAlerts.item(row, 1)

        if item:
            item.setText(text)

    
    def setup_logging(self):
        """Configure persistent application logging."""
        os.makedirs("logs", exist_ok=True)

        self.log_file = os.path.join("logs", "aw3nids.log")

        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            encoding="utf-8",
            force=True,
        )

        self.app_logger = logging.getLogger("AW3NIDS")
        self.app_logger.info("AW3NIDS application started")
    
    def setup_logs_page(self):
        """Connect the Logs page controls."""
        self.ui.tableLogs.setColumnCount(4)
        self.ui.tableLogs.setHorizontalHeaderLabels(
            ["Time", "Level", "Category", "Message"]
        )
        self.ui.tableLogs.setAlternatingRowColors(True)
        self.ui.tableLogs.setSortingEnabled(False)

        self.ui.txtSearchLogs.textChanged.connect(self.refresh_logs)
        self.ui.cmbLogLevel.currentTextChanged.connect(self.refresh_logs)
        self.ui.btnClearLogs.clicked.connect(self.clear_logs)
        self.ui.btnExportLogs.clicked.connect(self.export_logs)

        self.load_logs()


    def read_log_entries(self):
        """Read saved log entries from the application log file."""
        entries = []

        if not os.path.exists(self.log_file):
            return entries

        try:
            with open(self.log_file, "r", encoding="utf-8") as log_file:
                for line in log_file:
                    parts = line.rstrip("\n").split(" | ", 3)

                    if len(parts) == 4:
                        timestamp, level, category, message = parts
                        entries.append(
                            (timestamp, level, category, message)
                        )
                    elif line.strip():
                        entries.append(
                            ("", "INFO", "AW3NIDS", line.strip())
                        )

        except OSError:
            self.app_logger.exception("Failed to read application logs")

        return entries


    def load_logs(self):
        """Load saved logs into the Logs page."""
        self.refresh_logs()


    def refresh_logs(self, *_):
        """Refresh the table and apply the search and level filters."""
        entries = self.read_log_entries()

        total = len(entries)
        warnings = sum(
            1 for entry in entries if entry[1] == "WARNING"
        )
        errors = sum(
            1 for entry in entries
            if entry[1] in ("ERROR", "CRITICAL")
        )

        self.ui.lblTotalLogs.setText(str(total))
        self.ui.lblWarningLogs.setText(str(warnings))
        self.ui.lblErrorLogs.setText(str(errors))

        search_text = self.ui.txtSearchLogs.text().strip().lower()
        selected_level = self.ui.cmbLogLevel.currentText()

        filtered_entries = []

        for entry in entries:
            timestamp, level, category, message = entry

            if selected_level != "All Levels" and level != selected_level:
                continue

            searchable_text = " ".join(entry).lower()

            if search_text and search_text not in searchable_text:
                continue

            filtered_entries.append(entry)

        table = self.ui.tableLogs
        table.setRowCount(0)

        for entry in reversed(filtered_entries):
            row = table.rowCount()
            table.insertRow(row)

            for column, value in enumerate(entry):
                table.setItem(
                    row, column, QTableWidgetItem(str(value))
                )

        table.resizeColumnsToContents()
        table.horizontalHeader().setStretchLastSection(True)


    def clear_logs(self):
        """Clear the saved log file and refresh the table."""
        answer = QMessageBox.question(
            self,
            "Clear Logs",
            "Are you sure you want to clear all saved application logs?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if answer != QMessageBox.StandardButton.Yes:
            return

        try:
            with open(self.log_file, "w", encoding="utf-8"):
                pass

            self.refresh_logs()

        except OSError as error:
            QMessageBox.warning(
                self,
                "Clear Logs Failed",
                f"Could not clear the log file:\n{error}",
            )


    def export_logs(self):
        """Export the currently displayed logs to CSV."""
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Logs",
            "aw3nids_logs.csv",
            "CSV Files (*.csv)",
        )

        if not path:
            return

        try:
            with open(
                path, "w", newline="", encoding="utf-8-sig"
            ) as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Time", "Level", "Category", "Message"])

                table = self.ui.tableLogs

                for row in range(table.rowCount()):
                    writer.writerow([
                        table.item(row, column).text()
                        if table.item(row, column) else ""
                        for column in range(4)
                    ])

            QMessageBox.information(
                self,
                "Export Complete",
                "The displayed logs were exported successfully.",
            )

        except OSError as error:
            QMessageBox.warning(
                self,
                "Export Failed",
                f"Could not export logs:\n{error}",
            )