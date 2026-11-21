import os
import sys
import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from PySide6.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QPushButton, QVBoxLayout, QWidget,)

from About import AboutWindow


class IceCreamWindow(QWidget):
    def __init__(self):
        super().__init__()
       
        self.temperatures = []
        self.revenues = []
        self.selected_file = ""
        self.about_window = None

        self.setWindowTitle("Ice Cream Profit")
        self.resize(800, 600)
        self.init_ui()
        self.load_stylesheet()

        self.plot_temporary_graph()

    def init_ui(self):
        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        self.select_file_btn = QPushButton("Select CSV File")
        self.select_file_btn.clicked.connect(self.on_select_file)

        self.about_btn = QPushButton("About")
        self.about_btn.setObjectName("aboutBtn")
        self.about_btn.clicked.connect(self.open_about_window)

        top_layout.addWidget(self.select_file_btn)
        top_layout.addStretch()
        top_layout.addWidget(self.about_btn)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)

        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.canvas)
        self.setLayout(main_layout)

    def load_stylesheet(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        qss_path = os.path.join(base_dir, "style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())

    def plot_temporary_graph(self):
        self.ax.clear()
        self.ax.plot([1, 2, 3, 4], [10, 20, 15, 25])
        self.ax.set_title("Temporary Graph")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Value")
        self.canvas.draw()

    def on_select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Ice Cream CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)",
        )
        if file_path:
            self.selected_file = file_path
            self.load_data_from_csv(file_path)

    def load_data_from_csv(self, file_path):
        self.temperatures.clear()
        self.revenues.clear()

        with open(file_path, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                self.temperatures.append(float(row["Temperature"]))
                self.revenues.append(float(row["Revenue"]))

        self.plot_ice_cream_graph()

    def plot_ice_cream_graph(self):
        self.ax.clear()
        self.ax.scatter(self.temperatures, self.revenues, s=1)

        if len(self.temperatures) > 1:
            m, b = np.polyfit(self.temperatures, self.revenues, 1)
            x_line = np.linspace(min(self.temperatures), max(self.temperatures), 100)
            y_line = m * x_line + b
            self.ax.plot(x_line, y_line, color="red", label=f"y = {m:.2f}x + {b:.2f}")
            self.ax.legend()

        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)
        self.ax.set_title("Ice Cream Revenue vs Temperature")
        self.ax.set_xlabel("Temperature")
        self.ax.set_ylabel("Revenue")
        self.canvas.draw()

    def open_about_window(self):
            self.about_window = AboutWindow(self)
            self.about_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IceCreamWindow()
    window.show()
    sys.exit(app.exec())