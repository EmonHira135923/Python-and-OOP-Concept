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


        

        
        