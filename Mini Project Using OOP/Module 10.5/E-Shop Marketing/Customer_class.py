from User_class import User
from Seller_class import Seller
class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.cart = []
    
    def update_mail(self,email,password):
        self.set_email_pass(email,password)
        
    def __repr__(self):
        return f"Customer Name : {self.name},Customer E-mail : {self.email},Customer Pass : {self.password}"    

    def view_item(self,show):
        show.show_item()
        

