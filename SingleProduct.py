import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class SingleProduct(QtWidgets.QMainWindow):
    def __init__(self, PRid, CUid):
        self.CUid = CUid
        super().__init__()
        self.setWindowTitle("Single Product")
        self.resize(896, 600)

        self.centralwidget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.logo.setPixmap(QtGui.QPixmap("./src/s_icon-nbg.png"))
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.goToMainShop(self.CUid)

        self.panelButton = QtWidgets.QPushButton("Panel")
        self.panelButton.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.panelButton.setObjectName("panelButton")
        self.panelButton.setFixedWidth(100)
        self.panelButton.clicked.connect(lambda _,: self.customerPanel(self.CUid))

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(240, 30, 481, 51))
        self.header.setObjectName("header")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setText("Welcome to MG online Shop")

        self.productTitle = QtWidgets.QLabel(self.centralwidget)
        self.productTitle.setGeometry(QtCore.QRect(30, 140, 281, 111))
        self.productTitle.setObjectName("productTitle")

        self.productPrice = QtWidgets.QLabel(self.centralwidget)
        self.productPrice.setGeometry(QtCore.QRect(360, 150, 141, 61))
        self.productPrice.setObjectName("productPrice")

        self.productDescription = QtWidgets.QLabel(self.centralwidget)
        self.productDescription.setGeometry(QtCore.QRect(30, 250, 461, 131))
        self.productDescription.setObjectName("productDescription")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["count", "sellerName", "add to Buy"])

        self.productComments = QtWidgets.QLabel(self.centralwidget)
        self.productComments.setGeometry(QtCore.QRect(30, 390, 461, 131))
        self.productComments.setObjectName("productComments")

        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.panelButton)
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.productTitle)
        self.layout.addWidget(self.productPrice)
        self.layout.addWidget(self.productDescription)
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.productComments)
        self.setCentralWidget(self.centralwidget)


        self.loadCSS()
        self.loadProduct(PRid)
        self.loadInventory(PRid)



    def loadCSS(self):
        style_sheet = f"""
            QLabel#header {{
                {css.label_stylesheet_header}
            }}

            QLabel#productTitle {{
                {css.productTitle_stylesheet}
            }}

            QLabel#productPrice {{
                {css.price_stylesheet}
            }}

            QLabel#productDescription {{
                {css.productDescription_stylesheet}
            }}
            QPushButton#panelButton{{
                {css.panelButton}
            }}
            QPushButton#panelButton:hover {{
                {css.push_button_stylesheet_red_min_hover}
            }}
        """

        self.setStyleSheet(style_sheet)

    def loadProduct(self, PRid):
        product = db.findProduct(PRid)
        commentList = db.findComment(PRid)

        self.productTitle.setText(product[1])
        price = "{:,}".format(int(product[2]))
        self.productPrice.setText(f"price: {price} $")
        self.productDescription.setText(product[3])
        self.productComments.setText(str(commentList))
    def loadInventory(self, PRid):
        inventory = db.ShowInventory(PRid)
        self.tableWidget.setRowCount(len(inventory))

        for row, product in enumerate(inventory):

            count = QtWidgets.QTableWidgetItem(str(inventory[row][1]))
            sellerName = QtWidgets.QTableWidgetItem(str(inventory[row][2]))
            self.tableWidget.setItem(row, 0, count)
            self.tableWidget.setItem(row, 1, sellerName)
            button = QtWidgets.QPushButton("buy")
            button.clicked.connect(lambda _, : db.addToShoppingCart(self.CUid, PRid))
            self.tableWidget.setCellWidget(row, 2, button)

        self.tableWidget.resizeColumnsToContents()

    def goToMainShop(self, CLid):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()

    def customerPanel(self,CLid):
        from customerPanel import CustomerPanel
        self.close()
        self.CustomerPanel = CustomerPanel(CLid)
        self.CustomerPanel.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    singleProduct = SingleProduct("PR5", "Cl1")
    singleProduct.show()
    sys.exit(app.exec_())
