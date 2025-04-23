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
            else:    
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
  