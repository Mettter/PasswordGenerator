import random
import sys
from functools import partial

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QMessageBox, \
    QListWidget, QHBoxLayout, QComboBox, QMenu

from basewindow import BaseWindow

a_z_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
everything = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]{}|;:,.<>?"


class PasswordGeneratorApp(BaseWindow):
    def __init__(self) -> None:
        super().__init__("Password Generator")
        self.prompt = ''
        layout = QVBoxLayout()
        layout.addLayout(self.init_header_layout())
        layout.addLayout(self.init_main_layout())
        self.setLayout(layout)

    def init_header_layout(self):
        header_layout = QVBoxLayout()
        self.generate_password_button = QPushButton('Generate password')
        self.generate_password_button.clicked.connect(self.generate_password)

        self.password_label = QLabel("")

        self.password_string = QLineEdit()

        header_layout.addWidget(self.password_string)
        # header_layout.addWidget(self.password_label)
        header_layout.addWidget(self.generate_password_button)

        return header_layout

    def init_main_layout(self):
        main_layout = QHBoxLayout()
        return main_layout

    def generate_password(self) -> str:
        password = ''
        for i in range(len(everything)):
            password += everything[random.randint(0, len(everything) - 1)]
        print(password)
        self.password_string.setText(password)
        return password

def checkPassword(password):
    upperCaseLettersCount = 0
    if len(password) < 12:
        print("Your password is to short")
        return

    for i in range(len(password)):
        charOfPassword = password[i]
        if charOfPassword == charOfPassword.upper() and charOfPassword not in numbers:# and charOfPassword in a_z_letters
            upperCaseLettersCount += 1
    if upperCaseLettersCount > 0:
        print('Password contains upper case letters')
    else:
        print("Password does not contains upper case letters, it's not secure")
        return
    upperCaseLettersCount = 0

    for i in range(len(password)):
        if password[i] in numbers:
            upperCaseLettersCount += 1
    if upperCaseLettersCount > 0:
        print('Password contains numbers')
    else:
        print("Password does not contains numbers, it's not secure")
        return
    upperCaseLettersCount = 0

    for i in range(len(password)):
        if password[i] in special_chars:
            upperCaseLettersCount += 1
    if upperCaseLettersCount > 0:
        print('Password contains special characters')
    else:
        print("Password does not contains special characters, it's not secure")
        return

if __name__ == "__main__":
    # checkPassword(input())
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())