class Person:
    def __init__(self,name,age,height,weight,hobby):
        self.name = name 
        self.age = age
        self.height = height
        self.weight = weight
        self.hobby = hobby
        
    def eat(self):
        raise NotImplementedError
    
class Cricketer(Person):
    def __init__(self, name, age, height, weight, hobby,team,batsman=None,bowler=None,wicketkipper=None):
        self.team = team
        self.batsman = batsman
        self.bowler = bowler
        self.wicketkipper = wicketkipper   
        super().__init__(name, age, height, weight, hobby)   

    def eat(self):
        print("Eat Vegetable")
    
    def __add__(self,other):
        return self.age + other.age
    
    def __sub__(self,other):
        return self.age - other.age
    
    def __mul__(self,other):
        return self.age * other.age
    
    def __truediv__(self,other):
        return self.age / other.age
    
    def __gt__(self,other):
        return self.age > other.age
    



    def __repr__(self):
        return f"My name is {self.name},My age is now {self.age},My Height {self.height}c.m,My Weight Now {self.weight},My hobby is {self.hobby},Right Now, I Play in {self.team},I am a {self.batsman},I am a {self.bowler} also.And I am  a {self.wicketkipper}"


person = Cricketer("Sakib Al Hasan",39,70,90,"Adviser","Bangladesh","Batsman","Bowler",None)
person1 = Cricketer("Mushfiq",37,65,85,"Adviser","Bangladesh",None,None,"Wicket-Kipper")

# print(person)
# print(person1)
# person.eat()

add_two = person + person1
sub_two = person - person1
mul_two = person * person1
div_two = person / person1
much_two = person > person1

print(add_two)
print(sub_two)
print(mul_two)
print(div_two)
print(much_two)

