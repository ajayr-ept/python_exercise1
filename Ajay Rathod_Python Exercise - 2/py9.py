# Write a program which will handle the Sales Transaction
# This will be a menu driven program.
# It should be able to store the product details such as product name, product unit price, product cost,
# product_type(stockable, consumable, service), stock - separate dictionary
#     - Generate the unique sku automatically as follows PRD1, PRD3, PRD4...PRDn
#     - Use sku as the key
#     - There will be a "create product" method.
# There should be a separate method which will do the preparation of a dictionary of the product and return
# the prepared values which will be used to add a new product to  the dictionary.
# The create method of product should return the newly created index(which is sku in our case)

from datetime import date

# create a class product
class Product:
    # define a dictionary object
    product_dictionary = {}
    # define a product SKU object
    product_sku = "PRD"
    # define a SKU Index object
    sku = 0
    def __init__(self):
        self.product_dictionary.update({'PRD1':{'product_name': 'fff', 'product_unique_price': '10', 'product_cost': '1', 'product_type': '2', 'product_stock': '5'}})
    #define a prepare product method
    def prepare_product(self):

        # Enter the Product detaile
        print('*************** Products Details *************')
        product_name = input('Enter Product Name : ')
        product_unique_price = input('Enter Unique Price : ')
        product_cost = input("Enter product final cost :")
        product_type = input('Enter a Product type For Example ...[1-Stackable ,2-Consumable ,3-Service] :')
        product_stock = input('Enter Stock :')

        temp_dictionary = {'product_name': product_name,
                           'product_unique_price': product_unique_price,
                           'product_cost': product_cost,
                           'product_type': product_type,
                           'product_stock':product_stock }
        # define a return tem dictionary
        return temp_dictionary


    # define a create a product, method
    def create_products(self):
        # increment  SKU index variable
        self.sku = self.sku + 1

        # ret_dictionary = self.prepare_product()
        sku_of_product = self.product_sku + str(self.sku)
        # print a sku of product
        print(sku_of_product)

        # update for product dictionary in product sku
        self.product_dictionary.update(
            {sku_of_product: self.prepare_product()})

        # print a final dictionary for products
        print("final dictionary is", self.product_dictionary)
        # return values sku of product
        return sku_of_product

    # define a update stock method
    def update_stock(self):
        print('********************** Update *******************')
        print("Here the list of Products SKU, Please Enter SKU which is Display here !!!")

        # Display the list of SKU of products for user Selection
        for sku in self.product_dictionary.keys():
            # print a product sku
            print(sku)
        # use of while condition
        while (True):

            print('1 : ------ Update-----')
            print('2 : -------Exit------')

            choice = int(input("Enter Your choice :"))

            if (choice == 1):
                # here a enter a SKU of product
                user_entered_sku = input("Enter Your SKU for Update Stock of That Product :")
                # enter a new stock of product
                new_stock = int(input("Enter New Stock for updating :"))
                # here a use of if condition
                if user_entered_sku in self.product_dictionary.keys():

                    temp_dictionary = self.product_dictionary[user_entered_sku]
                    temp_dictionary.update({"product_stock": new_stock})
                    self.product_dictionary.update({user_entered_sku: temp_dictionary})

                    print("final Dictionary", self.product_dictionary)
                else:
                    print("Not found SKU Enter Match SKU :")
            else:
                print('No match SKU')

            if (choice == 2):
                break

# define a customer class
class Customer:

    customer_dictionary = {}
    customer_address_dictionary = {}
    customer_code = "cust"
    customer_code_index = 0

    def __init__(self):
        self.customer_dictionary.update({'cust1': {'customer_name': 'ff', 'customer_email': 'gg', 'customer_phone': '1231231'}})
        self.customer_address_dictionary.update({'cust1': {'customer_address1': 'ghdf', 'customer_address2': 'gfhdgf', 'customer_city': 'hrhdf', 'customer_zipcode': 256, 'customer_state': 'thd', 'customer_country': 'hgdt'}})
    # define a prepare customer
    def prepare_customer(self):

        # enter a customer details
        customer_name = input("Enter Customer Name :")
        customer_email = input("Enter Customer Email :")
        customer_phone = input("Enter Customer Phone No :")
        customer_address1 = input("Enter Customer Address1 :")
        customer_address2 = input("Enter Customer Address2 :")
        customer_city = input("Enter Customer City :")
        customer_zipcode = int(input("Enter Zipcode :"))
        customer_state = input("Enter Customer State :")
        customer_country = input("Enter Customer County :")

        # define a dictionary of customer detailes
        temp_dictionary_customer_details = {
                            "customer_name" : customer_name,
                            "customer_email" : customer_email,
                            "customer_phone" : customer_phone
        }
        # define a dictionary of customer address
        temp_dictionary_customer_address = {
                                            "customer_address1" : customer_address1,
                                            "customer_address2" : customer_address2,
                                            "customer_city"     : customer_city,
                                            "customer_zipcode"  : customer_zipcode,
                                            "customer_state"    : customer_state,
                                            "customer_country"  : customer_country
        }

        # return of temp dictionary of customer details and temp dictionary of customer address
        return temp_dictionary_customer_details,temp_dictionary_customer_address

    # define a method of create customer
    def create_customer(self):
        # define a variable of prepare customer method
        temp_customer_details, temp_customer_address = self.prepare_customer()
        # increment of customer code
        self.customer_code_index = self.customer_code_index + 1
        customer_unique_code = self.customer_code + str(self.customer_code_index)

        # print of customer unique code and customer code index
        print(customer_unique_code)
        print(self.customer_code_index)


        self.customer_dictionary.update(
            {
                customer_unique_code: temp_customer_details
            })

        self.customer_address_dictionary.update(
            {
                customer_unique_code: temp_customer_address
            })

        print("Final Dictionary :", self.customer_dictionary)
        print("Final Address Dictionary :", self.customer_address_dictionary)
        return self.prepare_customer


class SaleTransaction(Product,Customer):

    # define sales_order_dictionary which store sales order of products
    sales_order_dictionary = {}
    # sale_order_code use fo generate unique sale order code for Sales Orders
    sale_order_code = "SO"
    # sale_order_index use for generate sale order code
    sale_order_index = 0

    # define a prepare sale order method
    def prepare_sale_order(self):
        print('--------------prepare sale order-----------------------')
        # define a Temp sale order dictionary
        temp_sale_order_dictionary = {}

        # print Customer Details here
        print("Select Customer Code Which Display Here !!")

        # print of all customer code here using for loop
        for customer_code in self.customer_dictionary.keys():
            print(customer_code)

        # Enter a customer code for use side
        user_entered_customer_code = input("Enter Customer Code :")


        if user_entered_customer_code in self.customer_dictionary.keys():

            temp_sale_order_dictionary.update({
                "customer_code": user_entered_customer_code })

            date_of_sale_order = date.today()
            temp_sale_order_dictionary.update({"date_of_order": date_of_sale_order})

            print("Here List Of Products Details  !!!")
            for product_sku, product_details in self.product_dictionary.items():
                print("product_sku :", product_sku, "product_details :", product_details)

                # create temporary variable for list_of_product
                # for purpose of store multipale order of single product
                list_of_product = []
                list_sku = []
                # create final_sub_total_qty for store final sub total of list of products quantity
                final_sub_total_qty = 0


                # Here manu driven for multipale order of single product
                while (True):
                    print('**************************************')
                    print('1  : Add Products in Sale Order ')
                    print('2  : Exit ')
                    print('**************************************')

                    choice = int(input("Enter Your Choice :"))

                    if choice == 1:
                        user_entered_sku = input("Enter Product SKU Which display above :")

                        # check user entered sku is present in list of sku of products
                        # if present then find sub total of user entered quantity and store in tempoarary variable
                        if user_entered_sku in self.product_dictionary.keys() and user_entered_sku not in list_sku:
                            user_entered_qty = int(input("Enter product Quantity :"))


                            # get per unit price of quantity of user entered sku product
                            price_per_qty = int(self.product_dictionary.get(user_entered_sku,{}).get('product_unique_price'))
                            self.product_dictionary.get(user_entered_sku, {}).get("product_unit_price")

                            # compute sub total and store in temporary variable
                            sub_total_of_qty = price_per_qty * user_entered_qty

                            # add each product sub total in final sub total
                            final_sub_total_qty += sub_total_of_qty
                            print('sub total :',sub_total_of_qty)
                            print('final sub total :',final_sub_total_qty)

                            # if user entered quantity for order is smaller and equal then that product stock then reduced
                            # user entered quantity from product stock and add that quantity in sale order
                            if user_entered_qty <= int(
                                    self.product_dictionary.get(user_entered_sku, {}).get("product_stock")):

                                remaining_qty = int(self.product_dictionary.get(user_entered_sku, {}).get(
                                    "product_stock")) - user_entered_qty

                                # self.products_dictionary.update(self.products_dictionary.get(user_entered_sku,{}).get({"product_stock" : remainig_qty }))
                                self.product_dictionary.get(user_entered_sku, {}).update(
                                    {"product_stock": remaining_qty})

                                #append every order line in list of dictionary
                                list_of_product.append(
                                    {"product_sku": user_entered_sku, "product_qty": user_entered_qty,
                                     "sub_total": sub_total_of_qty})
                                list_sku.append(user_entered_sku)
                            else:

                                # if user entered quantity is greater then the product stock quantity then raise warning message
                                print("You don't have Enough stock for Quantity")


                        elif user_entered_sku in self.product_dictionary.keys() and user_entered_sku in list_sku:

                            user_entered_qty = int(input("Enter product Quantity :"))

                            # get per unit price of quantity of user entered sku product
                            price_per_qty = int(
                                self.product_dictionary.get(user_entered_sku, {}).get('product_unique_price'))
                            self.product_dictionary.get(user_entered_sku, {}).get("product_unit_price")

                            # compute sub total and store in temporary variable
                            sub_total_of_qty = price_per_qty * user_entered_qty

                            # add each product sub total in final sub total
                            final_sub_total_qty += sub_total_of_qty
                            print('sub total :', sub_total_of_qty)
                            print('final sub total :', final_sub_total_qty)

                            # if user entered quantity for order is smaller and equal then that product stock then reduced
                            # user entered quantity from product stock and add that quantity in sale order
                            if user_entered_qty <= int(
                                    self.product_dictionary.get(user_entered_sku, {}).get("product_stock")):

                                remaining_qty = int(self.product_dictionary.get(user_entered_sku, {}).get(
                                    "product_stock")) - user_entered_qty

                                #self.products_dictionary.update(self.products_dictionary.get(user_entered_sku,{}).get({"product_stock" : remainig_qty }))
                                self.product_dictionary.get(user_entered_sku, {}).update(
                                    {"product_stock": remaining_qty})

                                for order_line in list_of_product:
                                    if order_line["product_sku"] == user_entered_sku:
                                        order_line.update({"product_qty" : int(order_line["product_qty"])})

                                # append every order line in list of dictionary
                                list_of_product.append(
                                    {"product_sku": user_entered_sku, "product_qty": user_entered_qty,
                                     "sub_total": sub_total_of_qty})
                                list_sku.append(user_entered_sku)
                            else:

                                # if user entered quantity is greater then the product stock quantity then raise warning message
                                print("You don't have Enough stock for Quantity")

                        else:
                            # if user entered sku not found in list of sku then raise warning message for user
                            print("Your Entered Sku of Product is can not found in list of Product SKU !!")

                    if choice == 2:
                        break

                if len(list_of_product) > 0:

                    # finally created one sale order in form of dictionary and then return that dictionary for create sale order method and make state of this sale order is draft
                    temp_sale_order_dictionary.update(
                        {"order_line": list_of_product, "total": final_sub_total_qty, "state": "Draft"})

                    return temp_sale_order_dictionary


            else:
                # if match not then raise warning message
                print("Please Entered Correct Customer Code")


    def create_sale_order(self):
        print('-----------------create sale order--------------------')
        # get prepare sale order from prepare_sale_order method
        temp_Sale_order = self.prepare_sale_order()

        if bool(temp_Sale_order):
            # increase customer code index with 1
            self.sale_order_index = self.sale_order_index + 1

            # create temporary variable for storing the sale_order code
            sale_order_code = self.sale_order_code + str(self.sale_order_index)

            # update sale_order_dictionary with unique key is sale_order code
            self.sales_order_dictionary.update({
                sale_order_code: temp_Sale_order
            })
            print('..........................................')
            print("Final Sale Order Dictionary :", self.sales_order_dictionary)

            # return sale_order_code
            return sale_order_code



    def sales_order_list(self):
        print('-------------------change sale order------------------')
        # display all the sale order code here
        print('Here a List of sale Order code....')
        for sale_order_code in self.sales_order_dictionary.keys():
            print(sale_order_code)

    def draft_to_confirm_order(self):
        print('------------')

        user_side_sale_order_code = input('Enter a sale order code :')

        if user_side_sale_order_code in self.sales_order_dictionary.keys():

            status_state = self.sales_order_dictionary.get(user_side_sale_order_code).get('state')

            if status_state == "Draft":
                self.sales_order_dictionary.get(user_side_sale_order_code, {}).update({"state": "confirm"})
            print(self.sales_order_dictionary)

        else:
            print('Invalid values')
    def confirm_to_draft_order(self):
        print('------------')

        user_side_sale_order_code = input('Enter a sale order code :')

        if user_side_sale_order_code in self.sales_order_dictionary.keys():

            status_state = self.sales_order_dictionary.get(user_side_sale_order_code).get('state')

            if status_state == "confirm":
                self.sales_order_dictionary.get(user_side_sale_order_code, {}).update({"state": "Draft"})
            print(self.sales_order_dictionary)

        else:
            print('Invalid values')

    def cancle_to_draft_order(self):
        print('------------')

        user_side_sale_order_code = input('Enter a sale order code :')
        if user_side_sale_order_code in self.sales_order_dictionary.keys():
            status_state = self.sales_order_dictionary.get(user_side_sale_order_code).get('state')

            if status_state == "cancel":
                self.sales_order_dictionary.get(user_side_sale_order_code, {}).update({"state": "Draft"})
                print(self.sales_order_dictionary)

                for each_dict in self.sales_order_dictionary.get(user_side_sale_order_code).get('order_line'):
                    sku = each_dict.get('product_sku')

                    if sku in self.product_dictionary:
                        draft_qty = each_dict.get('product_qty')
                        stock = self.product_dictionary.get(sku).get('product_stock')
                        stock -= draft_qty
                        self.product_dictionary.get(sku).update({'product_stock': stock})

        else:
            print('Invalid values')

    def confirm_to_cancel_order(self):
        print('------------')
        user_side_sale_order_code = input('Enter a sale order code :')
        if user_side_sale_order_code in self.sales_order_dictionary.keys():
            status_state = self.sales_order_dictionary.get(user_side_sale_order_code).get('state')

            # change sale order state from draft to cancle state
            if status_state == "confirm":

                self.sales_order_dictionary.get(user_side_sale_order_code, {}).update({"state": "cancel"})
                print(self.sales_order_dictionary)

                for each_dict in self.sales_order_dictionary.get(user_side_sale_order_code).get('order_line'):
                    sku = each_dict.get('product_sku')

                    if sku in self.product_dictionary:
                        cancel_qty = each_dict.get('product_qty')
                        stock = self.product_dictionary.get(sku).get('product_stock')
                        stock += cancel_qty
                        self.product_dictionary.get(sku).update({'product_stock': stock})
        else:
            print('Invalid values')

    def draft_to_cancle_order(self):
        print('------------')

        user_side_sale_order_code = input('Enter a sale order code :')

        if user_side_sale_order_code in self.sales_order_dictionary.keys():
            status_state = self.sales_order_dictionary.get(user_side_sale_order_code).get('state')

            # change sale order state from draft to cancle state
            if status_state == "Draft":

                self.sales_order_dictionary.get(user_side_sale_order_code, {}).update({"state": "cancel"})
                print(self.sales_order_dictionary)

                for each_dict in self.sales_order_dictionary.get(user_side_sale_order_code).get('order_line'):
                    sku = each_dict.get('product_sku')

                    if sku in self.product_dictionary:
                        cancel_qty = each_dict.get('product_qty')
                        stock = self.product_dictionary.get(sku).get('product_stock')
                        stock += cancel_qty
                        self.product_dictionary.get(sku).update({'product_stock': stock})
        else:
            print('Invalid values')


    def confirm_to_done_order(self):
        print('------------')

        user_side_sale_order_code = input('Enter a sale order code :')

        if user_side_sale_order_code in self.sales_order_dictionary.keys():

            status_state = self.sales_order_dictionary.get(user_side_sale_order_code).get('state')

            if status_state == "confirm":
                self.sales_order_dictionary.get(user_side_sale_order_code, {}).update({"state": "Done"})
            print(self.sales_order_dictionary)

        else:
            print('Invalid values')

    def display_sale_order(self):
        print('------------------display sale order-------------------')
        print("Here the sale order code !!")

        for sale_order_code in self.sales_order_dictionary.keys():
            print(sale_order_code)

        user_entered_sale_order = input("Enter Sale_order for displaying details of sale order :")
        print('----------------------------------------------------------------------------------')

        # check sale_order available in sale_order_dictionary if yes then display details
        # else raise warning for user
        if user_entered_sale_order in self.sales_order_dictionary.keys():
            print("Order No :", user_entered_sale_order, "                               ",'Date :',
                  self.sales_order_dictionary.get(user_entered_sale_order, {}).get("date_of_order"))
            print()
            print('Order Status :',self.sales_order_dictionary.get(user_entered_sale_order).get('state'))
            print()
            print("Customer :", self.sales_order_dictionary.get(user_entered_sale_order, {}).get("customer_code"),',',
                  self.customer_dictionary.get(self.sales_order_dictionary.get(user_entered_sale_order,
                  {}).get("customer_code"),{}).get("customer_name"),
                  '       ',self.customer_address_dictionary.get(self.sales_order_dictionary.get(user_entered_sale_order,{}).get("customer_code"),{}).get("customer_address1"))

            print('          ',self.customer_dictionary.get(self.sales_order_dictionary.get(user_entered_sale_order,
                  {}).get("customer_code"),{}).get("customer_phone"),
                  '       ', self.customer_address_dictionary.get(
                    self.sales_order_dictionary.get(user_entered_sale_order, {}).get("customer_code"), {}).get(
                    "customer_address2"))

            print('          ', self.customer_dictionary.get(self.sales_order_dictionary.get(user_entered_sale_order,
                  {}).get("customer_code"),{}).get("customer_email"),
                  '       ', self.customer_address_dictionary.get(
                    self.sales_order_dictionary.get(user_entered_sale_order, {}).get("customer_code"), {}).get(
                    "customer_address2"))


            # print("\t\t", self.customer_address_dictionary.get(user_entered_sale_order).get('customer_address1'))
            # print("\t\t", self.customer_address_dictionary.get(user_entered_sale_order).get('customer_address2'))
            # print("\t\t", self.customer_address_dictionary.get(user_entered_sale_order).get('customer_city'),
            #       self.customer_address_dictionary.get(user_entered_sale_order).get('customer_state'))
            # print("\t\t", self.customer_address_dictionary.get(user_entered_sale_order).get('customer_zipcode'))
            # print("\t\t", self.customer_address_dictionary.get(user_entered_sale_order).get('customer_country'))
            #
            #


        print('=======================================================================================================')
        # print('Product Dictionary :',self.product_dictionary)
        # print('sales order Dictionary : ',self.sales_order_dictionary)
        # print('customer :',self.customer_dictionary)
        # print('customer address dict :',self.customer_address_dictionary)


sale1 = SaleTransaction()

while(True):

    print('--------------------------------------------')
    print('|    1 : Create a Product ')
    print('|    2 : Create a Customer ')
    print('|    3 : Update a Stock ')
    print('|    4 : Create a Sale Order ')
    print('|    5 : List of Sale Order ')
    print('| #########################################')
    print('|    6 : Draft To Confirm ')
    print('|    7 : Draft To Cancel')
    print('|    8 : Confirm To Draft ')
    print('|    9 : Confirm To Cancel ')
    print('|   10 : Cancel To Draft  ')
    print('|   11 : Confirm To Done')
    print('| -----------------------------------------')
    print('|   12 : Display Sale Order ')
    print('| #########################################')
    print('|   13 : Exit ')
    print('--------------------------------------------')

    choice = int(input("Enter your choice :"))

    if choice == 1:
        sale1.create_products()
    if choice == 2:
        sale1.create_customer()
    if choice == 3:
        sale1.update_stock()
    if choice == 4:
        sale1.create_sale_order()
    if choice == 5:
        sale1.sales_order_list()
    if choice == 6:
        sale1.draft_to_confirm_order()
    if choice == 7:
        sale1.draft_to_cancle_order()
    if choice == 8:
        sale1.confirm_to_draft_order()
    if choice == 9:
        sale1.confirm_to_cancel_order()
    if choice == 10:
        sale1.cancle_to_draft_order()
    if choice == 11:
        sale1.confirm_to_done_order()
    if choice == 12:
        sale1.display_sale_order()
    if choice == 13:
        break


