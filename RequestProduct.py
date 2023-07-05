from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class RequestProductPage(QtWidgets.QWidget):
    def __init__(self,CLid="CL0"):
        self.CLid=CLid
        super().__init__()
        self.setWindowTitle("Request Product")
        self.resize(800, 600)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.logo.setPixmap(QtGui.QPixmap("./src/s_icon-nbg.png"))
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.goToMainShop(self.CLid)

        self.Header = QtWidgets.QLabel(self)
        self.Header.setGeometry(QtCore.QRect(240, 30, 481, 51))
        self.Header.setObjectName("Header")
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setText("Welcome to Main Shop")

        self.titleLabel = QtWidgets.QLabel("Title:", self)
        self.titleEdit = QtWidgets.QLineEdit(self)

        self.priceLabel = QtWidgets.QLabel("Price:", self)
        self.priceEdit = QtWidgets.QLineEdit(self)

        self.descriptionLabel = QtWidgets.QLabel("Description:", self)
        self.descriptionEdit = QtWidgets.QTextEdit(self)

        self.requestButton = QtWidgets.QPushButton("Request Product", self)
        self.requestButton.clicked.connect(self.requestProduct)

        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.Header)
        self.layout.addWidget(self.titleLabel)
        self.layout.addWidget(self.titleEdit)
        self.layout.addWidget(self.priceLabel)
        self.layout.addWidget(self.priceEdit)
        self.layout.addWidget(self.descriptionLabel)
        self.layout.addWidget(self.descriptionEdit)
        self.layout.addWidget(self.requestButton)

        self.loadCSS()

    def loadCSS(self):
        style_sheet = f"""
                QLabel#Header{{
                    {css.label_stylesheet_header}
                }}
                """

        self.setStyleSheet(style_sheet)

    def requestProduct(self):
        title = self.titleEdit.text()
        price = self.priceEdit.text()
        description = self.descriptionEdit.toPlainText()
        db.addNewProduct(title, price, description)
        QtWidgets.QMessageBox.information(self, "Confirmation", "The product has been sent for approval.")
        self.titleEdit.clear()
        self.priceEdit.clear()
        self.descriptionEdit.clear()

    def goToMainShop(self, CLid):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    requestProductPage = RequestProductPage()
    requestProductPage.show()
    app.exec_()
