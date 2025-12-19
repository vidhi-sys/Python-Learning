class Item:
    def __init__(self,x:str ,y:float,z:int):
        self.x=x
        self.y=y
        self.z=z
        assert y>=0, "price must be positive"
        #to match our expectations
        # both price and quantity must take 0 or +ve values
        assert z>=0,"quantity must be positive"
        print("constructor created at object creation time ")
        
    def calculate_price(self):
        print(f"total price for object:{self.x}")
        result=self.y*self.z
        return result
item_01=Item("ball",25,10)
print("item name:"+item_01.x)
print("item price $ " ,item_01.y)
print("item quantity" ,item_01.z)
item_02=Item("bats",75,45)
print(item_01.calculate_price())
print(item_02.calculate_price())
        
