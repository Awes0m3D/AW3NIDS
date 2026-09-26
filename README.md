# AW3NIDS — Network Intrusion Detection System

AW3NIDS is a Python-based **Network Intrusion Detection System (NIDS)** designed to monitor network traffic, detect suspicious activity, generate security alerts, and provide security analytics through a graphical user interface.

The system is designed as a final-year Computer Science project and focuses on providing a practical and user-friendly approach to basic network security monitoring.

---

## 📌 Features

### 🖥️ Graphical User Interface

AW3NIDS provides a desktop interface built with **PySide6** and Qt Designer.

The application includes dedicated pages for:

* Dashboard
* Alerts
* Analytics
* Database
* Reports
* Logs

---

### 📡 Network Packet Capture

The system captures live network traffic using **Scapy**.

Captured packets can include:

* TCP
* UDP
* ICMP
* Other IP-based traffic

Packet information displayed by the application includes:

* Timestamp
* Source IP address
* Destination IP address
* Protocol
* Packet length

---

### 🛡️ Intrusion Detection

AW3NIDS analyzes network traffic for suspicious patterns and potential attacks.

Current detection capabilities include:

* Port scanning detection
* SYN flood detection
* Suspicious traffic analysis
* Packet-based threat detection

Additional detection methods can be added as the project develops.

---

### 🚨 Alert Management

When suspicious activity is detected, AW3NIDS generates an alert containing information such as:

* Detection time
* Threat type
* Source IP
* Destination IP
* Protocol
* Severity
* Alert status
* Additional details

Alerts are displayed in the application's dashboard and Alerts page.

---

### 📊 Network Analytics

The Analytics page provides information about network activity and detected threats.

The system can track information such as:

* Packet activity
* Protocol usage
* Traffic trends
* Detected alerts
* Threat statistics

Traffic information can be presented using graphical visualizations.

---

### 🗄️ Database

AW3NIDS uses **SQLite** for local data storage.

The database can be used to retain:

* Security alerts
* Packet-related information
* Historical security events
* Application records

This allows information to remain available after the application is closed.

---

### 📄 Reports

The Reports section is designed to provide summarized information about network security activity.

Reports can be used to review:

* Detected threats
* Alert statistics
* Network activity
* Historical events

---

### 📋 Logs

The Logs page provides a centralized location for reviewing application and security-related events.

Logs can assist with:

* Troubleshooting
* Monitoring application activity
* Reviewing detection events
* Investigating suspicious behavior

---

## 🏗️ Project Architecture

The project is organized into several components:

```text
AW3NIDS/
│
├── app/
│   ├── main_window.py
│   └── ui_main_window.py
│
├── core/
│   ├── alerts.py
│   ├── detector.py
│   └── packet_capture.py
│
├── database/
│   └── database.py
│
├── analytics/
│   └── ...
│
├── detection/
│   ├── port_scan.py
│   ├── syn_flood.py
│   └── ...
│
├── resources/
│   └── ui/
│       └── main_window.ui
│
├── main.py
├── requirements.txt
└── README.md
```

> The exact folder structure may change as the project continues to develop.

---

## ⚙️ Technologies Used

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| **Python**  | Main programming language |
| **PySide6** |                           |
