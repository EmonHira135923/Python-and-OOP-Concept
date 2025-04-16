class Fish:
    cart = []
    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,fish_name,fish_size,fish_price,place):
        self.cart.append(fish_name)
        self.cart.append(fish_size)
        self.cart.append(fish_price)
        self.cart.append(place)

Emon = Fish("Emon Hossain Hira")
Emon.add_to_cart("Elish",25,5000,"Lakshmipur")
print(Emon.cart)
Emon_Hira = Fish("EH Hira Diamond")
Emon_Hira.add_to_cart("Telapiya",15,500,"Any Place")
print(Emon_Hira.cart)
# print("Emon_Hira",Emon_Hira.cart)
