import os
import sys
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

GITHUB_URL = "https://github.com/rtsrooia-s/Exe4.1"


class AboutWindow(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("About")
        self.setGeometry(350, 350, 320, 340)

        layout = QVBoxLayout()

        self.image_label = QLabel()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pixmap = QPixmap(os.path.join(base_dir, "Rick.webp"))
        if not pixmap.isNull():
            self.image_label.setPixmap(
                pixmap.scaled(140, 140, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )

        self.name_label = QLabel("Rom Tsrooia")
        self.email_label = QLabel("rtsrooia@gmail.com")

        self.linkedin_label = QLabel(
            '<a href="https://www.linkedin.com/in/rom-zeruya/">LinkedIn</a>'
        )
        self.linkedin_label.setOpenExternalLinks(True)

        self.github_label = QLabel(
            f'<a href="{GITHUB_URL}">GitHub Repository</a>'
        )
        self.github_label.setOpenExternalLinks(True)

        layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.linkedin_label)
        layout.addWidget(self.github_label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AboutWindow()
    window.show()
    sys.exit(app.exec())