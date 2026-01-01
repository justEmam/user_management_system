from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QFrame, QMessageBox
)
from PyQt5.QtCore import Qt
from services.user_service import UserService

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Account")
        self.setFixedSize(400, 500)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        # ===== Card =====
        card = QFrame()
        card.setObjectName("card")
        card.setFixedSize(350, 450)

        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(15)
        card_layout.setContentsMargins(30, 30, 30, 30)
        card_layout.setAlignment(Qt.AlignCenter)

        # ===== Title =====
        title = QLabel("Create Account")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Fill in your details to register")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        # ===== Inputs =====
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setObjectName("input")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")
        self.email.setObjectName("input")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setObjectName("input")

        # ===== Create Button =====
        create_btn = QPushButton("Register")
        create_btn.setObjectName("loginButton")
        create_btn.setCursor(Qt.PointingHandCursor)
        create_btn.clicked.connect(self.register_action)

        # ===== Add Widgets =====
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addWidget(self.username)
        card_layout.addWidget(self.email)
        card_layout.addWidget(self.password)
        card_layout.addSpacing(10)
        card_layout.addWidget(create_btn)

        main_layout.addWidget(card)
        self.setStyleSheet(self.style_sheet())

    def style_sheet(self):
        return """
        QWidget {
            background: qlineargradient(
                spread:pad, x1:0, y1:0, x2:1, y2:1,
                stop:0 #141E30, stop:1 #243B55
            );
            font-family: 'Segoe UI';
        }

        QFrame#card {
            background-color: #ffffff;
            border-radius: 18px;
        }

        QLabel#title {
            font-size: 24px;
            font-weight: 600;
            color: #222;
        }

        QLabel#subtitle {
            font-size: 12px;
            color: #777;
        }

        QLineEdit#input {
            height: 40px;
            border-radius: 10px;
            border: 1px solid #ddd;
            padding-left: 12px;
            font-size: 14px;
        }

        QLineEdit#input:focus {
            border: 1px solid #4A90E2;
        }

        QPushButton#loginButton {
            height: 42px;
            border-radius: 12px;
            background-color: #4A90E2;
            color: white;
            font-size: 14px;
            font-weight: 500;
            border: none;
        }

        QPushButton#loginButton:hover {
            background-color: #357ABD;
        }

        QPushButton#loginButton:pressed {
            background-color: #2C5F9E;
        }
        """

    def register_action(self):
        username = self.username.text()
        email = self.email.text()
        password = self.password.text()

        if not username or not email or not password:
            QMessageBox.warning(self, "Error", "All fields are required")
            return

        if len(password) < 6:
            QMessageBox.warning(self, "Error", "Password must be at least 6 characters")
            return

        UserService.createUser(username,email,password)
        QMessageBox.information(self, "Success", "Account created successfully!")
        self.close()  
