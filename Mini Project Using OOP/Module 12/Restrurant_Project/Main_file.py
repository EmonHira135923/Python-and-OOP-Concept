class Restrurant:
    def __init__(self,name):
        self.name = name
        self.list_customer = []
        self.Menu_list = []
    
    def add_customer(self,customer): 
        try: 
            self.list_customer.append(customer)
            print("Added Customer")
        except:
            print("Please valid Input")   
    
    def show_customer(self):
        try:
            if not self.list_customer:    
                print("NO Customer here")
            else:
                for cus in self.list_customer:
                    print(cus)  
        except:
            print("Please valid Input")   
    
    
    def customer_remove(self,cus_name):
        try:
            for cus in self.list_customer:
                if cus.name == cus_name:
                    self.list_customer.remove(cus)
                    print("Customer Remove")
                    break
            print("NO Man in this list") 
        except:
            print("Please valid Input")        
    
    def add_item(self,item,price,quentity):
        try:
            product = {
                "name" : item,
                "price" : price,
                "quentity" : quentity
            }         
            self.Menu_list.append(product)
            print("Item added")
        except:
            print("Please valid Input")       
    
    def remove_item(self,item):
        try:
            for food in self.Menu_list:
                if food["name"] == item:
                    self.Menu_list.remove(food)
                    print("Item Deleted")
                    break
            else:       
                print("No item Here")
        except:
            print("Please valid Input")   
    
    def view_item(self):
        try:
            print(f".........Restrurant Food Item ............")
            if not self.Menu_list:
                print("No item Here")
            else:
                for item in self.Menu_list:
                    print(f"Item Name - {item['name']} - Price: {item['price']}, Quantity: {item['quentity']}")  
        except:
            print("Please valid Input")   
            
    def update_price(self,item_name,new_price):
        try:
            for item in self.Menu_list:
                if item["name"] == item_name:
                    item["price"] = new_price 
                    print("Price Update")
                    break
            else:           
                print("NO item there no change")
        except:
            print("Please valid Input")           
class Customer:
    def __init__(self,name,email,address):
        self.name = name 
        self.email = email
        self.address = address
        self.wallet = 0
        self.add_to_cart = []  
        self.past_order_history = []     
    
    def view_Menu_item(self,restrurant):
        try:
            if not restrurant.view_item:
                print("No Menu Item")
            else:
                restrurant.view_item()
        except:
            print("Please valid Input")        
    
    def view_balance(self):
        try:
            print(f"Your Balance Avilable Here : {self.wallet}")
        except:
            print("Please valid Input")   
        
    def add_money(self,amount):
        try:
            if amount > 0:
                self.wallet += amount
                print(f"Balance Added {amount}")
            else:
                print(f"No money added {self.wallet}") 
        except:
            print("Please valid Input")         
             
    def Order(self,restrurant,item_name,quentity):
        try:
            for item in restrurant.Menu_list:
                if item["name"] == item_name:
                    if item["quentity"] >= quentity:
                        product = {
                            "name": item["name"],
                            "price": item["price"],
                            "quentity": quentity
                        }
                        self.add_to_cart.append(product)
                        item["quentity"] -= quentity
                        print(f"Item Added and quentity avilable : {item['quentity']}")
                    else:
                        print(f"Item Limit Exceed and quantity avilable : {item['quentity']}")
        except:
            print("Please valid Input")   
                                
    def show_cart(self):
        try:
            print(f"......... {self.name} Cart ............")
            if not self.add_to_cart:
                print("No item Here")
            else:
                for item in self.add_to_cart:
                    print(f"Item Name - {item['name']} - Price: {item['price']}, Quantity: {item['quentity']}")                              
        except:
            print("Please valid Input")   
        
    def check_out(self):
        try:    
            total = 0
            if not self.add_to_cart:
                print("No item here and no charge")
            
            for item in self.add_to_cart:
                total += item["price"] * item["quentity"]
            
            if self.wallet >= total:
                self.wallet -= total
                print(f"Paid Succesfully and your wallet {self.wallet} Taka")
                self.add_to_cart.clear()
            else:
                print(f"Sorry Sir Please give me Total charge money {total}") 
        except:
            print("Please valid Input")       
        
    def past_order(self):
        try:
            
            if not self.add_to_cart:
                print("No item here and no past record")
            else:
                print(f"...........Past Order.............")
                for i, order in enumerate(self.past_order_history, 1):
                    print(f"\nOrder {i}:")
                    for item in order:
                        print(f"{item['name']} - {item['quantity']} pcs - {item['price']}") 
        except:
            print("Please valid Input")                                    
    
    def __repr__(self):
        return f"Customer Name : {self.name},Customer Email : {self.email},Customer Address : {self.address}"
class Admin:
    def __init__(self,name):
        self.name = name
          
    def add_customer(self,restrurant,customer):
        restrurant.add_customer(customer)
    
    def show_customer(self,restrurant):
        restrurant.show_customer()
    
    def remove_customer(self,restrurant,cus_name):
        restrurant.customer_remove(cus_name)
    
    def add_item(self,restrurant,item,price,quentity):
        restrurant.add_item(item,price,quentity)
    
    def remove_item(self,restrurant,item):
        restrurant.remove_item(item)
    
    def view_item(self,restrurant):
        restrurant.view_item()
        
    def update_price(self,restrurant,item_name,price):
        restrurant.update_price(item_name,price)


        

        
        