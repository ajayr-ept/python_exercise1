# Write a program which extends Program - 1
# Add appropriate class and perform inheritance
# Add the facility of scrapping the raw material product and actual product
# Add appropriate option in the menu for
# scrapping the raw material product
# scrapping the actual product
# Add appropriate methods to scrap the raw material product and actual product


class Manufacturing():
    def __init__(self,ramaterial,rawmateritalratioqty,actualproduct):
        self.rawmaterial=ramaterial
        self.rawmeterialratioqty=rawmateritalratioqty
        self.actualproduct=actualproduct

    def purchase_raw_material(self,RawQtyPur):
        #arg : raw material to purchse
        #increase current raw material with purchased raw material
        self.RawQtyPur=RawQtyPur
        self.rawmaterial+=int(RawQtyPur)

    def produce(self,ProduceQty,rawitemperproduct):
        #arg : qty to produce
        #print error if raw material is not enough
        #count remaining raw material and actual product
        self.ProduceQty=ProduceQty
        needofraw=rawitemperproduct*self.ProduceQty
        if(self.rawmaterial<needofraw):
            print("Not enough raw material available to produce the product, please do the purchase")
        else:
            self.rawmaterial-=int(needofraw)
            self.actualproduct+=(needofraw/rawitemperproduct)

    def display_raw_material_stock(self):
        #print raw material stock
        print("Remain raw material stock :"+str(self.rawmaterial))

    def display_final_product_stock(self):
        # print actual product stock
        print("Final Product stock is:" + str(self.actualproduct))

        # print actual product stock
        print("Final Product stock is:"+str(self.actualproduct))

    # define a choice method
    def choice(self):
        # print all the menu
        print("\n\n1.Purchase Raw Material Product")
        print("2.Manufacture Actual Product")
        print("3.Show Raw Material Quantity")
        print("4.Show Actual Product Quantity")
        print("5.scrapping the raw material product")
        print("6.scrapping the actual product")
        print("0.Exit \n Enter your choice:")
        #define a choice object and intgeter value input
        choice = int(input())
        # return a  values
        return choice
# create Scrap class in inherite the manufacturing class
class Scrap(Manufacturing):

    # create a constractor and Attribute
    def __init__(self,ramaterial,rawmateritalratioqty,actualproduct):
        Manufacturing.__init__(self,ramaterial,rawmateritalratioqty,actualproduct)

    def scrapraw(self,srQty):
        #qty that we want to scrap is argument
        #check for quantity and scrap from stock
        if self.rawmaterial >=srQty:
            self.rawmaterial-=srQty
            print(srQty,"is scraped from raw \nupdated raw is : ",self.rawmaterial)
        else:
            print("Raw material is not enough")

    def scrapaproduct(self,sapQty):
        # qty that we want to scrap is argument
        #check for quantity and scrap from stock
        if self.actualproduct >=sapQty:
            self.actualproduct-=sapQty
            print(sapQty, "is scraped from Actual product \n updated Actual product is : ",  self.actualproduct)
        else:
            print("Product is not enough")


s=Scrap(0,0,0)
choice=s.choice()

while choice!=0:
    if choice == 1:
        RawQtyPur = input("enter no of qty want to purchase: ")
        s.purchase_raw_material(RawQtyPur)
        choice=s.choice()
    elif choice == 2:
        ProduceQty = input("Enter no of product produce:")
        rawitemperproduct = input("Enter no of need raw material for 1 item:")
        s.produce(int(ProduceQty),int(rawitemperproduct))
        choice=s.choice()
    elif choice == 3:
        s.display_raw_material_stock()
        choice=s.choice()
    elif choice == 4:
        s.display_final_product_stock()
        choice=s.choice()
    elif choice == 5:
        srQty = int(input("Enter item scrap from raw material"))
        s.scrapraw(srQty)
        choice=s.choice()
    elif choice == 6:
        sapQty = int(input("Enter item scrap from Actual Product"))
        s.scrapaproduct(sapQty)
        choice=s.choice()
    else:
        print("Invalid choiice")
        choice=s.choice()
