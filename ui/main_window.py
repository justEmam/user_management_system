# main_window.py

# Responsibilities:

# Main dashboard layout

# Sidebar

# User table

# Navigation

# Rules:
# ❌ No DB queries
# ❌ No business rules
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Dashboard")
        self.setFixedSize(800, 500)

        layout = QVBoxLayout(self)
        label = QLabel("Welcome to the Main Window")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)
