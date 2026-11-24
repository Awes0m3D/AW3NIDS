import sys
from PySide6.QtWidgets import QApplication
from app.main_window import MainWindow
from pathlib import Path
from PySide6.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    icon_path = Path(__file__).parent / "resources" / "icons" / "aw3nids.ico"
    window.setWindowIcon(QIcon(str(icon_path)))
    window.show()

    sys.exit(app.exec())
