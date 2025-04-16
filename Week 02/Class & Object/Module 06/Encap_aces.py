class Animal:
    pass
    def __init__(self,Animal_Name,Price,quen):
        self.name = Animal_Name
        self.__Price = Price
        self._quen = quen
    def get_balance(self):
        return self.__Price   

Cat = Animal("Cat",1500,1)

print(Cat.name)
print(Cat.get_balance())
print(Cat._quen)
print(Cat._Animal__Price)


    
