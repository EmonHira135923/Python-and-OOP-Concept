class Gadget:
    def __init__(self,brand,Ram,Rom,Price,Made_in):
        self.brand = brand
        self.Ram = Ram
        self.Rom = Rom
        self.Price = Price
        self.Made_in = Made_in
    # def __repr__(self):
        # return f"Welcome Sir! This is a {self.brand} Company Laptop.It's {self.Ram} Ram and {self.Rom} Rom included.Its Present Price {self.Price} Taka and It's Made in {self.Made_in}"
    def __repr__(self):
        return f"Welcome Sir! This is a {self.brand} Company.It's {self.Ram} Ram and {self.Rom} Rom are included.Its Present Price {self.Price} Taka and It's Made in {self.Made_in}"


class Laptop:
    def __init__(self,key_board_size):
        self.key_board_size = key_board_size
    def __repr__(self):
        return f"Welcome Sir ! Latop Key board size is {self.key_board_size}"
class Phone:
    def __init__(self,phone_size):
        self.phone_size = phone_size
    def __repr__(self):
        return f"Welcome Sir ! Latop Key board size is {self.key_board_size}" 

# Emon = Laptop("Toshiba",12,256,45000,"Bangladesh",10)
# print(Emon)     
# Hira = Phone("Oppo",2,64,10000,"India",5)
# print(Hira)
Emon = Gadget("OPPO",2,64,10000,"India")
Hira = Gadget("Toshiba",12,256,100000,"Bangladesh")
print(Emon)
print(Hira)
        