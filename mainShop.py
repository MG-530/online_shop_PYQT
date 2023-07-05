import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class MainShop(QtWidgets.QMainWindow):
    def __init__(self, CUid):
        super().__init__()
        self.setWindowTitle(f"Main Shop >>>> hello {CUid}")
        self.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.logo.setPixmap(QtGui.QPixmap("./src/s_icon-nbg.png"))
        self.logo.setObjectName("logo")

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

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["PRid", "Title", "Price", "description", " more info"])

        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.panelButton)
        self.layout.addWidget(self.header)
        self.layout.addWidget(self.tableWidget)
        self.setCentralWidget(self.centralwidget)
        self.CUid = CUid

        self.loadCSS()
        self.loadProducts()

    def loadCSS(self):
        style_sheet = f"""
                QLabel#header{{
                    {css.label_stylesheet_header}
                }}
                QPushButton#panelButton{{
                    {css.panelButton}
                 }}
                QPushButton{{
                    {css.push_button_stylesheet_red_min}
                 }}
                QPushButton:hover, QPushButton#panelButton:hover {{
                    {css.push_button_stylesheet_red_min_hover}
                }}

                """

        self.setStyleSheet(style_sheet)

    def loadProducts(self):
        products = db.showActiveProduct()
        self.tableWidget.setRowCount(len(products))

        for row, product in enumerate(products):

            PRidItem = QtWidgets.QTableWidgetItem(str(product[0]))
            titleItem = QtWidgets.QTableWidgetItem(str(product[1]))
            price = "{:,}".format(int(product[2]))

            priceItem = QtWidgets.QTableWidgetItem(str(price))
            descriptionItem = QtWidgets.QTableWidgetItem(str(product[3]))

            self.tableWidget.setItem(row, 0, PRidItem)
            self.tableWidget.setItem(row, 1, titleItem)
            self.tableWidget.setItem(row, 2, priceItem)
            self.tableWidget.setItem(row, 3, descriptionItem)

            button = QtWidgets.QPushButton("More Info")
            button.clicked.connect(lambda _, PRid=str(product[0]): self.openSingleProduct(PRid, self.CUid))
            self.tableWidget.setCellWidget(row, 4, button)

        self.tableWidget.resizeColumnsToContents()

    def openSingleProduct(self, PRid, CUid):
        from SingleProduct import SingleProduct
        self.close()
        self.singleProduct = SingleProduct(PRid, CUid)
        self.singleProduct.show()

    def customerPanel(self,CLid):
        from customerPanel import CustomerPanel
        self.close()
        self.CustomerPanel = CustomerPanel(CLid)
        self.CustomerPanel.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainShop = MainShop("CUَ2")
    mainShop.show()
    sys.exit(app.exec_())
