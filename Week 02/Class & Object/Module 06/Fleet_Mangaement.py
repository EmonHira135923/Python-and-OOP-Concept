class Company:
    def __init__(self,name,owener):
        self.name = name
        self.owener = owener
        self.driver = []
        self.supervisor = []
        self.counter = []
class Driver:
    def __init__(self,name,district,license,age):
        self.name = name
        self.district = district
        self.license = license
        self.age = age
    def __repr__(self):
        return f"Driver Name : {self.name}\nDriver District : {self.district}\nDriver License : {self.license}\nDriver Age : {self.age}"

class Supervisor:
    def __init__(self,name,age,driver_name):
        self.name = name
        self.age = age
        self.driver_name = driver_name
    def __repr__(self):
        return f"Supervisor Name : {self.name}\nSuperVisor age : {self.age}\nDriver Name : {self.driver_name}"
class Counter:
    def __init__(self,start_place,end_place,ticket):
        self.start_place = start_place
        self.end_place = end_place
        self.tickekt = ticket
    def __repr__(self):
        return f"Counter Start Place : {self.start_place}\nCounter End Place : {self.end_place}\nTicket : {self.tickekt}"

Emon = Driver("Emon Hossain Hira","Lakshmipur",1205,25)
print(Emon)
Loknow = Supervisor("Loknow Shil",20,"Emon Hossain Hira")
print(Loknow)
Traveler = Counter("Dhaka","Coxs Bazar",1)
print(Traveler)
        
            
        