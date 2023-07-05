from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class ProductListPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product List")
        self.resize(800, 600)

        self.logo = QtWidgets.QLabel(self)
        self.logo.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.logo.setPixmap(QtGui.QPixmap("./src/s_icon-nbg.png"))
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.goToMainShop("CL00")

        self.Header = QtWidgets.QLabel(self)
        self.Header.setGeometry(QtCore.QRect(240, 30, 481, 51))
        self.Header.setObjectName("Header")
        self.Header.setAlignment(QtCore.Qt.AlignCenter)
        self.Header.setText("Welcome to Main Shop")

        self.layout = QtWidgets.QVBoxLayout(self)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["PRid", "Title", "Price", "Description", "Active"])

        self.loadProducts()
        self.loadCSS()

        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.Header)
        self.layout.addWidget(self.tableWidget)

    def loadCSS(self):
        style_sheet = f"""
                 QLabel#Header{{
                     {css.label_stylesheet_header}
                 }}
                 QPushButton{{
                    {css.push_button_stylesheet_red_min}
                 }}

                 """

        self.setStyleSheet(style_sheet)

    def loadProducts(self):
        products = db.showAllProduct()
        self.tableWidget.setRowCount(len(products))

        for row, product in enumerate(products):
            PRidItem = QtWidgets.QTableWidgetItem(str(product[0]))
            titleItem = QtWidgets.QTableWidgetItem(str(product[1]))
            price = "{:,}".format(int(product[2]))

            priceItem = QtWidgets.QTableWidgetItem(str(price))
            descriptionItem = QtWidgets.QTableWidgetItem(str(product[3]))
            activeItem = QtWidgets.QTableWidgetItem(str(product[4]))

            self.tableWidget.setItem(row, 0, PRidItem)
            self.tableWidget.setItem(row, 1, titleItem)
            self.tableWidget.setItem(row, 2, priceItem)
            self.tableWidget.setItem(row, 3, descriptionItem)
            self.tableWidget.setItem(row, 4, activeItem)

            if product[4] == "1":
                activeItem.setFlags(QtCore.Qt.ItemIsEnabled)
            else:
                button = QtWidgets.QPushButton("Activate")
                button.clicked.connect(lambda _, PRid=str(product[0]): self.activeProduct(PRid))
                self.tableWidget.setCellWidget(row, 4, button)

        self.tableWidget.resizeColumnsToContents()

    def activeProduct(self, PRid):
        success = db.activeProduct(PRid)
        if success:
            QtWidgets.QMessageBox.information(self, "Confirmation", "Product has been activated.")
            self.loadProducts()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to activate product.")

    def goToMainShop(self, CLid):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    product_list_page = ProductListPage()
    product_list_page.show()
    app.exec_()
