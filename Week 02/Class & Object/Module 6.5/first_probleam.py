class Product:
    def __init__(self,product_name):
        self.product = product_name

cus = Product("Alu")
print(cus.product)

class Shop:
    def __init__(self,cus_name,price,quentity):
        self.cus_name = cus_name
        self.price = price
        self.quen = quentity

Emon = Shop("Emon Hossain Hira",2500,2)
print(Emon.cus_name,Emon.price,Emon.quen)
        
        