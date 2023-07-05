# online_shop_PYQT
management system for online shop by PYQT

# Requirements
Python 3.7 (or above)

PyQt5 5.15.9

# Create own store
If you don't want to use the current products and sellers  and To create your  own store ,first delete the onlineShop.db file and then run createDB.py file

# what we have
loginAndSignUp --> user can login or singup in it and after it the user redirect to mainshop

mainshop       --> all active product show in table and each Product have Dynamics SingleProduct page

sellerPanel    --> it can add inventory to all active product in shop or Request Product

customerPanel  --> Display the Buy history and the Shipping card and favorites. The whole panel is available next to the logo.

OperatorPanel  --> can do three thing 

1. sellerPanel      --> show all info for seller and delete or activate seler
		   
2. CustomerListPage --> show all info for Customer and delete Customer

3. ProductListPage  --> show all info for seller and activate Product that seller Request


# how to enjoy 
 just run " python loginAndSignUp.py"  and sing up new user and see all Product

to run Operator Panel " python OperatorPanel.py"

to run seller Panel "python sellerPanel.py"

