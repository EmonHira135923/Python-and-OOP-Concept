from User_class import User

class Seller(User):
    
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.product_list = []
    
    def update_mail(self,email,password):
        self.set_email_pass(email,password) 
    
    def product_add(self,prodcut_name,price,quentity):
        prodcut = {"product name":prodcut_name,"price":price,"quantity":quentity}
        self.product_list.append(prodcut) 
        print("Item added") 
    
    def product_remove(self,product_name):
        for item in self.product_list:
            if item["product name"] == product_name:
                self.product_list.remove(item)
                print("Item Deleted",product_name)
                break
        else:
            print("NO ITEM FOUND!",item)
            
    def show_item(self):
        print(">>>>>>>>>>>> Avilabele Product <<<<<<<<<<<<<<")
        for item in self.product_list:
            if item["quantity"] > 0:
                print(item)
    
    def stock_item(self,name,quantity):
        for item in self.product_list:
            if item["product name"] == name:
                print("Item avilable",item["product name"])
                if item["quantity"] >= quantity:
                    item["quantity"] -= quantity
                    print("Added Your Cart")
                else:
                    print("Item Limit Exceed")          
    
    def __repr__(self):
        return f"Seller Name : {self.name},Seller E-mail : {self.email},Seller Pass : {self.password}"    

