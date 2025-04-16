from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def Move(self,left,right):
        pass

class Man(Person):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__()
    def Move(self,left,right):
        self.left = left
        self.right = right
        print(f"He is move {self.left} and also {self.right}") 


Emon = Man("Emon Hossain Hira",21)
Emon.Move("Left","Right")
