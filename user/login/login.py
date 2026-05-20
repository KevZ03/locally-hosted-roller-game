import dotenv
import os
import json
import subprocess
import sys
import threading
import socket

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit

from login_ui import Ui_MainWindow

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def discover_server_ip():
    cs = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    discovery_message = "DISCOVER_LOGIN_IP"
    cs.sendto(discovery_message.encode(), ("<broadcast>", 65535))

    while True:
        try:
            cs.settimeout(5)
            cs_ip, _ = cs.recvfrom(4096)
            return cs_ip.decode()
        except socket.timeout:
            print("No server response. Relaunch Login When Server is Up")
            break

ip_address = discover_server_ip()

def set_username(name):
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    os.environ["USER_NAME"] = name
    dotenv.set_key(dotenv_file, "USER_NAME", os.environ["USER_NAME"])

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stacked_pages.setCurrentIndex(0)

        self.user_text = False
        self.password_text = False

        self.ui.Login_text.setFocusPolicy(Qt.StrongFocus)
        self.ui.username_input.setMaxLength(15)
        self.ui.create_account_name.setMaxLength(15)
        self.ui.create_account_pass.setMaxLength(15)
        self.ui.password_input.setMaxLength(15)

        self.ui.username_input.textChanged.connect(self.detect_text_user)
        self.ui.password_input.textChanged.connect(self.detect_text_pass)

        self.ui.create_account_login.clicked.connect(lambda: self.ui.stacked_pages.setCurrentIndex(1))
        self.ui.back_login.clicked.connect(lambda: self.ui.stacked_pages.setCurrentIndex(0))
        self.ui.password_enter.clicked.connect(lambda: self.Login())
        self.ui.create_account_login.clicked.connect(lambda: self.Clear_Login_Page())

        self.ui.toggle_show_password.toggled.connect(lambda: self.show_pass())
        self.ui.create_account_button.clicked.connect(lambda: self.create_account())
        self.ui.back_login.clicked.connect(lambda: self.Clear_Create_Page())

    def create_account(self):
        user_name = self.ui.create_account_name.text()
        password = self.ui.create_account_pass.text()
        if user_name != "" and password != "":
            if str(user_name).isidentifier() and str(password).isidentifier():
                data = {
                    'state': '1',
                    'user': self.ui.create_account_name.text(),
                    'password': self.ui.create_account_pass.text()
                }

                server_socket.sendto('LOGIN'.encode(), (ip_address, 65535))
                json_data = json.dumps(data)
                server_socket.sendto(json_data.encode(), (ip_address, 65535))
                message, _ = server_socket.recvfrom(4096)

                if str(message.decode()) == 'true':
                    self.ui.Warning_create_account.setText("Account Created Successfully!")
                    self.ui.Warning_create_account.setStyleSheet("color: green;")

                    timer = threading.Timer(5, self.hide_create_account)
                    timer.start()
                    self.Clear_Create_Page(False)
                elif str(message.decode()) == 'exist':
                    self.ui.Warning_create_account.setText("Name is already taken!")
                    self.ui.Warning_create_account.setStyleSheet("color: red;")
                else:
                    self.ui.Warning_create_account.setText("Unable to Create Account")
                    self.ui.Warning_create_account.setStyleSheet("color: red;")
        elif user_name == "":
            self.ui.Warning_create_account.setStyleSheet("color: red;")
            self.ui.Warning_create_account.setText("Please Enter a Name!")
        elif password == "":
            self.ui.Warning_create_account.setStyleSheet("color: red;")
            self.ui.Warning_create_account.setText("Please Enter a Password!")

    def hide_create_account(self):
        self.ui.Warning_create_account.setText("")

    def show_pass(self):
        if self.ui.toggle_show_password.isChecked():
            self.ui.create_account_pass.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.create_account_pass.setEchoMode(QLineEdit.Password)

    def detect_text_user(self):
        if self.ui.username_input.text():
            self.ui.username_input.setProperty("urgent", True)
        else:
            self.ui.username_input.setProperty("urgent", False)
        self.ui.username_input.style().polish(self.ui.username_input)

    def detect_text_pass(self):
        if self.ui.password_input.text():
            self.ui.password_input.setProperty("urgent", True)
        else:
            self.ui.password_input.setProperty("urgent", False)
        self.ui.password_input.style().polish(self.ui.password_input)

    def Clear_Login_Page(self):
        self.ui.password_input.setText("")
        self.ui.username_input.setText("")
        self.ui.WarningText.setText("")

    def Clear_Create_Page(self, isOnce=True):
        self.ui.create_account_name.setText('')
        self.ui.create_account_pass.setText('')
        if isOnce: self.ui.Warning_create_account.setText('')

    def Login(self):
        if self.ui.username_input.text() and self.ui.password_input.text():
            self.ui.WarningText.setText("")
            self.Send_Login_Data()
        elif self.ui.username_input.text() == "":
            self.ui.WarningText.setText("Please Enter an User Name!")
        elif self.ui.password_input.text() == "":
            self.ui.WarningText.setText("Please Enter a Password!")

        self.ui.username_input.setText("")
        self.ui.password_input.setText("")

    def Send_Login_Data(self):
        data = {
            'state': '0',
            'user': self.ui.username_input.text(),
            'password': self.ui.password_input.text()
        }

        server_socket.sendto('LOGIN'.encode(), (ip_address, 65535))
        json_data = json.dumps(data)
        server_socket.sendto(json_data.encode(), (ip_address, 65535))
        message, _ = server_socket.recvfrom(4096)

        if message.decode() == 'false':
            self.ui.WarningText.setText('Wrong Account Details Please try Again!')
            timer = threading.Timer(4, self.hide_login_warning)
            timer.start()
        elif message.decode() == 'true':
            set_username(self.ui.username_input.text())
            self.close()  # Close the login window
            self.run_game_executable()  # Run the game executable after closing the login window

    def hide_login_warning(self):
        self.ui.WarningText.setText('')

    def run_game_executable(self):
        try:
            game_executable = os.path.join(os.path.dirname(sys.executable), "game.exe")
            result = subprocess.run([game_executable], check=True, text=True, env=os.environ.copy())
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Game executable failed with return code {e.returncode}")
            print(e.stderr)

def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
