from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from app.ui_about_dialog import Ui_AboutDialog


class AboutDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        pixmap = QPixmap(
            "resources/images/aw3nids_logo.png"
        )

        self.ui.lblLogo.setPixmap(
            pixmap.scaled(
                120,
                120
            )
        )

        self.ui.btnClose.clicked.connect(
            self.close
        )