class Booklist:
    pass
    def __init__(self,owener,designer,writter,price):
        self.owener = owener
        self.designer = designer
        self.writter = writter
        self.price = price

owe = str(input())
des = str(input())
wri = str(input())
pri = int(input())
result = Booklist(owe,des,wri,pri)
owen = str(input())
desi = str(input())
writ = str(input())
pric = int(input())
result_2 = Booklist(owen,desi,writ,pric)
print(result.owener,result.designer,result.writter,result.price)
print(result_2.owener,result_2.designer,result_2.writter,result_2.price)