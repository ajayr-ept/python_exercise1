"""Write a program having classes as Product, Order, Customer
Do appropriate inheritance of the above classes
Write appropriate methods / constructors in each classes
Following output is expected
Order No : SO001
Customer : Sanjay Patel
Customer Email : sanjay@dummy.com
Name of the product is 'Pencil'
Product Qty is : 15
Unit Price is 20
Order total is : 300
"""

class Product:#declar calss of product with name qty and uprice as var attribut ans product_detail and total is fun attribute
    def __init__(self,pName,qty,uprice):
        self.pName=pName
        self.qty=qty
        self.uprice=uprice
        #print(pName,qty,uprice) //test that value is set
    def product_detail(self):#present detail of producr
        print("name of product {}".format(self.pName))
        print("Product qty is :{}".format(self.qty))
        print("product unit price is :{}".format(self.uprice))
    def total(self):#return total of product
        print("product total is {}".format(self.qty*self.uprice))

class customer:#class with name and email of custmer attribute and cust_detail as fn attribute
    def __init__(self,cName,cEmail):

        self.cName=cName
        self.cEmil=cEmail
        #print(cName,cEmail)    //test that value is set
    def cust_detail(self):#present cust detail
        print("customer name is {}".format(self.cName))
        print("customer Email is {}".format(self.cEmil))

class order(Product,customer):#class with ono and order_detail as attribute ans inherite the product and custome class
    def __init__(self,oNo,cName,cEmail,pName,qty,uprice):
        customer.__init__(self,cName,cEmail)#calling super class init attribut
        Product.__init__(self,pName,qty,uprice)
        self.oNo=oNo
        #print(oNo) //test that value is set
    def order_detail(self):#present order detail
        print("order no is {}".format(self.oNo))
        self.cust_detail()#calling super class attribute
        self.product_detail()
        self.total()


or_dar=order("S0001","sanjay patel","sanjay@dummy.com","pencil",15,20)#creating obj of order class
or_dar.order_detail()#calling method using order calss






