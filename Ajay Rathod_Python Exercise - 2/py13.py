import datetime


class ProductMaster:
    def __init__(self):
        self.product_details = {'PRD1': {'pname': 'pen', 'uprice': 10.0, 'pcost': 8.0, 'ptype': 'stockable', 'stock': 20}, 'PRD2': {'pname': 'sw', 'uprice': 5.0, 'pcost': 3.0, 'ptype': 'stockable', 'stock': 50}}
        self.sku_counter = 1

    def prepare_product(self):
        # arg= -
        # return- return dictionary that will store into product details
        pname = input("Enter Product name :")
        uprice = float(input("Enter Unit price :"))
        pcost = float(input("Enter Product cost :"))
        stock = int(input("Enter Product Stock :"))
        product_type = ['stockable', 'consumable', 'service']
        # check for product type
        while True:
            ptype = int(input("1.stockable\n2.consumable\n3.service\nEnter product type (1/2/3) :"))
            if (ptype > 0) and ptype < 4:
                break
            print("invalid")
        ptype = product_type[ptype-1]
        sku = "PRD" + str(self.sku_counter)
        self.sku_counter = int(self.sku_counter) + 1
        return {sku: {'pname': pname, 'uprice': uprice, 'pcost': pcost, 'ptype': ptype, 'stock': stock}}

    def create_product(self):
        # arg:-
        # in store data into dictionary
        # return : sku that added into the dict of product
        pproduct = self.prepare_product()
        # to get sku from dict
        sku = list(pproduct.keys())
        self.product_details.update(pproduct)
        print(self.product_details)
        return sku[0]

    def update_stock(self):
        # arg:-
        # retun:-
        # it will check for the sku and if available than change the stock of that sku
        sku = input("Enter sku :")
        flag = self.product_details.get(sku, True)
        if flag:
            print("SKU not found!")
            return
        stock = int(input("Enter Product Stock :"))
        self.product_details.get(sku)['stock'] = stock
        print(self.product_details)


class CustomerMaster:
    def __init__(self):
        self.customers = {'cust_1': {'cname': 'aas', 'email': 'asd', 'phone': 'df'}}
        self.customer_address = {'cust_1': {'address1': 'as', 'address2': 'asdd', 'city': 'fdg', 'state': 'fdg', 'country': 'df', 'zipcode': 'dfg'}}
        self.cust_id_counter = 1

    def prepare_customer(self):
        # arg:-
        # return:- nested dict with data of customer details
        # it will take input and compute customer id
        cname = input("Enter Customer name :")
        email = input("Enter email :")
        phone = input("Enter phone :")
        cust_id = "cust_" + str(self.cust_id_counter)
        self.cust_id_counter = int(self.cust_id_counter) + 1
        return {cust_id: {'cname': cname, 'email': email, 'phone': phone}}

    def prepare_customer_address(self):
        # arg:-
        # return:- nested dict with data of customer address
        # it will take input of customer address
        address1 = input("Enter address1  :")
        address2 = input("Enter address2 :")
        city = input("Enter city :")
        state = input("Enter state :")
        country = input("Enter country :")
        zipcode = input("Enter zipcode :")
        return {'address1': address1, 'address2': address2,
                'city': city, 'state': state,
                'country': country,
                'zipcode': zipcode}

    def create_customer(self):
        # return: newly added cust_id
        # arg:-
        # get dect from function and that will be added into customer and customer_address dict
        cust_dict = self.prepare_customer()
        cust_id = list(cust_dict.keys())
        self.customers.update(cust_dict)
        cust_add_dict = self.prepare_customer_address()
        self.customer_address.update({cust_id[0]: cust_add_dict})
        print(self.customers)
        print(self.customer_address)
        return cust_id


class SaleMaster(ProductMaster, CustomerMaster):
    def __init__(self):
        self.sale_orders = {'SO1': {'cust_id': 'cust_1', 'date': '01/18/21', 'order_lines': [{'sku': 'PRD1', 'uprice': 10.0, 'qty': 7, 'sub_total': 70.0, 'state': 'draft'}, {'sku': 'PRD2', 'uprice': 5.0, 'qty': 30, 'sub_total': 150.0, 'state': 'draft'}], 'total': 220.0, 'state': 'draft'}, 'SO2': {'cust_id': 'cust_1', 'date': '01/18/21', 'order_lines': [{'sku': 'PRD1', 'uprice': 10.0, 'qty': 5, 'sub_total': 50, 'state': 'draft'}], 'total': 50, 'state': 'draft'}}
        self.sale_id_counter = 1
        CustomerMaster.__init__(self)
        ProductMaster.__init__(self)

    def create_sale_order(self):
        # arg:-
        # return :
        # it wil check for product and customer and call add product with cust id and soid
        if len(self.product_details) == 0 or len(self.customers) == 0:
            print("Not enough details of product or customer")
        else:
            cust_id = self.check_customer()
            self.prepare_sale_order(cust_id)

    def check_customer(self):
        # arg:-
        # return:cust_id that will select from input
        while True:
            print("CUST_ID\tNAME")
            print("---------------")
            for key, value in self.customers.items():
                print(key, "\t", value.get('cname'))
            cust_id = input("Enter custid : ")
            if self.customers.get(cust_id, True):
                print("customer not found")
            else:
                break
        return cust_id


    def prepare_sale_order(self, cust_id):
        # arg: selected customer id and generated sale order id
        # return:-
        so_id = "SO" + str(self.sale_id_counter)
        while True:
            print("SKU\t\tPRODUCT\tPRICE\tSTOCK")
            print("-------------------------------")
            for key, value in self.product_details.items():
                print(key, "\t", value.get('pname'), '\t', value.get('uprice'), '\t', value.get('stock'))

            sku= input("Enter sku :")
            # check for sku is correct or not
            if self.product_details.get(sku,True):
                print("product not found!!")
            else:
                qty = int(input("Enter Qty :"))
                # check for stock exist or not
                if self.product_details.get(sku).get('stock') == 0:
                    print("insufficient stock!! add stock")
                else:
                    uprice = self.product_details[sku]['uprice']
                    sdate = datetime.datetime.now()

                    if self.sale_orders.get(so_id, True):
                    # it will add new record
                        self.sale_id_counter = int(self.sale_id_counter) + 1
                        self.sale_orders[so_id] = {'cust_id': cust_id, 'date': sdate.strftime("%x"),
                                        'order_lines': [{'sku':sku,'uprice':uprice,'qty':qty,'sub_total':int(qty)*int(uprice),'state':'draft'}],
                                        'total':int(qty)*int(uprice),'state':'draft'
                                        }
                    else:
                        # it will append the dictionary

                        list_of_matched_sku = list(filter(lambda x: x['sku'] == sku, self.sale_orders.get(so_id).get('order_lines')))

                        if list_of_matched_sku:
                            index = self.sale_orders.get(so_id).get('order_lines').index(list_of_matched_sku[0])
                            self.sale_orders[so_id]['order_lines'][index]['qty'] += qty
                            self.sale_orders[so_id]['order_lines'][index]['sub_total'] = self.sale_orders[so_id]['order_lines'][index]['qty'] * self.sale_orders[so_id]['order_lines'][index]['uprice']
                        else:
                            order_lines = self.prepare_order_lines(sku, qty)
                            self.sale_orders[so_id]['order_lines'].append(order_lines)

                        self.sale_orders[so_id]['total'] += float(qty) * float(uprice)

                    print(self.sale_orders)
                    choic = input("want to add more product? Enter (y/n) :")
                    if choic == 'n':
                        break

    def prepare_order_lines(self, sku, qty):
        # arg- sku and qty of product that will be add into sales order
        # return:-order line dict of new product
        uprice = self.product_details[sku]['uprice']
        return {'sku': sku, 'uprice': uprice, 'qty': qty, 'sub_total': float(qty) * float(uprice),'state': 'draft'}

    def display_sale_order(self):
        # arg:-
        # return:-
        # it will generate the sale order details
        print(self.sale_orders)
        key = input("Enter sale order id :")
        # check oid exist or not
        if self.sale_orders.get(key, True):
            print("Not found")
        else:

            print("--------------------------------------------------------------------------------------------")
            print('Order No :', key, '\t\t\t\t\t\t\t\t\tOrder Date: ', self.sale_orders.get(key).get('date'))
            cust_code = self.sale_orders.get(key).get('cust_id')
            print("Customer:", cust_code, '', self.customers.get(cust_code).get('cname'))
            print("\t\t", self.customer_address.get(cust_code).get('address1'))
            print("\t\t", self.customer_address.get(cust_code).get('address2'))
            print("\t\t", self.customer_address.get(cust_code).get('city'),
                  self.customer_address.get(cust_code).get('state'))
            print("\t\t", self.customer_address.get(cust_code).get('zipcode'))
            print("\t\t", self.customer_address.get(cust_code).get('country'))
            print("\t\t", self.customers.get(cust_code).get('phone'))
            print("\t\t", self.customers.get(cust_code).get('email'))

            print("\nProduct Name\t\t\tProduct Price\t\t\tProduct Quantity\t\t\tSubtotal")
            print("====================================================================================")
            # print the product line
            for li in self.sale_orders.get(key).get('order_lines'):
                sku = li.get('sku')
                print(self.product_details.get(sku).get('pname'), '\t\t\t\t\t', li.get('uprice'), '\t\t\t\t\t',
                      li.get('qty'), '\t\t\t\t\t', li.get('sub_total'))
            print(self.sale_orders.get(key).get('state'), '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ttotal:',
                  self.sale_orders.get(key).get('total'))
            print("--------------------------------------------------------------------------------------------")


    def confirm_order(self):
        # arg:-
        # return:-
        # change the order state to confirm
        print(self.sale_orders)
        so_id = input("Enter order id :")
        if self.sale_orders.get(so_id, True):
            print("sell order id not found!")
        else:
            if self.sale_orders[so_id]['state'] == 'draft':
                for li in self.sale_orders.get(so_id).get('order_lines'):
                    li['state'] = 'confirm'
                self.sale_orders[so_id]['state'] = 'confirm'
                print(so_id, "Order confirmed")
            else:
                print(self.sale_orders[so_id]['state'], "not be confirm")
        return so_id

    def cancel_order(self,so_id):
        # arg:-
        # return:-
        # change the order state to cancel
        if self.sale_orders[so_id]['state'] == 'draft' or self.sale_orders[so_id]['state'] == 'confirm':
            for li in self.sale_orders.get(so_id).get('order_lines'):
                li['state'] = 'cancel'
            self.sale_orders[so_id]['state'] = 'cancel'
            print("Order cancelled")
        else:
            print(self.sale_orders[so_id]['state'], "not be cancel")

    def set_order_to_draft(self):
        # arg:-
        # return:-
        # change the order state to draft
        print(self.sale_orders)
        so_id = input("Enter order id :")
        if self.sale_orders.get(so_id, True):
            print("sell order id not found!")
        else:
            if self.sale_orders[so_id]['state'] == 'cancel':
                for li in self.sale_orders.get(so_id).get('order_lines'):
                    li['state'] = 'draft'
                self.sale_orders[so_id]['state'] = 'draft'
                print("Order cancelled")
            else:
                print(self.sale_orders[so_id]['state'], "not be draft")

    def print_all(self):
        print("Product:")
        print(self.product_details)
        print("Sale")
        print(self.sale_orders)


class Saleorder_Extended(SaleMaster):
    def __init__(self):
        self.delivery_order = {'DO1': {'sales_order': 'SO1', 'date': '01/19/21', 'stock_move': [{'product_code': 'PRD1', 'product_qty': 7, 'state': 'draft'}, {'product_code': 'PRD2', 'product_qty': 30, 'state': 'draft'}], 'state': 'draft'}}
        self.delivery_id_counter = 1
        SaleMaster.__init__(self)

    def confirm_order(self):
        # arg:-
        # return:-delivery order id
        # generate the delivery order if sale order is confirmed
        so_id = super().confirm_order()
        if self.sale_orders[so_id]['state'] == 'confirm':
            prepared_dict = self.prepare_delivery_order(so_id)
            d_id = list(prepared_dict.keys())
            self.delivery_order.update(prepared_dict)
            print(self.delivery_order)
            return d_id
        return None

    def prepare_delivery_order(self, so_id):
        # arg: soid that is sale order is which will be in delivery
        # return:prepared dict of deliver order
        delivery_id = 'DO'+str(self.delivery_id_counter)
        self.delivery_id_counter += 1
        sdate = datetime.datetime.now()
        date = sdate.strftime("%x")
        stock_move = []

        for li in self.sale_orders[so_id]['order_lines']:
            stock_move.append({'product_code': li['sku'],
                               'product_qty': li['qty'],
                               'state': 'drafdraftt'})

        return {delivery_id: {'sales_order': so_id,
                              'date': date,
                              'stock_move': stock_move,
                              'state': 'draft'}}

    def validate_delivery_order(self):
        # arg:-
        # retun: -
        # it will confirm the state of delivery order
        del_id = input("Enter delivery id to validate")
        if del_id in self.delivery_order.keys() and self.delivery_order[del_id]['state'] == 'draft':

            list_of_true_false = list(map(lambda a: a['product_qty'] <= self.product_details[a['product_code']]['stock'], self.delivery_order['DO1']['stock_move']))
            # example = [True, True] check for stock avalable or not
            if all(list_of_true_false):
                for stock_move in self.delivery_order[del_id]['stock_move']:
                    stock_move['state'] = 'done'
                    self.product_details[stock_move['product_code']]['stock'] -= stock_move['product_qty']

                self.delivery_order[del_id]['state'] = 'done'
                self.sale_orders[self.delivery_order[del_id]['sales_order']]['state'] = 'done'

                for itm in self.sale_orders[self.delivery_order[del_id]['sales_order']]['order_lines']:
                    itm['state'] = 'done'

            else:
                print("Not enough stock of product")
        else:
            print("Delivery id not found or this is already done")

        print(self.delivery_order)

    def check_in_extendedsale(self):
        # arg:-
        # return:-
        # it will check that sale order id is in the delivery or not
        print(self.sale_orders)
        so_id = input("Enter order id :")
        if self.sale_orders.get(so_id, True):
            print("sell order id not found!")
        else:
            list1 = list(map(lambda x: self.delivery_order[x]['sales_order'] != so_id or (self.delivery_order[x]['sales_order'] == so_id and self.delivery_order[x]['state'] == 'cancel'), self.delivery_order))
            # example:[True, True] it check soid is in the delivery or not and also check for state
            if all(list1):
                self.cancel_order(so_id)
            else:
                print(so_id, "already in the delivery process cancel the delivery order first")

    def cancel_delivery_order(self):
        # return:-
        # arg:-
        # it will change delivery state to cancel
        del_id = input("Enter delivery id to cancel")
        if del_id in self.delivery_order.keys() and self.delivery_order[del_id]['state'] == 'draft':
            for stock_move in self.delivery_order[del_id]['stock_move']:
                stock_move['state'] = 'cancel'
                self.product_details[stock_move['product_code']]['stock'] += stock_move['product_qty']
            self.delivery_order[del_id]['state'] = 'cancel'
            self.sale_orders[self.delivery_order[del_id]['sales_order']]['state'] = 'cancel'

            for itm in self.sale_orders[self.delivery_order[del_id]['sales_order']]['order_lines']:
                itm['state'] = 'cancel'
        else:
            print("delivery id not found or it can not be cancel")


def choice():
    # arg : -
    # give menu and take choice of user
    # return : choice of user
    print("1.create product")
    print("2.update stock")
    print("3.create customer")
    print("4.create sale order")
    print("5.display sale order")
    print("6.change sale order state")
    print("7.print dict of sale and product")
    print("8.validate delivery order")
    print("9.cancel sale order")
    print("0.Exit!!")
    choice = input("Enter Your Choice :")
    return choice


ch = choice()
se = Saleorder_Extended()

def change_order_state():
    # arg:-
    # return:-
    # it will change the order state
    print("1.confirm order")
    print("2. cancel order")
    print("3. set order to draft")
    choice = input("Enter Your Choice :")

    if choice == '1':
        d_id = se.confirm_order()
        print(d_id,"generated for delivery")
    elif choice == '2':
        se.check_in_extendedsale()
    elif choice == '3':
        se.set_order_to_draft()
    else:
        print("invalid")


while ch != '0':
    if ch == '1':
        sku = se.create_product()
        print(sku, "Added...")
    elif ch == '2':
        se.update_stock()
    elif ch == '3':
        cust_id = se.create_customer()
        print(cust_id, "Added...")
    elif ch == '4':
        se.create_sale_order()
    elif ch == '5':
        se.display_sale_order()
    elif ch == '6':
        change_order_state()
    elif ch == '7':
        se.print_all()
    elif ch == '8':
        se.validate_delivery_order()
    elif ch == '9':
        se.cancel_delivery_order()
    else:
        print("Invalid choiice")
    ch = choice()
