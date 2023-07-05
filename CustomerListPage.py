from PyQt5 import QtWidgets, QtCore, QtGui
import database as db
import css


class CustomerListPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("customer List")
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
        self.tableWidget.setHorizontalHeaderLabels(["CUid", "firstname", "lastName", "phoneNumber", "address" ,"Wallet","password","delete Customer"])

        self.loadCustomers()
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

    def loadCustomers(self):
        customers = db.showAllCustomer()
        self.tableWidget.setRowCount(len(customers))

        for row, customer in enumerate(customers):
            CUidItem = QtWidgets.QTableWidgetItem(str(customer[0]))
            firstnameItem = QtWidgets.QTableWidgetItem(str(customer[1]))

            lastNameItem = QtWidgets.QTableWidgetItem(str(customer[2]))
            phoneNumberItem = QtWidgets.QTableWidgetItem(str(customer[3]))
            addressItem = QtWidgets.QTableWidgetItem(str(customer[4]))
            WalletItem = QtWidgets.QTableWidgetItem(str(str(customer[5])))
            passwordItem = QtWidgets.QTableWidgetItem(str(str(customer[9])))
            button = QtWidgets.QPushButton("delete Customer")
            button.clicked.connect(lambda _, CUid=str(customer[0]): self.deleteCustomer(CUid))



            self.tableWidget.setItem(row, 0, CUidItem)
            self.tableWidget.setItem(row, 1, firstnameItem)
            self.tableWidget.setItem(row, 2, lastNameItem)
            self.tableWidget.setItem(row, 3, phoneNumberItem)
            self.tableWidget.setItem(row, 4, addressItem)
            self.tableWidget.setItem(row, 5, WalletItem)
            self.tableWidget.setItem(row, 6, passwordItem)



            self.tableWidget.setCellWidget(row, 7, button)

        self.tableWidget.resizeColumnsToContents()

    def deleteCustomer(self, CUid):
        success = db.deleteCustomer(CUid)
        if success:
            QtWidgets.QMessageBox.information(self, "Confirmation", "Product has been activated.")
            self.loadCustomers()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Failed to activate product.")

    def goToMainShop(self, CLid="CL0"):
        from mainShop import MainShop
        self.close()
        self.mainShop = MainShop(CLid)
        self.mainShop.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    CustomerListPage = CustomerListPage()
    CustomerListPage.show()
    app.exec_()
