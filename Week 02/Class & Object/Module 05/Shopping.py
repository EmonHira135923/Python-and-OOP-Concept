class MyShopping:
    pass
    def __init__(self,name):
        self.name = name
        self.cart = []
    def add_to_cart(self,item,price,quentity):
        product = {'item': item,'price': price,'quentity':quentity}
        self.cart.append(product)
    def check_out(self,amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quentity']
        if total == amount:
            print(f"Thank You Sir,Your Taka All Clear {amount-total}")  
        elif amount > total:
            print(f"Thank You Sir! Take your money {amount-total}")    
        elif amount < total:
            print(f"Thank You Sir! Please Clear Your Money {amount-total}") 

    def remove_item(self,item_del):
        flag = False

        for item in self.cart:
            if item['item'] == item_del:
                flag = True
                self.cart.remove(item)
                break
        if flag == True:
            print(person_1.cart)
        else:
            print("NO item in this list")    
            


item1 = str(input())
item1_quen = int(input())
item1_price = int(input())
item2 = str(input())
item2_quen = int(input())
item2_price = int(input())
item3 = str(input())
item3_quen = int(input())
item3_price = int(input())
item4 = str(input())
item4_quen = int(input())
item4_price = int(input())

print(f" Market Avilable Item  \n {item1} : {item1_quen}Kg {item1_price} taka\n {item2} : {item2_quen}Kg  {item2_price} taka\n {item3} : {item3_quen} Case  {item3_price} Taka\n {item4} : {item4_quen} Kg {item4_price}Taka")

for i in range(2):
    print('\n')

person_name = str(input())
person_1 = MyShopping(person_name)

choice_item = str(input())
choice_item_quen = int(input())
choice_item_price = int(input())

person_1.add_to_cart(choice_item,choice_item_price,choice_item_quen)
print(*person_1.cart)

print(type(person_1.cart))

for i in range(2):
    print("\n")

amount = int(input())
person_1.check_out(amount)

item_del = str(input())
person_1.remove_item(item_del)

for i in range(2):
    print("\n")

after_choice_item_quen = item1_quen - choice_item_quen



print(f"After You Complete Your Market avilable  {item1} : {after_choice_item_quen}")




