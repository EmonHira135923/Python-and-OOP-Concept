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
        products = {'product_name': product_name,price: price,quentity:quentity}
        self.cart.append(products)

    def buy_product(self,product_Name):
        
        flag = False

        for item in self.cart:
            if(item['product_name']==product_Name):
                flag = True
                self.cart.append(product_Name)
                break
        if flag == True:
            print(f'{self.cart} and Thank You Sir')
        else:
            print(f"Sorry Sir!NO item")        
  
    
cus_name = str(input())
Emon = Shop(cus_name)
product_name,product_price,product_quentity = input().split()
product_name = str(product_name)
product_price = int(product_price)
product_quentity = int(product_quentity)

Emon.add_product(product_name,product_price,product_quentity)

product_name_need = str(input()) 
Emon.buy_product(product_name_need)



    

    
