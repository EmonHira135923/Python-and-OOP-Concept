class Booklist:
    pass
    def __init__(self,Owener,Book_name,price):
        self.owener = Owener
        self.Book_name = Book_name
        self.price = price

list_call = Booklist("Rahat","Phitron C Programming",2100)
list_call_next = Booklist("Sifat","Phitron C++ Programming",2100)
list_call_next_next = Booklist("Jhankar","Phitron Python Programming",2100)
print(list_call.owener,list_call.Book_name,list_call.price)
print(list_call_next.owener,list_call_next.Book_name,list_call_next.price)
print(list_call_next_next.owener,list_call_next_next.Book_name,list_call_next_next.price)