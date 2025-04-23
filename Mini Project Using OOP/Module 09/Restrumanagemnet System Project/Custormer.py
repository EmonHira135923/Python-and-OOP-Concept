from user_class import *
from Order import *
from Menu import *
from Food_item import *

class Customer(User):
    def __init__(self, name, email, phone, address):  
        super().__init__(name, email, phone, address)
        self.cart = Order()
           
    def __repr__(self):
        return f"Customer Name: {self.name},Customer Email: {self.email},Customer Phone: {self.phone},Customer Address: {self.address}"     
    
    def view_menu(self,restrurant):
        restrurant.Menu.show_item_menu() # complete
    
    def add_to_cart(self,restrurant,item_name,quantity):
        item_find =  restrurant.Menu.find_item_menu(item_name)
        if item_find:
            item_find.quantity = quantity
            self.cart.add_items(item_find)
            print("Item added")
        else:
            print(f"Sorry Sir! There are No Item Found")
            
    def view_cart(self):

        print(f">>>>>>>> View Cart <<<<<<<<<")
        print(f"ItemName Price Quentity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t {item.price}\t {quantity}")
        print(f"Total Price : {self.cart.total_price}")
    

        
  