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
                
                order_copy = []                
                for item in self.add_to_cart:
                    order_copy.append({
                        "name": item["name"],
                        "price": item["price"],
                        "quentity": item["quentity"]
                    })

                self.past_order_history.append(order_copy)
                
                print(f"Paid Succesfully and your wallet {self.wallet} Taka")
                self.add_to_cart.clear()
            else:
                print(f"Sorry Sir Please give me Total charge money {total}") 
        except:
            print("Please valid Input")       
        
    def past_order(self):
        try:
            if not self.past_order_history:
                print("No item here and no past record")
            else:
                print(f"...........Past Order.............")
                for i, order in enumerate(self.past_order_history, start=1):
                    print(f"\nOrder {i}:")
                    for item in order:
                        print(f"Item Name: {item['name']} | Price: {item['price']} | Quantity: {item['quentity']}")
                    print("------------------------")
        except:
            print("Please valid Input")                                    
    
    def __repr__(self):
        return f"Customer Name : {self.name},Customer Email : {self.email},Customer Address : {self.address}"
