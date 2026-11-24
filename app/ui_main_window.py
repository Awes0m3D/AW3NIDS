# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDateEdit, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(968, 546)
        MainWindow.setAutoFillBackground(False)
        self.actionStartMonitoring = QAction(MainWindow)
        self.actionStartMonitoring.setObjectName(u"actionStartMonitoring")
        self.actionStopMonitoring = QAction(MainWindow)
        self.actionStopMonitoring.setObjectName(u"actionStopMonitoring")
        self.actionClearAlerts = QAction(MainWindow)
        self.actionClearAlerts.setObjectName(u"actionClearAlerts")
        self.actionExportReport = QAction(MainWindow)
        self.actionExportReport.setObjectName(u"actionExportReport")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 230, 421))
        self.horizontalLayoutWidget.setMaximumSize(QSize(230, 16777215))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(self.horizontalLayoutWidget)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setEnabled(True)
        self.sidebarFrame.setMinimumSize(QSize(230, 0))
        self.sidebarFrame.setMaximumSize(QSize(230, 16777215))
        self.sidebarFrame.setAutoFillBackground(False)
        self.sidebarFrame.setStyleSheet(u"background-color:#1E293B;")
        self.sidebarFrame.setFrameShape(QFrame.StyledPanel)
        self.sidebarFrame.setFrameShadow(QFrame.Raised)
        self.iblAppLogo = QLabel(self.sidebarFrame)
        self.iblAppLogo.setObjectName(u"iblAppLogo")
        self.iblAppLogo.setGeometry(QRect(0, 0, 231, 51))
        self.iblAppLogo.setStyleSheet(u"font-size: 22pt;\n"
"font: 87 8pt \"Product Sans Black\";\n"
"font-weight: bold;\n"
"color: white;")
        self.iblAppLogo.setScaledContents(True)
        self.iblAppLogo.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget_2 = QWidget(self.sidebarFrame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 52, 171, 361))
        self.NavSidebar = QVBoxLayout(self.verticalLayoutWidget_2)
        self.NavSidebar.setObjectName(u"NavSidebar")
        self.NavSidebar.setContentsMargins(0, 0, 0, 0)
        self.btnDashboard = QPushButton(self.verticalLayoutWidget_2)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnDashboard)

        self.btnLiveCapture = QPushButton(self.verticalLayoutWidget_2)
        self.btnLiveCapture.setObjectName(u"btnLiveCapture")
        self.btnLiveCapture.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnLiveCapture)

        self.btnAlerts = QPushButton(self.verticalLayoutWidget_2)
        self.btnAlerts.setObjectName(u"btnAlerts")
        self.btnAlerts.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnAlerts)

        self.btnSimulator = QPushButton(self.verticalLayoutWidget_2)
        self.btnSimulator.setObjectName(u"btnSimulator")
        self.btnSimulator.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnSimulator)

        self.btnAnalytics = QPushButton(self.verticalLayoutWidget_2)
        self.btnAnalytics.setObjectName(u"btnAnalytics")
        self.btnAnalytics.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnAnalytics)

        self.btnDatabase = QPushButton(self.verticalLayoutWidget_2)
        self.btnDatabase.setObjectName(u"btnDatabase")
        self.btnDatabase.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnDatabase)

        self.btnReports = QPushButton(self.verticalLayoutWidget_2)
        self.btnReports.setObjectName(u"btnReports")
        self.btnReports.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnReports)

        self.btnLogs = QPushButton(self.verticalLayoutWidget_2)
        self.btnLogs.setObjectName(u"btnLogs")
        self.btnLogs.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnLogs)

        self.btnSettings = QPushButton(self.verticalLayoutWidget_2)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setStyleSheet(u"QPushButton{\n"
"	font: 8pt \"Product Sans\";\n"
"	background_color: #334155; \n"
"	color: white;\n"
"	border: none;\n"
"	padding:9px;\n"
"	text-align: left;\n"
"	font-size: 11pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#475569;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #0EA5E9;\n"
"}")

        self.NavSidebar.addWidget(self.btnSettings)


        self.horizontalLayout.addWidget(self.sidebarFrame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(240, 0, 721, 421))
        self.stackedWidget.setFrameShape(QFrame.Box)
        self.pageDashboard = QWidget()
        self.pageDashboard.setObjectName(u"pageDashboard")
        self.gridLayoutWidget_2 = QWidget(self.pageDashboard)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 20, 341, 41))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.framePackets = QFrame(self.gridLayoutWidget_2)
        self.framePackets.setObjectName(u"framePackets")
        self.framePackets.setFrameShape(QFrame.StyledPanel)
        self.framePackets.setFrameShadow(QFrame.Sunken)
        self.lblPacketTitle = QLabel(self.framePackets)
        self.lblPacketTitle.setObjectName(u"lblPacketTitle")
        self.lblPacketTitle.setGeometry(QRect(10, 0, 91, 16))
        self.lblPacketCount = QLabel(self.framePackets)
        self.lblPacketCount.setObjectName(u"lblPacketCount")
        self.lblPacketCount.setGeometry(QRect(10, 20, 81, 16))

        self.gridLayout_2.addWidget(self.framePackets, 0, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.pageDashboard)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 60, 341, 41))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frameHosts = QFrame(self.gridLayoutWidget_3)
        self.frameHosts.setObjectName(u"frameHosts")
        self.frameHosts.setFrameShape(QFrame.StyledPanel)
        self.frameHosts.setFrameShadow(QFrame.Sunken)
        self.lblHostTitle = QLabel(self.frameHosts)
        self.lblHostTitle.setObjectName(u"lblHostTitle")
        self.lblHostTitle.setGeometry(QRect(10, 0, 91, 16))
        self.lblHostCount = QLabel(self.frameHosts)
        self.lblHostCount.setObjectName(u"lblHostCount")
        self.lblHostCount.setGeometry(QRect(10, 20, 71, 16))

        self.gridLayout_4.addWidget(self.frameHosts, 0, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.pageDashboard)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(370, 20, 331, 41))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frameStatus = QFrame(self.gridLayoutWidget_4)
        self.frameStatus.setObjectName(u"frameStatus")
        self.frameStatus.setFrameShape(QFrame.StyledPanel)
        self.frameStatus.setFrameShadow(QFrame.Sunken)
        self.lblNetworkStatusTitle = QLabel(self.frameStatus)
        self.lblNetworkStatusTitle.setObjectName(u"lblNetworkStatusTitle")
        self.lblNetworkStatusTitle.setGeometry(QRect(10, 0, 91, 16))
        self.lblNetworkStatus = QLabel(self.frameStatus)
        self.lblNetworkStatus.setObjectName(u"lblNetworkStatus")
        self.lblNetworkStatus.setGeometry(QRect(10, 20, 141, 16))

        self.gridLayout_5.addWidget(self.frameStatus, 0, 0, 1, 1)

        self.gridLayoutWidget_29 = QWidget(self.pageDashboard)
        self.gridLayoutWidget_29.setObjectName(u"gridLayoutWidget_29")
        self.gridLayoutWidget_29.setGeometry(QRect(370, 60, 331, 41))
        self.gridLayout_30 = QGridLayout(self.gridLayoutWidget_29)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frameThreats = QFrame(self.gridLayoutWidget_29)
        self.frameThreats.setObjectName(u"frameThreats")
        self.frameThreats.setFrameShape(QFrame.StyledPanel)
        self.frameThreats.setFrameShadow(QFrame.Sunken)
        self.lblThreatTitle = QLabel(self.frameThreats)
        self.lblThreatTitle.setObjectName(u"lblThreatTitle")
        self.lblThreatTitle.setGeometry(QRect(10, 0, 91, 16))
        self.lblThreatCount = QLabel(self.frameThreats)
        self.lblThreatCount.setObjectName(u"lblThreatCount")
        self.lblThreatCount.setGeometry(QRect(10, 20, 71, 16))

        self.gridLayout_30.addWidget(self.frameThreats, 1, 0, 1, 1)

        self.lblNetworkTraffic = QLabel(self.pageDashboard)
        self.lblNetworkTraffic.setObjectName(u"lblNetworkTraffic")
        self.lblNetworkTraffic.setGeometry(QRect(10, 100, 251, 16))
        self.lblNetworkTraffic.setAlignment(Qt.AlignCenter)
        self.frameGraph = QFrame(self.pageDashboard)
        self.frameGraph.setObjectName(u"frameGraph")
        self.frameGraph.setGeometry(QRect(10, 120, 701, 131))
        self.frameGraph.setFrameShape(QFrame.Box)
        self.frameGraph.setFrameShadow(QFrame.Sunken)
        self.graphContainer = QWidget(self.frameGraph)
        self.graphContainer.setObjectName(u"graphContainer")
        self.graphContainer.setGeometry(QRect(-10, -10, 721, 151))
        self.verticalLayout_10 = QVBoxLayout(self.graphContainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayoutWidget_7 = QWidget(self.pageDashboard)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(9, 259, 701, 151))
        self.horizontalLayoutTables = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayoutTables.setObjectName(u"horizontalLayoutTables")
        self.horizontalLayoutTables.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.horizontalLayoutWidget_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lblLivePacketsHeader = QLabel(self.frame)
        self.lblLivePacketsHeader.setObjectName(u"lblLivePacketsHeader")
        self.lblLivePacketsHeader.setGeometry(QRect(130, 0, 101, 20))
        self.lblLivePacketsHeader.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")
        self.lblLivePacketsHeader.setAlignment(Qt.AlignCenter)
        self.tableLivePackets = QTableWidget(self.frame)
        if (self.tableLivePackets.columnCount() < 5):
            self.tableLivePackets.setColumnCount(5)
        font = QFont()
        font.setPointSize(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font)
        self.tableLivePackets.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableLivePackets.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableLivePackets.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font)
        self.tableLivePackets.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font)
        self.tableLivePackets.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableLivePackets.setObjectName(u"tableLivePackets")
        self.tableLivePackets.setGeometry(QRect(0, 20, 351, 131))
        self.tableLivePackets.setFrameShape(QFrame.Box)
        self.tableLivePackets.setFrameShadow(QFrame.Sunken)
        self.tableLivePackets.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableLivePackets.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableLivePackets.setAlternatingRowColors(True)
        self.tableLivePackets.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableLivePackets.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableLivePackets.setSortingEnabled(False)
        self.tableRecentAlerts = QTableWidget(self.frame)
        if (self.tableRecentAlerts.columnCount() < 6):
            self.tableRecentAlerts.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableRecentAlerts.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableRecentAlerts.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableRecentAlerts.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableRecentAlerts.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableRecentAlerts.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableRecentAlerts.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.tableRecentAlerts.setObjectName(u"tableRecentAlerts")
        self.tableRecentAlerts.setGeometry(QRect(350, 20, 351, 131))
        self.tableRecentAlerts.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableRecentAlerts.setGridStyle(Qt.SolidLine)
        self.tableRecentAlerts.setColumnCount(6)
        self.lblRecentAlerts = QLabel(self.frame)
        self.lblRecentAlerts.setObjectName(u"lblRecentAlerts")
        self.lblRecentAlerts.setGeometry(QRect(480, 0, 101, 20))
        self.lblRecentAlerts.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")
        self.lblRecentAlerts.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutTables.addWidget(self.frame)

        self.frameDashboard = QFrame(self.pageDashboard)
        self.frameDashboard.setObjectName(u"frameDashboard")
        self.frameDashboard.setGeometry(QRect(9, 9, 701, 401))
        self.frameDashboard.setFrameShape(QFrame.StyledPanel)
        self.frameDashboard.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.pageDashboard)
        self.frameDashboard.raise_()
        self.gridLayoutWidget_2.raise_()
        self.gridLayoutWidget_3.raise_()
        self.gridLayoutWidget_4.raise_()
        self.gridLayoutWidget_29.raise_()
        self.lblNetworkTraffic.raise_()
        self.frameGraph.raise_()
        self.horizontalLayoutWidget_7.raise_()
        self.pageCapture = QWidget()
        self.pageCapture.setObjectName(u"pageCapture")
        self.verticalLayoutWidget_9 = QWidget(self.pageCapture)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 10, 701, 401))
        self.verticalLayoutLiveCapture = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayoutLiveCapture.setObjectName(u"verticalLayoutLiveCapture")
        self.verticalLayoutLiveCapture.setContentsMargins(0, 0, 0, 0)
        self.frameCapture = QFrame(self.verticalLayoutWidget_9)
        self.frameCapture.setObjectName(u"frameCapture")
        self.frameCapture.setFrameShape(QFrame.StyledPanel)
        self.frameCapture.setFrameShadow(QFrame.Sunken)
        self.cmbInterface = QComboBox(self.frameCapture)
        self.cmbInterface.addItem("")
        self.cmbInterface.setObjectName(u"cmbInterface")
        self.cmbInterface.setGeometry(QRect(70, 10, 441, 21))
        self.lblInterface = QLabel(self.frameCapture)
        self.lblInterface.setObjectName(u"lblInterface")
        self.lblInterface.setGeometry(QRect(10, 10, 61, 21))
        self.btnRefreshInterfaces = QPushButton(self.frameCapture)
        self.btnRefreshInterfaces.setObjectName(u"btnRefreshInterfaces")
        self.btnRefreshInterfaces.setGeometry(QRect(530, 10, 75, 23))
        self.lblLivePacketTable = QLabel(self.frameCapture)
        self.lblLivePacketTable.setObjectName(u"lblLivePacketTable")
        self.lblLivePacketTable.setGeometry(QRect(10, 70, 121, 20))
        self.lblLivePacketTable.setAlignment(Qt.AlignCenter)
        self.tableLivePackets_2 = QTableWidget(self.frameCapture)
        if (self.tableLivePackets_2.columnCount() < 6):
            self.tableLivePackets_2.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableLivePackets_2.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableLivePackets_2.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableLivePackets_2.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableLivePackets_2.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableLivePackets_2.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.tableLivePackets_2.setObjectName(u"tableLivePackets_2")
        self.tableLivePackets_2.setGeometry(QRect(10, 90, 471, 301))
        self.tableLivePackets_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableLivePackets_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableLivePackets_2.setColumnCount(6)
        self.GroupCaptureDetails_2 = QGroupBox(self.frameCapture)
        self.GroupCaptureDetails_2.setObjectName(u"GroupCaptureDetails_2")
        self.GroupCaptureDetails_2.setGeometry(QRect(590, 90, 101, 291))
        self.formLayout = QFormLayout(self.GroupCaptureDetails_2)
        self.formLayout.setObjectName(u"formLayout")
        self.lblDetailTime = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailTime.setObjectName(u"lblDetailTime")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblDetailTime)

        self.lblDetailSrc = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailSrc.setObjectName(u"lblDetailSrc")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblDetailSrc)

        self.lblDetailDst = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailDst.setObjectName(u"lblDetailDst")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblDetailDst)

        self.lblDetailProtocol = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailProtocol.setObjectName(u"lblDetailProtocol")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblDetailProtocol)

        self.lblDetailSrcPort = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailSrcPort.setObjectName(u"lblDetailSrcPort")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblDetailSrcPort)

        self.lblDetailTTL = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailTTL.setObjectName(u"lblDetailTTL")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lblDetailTTL)

        self.lblDetailLength = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailLength.setObjectName(u"lblDetailLength")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblDetailLength)

        self.lblDetailFlags = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailFlags.setObjectName(u"lblDetailFlags")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.lblDetailFlags)

        self.lblDetailDstPort = QLabel(self.GroupCaptureDetails_2)
        self.lblDetailDstPort.setObjectName(u"lblDetailDstPort")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblDetailDstPort)

        self.GroupCaptureDetails = QGroupBox(self.frameCapture)
        self.GroupCaptureDetails.setObjectName(u"GroupCaptureDetails")
        self.GroupCaptureDetails.setGeometry(QRect(490, 100, 101, 281))
        self.formLayout_4 = QFormLayout(self.GroupCaptureDetails)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.time = QLabel(self.GroupCaptureDetails)
        self.time.setObjectName(u"time")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.time)

        self.sourceip = QLabel(self.GroupCaptureDetails)
        self.sourceip.setObjectName(u"sourceip")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.sourceip)

        self.destination = QLabel(self.GroupCaptureDetails)
        self.destination.setObjectName(u"destination")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.destination)

        self.protocol = QLabel(self.GroupCaptureDetails)
        self.protocol.setObjectName(u"protocol")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.protocol)

        self.sourceports = QLabel(self.GroupCaptureDetails)
        self.sourceports.setObjectName(u"sourceports")

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.sourceports)

        self.ttl = QLabel(self.GroupCaptureDetails)
        self.ttl.setObjectName(u"ttl")

        self.formLayout_4.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ttl)

        self.length = QLabel(self.GroupCaptureDetails)
        self.length.setObjectName(u"length")

        self.formLayout_4.setWidget(7, QFormLayout.ItemRole.LabelRole, self.length)

        self.flags = QLabel(self.GroupCaptureDetails)
        self.flags.setObjectName(u"flags")

        self.formLayout_4.setWidget(8, QFormLayout.ItemRole.LabelRole, self.flags)

        self.destinationport = QLabel(self.GroupCaptureDetails)
        self.destinationport.setObjectName(u"destinationport")

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.LabelRole, self.destinationport)

        self.horizontalLayoutWidget_4 = QWidget(self.frameCapture)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 40, 291, 31))
        self.horizontalLayoutCAptureButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayoutCAptureButtons.setObjectName(u"horizontalLayoutCAptureButtons")
        self.horizontalLayoutCAptureButtons.setContentsMargins(0, 0, 0, 0)
        self.btnStartCapture = QPushButton(self.horizontalLayoutWidget_4)
        self.btnStartCapture.setObjectName(u"btnStartCapture")

        self.horizontalLayoutCAptureButtons.addWidget(self.btnStartCapture)

        self.btnStopCapture = QPushButton(self.horizontalLayoutWidget_4)
        self.btnStopCapture.setObjectName(u"btnStopCapture")

        self.horizontalLayoutCAptureButtons.addWidget(self.btnStopCapture)


        self.verticalLayoutLiveCapture.addWidget(self.frameCapture)

        self.stackedWidget.addWidget(self.pageCapture)
        self.pageAlerts = QWidget()
        self.pageAlerts.setObjectName(u"pageAlerts")
        self.verticalLayoutWidget_4 = QWidget(self.pageAlerts)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 10, 701, 401))
        self.verticalLayoutAlerts = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayoutAlerts.setObjectName(u"verticalLayoutAlerts")
        self.verticalLayoutAlerts.setContentsMargins(0, 0, 0, 0)
        self.frameAlerts = QFrame(self.verticalLayoutWidget_4)
        self.frameAlerts.setObjectName(u"frameAlerts")
        self.frameAlerts.setFrameShape(QFrame.StyledPanel)
        self.frameAlerts.setFrameShadow(QFrame.Sunken)
        self.layoutWidget_3 = QWidget(self.frameAlerts)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(40, 40, 621, 41))
        self.horizontalLayoutAlerts = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayoutAlerts.setObjectName(u"horizontalLayoutAlerts")
        self.horizontalLayoutAlerts.setContentsMargins(0, 0, 0, 0)
        self.frameTotalAlerts = QFrame(self.layoutWidget_3)
        self.frameTotalAlerts.setObjectName(u"frameTotalAlerts")
        self.frameTotalAlerts.setFrameShape(QFrame.StyledPanel)
        self.frameTotalAlerts.setFrameShadow(QFrame.Sunken)
        self.lblTotalAlerts = QLabel(self.frameTotalAlerts)
        self.lblTotalAlerts.setObjectName(u"lblTotalAlerts")
        self.lblTotalAlerts.setGeometry(QRect(10, 20, 151, 20))
        self.lblTotalAlerts.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblTotalAlertsTitle = QLabel(self.frameTotalAlerts)
        self.lblTotalAlertsTitle.setObjectName(u"lblTotalAlertsTitle")
        self.lblTotalAlertsTitle.setGeometry(QRect(10, 0, 151, 20))
        self.lblTotalAlertsTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayoutAlerts.addWidget(self.frameTotalAlerts)

        self.frameCRIITICAL = QFrame(self.layoutWidget_3)
        self.frameCRIITICAL.setObjectName(u"frameCRIITICAL")
        self.frameCRIITICAL.setFrameShape(QFrame.StyledPanel)
        self.frameCRIITICAL.setFrameShadow(QFrame.Sunken)
        self.lblMediumTitle = QLabel(self.frameCRIITICAL)
        self.lblMediumTitle.setObjectName(u"lblMediumTitle")
        self.lblMediumTitle.setGeometry(QRect(0, 0, 151, 20))
        self.lblMediumTitle.setAlignment(Qt.AlignCenter)
        self.lblMediumAlerts = QLabel(self.frameCRIITICAL)
        self.lblMediumAlerts.setObjectName(u"lblMediumAlerts")
        self.lblMediumAlerts.setGeometry(QRect(0, 20, 151, 20))
        self.lblMediumAlerts.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutAlerts.addWidget(self.frameCRIITICAL)

        self.frameHIGH = QFrame(self.layoutWidget_3)
        self.frameHIGH.setObjectName(u"frameHIGH")
        self.frameHIGH.setFrameShape(QFrame.StyledPanel)
        self.frameHIGH.setFrameShadow(QFrame.Sunken)
        self.lblHighAlerts = QLabel(self.frameHIGH)
        self.lblHighAlerts.setObjectName(u"lblHighAlerts")
        self.lblHighAlerts.setGeometry(QRect(0, 20, 151, 20))
        self.lblHighAlerts.setAlignment(Qt.AlignCenter)
        self.lblHighTitle = QLabel(self.frameHIGH)
        self.lblHighTitle.setObjectName(u"lblHighTitle")
        self.lblHighTitle.setGeometry(QRect(0, 0, 151, 20))
        self.lblHighTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutAlerts.addWidget(self.frameHIGH)

        self.frameMEDIUM = QFrame(self.layoutWidget_3)
        self.frameMEDIUM.setObjectName(u"frameMEDIUM")
        self.frameMEDIUM.setFrameShape(QFrame.StyledPanel)
        self.frameMEDIUM.setFrameShadow(QFrame.Sunken)
        self.lblCriticalTitle = QLabel(self.frameMEDIUM)
        self.lblCriticalTitle.setObjectName(u"lblCriticalTitle")
        self.lblCriticalTitle.setGeometry(QRect(0, 0, 151, 20))
        self.lblCriticalTitle.setAlignment(Qt.AlignCenter)
        self.lblCriticalAlerts = QLabel(self.frameMEDIUM)
        self.lblCriticalAlerts.setObjectName(u"lblCriticalAlerts")
        self.lblCriticalAlerts.setGeometry(QRect(0, 20, 151, 20))
        self.lblCriticalAlerts.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutAlerts.addWidget(self.frameMEDIUM)

        self.horizontalLayoutWidget_11 = QWidget(self.frameAlerts)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(180, 370, 341, 31))
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_11)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_9.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget_11)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_9.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget_11)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.horizontalLayoutWidget_9 = QWidget(self.frameAlerts)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(30, 90, 639, 25))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lblSearchSeverity = QLabel(self.horizontalLayoutWidget_9)
        self.lblSearchSeverity.setObjectName(u"lblSearchSeverity")

        self.horizontalLayout_8.addWidget(self.lblSearchSeverity)

        self.txtSearchAlerts = QLineEdit(self.horizontalLayoutWidget_9)
        self.txtSearchAlerts.setObjectName(u"txtSearchAlerts")

        self.horizontalLayout_8.addWidget(self.txtSearchAlerts)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_8)

        self.comboSeverity = QComboBox(self.horizontalLayoutWidget_9)
        self.comboSeverity.addItem("")
        self.comboSeverity.addItem("")
        self.comboSeverity.addItem("")
        self.comboSeverity.addItem("")
        self.comboSeverity.addItem("")
        self.comboSeverity.setObjectName(u"comboSeverity")

        self.horizontalLayout_2.addWidget(self.comboSeverity)

        self.cmbAlertType = QComboBox(self.horizontalLayoutWidget_9)
        self.cmbAlertType.addItem("")
        self.cmbAlertType.addItem("")
        self.cmbAlertType.addItem("")
        self.cmbAlertType.addItem("")
        self.cmbAlertType.addItem("")
        self.cmbAlertType.setObjectName(u"cmbAlertType")

        self.horizontalLayout_2.addWidget(self.cmbAlertType)

        self.btnClearFilters = QPushButton(self.horizontalLayoutWidget_9)
        self.btnClearFilters.setObjectName(u"btnClearFilters")

        self.horizontalLayout_2.addWidget(self.btnClearFilters)

        self.tableAlerts = QTableWidget(self.frameAlerts)
        if (self.tableAlerts.columnCount() < 7):
            self.tableAlerts.setColumnCount(7)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableAlerts.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableAlerts.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableAlerts.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableAlerts.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableAlerts.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableAlerts.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableAlerts.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.tableAlerts.setObjectName(u"tableAlerts")
        self.tableAlerts.setGeometry(QRect(10, 120, 681, 111))
        self.lblIPResponse = QLabel(self.frameAlerts)
        self.lblIPResponse.setObjectName(u"lblIPResponse")
        self.lblIPResponse.setGeometry(QRect(30, 230, 639, 21))
        self.lblIPResponse.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";\n"
"")
        self.lblIPResponse.setAlignment(Qt.AlignCenter)
        self.tableBlockedIPs = QTableWidget(self.frameAlerts)
        if (self.tableBlockedIPs.columnCount() < 4):
            self.tableBlockedIPs.setColumnCount(4)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableBlockedIPs.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableBlockedIPs.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableBlockedIPs.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableBlockedIPs.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        self.tableBlockedIPs.setObjectName(u"tableBlockedIPs")
        self.tableBlockedIPs.setGeometry(QRect(10, 280, 681, 81))
        self.layoutWidget = QWidget(self.frameAlerts)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 250, 639, 29))
        self.widgetIPControls = QHBoxLayout(self.layoutWidget)
        self.widgetIPControls.setObjectName(u"widgetIPControls")
        self.widgetIPControls.setContentsMargins(0, 0, 0, 0)
        self.lblIPAddress = QLabel(self.layoutWidget)
        self.lblIPAddress.setObjectName(u"lblIPAddress")

        self.widgetIPControls.addWidget(self.lblIPAddress)

        self.txtIPAddress = QLineEdit(self.layoutWidget)
        self.txtIPAddress.setObjectName(u"txtIPAddress")

        self.widgetIPControls.addWidget(self.txtIPAddress)

        self.btnBlockIP = QPushButton(self.layoutWidget)
        self.btnBlockIP.setObjectName(u"btnBlockIP")

        self.widgetIPControls.addWidget(self.btnBlockIP)

        self.btnUnblockIP = QPushButton(self.layoutWidget)
        self.btnUnblockIP.setObjectName(u"btnUnblockIP")

        self.widgetIPControls.addWidget(self.btnUnblockIP)

        self.AlertsPageTitle = QLabel(self.frameAlerts)
        self.AlertsPageTitle.setObjectName(u"AlertsPageTitle")
        self.AlertsPageTitle.setGeometry(QRect(30, 0, 131, 41))
        self.AlertsPageTitle.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.AlertsPageTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayoutAlerts.addWidget(self.frameAlerts)

        self.stackedWidget.addWidget(self.pageAlerts)
        self.pageLogs = QWidget()
        self.pageLogs.setObjectName(u"pageLogs")
        self.verticalLayoutWidget_5 = QWidget(self.pageLogs)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 701, 401))
        self.LayoutLogs = QVBoxLayout(self.verticalLayoutWidget_5)
        self.LayoutLogs.setObjectName(u"LayoutLogs")
        self.LayoutLogs.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.verticalLayoutWidget_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 281, 21))
        self.LogsPageTitle = QLabel(self.frame_2)
        self.LogsPageTitle.setObjectName(u"LogsPageTitle")
        self.LogsPageTitle.setGeometry(QRect(-10, 0, 141, 31))
        self.LogsPageTitle.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.LogsPageTitle.setAlignment(Qt.AlignCenter)
        self.layoutWidget_4 = QWidget(self.frame_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(30, 60, 631, 51))
        self.horizontalLayoutAlerts_2 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayoutAlerts_2.setObjectName(u"horizontalLayoutAlerts_2")
        self.horizontalLayoutAlerts_2.setContentsMargins(0, 0, 0, 0)
        self.frameTotalLogs = QFrame(self.layoutWidget_4)
        self.frameTotalLogs.setObjectName(u"frameTotalLogs")
        self.frameTotalLogs.setFrameShape(QFrame.StyledPanel)
        self.frameTotalLogs.setFrameShadow(QFrame.Sunken)
        self.lblTotalLogs = QLabel(self.frameTotalLogs)
        self.lblTotalLogs.setObjectName(u"lblTotalLogs")
        self.lblTotalLogs.setGeometry(QRect(10, 20, 151, 31))
        self.lblTotalLogs.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lblTotalLogs.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblTotalAlertsTitle_2 = QLabel(self.frameTotalLogs)
        self.lblTotalAlertsTitle_2.setObjectName(u"lblTotalAlertsTitle_2")
        self.lblTotalAlertsTitle_2.setGeometry(QRect(10, 0, 171, 20))
        self.lblTotalAlertsTitle_2.setStyleSheet(u"\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.lblTotalAlertsTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayoutAlerts_2.addWidget(self.frameTotalLogs)

        self.frameWarnings = QFrame(self.layoutWidget_4)
        self.frameWarnings.setObjectName(u"frameWarnings")
        self.frameWarnings.setFrameShape(QFrame.StyledPanel)
        self.frameWarnings.setFrameShadow(QFrame.Sunken)
        self.lblWarningLogs = QLabel(self.frameWarnings)
        self.lblWarningLogs.setObjectName(u"lblWarningLogs")
        self.lblWarningLogs.setGeometry(QRect(10, 20, 161, 31))
        self.lblWarningLogs.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lblWarningLogs.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblHighTitle_2 = QLabel(self.frameWarnings)
        self.lblHighTitle_2.setObjectName(u"lblHighTitle_2")
        self.lblHighTitle_2.setGeometry(QRect(10, 0, 181, 20))
        self.lblHighTitle_2.setStyleSheet(u"\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.lblHighTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayoutAlerts_2.addWidget(self.frameWarnings)

        self.frameErrors = QFrame(self.layoutWidget_4)
        self.frameErrors.setObjectName(u"frameErrors")
        self.frameErrors.setFrameShape(QFrame.StyledPanel)
        self.frameErrors.setFrameShadow(QFrame.Sunken)
        self.lblCriticalTitle_2 = QLabel(self.frameErrors)
        self.lblCriticalTitle_2.setObjectName(u"lblCriticalTitle_2")
        self.lblCriticalTitle_2.setGeometry(QRect(10, 0, 171, 20))
        self.lblCriticalTitle_2.setStyleSheet(u"\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.lblCriticalTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lblErrorLogs = QLabel(self.frameErrors)
        self.lblErrorLogs.setObjectName(u"lblErrorLogs")
        self.lblErrorLogs.setGeometry(QRect(10, 20, 131, 31))
        self.lblErrorLogs.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.lblErrorLogs.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayoutAlerts_2.addWidget(self.frameErrors)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 110, 47, 20))
        self.horizontalLayoutWidget_16 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(30, 130, 491, 31))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.txtSearchLogs = QLineEdit(self.horizontalLayoutWidget_16)
        self.txtSearchLogs.setObjectName(u"txtSearchLogs")

        self.horizontalLayout_5.addWidget(self.txtSearchLogs)

        self.cmbLogLevel = QComboBox(self.horizontalLayoutWidget_16)
        self.cmbLogLevel.addItem("")
        self.cmbLogLevel.addItem("")
        self.cmbLogLevel.addItem("")
        self.cmbLogLevel.addItem("")
        self.cmbLogLevel.addItem("")
        self.cmbLogLevel.setObjectName(u"cmbLogLevel")

        self.horizontalLayout_5.addWidget(self.cmbLogLevel)

        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 160, 91, 21))
        self.tableLogs = QTableWidget(self.frame_2)
        if (self.tableLogs.columnCount() < 4):
            self.tableLogs.setColumnCount(4)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableLogs.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        self.tableLogs.setObjectName(u"tableLogs")
        self.tableLogs.setGeometry(QRect(30, 180, 631, 181))
        self.horizontalLayoutWidget_17 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(500, 360, 160, 41))
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnClearLogs = QPushButton(self.horizontalLayoutWidget_17)
        self.btnClearLogs.setObjectName(u"btnClearLogs")

        self.horizontalLayout_12.addWidget(self.btnClearLogs)

        self.btnExportLogs = QPushButton(self.horizontalLayoutWidget_17)
        self.btnExportLogs.setObjectName(u"btnExportLogs")

        self.horizontalLayout_12.addWidget(self.btnExportLogs)


        self.LayoutLogs.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.pageLogs)
        self.pageAnalytics = QWidget()
        self.pageAnalytics.setObjectName(u"pageAnalytics")
        self.verticalLayoutWidget_12 = QWidget(self.pageAnalytics)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(10, 10, 701, 401))
        self.LayoutAnalytics = QVBoxLayout(self.verticalLayoutWidget_12)
        self.LayoutAnalytics.setObjectName(u"LayoutAnalytics")
        self.LayoutAnalytics.setContentsMargins(0, 0, 0, 0)
        self.frameAnalyticsContent = QFrame(self.verticalLayoutWidget_12)
        self.frameAnalyticsContent.setObjectName(u"frameAnalyticsContent")
        self.frameAnalyticsContent.setFrameShape(QFrame.StyledPanel)
        self.frameAnalyticsContent.setFrameShadow(QFrame.Sunken)
        self.label_15 = QLabel(self.frameAnalyticsContent)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 80, 101, 16))
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_16 = QLabel(self.frameAnalyticsContent)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(350, 80, 101, 16))
        self.label_16.setAlignment(Qt.AlignCenter)
        self.layoutWidget1 = QWidget(self.frameAnalyticsContent)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 100, 661, 121))
        self.ThreatsAnalyticsLay = QHBoxLayout(self.layoutWidget1)
        self.ThreatsAnalyticsLay.setObjectName(u"ThreatsAnalyticsLay")
        self.ThreatsAnalyticsLay.setContentsMargins(0, 0, 0, 0)
        self.frameThreatActivity = QFrame(self.layoutWidget1)
        self.frameThreatActivity.setObjectName(u"frameThreatActivity")
        self.frameThreatActivity.setFrameShape(QFrame.StyledPanel)
        self.frameThreatActivity.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget = QWidget(self.frameThreatActivity)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-10, 0, 351, 121))
        self.LayoutGraphAnalytics = QVBoxLayout(self.verticalLayoutWidget)
        self.LayoutGraphAnalytics.setObjectName(u"LayoutGraphAnalytics")
        self.LayoutGraphAnalytics.setContentsMargins(0, 0, 0, 0)

        self.ThreatsAnalyticsLay.addWidget(self.frameThreatActivity)

        self.frameAttackBreakdown = QFrame(self.layoutWidget1)
        self.frameAttackBreakdown.setObjectName(u"frameAttackBreakdown")
        self.frameAttackBreakdown.setFrameShape(QFrame.StyledPanel)
        self.frameAttackBreakdown.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.frameAttackBreakdown)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 291, 101))
        self.gridLayoutStats = QGridLayout(self.gridLayoutWidget)
        self.gridLayoutStats.setObjectName(u"gridLayoutStats")
        self.gridLayoutStats.setContentsMargins(0, 0, 0, 0)
        self.lblPortScan = QLabel(self.gridLayoutWidget)
        self.lblPortScan.setObjectName(u"lblPortScan")
        self.lblPortScan.setAlignment(Qt.AlignCenter)

        self.gridLayoutStats.addWidget(self.lblPortScan, 0, 0, 1, 1)

        self.lblSynFloodCount = QLabel(self.gridLayoutWidget)
        self.lblSynFloodCount.setObjectName(u"lblSynFloodCount")
        self.lblSynFloodCount.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lblSynFloodCount.setAlignment(Qt.AlignCenter)

        self.gridLayoutStats.addWidget(self.lblSynFloodCount, 1, 1, 1, 1)

        self.lblPortScanCount = QLabel(self.gridLayoutWidget)
        self.lblPortScanCount.setObjectName(u"lblPortScanCount")
        self.lblPortScanCount.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lblPortScanCount.setAlignment(Qt.AlignCenter)

        self.gridLayoutStats.addWidget(self.lblPortScanCount, 0, 1, 1, 1)

        self.lblIcmpFloodCount = QLabel(self.gridLayoutWidget)
        self.lblIcmpFloodCount.setObjectName(u"lblIcmpFloodCount")
        self.lblIcmpFloodCount.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lblIcmpFloodCount.setAlignment(Qt.AlignCenter)

        self.gridLayoutStats.addWidget(self.lblIcmpFloodCount, 2, 1, 1, 1)

        self.lblSynFlood = QLabel(self.gridLayoutWidget)
        self.lblSynFlood.setObjectName(u"lblSynFlood")
        self.lblSynFlood.setAlignment(Qt.AlignCenter)

        self.gridLayoutStats.addWidget(self.lblSynFlood, 1, 0, 1, 1)

        self.lblIcmpFlood = QLabel(self.gridLayoutWidget)
        self.lblIcmpFlood.setObjectName(u"lblIcmpFlood")
        self.lblIcmpFlood.setAlignment(Qt.AlignCenter)

        self.gridLayoutStats.addWidget(self.lblIcmpFlood, 2, 0, 1, 1)

        self.lblArpSpoof = QLabel(self.gridLayoutWidget)
        self.lblArpSpoof.setObjectName(u"lblArpSpoof")
        self.lblArpSpoof.setAlignment(Qt.AlignCenter)

        self.gridLayoutStats.addWidget(self.lblArpSpoof, 3, 0, 1, 1)

        self.lblArpSpoofCount = QLabel(self.gridLayoutWidget)
        self.lblArpSpoofCount.setObjectName(u"lblArpSpoofCount")
        self.lblArpSpoofCount.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.lblArpSpoofCount.setAlignment(Qt.AlignCenter)

        self.gridLayoutStats.addWidget(self.lblArpSpoofCount, 3, 1, 1, 1)


        self.ThreatsAnalyticsLay.addWidget(self.frameAttackBreakdown)

        self.layoutWidget_2 = QWidget(self.frameAnalyticsContent)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(40, 40, 621, 41))
        self.LayoutAnalyticsStats = QHBoxLayout(self.layoutWidget_2)
        self.LayoutAnalyticsStats.setObjectName(u"LayoutAnalyticsStats")
        self.LayoutAnalyticsStats.setContentsMargins(0, 0, 0, 0)
        self.frameTotalPackets = QFrame(self.layoutWidget_2)
        self.frameTotalPackets.setObjectName(u"frameTotalPackets")
        self.frameTotalPackets.setFrameShape(QFrame.StyledPanel)
        self.frameTotalPackets.setFrameShadow(QFrame.Sunken)
        self.lblTotalPackets = QLabel(self.frameTotalPackets)
        self.lblTotalPackets.setObjectName(u"lblTotalPackets")
        self.lblTotalPackets.setGeometry(QRect(0, 20, 151, 20))
        self.lblTotalPackets.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.frameTotalPackets)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 151, 20))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.LayoutAnalyticsStats.addWidget(self.frameTotalPackets)

        self.frameTotalThreats = QFrame(self.layoutWidget_2)
        self.frameTotalThreats.setObjectName(u"frameTotalThreats")
        self.frameTotalThreats.setFrameShape(QFrame.StyledPanel)
        self.frameTotalThreats.setFrameShadow(QFrame.Sunken)
        self.lblTotalThreats = QLabel(self.frameTotalThreats)
        self.lblTotalThreats.setObjectName(u"lblTotalThreats")
        self.lblTotalThreats.setGeometry(QRect(0, 20, 151, 20))
        self.lblTotalThreats.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.frameTotalThreats)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 151, 20))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.LayoutAnalyticsStats.addWidget(self.frameTotalThreats)

        self.frameActiveHosts = QFrame(self.layoutWidget_2)
        self.frameActiveHosts.setObjectName(u"frameActiveHosts")
        self.frameActiveHosts.setFrameShape(QFrame.StyledPanel)
        self.frameActiveHosts.setFrameShadow(QFrame.Sunken)
        self.lblActiveHosts = QLabel(self.frameActiveHosts)
        self.lblActiveHosts.setObjectName(u"lblActiveHosts")
        self.lblActiveHosts.setGeometry(QRect(0, 20, 141, 20))
        self.lblActiveHosts.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.frameActiveHosts)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 151, 20))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.LayoutAnalyticsStats.addWidget(self.frameActiveHosts)

        self.frameUptime = QFrame(self.layoutWidget_2)
        self.frameUptime.setObjectName(u"frameUptime")
        self.frameUptime.setFrameShape(QFrame.StyledPanel)
        self.frameUptime.setFrameShadow(QFrame.Sunken)
        self.lblUptime = QLabel(self.frameUptime)
        self.lblUptime.setObjectName(u"lblUptime")
        self.lblUptime.setGeometry(QRect(0, 20, 151, 20))
        self.lblUptime.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.frameUptime)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 151, 20))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.LayoutAnalyticsStats.addWidget(self.frameUptime)

        self.AnalyitcsPageTitle = QLabel(self.frameAnalyticsContent)
        self.AnalyitcsPageTitle.setObjectName(u"AnalyitcsPageTitle")
        self.AnalyitcsPageTitle.setGeometry(QRect(260, 0, 171, 31))
        self.AnalyitcsPageTitle.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";")
        self.AnalyitcsPageTitle.setAlignment(Qt.AlignCenter)

        self.LayoutAnalytics.addWidget(self.frameAnalyticsContent)

        self.stackedWidget.addWidget(self.pageAnalytics)
        self.pageReports = QWidget()
        self.pageReports.setObjectName(u"pageReports")
        self.verticalLayoutWidget_6 = QWidget(self.pageReports)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 10, 701, 401))
        self.verticalLayoutReports = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayoutReports.setObjectName(u"verticalLayoutReports")
        self.verticalLayoutReports.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameReports = QFrame(self.verticalLayoutWidget_6)
        self.frameReports.setObjectName(u"frameReports")
        self.frameReports.setFrameShape(QFrame.StyledPanel)
        self.frameReports.setFrameShadow(QFrame.Sunken)
        self.horizontalLayoutWidget_3 = QWidget(self.frameReports)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(16, 40, 661, 41))
        self.layoutGenerateReport = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.layoutGenerateReport.setObjectName(u"layoutGenerateReport")
        self.layoutGenerateReport.setContentsMargins(0, 0, 0, 0)
        self.lblReportType = QLabel(self.horizontalLayoutWidget_3)
        self.lblReportType.setObjectName(u"lblReportType")

        self.layoutGenerateReport.addWidget(self.lblReportType)

        self.cmbReportType = QComboBox(self.horizontalLayoutWidget_3)
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.addItem("")
        self.cmbReportType.setObjectName(u"cmbReportType")

        self.layoutGenerateReport.addWidget(self.cmbReportType)

        self.lblDateFrom = QLabel(self.horizontalLayoutWidget_3)
        self.lblDateFrom.setObjectName(u"lblDateFrom")

        self.layoutGenerateReport.addWidget(self.lblDateFrom)

        self.dateReportFrom = QDateEdit(self.horizontalLayoutWidget_3)
        self.dateReportFrom.setObjectName(u"dateReportFrom")
        self.dateReportFrom.setCalendarPopup(True)

        self.layoutGenerateReport.addWidget(self.dateReportFrom)

        self.lblDateTo = QLabel(self.horizontalLayoutWidget_3)
        self.lblDateTo.setObjectName(u"lblDateTo")

        self.layoutGenerateReport.addWidget(self.lblDateTo)

        self.dateReportTo = QDateEdit(self.horizontalLayoutWidget_3)
        self.dateReportTo.setObjectName(u"dateReportTo")

        self.layoutGenerateReport.addWidget(self.dateReportTo)

        self.btnGenerateReport = QPushButton(self.horizontalLayoutWidget_3)
        self.btnGenerateReport.setObjectName(u"btnGenerateReport")

        self.layoutGenerateReport.addWidget(self.btnGenerateReport)

        self.lblReportsSubtitle = QLabel(self.frameReports)
        self.lblReportsSubtitle.setObjectName(u"lblReportsSubtitle")
        self.lblReportsSubtitle.setGeometry(QRect(0, 20, 261, 21))
        self.lblReportsSubtitle.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_13 = QWidget(self.frameReports)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(50, 90, 591, 41))
        self.layoutReportCards = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.layoutReportCards.setObjectName(u"layoutReportCards")
        self.layoutReportCards.setContentsMargins(0, 0, 0, 0)
        self.frameReportsTotalAlerts = QFrame(self.horizontalLayoutWidget_13)
        self.frameReportsTotalAlerts.setObjectName(u"frameReportsTotalAlerts")
        self.frameReportsTotalAlerts.setFrameShape(QFrame.StyledPanel)
        self.frameReportsTotalAlerts.setFrameShadow(QFrame.Sunken)
        self.lblReportTotalAlertsTitle = QLabel(self.frameReportsTotalAlerts)
        self.lblReportTotalAlertsTitle.setObjectName(u"lblReportTotalAlertsTitle")
        self.lblReportTotalAlertsTitle.setGeometry(QRect(0, -1, 141, 21))
        self.lblReportTotalAlertsTitle.setAlignment(Qt.AlignCenter)
        self.label_22 = QLabel(self.frameReportsTotalAlerts)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(-4, 20, 151, 21))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.layoutReportCards.addWidget(self.frameReportsTotalAlerts)

        self.frameHighAlerts = QFrame(self.horizontalLayoutWidget_13)
        self.frameHighAlerts.setObjectName(u"frameHighAlerts")
        self.frameHighAlerts.setFrameShape(QFrame.StyledPanel)
        self.frameHighAlerts.setFrameShadow(QFrame.Sunken)
        self.lblReportHighAlertsTitle = QLabel(self.frameHighAlerts)
        self.lblReportHighAlertsTitle.setObjectName(u"lblReportHighAlertsTitle")
        self.lblReportHighAlertsTitle.setGeometry(QRect(-4, 0, 151, 21))
        self.lblReportHighAlertsTitle.setAlignment(Qt.AlignCenter)
        self.lblReportHighAlerts_2 = QLabel(self.frameHighAlerts)
        self.lblReportHighAlerts_2.setObjectName(u"lblReportHighAlerts_2")
        self.lblReportHighAlerts_2.setGeometry(QRect(0, 20, 141, 21))
        self.lblReportHighAlerts_2.setAlignment(Qt.AlignCenter)

        self.layoutReportCards.addWidget(self.frameHighAlerts)

        self.frameMediumAlerts = QFrame(self.horizontalLayoutWidget_13)
        self.frameMediumAlerts.setObjectName(u"frameMediumAlerts")
        self.frameMediumAlerts.setFrameShape(QFrame.StyledPanel)
        self.frameMediumAlerts.setFrameShadow(QFrame.Sunken)
        self.lblReportMediumAlertsTitle = QLabel(self.frameMediumAlerts)
        self.lblReportMediumAlertsTitle.setObjectName(u"lblReportMediumAlertsTitle")
        self.lblReportMediumAlertsTitle.setGeometry(QRect(0, 0, 141, 20))
        self.lblReportMediumAlertsTitle.setAlignment(Qt.AlignCenter)
        self.lblReportMediumAlerts = QLabel(self.frameMediumAlerts)
        self.lblReportMediumAlerts.setObjectName(u"lblReportMediumAlerts")
        self.lblReportMediumAlerts.setGeometry(QRect(0, 20, 141, 21))
        self.lblReportMediumAlerts.setAlignment(Qt.AlignCenter)

        self.layoutReportCards.addWidget(self.frameMediumAlerts)

        self.frameLowAlerts = QFrame(self.horizontalLayoutWidget_13)
        self.frameLowAlerts.setObjectName(u"frameLowAlerts")
        self.frameLowAlerts.setFrameShape(QFrame.StyledPanel)
        self.frameLowAlerts.setFrameShadow(QFrame.Sunken)
        self.lblReportLowAlertsTitle = QLabel(self.frameLowAlerts)
        self.lblReportLowAlertsTitle.setObjectName(u"lblReportLowAlertsTitle")
        self.lblReportLowAlertsTitle.setGeometry(QRect(0, 0, 141, 21))
        self.lblReportLowAlertsTitle.setAlignment(Qt.AlignCenter)
        self.lblReportLowAlerts = QLabel(self.frameLowAlerts)
        self.lblReportLowAlerts.setObjectName(u"lblReportLowAlerts")
        self.lblReportLowAlerts.setGeometry(QRect(0, 20, 141, 21))
        self.lblReportLowAlerts.setAlignment(Qt.AlignCenter)

        self.layoutReportCards.addWidget(self.frameLowAlerts)

        self.tableReports = QTableWidget(self.frameReports)
        if (self.tableReports.columnCount() < 5):
            self.tableReports.setColumnCount(5)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter)
        self.tableReports.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter)
        self.tableReports.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter)
        self.tableReports.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter)
        self.tableReports.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter)
        self.tableReports.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        self.tableReports.setObjectName(u"tableReports")
        self.tableReports.setGeometry(QRect(90, 140, 511, 201))
        self.tableReports.setLayoutDirection(Qt.LeftToRight)
        self.tableReports.setFrameShape(QFrame.StyledPanel)
        self.tableReports.setFrameShadow(QFrame.Sunken)
        self.tableReports.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableReports.setAlternatingRowColors(True)
        self.tableReports.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalLayoutWidget_14 = QWidget(self.frameReports)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(190, 350, 321, 31))
        self.layourRepotsBtns = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.layourRepotsBtns.setObjectName(u"layourRepotsBtns")
        self.layourRepotsBtns.setContentsMargins(0, 0, 0, 0)
        self.btnExportCSV_2 = QPushButton(self.horizontalLayoutWidget_14)
        self.btnExportCSV_2.setObjectName(u"btnExportCSV_2")

        self.layourRepotsBtns.addWidget(self.btnExportCSV_2)

        self.btnExportPDF = QPushButton(self.horizontalLayoutWidget_14)
        self.btnExportPDF.setObjectName(u"btnExportPDF")

        self.layourRepotsBtns.addWidget(self.btnExportPDF)

        self.btnResetReport = QPushButton(self.horizontalLayoutWidget_14)
        self.btnResetReport.setObjectName(u"btnResetReport")

        self.layourRepotsBtns.addWidget(self.btnResetReport)


        self.verticalLayout.addWidget(self.frameReports)


        self.verticalLayoutReports.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.pageReports)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.verticalLayout_14 = QVBoxLayout(self.pageSettings)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayoutSettings = QVBoxLayout()
        self.verticalLayoutSettings.setObjectName(u"verticalLayoutSettings")
        self.scrollArea = QScrollArea(self.pageSettings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 28))
        self.frameSettings = QFrame(self.scrollAreaWidgetContents)
        self.frameSettings.setObjectName(u"frameSettings")
        self.frameSettings.setGeometry(QRect(0, 0, 701, 399))
        self.frameSettings.setMinimumSize(QSize(0, 120))
        self.frameSettings.setFrameShape(QFrame.StyledPanel)
        self.frameSettings.setFrameShadow(QFrame.Raised)
        self.groupDetection = QGroupBox(self.frameSettings)
        self.groupDetection.setObjectName(u"groupDetection")
        self.groupDetection.setGeometry(QRect(10, 170, 201, 151))
        self.formLayoutWidget_2 = QWidget(self.groupDetection)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(20, 20, 151, 126))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.label_8 = QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.label_9 = QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.label_10 = QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.label_11 = QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.spinPortScanWindow = QSpinBox(self.formLayoutWidget_2)
        self.spinPortScanWindow.setObjectName(u"spinPortScanWindow")
        self.spinPortScanWindow.setValue(5)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinPortScanWindow)

        self.spinSynWindow = QSpinBox(self.formLayoutWidget_2)
        self.spinSynWindow.setObjectName(u"spinSynWindow")
        self.spinSynWindow.setValue(5)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinSynWindow)

        self.spinCooldown = QSpinBox(self.formLayoutWidget_2)
        self.spinCooldown.setObjectName(u"spinCooldown")
        self.spinCooldown.setValue(30)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.spinCooldown)

        self.spinSynThreshold = QSpinBox(self.formLayoutWidget_2)
        self.spinSynThreshold.setObjectName(u"spinSynThreshold")
        self.spinSynThreshold.setValue(20)

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinSynThreshold)

        self.spinPortScanThreshold = QSpinBox(self.formLayoutWidget_2)
        self.spinPortScanThreshold.setObjectName(u"spinPortScanThreshold")
        self.spinPortScanThreshold.setValue(20)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinPortScanThreshold)

        self.groupAppearance = QGroupBox(self.frameSettings)
        self.groupAppearance.setObjectName(u"groupAppearance")
        self.groupAppearance.setGeometry(QRect(450, 140, 241, 91))
        self.formLayoutWidget_3 = QWidget(self.groupAppearance)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(20, 20, 211, 54))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cmbAccent = QComboBox(self.formLayoutWidget_3)
        self.cmbAccent.addItem("")
        self.cmbAccent.setObjectName(u"cmbAccent")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbAccent)

        self.cmbTheme = QComboBox(self.formLayoutWidget_3)
        self.cmbTheme.addItem("")
        self.cmbTheme.addItem("")
        self.cmbTheme.setObjectName(u"cmbTheme")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbTheme)

        self.label_3 = QLabel(self.formLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_14 = QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.groupBox_3 = QGroupBox(self.frameSettings)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 50, 431, 111))
        self.formLayoutWidget = QWidget(self.groupBox_3)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 50, 161, 51))
        self.formLayoutGenSettings = QFormLayout(self.formLayoutWidget)
        self.formLayoutGenSettings.setObjectName(u"formLayoutGenSettings")
        self.formLayoutGenSettings.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayoutGenSettings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.spinPacketHistory = QSpinBox(self.formLayoutWidget)
        self.spinPacketHistory.setObjectName(u"spinPacketHistory")
        self.spinPacketHistory.setMinimum(10)
        self.spinPacketHistory.setMaximum(10000)
        self.spinPacketHistory.setValue(500)

        self.formLayoutGenSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinPacketHistory)

        self.lblRefreshRate = QLabel(self.formLayoutWidget)
        self.lblRefreshRate.setObjectName(u"lblRefreshRate")

        self.formLayoutGenSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblRefreshRate)

        self.spinRefreshRate = QSpinBox(self.formLayoutWidget)
        self.spinRefreshRate.setObjectName(u"spinRefreshRate")
        self.spinRefreshRate.setMinimum(100)
        self.spinRefreshRate.setMaximum(10000)
        self.spinRefreshRate.setValue(100)

        self.formLayoutGenSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinRefreshRate)

        self.cmbSetInterface = QComboBox(self.groupBox_3)
        self.cmbSetInterface.setObjectName(u"cmbSetInterface")
        self.cmbSetInterface.setGeometry(QRect(131, 20, 281, 20))
        self.lblInterfaces = QLabel(self.groupBox_3)
        self.lblInterfaces.setObjectName(u"lblInterfaces")
        self.lblInterfaces.setGeometry(QRect(20, 20, 105, 20))
        self.horizontalLayoutWidget_8 = QWidget(self.frameSettings)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(120, 350, 431, 41))
        self.ButtonsLayout = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.ButtonsLayout.setObjectName(u"ButtonsLayout")
        self.ButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSaveSettings = QPushButton(self.horizontalLayoutWidget_8)
        self.btnSaveSettings.setObjectName(u"btnSaveSettings")

        self.ButtonsLayout.addWidget(self.btnSaveSettings)

        self.btnResetSettings = QPushButton(self.horizontalLayoutWidget_8)
        self.btnResetSettings.setObjectName(u"btnResetSettings")

        self.ButtonsLayout.addWidget(self.btnResetSettings)

        self.groupNotifications = QGroupBox(self.frameSettings)
        self.groupNotifications.setObjectName(u"groupNotifications")
        self.groupNotifications.setGeometry(QRect(220, 170, 221, 151))
        self.verticalLayoutWidget_8 = QWidget(self.groupNotifications)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(20, 20, 181, 121))
        self.LayoutSetNoti = QVBoxLayout(self.verticalLayoutWidget_8)
        self.LayoutSetNoti.setObjectName(u"LayoutSetNoti")
        self.LayoutSetNoti.setContentsMargins(0, 0, 0, 0)
        self.chkSaveDatabase = QCheckBox(self.verticalLayoutWidget_8)
        self.chkSaveDatabase.setObjectName(u"chkSaveDatabase")

        self.LayoutSetNoti.addWidget(self.chkSaveDatabase)

        self.chkWriteLog = QCheckBox(self.verticalLayoutWidget_8)
        self.chkWriteLog.setObjectName(u"chkWriteLog")

        self.LayoutSetNoti.addWidget(self.chkWriteLog)

        self.chkPopup = QCheckBox(self.verticalLayoutWidget_8)
        self.chkPopup.setObjectName(u"chkPopup")

        self.LayoutSetNoti.addWidget(self.chkPopup)

        self.chkPlaySound = QCheckBox(self.verticalLayoutWidget_8)
        self.chkPlaySound.setObjectName(u"chkPlaySound")

        self.LayoutSetNoti.addWidget(self.chkPlaySound)

        self.lblSettingsTitle = QLabel(self.frameSettings)
        self.lblSettingsTitle.setObjectName(u"lblSettingsTitle")
        self.lblSettingsTitle.setGeometry(QRect(20, 0, 141, 51))
        self.lblSettingsTitle.setStyleSheet(u"font: 75 22pt \"MS Shell Dlg 2\";")
        self.lblSettingsTitle.setAlignment(Qt.AlignCenter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayoutSettings.addWidget(self.scrollArea)


        self.verticalLayout_14.addLayout(self.verticalLayoutSettings)

        self.stackedWidget.addWidget(self.pageSettings)
        self.pageSimulator = QWidget()
        self.pageSimulator.setObjectName(u"pageSimulator")
        self.verticalLayoutWidget_10 = QWidget(self.pageSimulator)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 10, 701, 401))
        self.verticalLayoutSimulator = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayoutSimulator.setObjectName(u"verticalLayoutSimulator")
        self.verticalLayoutSimulator.setContentsMargins(0, 0, 0, 0)
        self.frameSimulator = QFrame(self.verticalLayoutWidget_10)
        self.frameSimulator.setObjectName(u"frameSimulator")
        self.frameSimulator.setFrameShape(QFrame.StyledPanel)
        self.frameSimulator.setFrameShadow(QFrame.Sunken)
        self.lblSimulatorTitle = QLabel(self.frameSimulator)
        self.lblSimulatorTitle.setObjectName(u"lblSimulatorTitle")
        self.lblSimulatorTitle.setGeometry(QRect(20, 20, 191, 41))
        font1 = QFont()
        font1.setPointSize(18)
        self.lblSimulatorTitle.setFont(font1)
        self.lblSimulatorTitle.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_10 = QWidget(self.frameSimulator)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(30, 60, 271, 31))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.lblAttactTypeSim = QLabel(self.horizontalLayoutWidget_10)
        self.lblAttactTypeSim.setObjectName(u"lblAttactTypeSim")

        self.horizontalLayout_10.addWidget(self.lblAttactTypeSim)

        self.cmbAttackType = QComboBox(self.horizontalLayoutWidget_10)
        self.cmbAttackType.setObjectName(u"cmbAttackType")

        self.horizontalLayout_10.addWidget(self.cmbAttackType)

        self.horizontalLayoutWidget_12 = QWidget(self.frameSimulator)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(30, 100, 211, 41))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lblPacketsTitle = QLabel(self.horizontalLayoutWidget_12)
        self.lblPacketsTitle.setObjectName(u"lblPacketsTitle")

        self.horizontalLayout_11.addWidget(self.lblPacketsTitle)

        self.spinSimPacketCount = QSpinBox(self.horizontalLayoutWidget_12)
        self.spinSimPacketCount.setObjectName(u"spinSimPacketCount")

        self.horizontalLayout_11.addWidget(self.spinSimPacketCount)

        self.btnRunSimulation = QPushButton(self.horizontalLayoutWidget_12)
        self.btnRunSimulation.setObjectName(u"btnRunSimulation")

        self.horizontalLayout_11.addWidget(self.btnRunSimulation)

        self.horizontalLayoutWidget_15 = QWidget(self.frameSimulator)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(30, 150, 641, 231))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.txtSimulationLog = QTextEdit(self.horizontalLayoutWidget_15)
        self.txtSimulationLog.setObjectName(u"txtSimulationLog")
        self.txtSimulationLog.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.txtSimulationLog)

        self.btnClearLogSim = QPushButton(self.horizontalLayoutWidget_15)
        self.btnClearLogSim.setObjectName(u"btnClearLogSim")

        self.horizontalLayout_15.addWidget(self.btnClearLogSim)


        self.verticalLayoutSimulator.addWidget(self.frameSimulator)

        self.stackedWidget.addWidget(self.pageSimulator)
        self.pageDatabase = QWidget()
        self.pageDatabase.setObjectName(u"pageDatabase")
        self.verticalLayoutWidget_7 = QWidget(self.pageDatabase)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 10, 701, 401))
        self.verticalLayoutDatabase = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayoutDatabase.setObjectName(u"verticalLayoutDatabase")
        self.verticalLayoutDatabase.setContentsMargins(0, 0, 0, 0)
        self.frameDatabase = QFrame(self.verticalLayoutWidget_7)
        self.frameDatabase.setObjectName(u"frameDatabase")
        self.frameDatabase.setFrameShape(QFrame.StyledPanel)
        self.frameDatabase.setFrameShadow(QFrame.Sunken)
        self.lblDatabaseTitle = QLabel(self.frameDatabase)
        self.lblDatabaseTitle.setObjectName(u"lblDatabaseTitle")
        self.lblDatabaseTitle.setGeometry(QRect(240, 10, 191, 21))
        self.lblDatabaseTitle.setFont(font1)
        self.lblDatabaseTitle.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_2 = QWidget(self.frameDatabase)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 40, 671, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.txtSearch = QLineEdit(self.horizontalLayoutWidget_2)
        self.txtSearch.setObjectName(u"txtSearch")

        self.horizontalLayout_3.addWidget(self.txtSearch)

        self.btnSearch = QPushButton(self.horizontalLayoutWidget_2)
        self.btnSearch.setObjectName(u"btnSearch")

        self.horizontalLayout_3.addWidget(self.btnSearch)

        self.tableDatabase = QTableWidget(self.frameDatabase)
        if (self.tableDatabase.columnCount() < 12):
            self.tableDatabase.setColumnCount(12)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableDatabase.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableDatabase.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableDatabase.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableDatabase.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableDatabase.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableDatabase.setHorizontalHeaderItem(5, __qtablewidgetitem41)
        self.tableDatabase.setObjectName(u"tableDatabase")
        self.tableDatabase.setGeometry(QRect(10, 121, 681, 231))
        self.tableDatabase.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableDatabase.setAlternatingRowColors(True)
        self.tableDatabase.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableDatabase.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableDatabase.setSortingEnabled(True)
        self.tableDatabase.setColumnCount(12)
        self.tableDatabase.horizontalHeader().setStretchLastSection(True)
        self.tableDatabase.verticalHeader().setStretchLastSection(True)
        self.horizontalLayoutWidget_5 = QWidget(self.frameDatabase)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(40, 360, 621, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnDeleteAlert = QPushButton(self.horizontalLayoutWidget_5)
        self.btnDeleteAlert.setObjectName(u"btnDeleteAlert")

        self.horizontalLayout_6.addWidget(self.btnDeleteAlert)

        self.btnClearDatabase = QPushButton(self.horizontalLayoutWidget_5)
        self.btnClearDatabase.setObjectName(u"btnClearDatabase")

        self.horizontalLayout_6.addWidget(self.btnClearDatabase)

        self.btnExportCSV = QPushButton(self.horizontalLayoutWidget_5)
        self.btnExportCSV.setObjectName(u"btnExportCSV")

        self.horizontalLayout_6.addWidget(self.btnExportCSV)

        self.btnRefreshDatabase = QPushButton(self.horizontalLayoutWidget_5)
        self.btnRefreshDatabase.setObjectName(u"btnRefreshDatabase")

        self.horizontalLayout_6.addWidget(self.btnRefreshDatabase)

        self.horizontalLayoutWidget_6 = QWidget(self.frameDatabase)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(50, 80, 621, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lblThreatDatabaseSel = QLabel(self.horizontalLayoutWidget_6)
        self.lblThreatDatabaseSel.setObjectName(u"lblThreatDatabaseSel")

        self.horizontalLayout_4.addWidget(self.lblThreatDatabaseSel)

        self.cmbThreat = QComboBox(self.horizontalLayoutWidget_6)
        self.cmbThreat.addItem("")
        self.cmbThreat.addItem("")
        self.cmbThreat.addItem("")
        self.cmbThreat.addItem("")
        self.cmbThreat.addItem("")
        self.cmbThreat.setObjectName(u"cmbThreat")

        self.horizontalLayout_4.addWidget(self.cmbThreat)

        self.lblSeveritySel = QLabel(self.horizontalLayoutWidget_6)
        self.lblSeveritySel.setObjectName(u"lblSeveritySel")

        self.horizontalLayout_4.addWidget(self.lblSeveritySel)

        self.cmbSeverity = QComboBox(self.horizontalLayoutWidget_6)
        self.cmbSeverity.addItem("")
        self.cmbSeverity.addItem("")
        self.cmbSeverity.addItem("")
        self.cmbSeverity.addItem("")
        self.cmbSeverity.addItem("")
        self.cmbSeverity.setObjectName(u"cmbSeverity")

        self.horizontalLayout_4.addWidget(self.cmbSeverity)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayoutDatabase.addWidget(self.frameDatabase)

        self.stackedWidget.addWidget(self.pageDatabase)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 430, 951, 51))
        self.verticalLayoutState = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayoutState.setObjectName(u"verticalLayoutState")
        self.verticalLayoutState.setContentsMargins(0, 0, 0, 0)
        self.frameState = QFrame(self.verticalLayoutWidget_3)
        self.frameState.setObjectName(u"frameState")
        self.frameState.setFrameShape(QFrame.StyledPanel)
        self.frameState.setFrameShadow(QFrame.Raised)
        self.lblStatusTitle = QLabel(self.frameState)
        self.lblStatusTitle.setObjectName(u"lblStatusTitle")
        self.lblStatusTitle.setGeometry(QRect(20, 0, 51, 20))
        self.lblStatusDetail = QLabel(self.frameState)
        self.lblStatusDetail.setObjectName(u"lblStatusDetail")
        self.lblStatusDetail.setGeometry(QRect(70, 0, 101, 21))
        self.lblInterfaceDetail = QLabel(self.frameState)
        self.lblInterfaceDetail.setObjectName(u"lblInterfaceDetail")
        self.lblInterfaceDetail.setGeometry(QRect(80, 20, 291, 21))
        self.lblInterfaceTitle = QLabel(self.frameState)
        self.lblInterfaceTitle.setObjectName(u"lblInterfaceTitle")
        self.lblInterfaceTitle.setGeometry(QRect(20, 20, 51, 20))

        self.verticalLayoutState.addWidget(self.frameState)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 968, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuScan = QMenu(self.menubar)
        self.menuScan.setObjectName(u"menuScan")
        self.menuReports = QMenu(self.menubar)
        self.menuReports.setObjectName(u"menuReports")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuScan.menuAction())
        self.menubar.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.actionAbout)
        self.toolBar.addAction(self.actionStartMonitoring)
        self.toolBar.addAction(self.actionStopMonitoring)
        self.toolBar.addAction(self.actionClearAlerts)
        self.toolBar.addAction(self.actionExportReport)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AW3NIDS", None))
        self.actionStartMonitoring.setText(QCoreApplication.translate("MainWindow", u"Start Monitoring", None))
        self.actionStopMonitoring.setText(QCoreApplication.translate("MainWindow", u"Stop Monitoring", None))
        self.actionClearAlerts.setText(QCoreApplication.translate("MainWindow", u"Clear Table", None))
        self.actionExportReport.setText(QCoreApplication.translate("MainWindow", u"Export Report", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About AW3NIDS", None))
        self.iblAppLogo.setText(QCoreApplication.translate("MainWindow", u"AW3NIDS", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.btnLiveCapture.setText(QCoreApplication.translate("MainWindow", u"Live Capture", None))
        self.btnAlerts.setText(QCoreApplication.translate("MainWindow", u"Alerts", None))
        self.btnSimulator.setText(QCoreApplication.translate("MainWindow", u"Attack Simulator", None))
        self.btnAnalytics.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.btnDatabase.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.btnReports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btnLogs.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lblPacketTitle.setText(QCoreApplication.translate("MainWindow", u"Packets Captured", None))
        self.lblPacketCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblHostTitle.setText(QCoreApplication.translate("MainWindow", u"Active Hosts", None))
        self.lblHostCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblNetworkStatusTitle.setText(QCoreApplication.translate("MainWindow", u"Network Status", None))
        self.lblNetworkStatus.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.lblThreatTitle.setText(QCoreApplication.translate("MainWindow", u"Threats Detected", None))
        self.lblThreatCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblNetworkTraffic.setText(QCoreApplication.translate("MainWindow", u"Network Traffic Graph", None))
        self.lblLivePacketsHeader.setText(QCoreApplication.translate("MainWindow", u"Live Packets", None))
        ___qtablewidgetitem = self.tableLivePackets.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        ___qtablewidgetitem1 = self.tableLivePackets.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Source IP", None))
        ___qtablewidgetitem2 = self.tableLivePackets.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Destination IP", None))
        ___qtablewidgetitem3 = self.tableLivePackets.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Protocol", None))
        ___qtablewidgetitem4 = self.tableLivePackets.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem5 = self.tableRecentAlerts.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        ___qtablewidgetitem6 = self.tableRecentAlerts.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Threat", None))
        ___qtablewidgetitem7 = self.tableRecentAlerts.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Source IP", None))
        ___qtablewidgetitem8 = self.tableRecentAlerts.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Severity", None))
        ___qtablewidgetitem9 = self.tableRecentAlerts.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        ___qtablewidgetitem10 = self.tableRecentAlerts.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.lblRecentAlerts.setText(QCoreApplication.translate("MainWindow", u"Recent Alerts", None))
        self.cmbInterface.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))

        self.cmbInterface.setCurrentText(QCoreApplication.translate("MainWindow", u"None", None))
        self.lblInterface.setText(QCoreApplication.translate("MainWindow", u"Interface", None))
        self.btnRefreshInterfaces.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.lblLivePacketTable.setText(QCoreApplication.translate("MainWindow", u"Live Packet Table", None))
        ___qtablewidgetitem11 = self.tableLivePackets_2.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        ___qtablewidgetitem12 = self.tableLivePackets_2.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Source ", None))
        ___qtablewidgetitem13 = self.tableLivePackets_2.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Destination ", None))
        ___qtablewidgetitem14 = self.tableLivePackets_2.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Protocol", None))
        ___qtablewidgetitem15 = self.tableLivePackets_2.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.GroupCaptureDetails_2.setTitle(QCoreApplication.translate("MainWindow", u"Packet Details", None))
        self.lblDetailTime.setText("")
        self.lblDetailSrc.setText("")
        self.lblDetailDst.setText("")
        self.lblDetailProtocol.setText("")
        self.lblDetailSrcPort.setText("")
        self.lblDetailTTL.setText("")
        self.lblDetailLength.setText("")
        self.lblDetailFlags.setText("")
        self.lblDetailDstPort.setText("")
        self.GroupCaptureDetails.setTitle("")
        self.time.setText(QCoreApplication.translate("MainWindow", u"Time: ", None))
        self.sourceip.setText(QCoreApplication.translate("MainWindow", u"Source IP:", None))
        self.destination.setText(QCoreApplication.translate("MainWindow", u"Desination IP:", None))
        self.protocol.setText(QCoreApplication.translate("MainWindow", u"Protocol: ", None))
        self.sourceports.setText(QCoreApplication.translate("MainWindow", u"Source Ports: ", None))
        self.ttl.setText(QCoreApplication.translate("MainWindow", u"TTL: ", None))
        self.length.setText(QCoreApplication.translate("MainWindow", u"Length:", None))
        self.flags.setText(QCoreApplication.translate("MainWindow", u"TCP Flags: ", None))
        self.destinationport.setText(QCoreApplication.translate("MainWindow", u"Destination Port:", None))
        self.btnStartCapture.setText(QCoreApplication.translate("MainWindow", u"Start Capture", None))
        self.btnStopCapture.setText(QCoreApplication.translate("MainWindow", u"Stop Capture", None))
        self.lblTotalAlerts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblTotalAlertsTitle.setText(QCoreApplication.translate("MainWindow", u"Total Alerts", None))
        self.lblMediumTitle.setText(QCoreApplication.translate("MainWindow", u"MEDIUM", None))
        self.lblMediumAlerts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblHighAlerts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblHighTitle.setText(QCoreApplication.translate("MainWindow", u"HIGH ", None))
        self.lblCriticalTitle.setText(QCoreApplication.translate("MainWindow", u"CRITICAL", None))
        self.lblCriticalAlerts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"View Details", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Clear Alerts", None))
        self.lblSearchSeverity.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.txtSearchAlerts.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search alerts...", None))
        self.comboSeverity.setItemText(0, QCoreApplication.translate("MainWindow", u"All Severities", None))
        self.comboSeverity.setItemText(1, QCoreApplication.translate("MainWindow", u"Critical", None))
        self.comboSeverity.setItemText(2, QCoreApplication.translate("MainWindow", u"High", None))
        self.comboSeverity.setItemText(3, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.comboSeverity.setItemText(4, QCoreApplication.translate("MainWindow", u"Low", None))

        self.cmbAlertType.setItemText(0, QCoreApplication.translate("MainWindow", u"All Types", None))
        self.cmbAlertType.setItemText(1, QCoreApplication.translate("MainWindow", u"Port Scan", None))
        self.cmbAlertType.setItemText(2, QCoreApplication.translate("MainWindow", u"SYN Flood", None))
        self.cmbAlertType.setItemText(3, QCoreApplication.translate("MainWindow", u"Suspicious Traffic", None))
        self.cmbAlertType.setItemText(4, QCoreApplication.translate("MainWindow", u"Other", None))

        self.btnClearFilters.setText(QCoreApplication.translate("MainWindow", u"Clear Filters", None))
        ___qtablewidgetitem16 = self.tableAlerts.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        ___qtablewidgetitem17 = self.tableAlerts.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Sevcerity", None))
        ___qtablewidgetitem18 = self.tableAlerts.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Alert Type", None))
        ___qtablewidgetitem19 = self.tableAlerts.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Source IP", None))
        ___qtablewidgetitem20 = self.tableAlerts.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Destination IP", None))
        ___qtablewidgetitem21 = self.tableAlerts.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Protocol", None))
        ___qtablewidgetitem22 = self.tableAlerts.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.lblIPResponse.setText(QCoreApplication.translate("MainWindow", u" Alert Response", None))
        ___qtablewidgetitem23 = self.tableBlockedIPs.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        ___qtablewidgetitem24 = self.tableBlockedIPs.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Blocked At", None))
        ___qtablewidgetitem25 = self.tableBlockedIPs.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Reason", None))
        ___qtablewidgetitem26 = self.tableBlockedIPs.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.lblIPAddress.setText(QCoreApplication.translate("MainWindow", u"IP Address:", None))
        self.txtIPAddress.setText("")
        self.txtIPAddress.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter IP Address...", None))
        self.btnBlockIP.setText(QCoreApplication.translate("MainWindow", u"Block IP", None))
        self.btnUnblockIP.setText(QCoreApplication.translate("MainWindow", u"Unblock IP", None))
        self.AlertsPageTitle.setText(QCoreApplication.translate("MainWindow", u"Alerts", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"View and investigate AW3NIDS application events", None))
        self.LogsPageTitle.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.lblTotalLogs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblTotalAlertsTitle_2.setText(QCoreApplication.translate("MainWindow", u"Total Logs", None))
        self.lblWarningLogs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblHighTitle_2.setText(QCoreApplication.translate("MainWindow", u"Warnings ", None))
        self.lblCriticalTitle_2.setText(QCoreApplication.translate("MainWindow", u"Errors", None))
        self.lblErrorLogs.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Filters", None))
        self.txtSearchLogs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search messages...", None))
        self.cmbLogLevel.setItemText(0, QCoreApplication.translate("MainWindow", u"All Levels", None))
        self.cmbLogLevel.setItemText(1, QCoreApplication.translate("MainWindow", u"INFO", None))
        self.cmbLogLevel.setItemText(2, QCoreApplication.translate("MainWindow", u"WARNING", None))
        self.cmbLogLevel.setItemText(3, QCoreApplication.translate("MainWindow", u"ERROR", None))
        self.cmbLogLevel.setItemText(4, QCoreApplication.translate("MainWindow", u"CRITICAL", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Event history", None))
        ___qtablewidgetitem27 = self.tableLogs.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        ___qtablewidgetitem28 = self.tableLogs.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Level", None))
        ___qtablewidgetitem29 = self.tableLogs.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        ___qtablewidgetitem30 = self.tableLogs.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btnClearLogs.setText(QCoreApplication.translate("MainWindow", u"Clear Logs", None))
        self.btnExportLogs.setText(QCoreApplication.translate("MainWindow", u"Export Logs", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Threat Activity", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Attack Breakdown", None))
        self.lblPortScan.setText(QCoreApplication.translate("MainWindow", u"Port Scan", None))
        self.lblSynFloodCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblPortScanCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblIcmpFloodCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblSynFlood.setText(QCoreApplication.translate("MainWindow", u"SYN Flood", None))
        self.lblIcmpFlood.setText(QCoreApplication.translate("MainWindow", u"ICMP Flood", None))
        self.lblArpSpoof.setText(QCoreApplication.translate("MainWindow", u"ARP Spoof", None))
        self.lblArpSpoofCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblTotalPackets.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Packets", None))
        self.lblTotalThreats.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Threats", None))
        self.lblActiveHosts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Active Hosts", None))
        self.lblUptime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Uptime", None))
        self.AnalyitcsPageTitle.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
        self.lblReportType.setText(QCoreApplication.translate("MainWindow", u"Report Type:", None))
        self.cmbReportType.setItemText(0, QCoreApplication.translate("MainWindow", u"All Alerts", None))
        self.cmbReportType.setItemText(1, QCoreApplication.translate("MainWindow", u"SYN Flood", None))
        self.cmbReportType.setItemText(2, QCoreApplication.translate("MainWindow", u"Port Scan", None))
        self.cmbReportType.setItemText(3, QCoreApplication.translate("MainWindow", u"Other Threats", None))

        self.lblDateFrom.setText(QCoreApplication.translate("MainWindow", u"Date From:", None))
        self.lblDateTo.setText(QCoreApplication.translate("MainWindow", u"Date To:", None))
        self.btnGenerateReport.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        self.lblReportsSubtitle.setText(QCoreApplication.translate("MainWindow", u"Generate and review intrusion detection reports", None))
        self.lblReportTotalAlertsTitle.setText(QCoreApplication.translate("MainWindow", u"Total Alerts", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblReportHighAlertsTitle.setText(QCoreApplication.translate("MainWindow", u"High Severity", None))
        self.lblReportHighAlerts_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblReportMediumAlertsTitle.setText(QCoreApplication.translate("MainWindow", u"Medium Severity", None))
        self.lblReportMediumAlerts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lblReportLowAlertsTitle.setText(QCoreApplication.translate("MainWindow", u"Low Severity", None))
        self.lblReportLowAlerts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem31 = self.tableReports.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        ___qtablewidgetitem32 = self.tableReports.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Threat", None))
        ___qtablewidgetitem33 = self.tableReports.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Source IP", None))
        ___qtablewidgetitem34 = self.tableReports.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Severity", None))
        ___qtablewidgetitem35 = self.tableReports.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.btnExportCSV_2.setText(QCoreApplication.translate("MainWindow", u"Export CSV", None))
        self.btnExportPDF.setText(QCoreApplication.translate("MainWindow", u"Export PDF", None))
        self.btnResetReport.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.groupDetection.setTitle(QCoreApplication.translate("MainWindow", u"Detection Settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Port Scan Threshold ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"SYN Flood Threshold", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Port Scan Window ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SYN Window", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Alert Cooldown", None))
        self.groupAppearance.setTitle(QCoreApplication.translate("MainWindow", u"Appearance", None))
        self.cmbAccent.setItemText(0, QCoreApplication.translate("MainWindow", u"Blue", None))

        self.cmbTheme.setItemText(0, QCoreApplication.translate("MainWindow", u"Light", None))
        self.cmbTheme.setItemText(1, QCoreApplication.translate("MainWindow", u"Dark", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Accent Color", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"General Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Packet History", None))
        self.lblRefreshRate.setText(QCoreApplication.translate("MainWindow", u"Refresh Rate (ms)", None))
        self.lblInterfaces.setText(QCoreApplication.translate("MainWindow", u"Monitoring Interface: ", None))
        self.btnSaveSettings.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.btnResetSettings.setText(QCoreApplication.translate("MainWindow", u"Reset Settings", None))
        self.groupNotifications.setTitle(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.chkSaveDatabase.setText(QCoreApplication.translate("MainWindow", u"Save Alerts to Database", None))
        self.chkWriteLog.setText(QCoreApplication.translate("MainWindow", u"Write Log File", None))
        self.chkPopup.setText(QCoreApplication.translate("MainWindow", u"Popup Notification", None))
        self.chkPlaySound.setText(QCoreApplication.translate("MainWindow", u"Play Sounds", None))
        self.lblSettingsTitle.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lblSimulatorTitle.setText(QCoreApplication.translate("MainWindow", u"Attack Simulator", None))
        self.lblAttactTypeSim.setText(QCoreApplication.translate("MainWindow", u"Attack Type:", None))
        self.lblPacketsTitle.setText(QCoreApplication.translate("MainWindow", u"Packets:", None))
        self.spinSimPacketCount.setSpecialValueText(QCoreApplication.translate("MainWindow", u"100", None))
        self.btnRunSimulation.setText(QCoreApplication.translate("MainWindow", u"Start Simulation", None))
        self.btnClearLogSim.setText(QCoreApplication.translate("MainWindow", u"Clear Log", None))
        self.lblDatabaseTitle.setText(QCoreApplication.translate("MainWindow", u"Database Viewer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Search:", None))
        self.txtSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by ip Address...", None))
        self.btnSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem36 = self.tableDatabase.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        ___qtablewidgetitem37 = self.tableDatabase.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Threat", None))
        ___qtablewidgetitem38 = self.tableDatabase.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Source IP", None))
        ___qtablewidgetitem39 = self.tableDatabase.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Severity", None))
        ___qtablewidgetitem40 = self.tableDatabase.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem41 = self.tableDatabase.horizontalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.btnDeleteAlert.setText(QCoreApplication.translate("MainWindow", u"Delete Selected", None))
        self.btnClearDatabase.setText(QCoreApplication.translate("MainWindow", u"Clear Database", None))
        self.btnExportCSV.setText(QCoreApplication.translate("MainWindow", u"Export CSV", None))
        self.btnRefreshDatabase.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.lblThreatDatabaseSel.setText(QCoreApplication.translate("MainWindow", u"Threat:", None))
        self.cmbThreat.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.cmbThreat.setItemText(1, QCoreApplication.translate("MainWindow", u"Port Scan", None))
        self.cmbThreat.setItemText(2, QCoreApplication.translate("MainWindow", u"SYN Flood", None))
        self.cmbThreat.setItemText(3, QCoreApplication.translate("MainWindow", u"ICMP Flood", None))
        self.cmbThreat.setItemText(4, QCoreApplication.translate("MainWindow", u"ARP Spoof", None))

        self.lblSeveritySel.setText(QCoreApplication.translate("MainWindow", u"Severity:", None))
        self.cmbSeverity.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.cmbSeverity.setItemText(1, QCoreApplication.translate("MainWindow", u"Low", None))
        self.cmbSeverity.setItemText(2, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.cmbSeverity.setItemText(3, QCoreApplication.translate("MainWindow", u"High", None))
        self.cmbSeverity.setItemText(4, QCoreApplication.translate("MainWindow", u"Critical", None))

        self.lblStatusTitle.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.lblStatusDetail.setText(QCoreApplication.translate("MainWindow", u"Offline", None))
        self.lblInterfaceDetail.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.lblInterfaceTitle.setText(QCoreApplication.translate("MainWindow", u"Interface:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuScan.setTitle(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.menuReports.setTitle(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

