class User:
    
    verifay =  [] 
      
    def __init__(self,name,email,password):
        self.name = name
        self.__email = email
        self.__password = password
        
        if self.email in User.verifay:
            print("Please Insert New e-mail that's using")
        else:
            self.verifay.append(email)
            print("Email Implement")
        
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    
    def set_email_pass(self,email,password):
        
        if  email in User.verifay:
            print("Please Insert New e-mail that's using")
        else:
            if self.email in User.verifay:
                User.verifay.remove(self.email)
                print("Delete Your Mail")
            
            self.__email = email
            self.__password = password
            self.verifay.append(self.email)
        
    def __repr__(self):
        return f"User Name : {self.name},User E-mail : {self.email},User Pass : {self.password}"           

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
    
        
    
        

     

    
        