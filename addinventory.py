import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class InventoryPage(QtWidgets.QMainWindow):
    def __init__(self, Slid):
        super().__init__()
        self.setWindowTitle("Inventory Page")
        self.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(0, 0, 181, 111))
        self.logo.setPixmap(QtGui.QPixmap("../src/s_icon-nbg.png"))
        self.logo.setObjectName("logo")
        self.logo.mousePressEvent = lambda event: self.goToMainShop(self.CLid)

        self.homeButton = QtWidgets.QPushButton("home")
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.homeButton.setFixedWidth(100)
        self.homeButton.clicked.connect(lambda _: self.goToMainShop(self.CLid))

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(240, 30, 481, 51))
        self.header.setObjectName("header")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setText("Welcome to MG online Shop")

        self.layout.addWidget(self.logo)
        self.layout.addWidget(self.header)
        self.setCentralWidget(self.centralwidget)
        self.addActiveProducts()
        self.loadCSS()
        self.Slid = Slid

    def loadCSS(self):
        style_sheet = f"""
                QLabel#header{{
                    {css.label_stylesheet_header}
                }}
                QPushButton{{
                    {css.push_button_stylesheet_red_min}
                 }}
                QPushButton:hover{{
                    {css.push_button_stylesheet_red_min_hover}
                }}
                """

        self.setStyleSheet(style_sheet)

    def addActiveProducts(self):
        self.active_products_list = QtWidgets.QListWidget(self.centralwidget)
        self.active_products_list.setGeometry(QtCore.QRect(10, 220, 781, 200))
        self.active_products_list.setObjectName("active_products_list")

        active_products = db.showActiveProduct()
        for product in active_products:
            item = QtWidgets.QListWidgetItem(f"Product ID: {product[0]}, Name: {product[1]}")
            item.setData(QtCore.Qt.UserRole, product[0])  # Store the product ID as item data
            self.active_products_list.addItem(item)

        self.layout.addWidget(self.active_products_list)
        self.active_products_list.itemClicked.connect(self.changeInventoryForProduct)

    def changeInventoryForProduct(self, item):
        product_id = item.data(QtCore.Qt.UserRole)  # Retrieve the stored product ID
        new_count, ok = QtWidgets.QInputDialog.getInt(
            self, "Change Inventory Count", "Enter new inventory count:"
        )

        if ok:
            db.newInventory(product_id, new_count, self.Slid)

            # Show a confirmation message
            QtWidgets.QMessageBox.information(
                self, "Inventory Change", "Inventory count has been updated successfully!"
            )

    def goToMainShop(self, CLid):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    inventory_page = InventoryPage("SL10")
    inventory_page.show()
    sys.exit(app.exec_())
