class Grand_Father_Family:
    def __init__(self,Grand_Father,Grand_Mother):
        self.grand_fa = Grand_Father
        self.grand_ma = Grand_Mother
    def __repr__(self):
        return f"Hi, Introducing My Family . My Family Build Up this man ... This man my grand pa... My GrandFather Name is {self.grand_fa} and His Wife {self.grand_ma}."

class Grand_Father_Child(Grand_Father_Family):
    def __init__(self, Grand_Father, Grand_Mother,Daughter_1,Daughter_2,Son_1,Son_2,Son_3,Son_4,Son_5,Son_6):
        self.grand_fa = Grand_Father
        self.grand_ma = Grand_Mother
        self.daug_1 = Daughter_1
        self.daug_2 = Daughter_2
        self.son_1 = Son_1
        self.son_2 = Son_2
        self.son_3 = Son_3
        self.son_4 = Son_4
        self.son_5 = Son_5
        self.son_6 = Son_6
        super().__init__(Grand_Father, Grand_Mother)
    def __repr__(self):
        # return  f"His Two Daugther. Frist Name is {self.daug_1} and Secend Name is {self.daug_2}" 
        return f" Hi, Introducing My Family . My Family Build Up this man ... This man my grand pa... My GrandFather Name is {self.grand_fa} and His Wife {self.grand_ma}.His Two Daugther. Frist Name is {self.daug_1} and Secend Name is {self.daug_2}"

class Boro_Fufi_Family(Grand_Father_Child):
    def __init__(self, Grand_Father, Grand_Mother, Daughter_1, Daughter_2, Son_1, Son_2, Son_3, Son_4, Son_5,Son_6,Fufi_son_1,Fufi_son_2,Fufi_son_3,Fufi_daughter):
        self.grand_fa = Grand_Father
        self.grand_ma = Grand_Mother
        self.daug_1 = Daughter_1
        self.daug_2 = Daughter_2
        self.son_1 = Son_1
        self.son_2 = Son_2
        self.son_3 = Son_3
        self.son_4 = Son_4
        self.son_5 = Son_5
        self.son_6 = Son_6
        self.fufi_son_1 = Fufi_son_1
        self.fufi_son_2 = Fufi_son_2
        self.fufi_son_3 = Fufi_son_3
        self.fufi_daughter = Fufi_daughter
        super().__init__(Grand_Father, Grand_Mother, Daughter_1, Daughter_2, Son_1, Son_2, Son_3, Son_4, Son_5,Son_6) 
    def __repr__(self):
        return f"Hi, Introducing My Family . My Family Build Up this man ... This man my grand pa... My GrandFather Name is {self.grand_fa} and His Wife {self.grand_ma}.His Two Daugther. Frist Name is {self.daug_1} and Secend Name is {self.daug_2}"

# My_Family_f = Grand_Father_Family("Badsha Miya Hawlader","Toyoba Khattun")
My_Family_s = Grand_Father_Child("Badsha Miya Hawlader","Toyoba Khattun","Lutfa","Sultana","Elisah","Boshir","Selim","Mohsin","Khorsed","Sobuj")
# print(My_Family_f)        
print(My_Family_s)