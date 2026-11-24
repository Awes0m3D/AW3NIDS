🛡️ AW3NIDS

Advanced Web/Network Intrusion Detection System

A Python-based Network Intrusion Detection System designed to monitor network traffic, identify suspicious activities, generate security alerts, and provide network activity analysis through a graphical user interface.

"Python" (https://img.shields.io/badge/Python-3.x-blue?logo=python)
"PySide6" (https://img.shields.io/badge/GUI-PySide6-green)
"Scapy" (https://img.shields.io/badge/Packet%20Capture-Scapy-orange)
"SQLite" (https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
"Platform" (https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
"Status" (https://img.shields.io/badge/Status-In%20Development-yellow)

---

📌 About The Project

AW3NIDS (Advanced Web/Network Intrusion Detection System) is a Python-based cybersecurity application developed to monitor network traffic and detect potentially malicious activities in real time.

The application captures and analyzes network packets, identifies suspicious traffic patterns, generates security alerts, and stores relevant information for further investigation.

AW3NIDS provides a graphical interface built with PySide6, allowing users to monitor network activity without relying entirely on command-line tools.

The project aims to demonstrate how network monitoring, intrusion detection, alert management, and security response mechanisms can be integrated into a single application.

🎯 Project Objectives

- Monitor network traffic in real time.
- Capture and analyze network packets.
- Identify suspicious network activities.
- Detect common network-based attacks.
- Generate alerts when suspicious activities are identified.
- Store security alerts and application logs.
- Visualize network traffic and security statistics.
- Provide an interface for monitoring and responding to threats.

✨ Key Features

1. Network Monitoring

- Real-time packet capture using Scapy.
- Network interface selection.
- Start and stop monitoring controls.
- Live packet information.
- TCP, UDP, and ICMP protocol identification.
- Network traffic statistics.

2. Intrusion Detection

- Port-scan detection.
- SYN-flood detection.
- Suspicious traffic identification.
- Detection event reporting.
- Security alert generation.

3. Security Alerts

- Centralized alert management.
- Source IP identification.
- Threat severity classification.
- Alert history.
- Security response functionality.

4. Dashboard

- Network monitoring overview.
- Live packet information.
- Recent security alerts.
- Network traffic visualization.
- Monitoring status indicators.

5. Database Management

- SQLite database integration.
- Alert storage.
- Saved alert retrieval.
- Persistent security information.

6. Analytics

- Network activity analysis.
- Packet statistics.
- Traffic visualization.
- Security activity overview.

7. Reports

- Security report generation.
- Alert history reporting.
- CSV export functionality.

8. System Logs

- Application event logging.
- Monitoring activity records.
- Security event records.
- Log searching and filtering.
- Log export functionality.

9. Firewall Response

- IP-blocking functionality.
- Windows Firewall integration.
- Firewall rule management.

---

🛠️ Technologies Used

Technology| Purpose
Python| Main programming language
PySide6| Graphical user interface
Qt Designer| Interface design
Scapy| Network packet capture and analysis
SQLite| Database management
Matplotlib| Network traffic visualization
PyInstaller| Application packaging

📂 Project Structure

AW3NIDS/
│
├── main.py
│
├── app/
│   ├── main_window.py
│   └── ui_main_window.py
│
├── core/
│   ├── alerts.py
│   ├── detector.py
│   ├── firewall.py
│   └── packet_capture.py
│
├── database/
│   ├── database.py
│   └── aw3nids.db
│
├── resources/
│   ├── ui/
│   │   └── main_window.ui
│   └── icons/
│
├── analytics/
│
├── reports/
│
├── logs/
│
├── requirements.txt
│
└── README.md

Note: This is a representative project structure. Some directories and filenames may differ from the current repository.

⚙️ Installation

Prerequisites

Before installing AW3NIDS, ensure you have:

- Python installed.
- Git installed.
- Windows operating system.
- Npcap installed for packet capture on Windows.
- Administrator privileges where required for network capture and firewall operations.

1. Clone the Repository

git clone https://github.com/Awes0m3D/AW3NIDS.git

2. Navigate to the Project Directory

cd AW3NIDS

3. Create a Virtual Environment

python -m venv .venv

4. Activate the Virtual Environment

Windows:

.venv\Scripts\activate

5. Install Dependencies

pip install -r requirements.txt

6. Run the Application

python main.py

---

🚀 Application Usage

1. Launch AW3NIDS.
2. Navigate to the Dashboard.
3. Select an available network interface.
4. Start network monitoring.
5. Observe captured packets and network statistics.
6. Review detected suspicious activities in the Alerts section.
7. Examine network activity through Analytics.
8. Generate security reports.
9. Review application events in the Logs section.

Note: Some monitoring and firewall operations may require administrator privileges. Only monitor networks you own or have explicit permission to test.

---

🖥️ Application Modules

Module| Description
Dashboard| Main network monitoring interface
Database| Manages stored security information
Alerts| Displays detected threats and security events
Analytics| Presents network statistics and visualizations
Reports| Generates and exports security reports
Logs| Records application and monitoring events

---

🔐 Security Considerations

AW3NIDS is designed for authorized network monitoring and security research.

- Only monitor networks you are authorized to inspect.
- Firewall blocking operations should be performed carefully.
- Detection results should be reviewed before taking security actions.
- Network monitoring permissions may vary depending on the operating system.
- The application should be tested in a controlled environment before deployment.

---

📈 Development Status

AW3NIDS is currently under active development.

Component| Status
Graphical User Interface| Implemented
Network Packet Capture| Implemented
Live Network Monitoring| Implemented
Port-Scan Detection| Implemented
SYN-Flood Detection| Under Testing
Alert Management| Implemented
SQLite Integration| Implemented
Analytics| Under Development
Report Generation| Implemented
Application Logging| Implemented
Firewall Integration| Under Testing
PyInstaller Packaging| Under Development

Features may change as development and testing continue.

---

🔮 Future Improvements

Planned improvements include:

- Additional intrusion detection techniques.
- Improved detection accuracy.
- ARP-spoofing detection.
- ICMP-flood detection.
- Alert deduplication and configurable cooldowns.
- Enhanced network analytics.
- Improved firewall response mechanisms.
- Performance optimization.
- Improved standalone application packaging.

---

🎓 Project Information

Project Name: AW3NIDS

Network Intrusion Detection System

Developer: Awesome Achese

Programming Language: Python

---

🤝 Contributions

Suggestions, bug reports, and improvements are welcome.

If you find an issue or have an idea for improving AW3NIDS, feel free to open an issue or submit a pull request.

---

📜 License

This project is currently developed as an academic project.

A formal open-source license may be added when the project is ready for public distribution.

---

🛡️ AW3NIDS

Monitor. Detect. Analyze. Respond.

Building a safer network through intelligent monitoring and intrusion detection.