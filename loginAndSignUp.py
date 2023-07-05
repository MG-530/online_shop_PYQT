import css
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *

import database as db
import sys
from SingleProduct import SingleProduct
from mainShop import MainShop


class User(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Form")
        self.resize(896, 600)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.logo.setPixmap(QtGui.QPixmap("./src/s_icon-nbg.png"))
        self.logo.setObjectName("logo")

        self.Header = QtWidgets.QLabel(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(240, 30, 481, 51))
        self.Header.setObjectName("Header")
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setText("Welcome to MG online Shop")

        self.loginColumn = QtWidgets.QColumnView(self.centralwidget)
        self.loginColumn.setGeometry(QtCore.QRect(20, 200, 370, 241))
        self.loginColumn.setObjectName("loginColumn")

        self.loginText = QtWidgets.QLabel(self.centralwidget)
        self.loginText.setGeometry(QtCore.QRect(60, 220, 281, 41))
        self.loginText.setObjectName("loginText")
        self.loginText.setAlignment(QtCore.Qt.AlignCenter)

        self.loginPhoneNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.loginPhoneNumber.setGeometry(QtCore.QRect(60, 270, 281, 25))
        self.loginPhoneNumber.setObjectName("loginPhoneNumber")
        self.loginPhoneNumber.setMaxLength(11)
        validator = QtGui.QIntValidator(self.loginPhoneNumber)
        self.loginPhoneNumber.setValidator(validator)

        self.loginPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.loginPassword.setGeometry(QtCore.QRect(60, 310, 281, 25))
        self.loginPassword.setText("")
        self.loginPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPassword.setObjectName("loginPassword")

        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(140, 360, 111, 51))
        self.login.setObjectName("login")
        self.login.clicked.connect(self.loginOpenMainShop)

        self.signUpColumn = QtWidgets.QColumnView(self.centralwidget)
        self.signUpColumn.setGeometry(QtCore.QRect(450, 130, 370, 430))
        self.signUpColumn.setObjectName("signUpColumn")

        self.signUPText = QtWidgets.QLabel(self.centralwidget)
        self.signUPText.setGeometry(QtCore.QRect(490, 150, 281, 41))
        self.signUPText.setObjectName("signUPText")
        self.signUPText.setAlignment(QtCore.Qt.AlignCenter)

        self.firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.firstname.setGeometry(QtCore.QRect(490, 200, 281, 25))
        self.firstname.setInputMask("")
        self.firstname.setObjectName("firstname")

        self.lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lastname.setGeometry(QtCore.QRect(490, 240, 281, 25))
        self.lastname.setInputMask("")
        self.lastname.setText("")
        self.lastname.setObjectName("lastname")

        self.phoneNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneNumber.setGeometry(QtCore.QRect(490, 280, 281, 25))
        self.phoneNumber.setInputMask("")
        self.phoneNumber.setText("")
        self.phoneNumber.setMaxLength(11)
        self.phoneNumber.setObjectName("phoneNumber")
        validator = QtGui.QIntValidator(self.phoneNumber)
        self.phoneNumber.setValidator(validator)

        self.Address = QtWidgets.QTextEdit(self.centralwidget)
        self.Address.setGeometry(QtCore.QRect(490, 360, 281, 111))
        self.Address.setObjectName("textEdit")

        self.singUpPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.singUpPassword.setGeometry(QtCore.QRect(490, 320, 281, 25))
        self.singUpPassword.setText("")
        self.singUpPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.singUpPassword.setObjectName("loginPassword")

        self.signUp = QtWidgets.QPushButton(self.centralwidget)
        self.signUp.setGeometry(QtCore.QRect(570, 480, 121, 51))
        self.signUp.setObjectName("signUp")
        self.signUp.clicked.connect(self.signUpOpenMainShop)

        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.loadCSS()
        self.retranslateUi()

    def loadCSS(self):
        style_sheet = f"""
       
            QLineEdit{{
                {css.line_edit_stylesheet}
            }}
            QTextEdit{{
                {css.text_edit_stylesheet}
            }}
            QLabel{{
                {css.label_stylesheet}
            }}
            QColumnView{{
                {css.column_view_stylesheet}
            }}
            QTextBrowser{{
                {css.text_browser_stylesheet}
            }}
            QLabel#Header{{
                {css.label_stylesheet_header}
            }}
            QPushButton{{
                {css.push_button_stylesheet_red}
        
            }}
            QLabel#signUPText,QLabel#loginText{{
                {css.label_stylesheet}
            }}
            """

        self.setStyleSheet(style_sheet)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("user", "User Form"))

        self.loginPassword.setPlaceholderText(_translate("user", "Password"))
        self.singUpPassword.setPlaceholderText(_translate("user", "Password"))
        self.Address.setPlaceholderText(_translate("user", "Address"))

        self.login.setText(_translate("user", "Sign in"))
        self.loginPhoneNumber.setPlaceholderText(_translate("user", "Phone Number"))
        self.signUp.setText(_translate("user", "Sign up"))

        self.lastname.setPlaceholderText(_translate("user", "Lastname"))
        self.firstname.setPlaceholderText(_translate("user", "Firstname"))
        self.phoneNumber.setPlaceholderText(_translate("user", "Phone Number (09)"))

        self.Header.setText(_translate("user", "Welcome to MG Online Shop"))
        self.signUPText.setText(_translate("user", "Create new account"))

    def signUpOpenMainShop(self):
        if db.singUp(self.firstname.text(), self.lastname.text(), self.singUpPassword.text(), self.phoneNumber.text(),
                     self.Address.toPlainText()):
            self.close()
            self.mainShop = MainShop(db.getCUid(self.phoneNumber.text()))
            self.mainShop.show()
        else:
            return 0

    def loginOpenMainShop(self):
        if db.login(self.loginPhoneNumber.text(), self.loginPassword.text()):
            CLid = self.loginPhoneNumber.text()
            self.close()
            self.mainShop = MainShop(db.getCUid(self.loginPhoneNumber.text()))
            self.mainShop.show()
        else:
            return 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    userPage = User()
    userPage.show()
    sys.exit(app.exec_())
