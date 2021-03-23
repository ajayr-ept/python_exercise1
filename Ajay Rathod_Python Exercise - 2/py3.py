# Write a program which is having a class InventoryManagement.
# System should manage the quantity of purchase and sales processes.
# If the system is not having enough quantity during sales, the system should show a
# warning message “Not enough product quantities to sell”.
# Write appropriate constructor, methods to manage the sales and purchase processes.
# There should be a provision to view the available quantities.
# This should be a menu driven program, which allows to
# Purchase Product
# Sale Product
# View Available Product Quantities
# Exit
# Whenever sales take place, the system should process the quantities and then should show the
# available quantities.

# create a class Inventory Management
class InventoryManagement:
    # Define constractor and attribute
    def __init__(self):
        self.product_qty = 0


    # create a Sales method
    def sales(self,sale_qty):
        # define if condition in sale_qty and product_qty
        if sale_qty > self.product_qty:
            print('Not enough product quantities to sell')
        else:
            # product qty to substract sale
            self.product_qty -= sale_qty


    # create a Purchase Processes
    def purchase_processes(self,purchase_qty):
        # include a product qty
        self.product_qty += purchase_qty

    # define view Method for view available product
    def view_available_product(self):
        # print all available product
        print('View available Product : ',self.product_qty)

# create Inventory Management class of object
obj = InventoryManagement()

#define choice variable
choice = 1

#define while loop
while choice!=0:
    # print all the manu
    print('=====================================')
    print('1 : Sale Product ')
    print('2 : Purchase Product ')
    print('3 : View Available Product Quantities')
    print('4 : Exit')
    print('======================================')
    print('Enter your Choice Number :')
    choice = int(input())

    #define a if condition to check for enterd number is  wrong or right
    if choice == 1:
        SaleProduct = int(input("Enter sale product : "))
        obj.sales(SaleProduct)
    elif choice == 2:
        PurchaseProduct = int(input('Enter purchase product :'))
        obj.purchase_processes(PurchaseProduct)
    elif choice == 3:
        obj.view_available_product()
    elif choice == 4:
        print('Exit')
        break
    else:
        print('Invalid values')




