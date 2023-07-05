from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class OperatorPanel(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operator Panel")
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

        self.SellerListButton = QtWidgets.QPushButton("seller List", self)
        self.SellerListButton.clicked.connect(lambda : self.sellerListPage())

        self.customerListButton = QtWidgets.QPushButton("customer List", self)
        self.customerListButton.clicked.connect(lambda : self.customerListPage())

        self.productListButton = QtWidgets.QPushButton("Product List", self)
        self.productListButton.clicked.connect(lambda : self.productListPage())


        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.Header)
        self.layout.addWidget(self.SellerListButton)
        self.layout.addWidget(self.customerListButton)
        self.layout.addWidget(self.productListButton)

        self.loadCSS()

    def loadCSS(self):
        style_sheet = f"""
                QLabel#Header{{
                    {css.label_stylesheet_header}
                }}
                """

        self.setStyleSheet(style_sheet)

    def sellerListPage(self):
        from SellerListPage import SellerListPage
        self.close()
        self.SellerListPage = SellerListPage()
        self.SellerListPage.show()

    def customerListPage(self):
        from CustomerListPage import CustomerListPage
        self.close()
        self.CustomerListPage = CustomerListPage()
        self.CustomerListPage.show()
    def productListPage(self):
        from ProductListPage import ProductListPage
        self.close()
        self.ProductListPage = ProductListPage()
        self.ProductListPage.show()

    def goToMainShop(self, CLid="CL0"):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    OperatorPanel = OperatorPanel()
    OperatorPanel.show()
    app.exec_()
