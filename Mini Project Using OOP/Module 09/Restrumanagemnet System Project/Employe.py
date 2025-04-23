from user_class import *
from Food_item import *
from restrurant import *
from Menu import *
from user_class import *

class Employee(User):
    def __init__(self, name, email, phone, address, age, position, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.position = position
        self.salary = salary
    def __repr__(self): 
        return f"Employe: {self.name},Employe Email: {self.email},Employe Phone: {self.phone},Employe Address: {self.address},Employe age {self.age},Employe position {self.position},Employe Salary {self.salary}"
       
       #Done all