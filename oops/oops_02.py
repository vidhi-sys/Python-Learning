class Item:
    pay_rate=0.8
    all=[]
    def __init__(self,x:str ,y:float,z:int):
        self.x=x
        self.y=y
        self.z=z
        Item.all.append(self)
        
        
    def calculate_price(self):
        print(f"total price for object:{self.x}")
        result=self.y*self.z
        return result
    def apply_discount(self):
        self.y=self.y*self.pay_rate
        #read instance level so we didnt use Item.pay_rate
    def __repr__(self):
        return f"{self.x,self.y,self.z}"
        
item_01=Item("ball",25,10)
item_02=Item("bats",75,45)
        
item_03=Item("cat food",25,10)
item_04=Item("knife",75,45)
#class and instance attributes 
print(Item.pay_rate)
#magic method
print(Item.__dict__)
print(item_02.__dict__)
item_01.apply_discount();
print("discounted price",item_01.y)
# setting pay_rate for bats only
item_02.pay_rate=0.9
item_02.apply_discount();
print("discounted price",item_02.y)
print(Item.all)
for i in Item.all :
    print(i.x)
    

        
