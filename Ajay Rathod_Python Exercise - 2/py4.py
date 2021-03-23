# Write a program which is having a class InventoryManagement.
# System should manage the quantity of purchase and sales processes.
# Users should be able to purchase the product with different prices in the
# same object of Inventory Management - Use a dictionary, maintain a numerical index and store
# product price and product quantity against it.
# Whenever the product is sold, it will start deducting the product qty whichever entry is done
# first in the dictionary, so qty will be deducted as FIFO (First In First Out).
# Whenever product qty is deducted change the price of that index.
# Formula -
# Once the qty from each purchase is used make sure, it is not used again, so update the dictionary
# accordingly.
# Program should be able to handle the valuation.
# Formula for valuation - sum of price * qty / sum of total qty.
# Write appropriate constructor, methods to manage the sales and purchase processes.
# There should be a provision to view the available quantities.
# This should be a menu driven program, which allows to
# Purchase Product
# Sale Product
# View Available Product Quantities
# Exit
#
# Whenever sales take place, the system should process the quantities and then should show the available
# quantities.

# create a class for Inventory Management
class InventoryManagement:
    # define all the variable
    index = 1
    sub_total = 0
    final_product_qty = 0
    valuation = 0
    purchase_product_dictionary = {}

    # create a purchase product method
    def purchase_product(self):
        # enter the product qty
        purchase_qty = (int(input('Enter purchase qty :')))
        product_qty = (int(input('Enter product qty')))

        # dictionary  update method use for key and values for updating
        self.purchase_product_dictionary.update({self.index:
                                                {'sub_total':purchase_qty * product_qty ,
                                                'qty': product_qty}})
        # index values increase
        self.index += 1
        # final product qty for increase
        self.final_product_qty += product_qty
        # sub total for increase
        self.sub_total += product_qty
        # here print for purchase product dictionary
        print('Dictionary :',self.purchase_product_dictionary)
        # available method call
        self.available()

    # define sales product method
    def sales_product(self):
        # input a sale quantity
        sale_qty = int(input("Enter No of Sales Quantity  :"))

        # define a if condition in compare to final product to sale qty
        if(self.final_product_qty < sale_qty):
            print('not any product qty :')
        # define elif in equality compare final product qty to sale qty
        elif (self.final_product_qty == sale_qty):
            self.purchase_product_dictionary = {}
            self.final_product_qty = 0
            self.sub_total = 0
        else:
            # define a for loop in index and values is define and list method use
            for index,val1 in list(self.purchase_product_dictionary.items()):
                # define a if condition in compare values qty to sale qty
                if (val1['qty'] > sale_qty):

                    #
                    self.sub_total -= (sale_qty * (val1['sub_total'] / val1['qty']))
                    val1['sub_total'] = val1['sub_total'] - sale_qty * (val1['sub_total'] / val1['qty'])
                    val1['qty'] = val1['qty'] - sale_qty
                    self.final_product_qty -= sale_qty
                else:

                    sale_qty = sale_qty - val1['qty']
                    val1['sub_total'] = 0
                    val1['qty'] = 0

                list_of_sale_product = list(self.purchase_product_dictionary)
                for d in list_of_sale_product:
                    if (self.purchase_product_dictionary[d]['sub_total'] == 0):
                        del self.purchase_product_dictionary[d]

    def available(self):
        print("Final Product Quantity is : ",self.final_product_qty)

    def valuation_pro(self):
        print("Sub Total is :", self.sub_total)
        print("Dictionary is :", self.purchase_product_dictionary)

obj = InventoryManagement()
choice = 1
while choice!=0:
    print('=====================================')
    print('1 : Sale Product ')
    print('2 : Purchase Product ')
    print('3 : View Available Product Quantities')
    print('4 : Valuation ')
    print('5 : Exit')
    print('======================================')
    print('Enter your Choice Number :')
    choice = int(input())


    if choice == 1:
        obj.sales_product()
    elif choice == 2:
        obj.purchase_product()
    elif choice == 3:
        obj.available()
    elif choice == 4:
        obj.valuation_pro()
    elif choice == 5:
        print('Exit')
        break
    else:
        print('Invalide values')
