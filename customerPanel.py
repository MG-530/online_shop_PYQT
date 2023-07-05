from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class CustomerPanel(QtWidgets.QWidget):
    def __init__(self,CUid):
        self.CUid = CUid
        super().__init__()
        self.setWindowTitle(f"customer Panel for {CUid}")
        self.resize(800, 600)

        self.layout = QtWidgets.QVBoxLayout(self)

        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.logo.setPixmap(QtGui.QPixmap("./src/s_icon-nbg.png"))
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.goToMainShop(self.CUid)

        self.Header = QtWidgets.QLabel(self)
        self.Header.setGeometry(QtCore.QRect(240, 30, 481, 51))
        self.Header.setObjectName("Header")
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setText("Welcome to Main Shop")

        self.HistoryButton = QtWidgets.QPushButton("History", self)
        self.HistoryButton.clicked.connect(lambda : self.showMyHistory(CUid))

        self.shoppingCartButton = QtWidgets.QPushButton("shoppingCart", self)
        self.shoppingCartButton.clicked.connect(lambda : self.showShoppingCart(CUid))

        self.favoriteButton = QtWidgets.QPushButton("favorite", self)
        self.favoriteButton.clicked.connect(lambda : self.showFavorite(CUid))

        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.Header)
        self.layout.addWidget(self.HistoryButton)
        self.layout.addWidget(self.shoppingCartButton)
        self.layout.addWidget(self.favoriteButton)

        self.loadCSS()

    def loadCSS(self):
        style_sheet = f"""
                QLabel#Header{{
                    {css.label_stylesheet_header}
                }}
                """

        self.setStyleSheet(style_sheet)

    def showMyHistory(self,CUid):
        history = str(db.showMyHistory(CUid))
        QtWidgets.QMessageBox.information(self, "history" ,history)

    def showShoppingCart(self,CUid):
        ShoppingCart = str(db.showShoppingCart(CUid))
        QtWidgets.QMessageBox.information(self, "ShoppingCart" ,ShoppingCart)

    def showFavorite(self,CUid):
        Favorite = str(db.showFavorite(CUid))
        QtWidgets.QMessageBox.information(self, "Favorite" ,Favorite)

    def goToMainShop(self, CLid="CL0"):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    CustomerPanel = CustomerPanel("CU1")
    CustomerPanel.show()
    app.exec_()
