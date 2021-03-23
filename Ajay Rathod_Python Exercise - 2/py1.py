# Write a program that contains ‘manufacturing’ class which allows product manufacturing.
# It purchases raw material from the market and produces a product.
# One should manage the raw material product to produce the actual product.
# One should manage the ratio of raw material to produce the actual product.
# Example - 2 wheels(raw material) are required to produce 1 bicycle(actual product)
# Take input from user raw material, raw material ratio qty, actual product
# While producing the actual product, if the system doesn’t have enough of its stock of raw material,
# it should show a warning message as “Not enough raw material available to produce the product, please
# do the purchase”.
# Program should be menu driven allowing to
# Purchase Raw Material Product
# Manufacture Actual Product
# Show Raw Material Quantity
# Show Actual Product Quantity
# Exit
# Following attributes and method function should be part of the class
# Appropriate constructor to set the values for raw material product, actual product, raw material ratio
# qty value, raw material qty
# produce() - taking no qty to be produced for actual product as argument
# display_raw_material_stock()
# display_final_product_stock()
# purchase_raw_material() - taking no of qty of raw material to be purchased

# create class for Manufacturing
class Manufacturing:
    def __init__(self,rawmaterial,rawmaterialratioqty,actualproduct):
        self.rawmaterial=rawmaterial
        self.rawmeterialratioqty=rawmaterialratioqty
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
        else: # else condition create
            # count raw material and actual product to product qty
            self.rawmaterial-=int(needofraw)
            self.actualproduct+=self.ProduceQty
    # define a display raw material stock method
    def display_raw_material_stock(self):
        #print raw material stock
        print("Remain raw material stock :"+str(self.rawmaterial))

    # define a method for display final product stock
    def display_final_product_stock(self):
        # print actual product stock
        print("Final Product stock is:"+str(self.actualproduct))
    # define a choice method and print all manus
    def choice(self):
        #print all the manu
        print("1.Purchase Raw Material Product")
        print("2.Manufacture Actual Product")
        print("3.Show Raw Material Quantity")
        print("4.Show Actual Product Quantity")
        print("0.Exit \n Enter your choice:")
        # here a input any number
        choice = int(input())
        # # return a values
        return choice

# create a onject for Manufacturing class
obj=Manufacturing(0,0,0)
choice=obj.choice()
# define a while loop
while choice!=0:
    # define a if condition and choice number
    if choice == 1:
        # enter teh values of raw qty purchase
        RawQtyPur = input("enter no of qty want to purchase: ")
        obj.purchase_raw_material(RawQtyPur)
        choice=obj.choice()
    # define a if else condition here
    elif choice == 2:
        ProduceQty = input("Enter no of product produce:")
        rawitemperproduct = input("Enter no of need raw material for 1 item:")
        obj.produce(int(ProduceQty),int(rawitemperproduct))
        choice=obj.choice()
    elif choice == 3:
        obj.display_raw_material_stock()
        choice=obj.choice()
    elif choice == 4:
        obj.display_final_product_stock()
        choice=obj.choice()
    else:
        print("Invalid choiice")
        choice=obj.choice()
