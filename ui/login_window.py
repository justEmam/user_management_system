import sys
from services.auth_service import AuthService,Session
from ui.main_window import MainWindow
from ui.reigster_window import RegisterWindow
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QFrame,QMessageBox
)
from PyQt5.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(420, 520)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        # ===== Card =====
        card = QFrame()
        card.setObjectName("card")
        card.setFixedSize(360, 460)

        card_layout = QVBoxLayout(card)
        card_layout.setSpacing(20)
        card_layout.setContentsMargins(30, 30, 30, 30)
        card_layout.setAlignment(Qt.AlignCenter)

        # ===== Title =====
        title = QLabel("Welcome Back")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Please login to your account")
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignCenter)

        # ===== Inputs =====
        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setObjectName("input")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setObjectName("input")

        # ===== Button =====
        login_btn = QPushButton("Login")
        login_btn.setObjectName("loginButton")
        login_btn.setCursor(Qt.PointingHandCursor)
        create_account_btn = QPushButton("Create Account")
        create_account_btn.setObjectName("createAccountButton")
        create_account_btn.setCursor(Qt.PointingHandCursor)


        # ===== Footer =====
        footer = QLabel("© 2026 Your App")
        footer.setObjectName("footer")
        footer.setAlignment(Qt.AlignCenter)

        # ===== Add Widgets =====
        card_layout.addWidget(title)
        card_layout.addWidget(subtitle)
        card_layout.addSpacing(10)
        card_layout.addWidget(self.username)
        card_layout.addWidget(self.password)
        card_layout.addSpacing(15)
        card_layout.addWidget(login_btn)
        card_layout.addWidget(create_account_btn)
        card_layout.addStretch()
        card_layout.addWidget(footer)

        main_layout.addWidget(card)
        create_account_btn.clicked.connect(self.create_account_action)
        login_btn.clicked.connect(self.login_action)
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
            font-size: 26px;
            font-weight: 600;
            color: #222;
        }

        QLabel#subtitle {
            font-size: 13px;
            color: #777;
        }

        QLineEdit#input {
            height: 42px;
            border-radius: 10px;
            border: 1px solid #ddd;
            padding-left: 12px;
            font-size: 14px;
        }

        QLineEdit#input:focus {
            border: 1px solid #4A90E2;
        }

        QPushButton#loginButton {
            height: 45px;
            border-radius: 12px;
            background-color: #4A90E2;
            color: white;
            font-size: 15px;
            font-weight: 500;
            border: none;
        }

        QPushButton#loginButton:hover {
            background-color: #357ABD;
        }

        QPushButton#loginButton:pressed {
            background-color: #2C5F9E;
        }

        QLabel#footer {
            font-size: 11px;
            color: #aaa;
        }
        """
    def login_action(self) -> None:
        username = self.username.text()
        password = self.password.text()
        if len(password) < 6:
            QMessageBox.warning(self,"Invalid Password","must be atleast 6 chars")
        else: 
            try:
                user = AuthService.login(username,password)
                print("Login Sucessfully")
                self.main_window = MainWindow()
                self.main_window.show()
                self.close()

            except ValueError:
                QMessageBox.warning(self,'Error',"Wrong Username or PW")
    def create_account_action(self) -> None:
        self.register_window = RegisterWindow()
        self.register_window.show()






