from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class SellerPanel(QtWidgets.QWidget):
    def __init__(self,SLid):
        super().__init__()
        self.setWindowTitle("Seller Panel")
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

        self.requestButton = QtWidgets.QPushButton("Request Product", self)
        self.requestButton.clicked.connect(self.requestProduct)

        self.addinventory = QtWidgets.QPushButton("New inventory", self)
        self.addinventory.clicked.connect(lambda : self.addinventory(SLid))

        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.Header)
        self.layout.addWidget(self.requestButton)
        self.layout.addWidget(self.addinventory)

        self.loadCSS()

    def loadCSS(self):
        style_sheet = f"""
                QLabel#Header{{
                    {css.label_stylesheet_header}
                }}
                """

        self.setStyleSheet(style_sheet)

    def requestProduct(self):
        from RequestProduct import RequestProductPage
        self.close()
        self.RequestProduct = RequestProductPage()
        self.RequestProduct.show()

    def addinventory(self,Slid):
        from addinventory import inventory_page
        self.close()
        self.inventory_page = inventory_page(Slid)
        self.inventory_page.show()

    def goToMainShop(self, CLid="CL0"):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    SellerPanelPage = SellerPanel("SL0")
    SellerPanelPage.show()
    app.exec_()
