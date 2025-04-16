class Product:
    def __init__(self,product_name,price,quentity):
        self.product_name = product_name
        self.price = price
        self.quen = quentity

class Shop:
    def __init__(self,buyer):
        self.cus_name = buyer
        self.cart = []
    def add_product(self,product_name,price,quentity):
        products = {'product_name': product_name,'price': price,'quentity':quentity}
        self.cart.append(products)
        
  
    
cus_name = str(input())
Emon = Shop(cus_name)
product_name,product_price,product_quentity = input().split()
product_name = str(product_name)
product_price= int(product_price)
product_quentity = int(product_quentity)

Emon.add_product(product_name,product_price,product_quentity)

print(Emon.cus_name,product_name,product_price,product_quentity)



    

    
