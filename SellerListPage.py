from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class SellerListPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("seller List")
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
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["SLid", "firstname", "lastName", "phoneNumber", "address" ,"Wallet","delete seller" ,"active"])

        self.loadSellers()
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

    def loadSellers(self):
        sellers = db.showAllSeller()
        self.tableWidget.setRowCount(len(sellers))

        for row, seller in enumerate(sellers):
            SLidItem = QtWidgets.QTableWidgetItem(str(seller[0]))
            firstnameItem = QtWidgets.QTableWidgetItem(str(seller[1]))

            lastNameItem = QtWidgets.QTableWidgetItem(str(seller[3]))
            phoneNumberItem = QtWidgets.QTableWidgetItem(str(seller[4]))
            addressItem = QtWidgets.QTableWidgetItem(str(seller[5]))
            WalletItem = QtWidgets.QTableWidgetItem(str(str(seller[6])))
            deleteButton = QtWidgets.QPushButton("delete Seller")
            deleteButton.clicked.connect(lambda _, SLid=str(seller[0]): self.deleteSeller(SLid))
            activeItem = QtWidgets.QTableWidgetItem(str(seller[8]))


            self.tableWidget.setItem(row, 0, SLidItem)
            self.tableWidget.setItem(row, 1, firstnameItem)
            self.tableWidget.setItem(row, 2, lastNameItem)
            self.tableWidget.setItem(row, 3, phoneNumberItem)
            self.tableWidget.setItem(row, 4, addressItem)
            self.tableWidget.setItem(row, 5, WalletItem)
            self.tableWidget.setCellWidget(row, 6, deleteButton)
            self.tableWidget.setItem(row, 7, activeItem)

            if seller[8] == "1":
                activeItem.setFlags(QtCore.Qt.ItemIsEnabled)
            else:
                activeButton = QtWidgets.QPushButton("active Seller")
                activeButton.clicked.connect(lambda _, PRid=str(seller[0]): self.activeSeller(PRid))
                self.tableWidget.setCellWidget(row, 7, activeButton)

        self.tableWidget.resizeColumnsToContents()

    def deleteSeller(self, SLid):
        success = db.deleteSeller(SLid)
        if success:
            QtWidgets.QMessageBox.information(self, "Confirmation", "Product has been activated.")
            self.loadSellers()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to activate product.")

    def activeSeller(self,SLid):
        success = db.activeSeller(SLid)
        if success:
            QtWidgets.QMessageBox.information(self, "Confirmation", "Product has been activated.")
            self.loadSellers()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to activate product.")

    def goToMainShop(self, CLid):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    SellerListPage = SellerListPage()
    SellerListPage.show()
    app.exec_()
