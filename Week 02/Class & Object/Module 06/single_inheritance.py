class Company:
    def __init__(self,company_name,owener):
        self.company_name = company_name
        self.owener = owener
    def __repr__(self):
        return f"My Company name is {self.company_name}. I am a owener and my name is {self.owener}"

class Company_Place(Company):
    def __init__(self, company_name, owener,Place,Address):
        self.company_name = company_name
        self.owener = owener
        self.place = Place
        self.address = Address
        super().__init__(company_name, owener)
    def __repr__(self):
        return f"Hi, This is {self.company_name}. Our Owener {self.owener}. It Place in {self.place}. It Address in {self.address}"

# my_company = Company("Bangladesh IT LTD","Emon Hossain Hira")
# print(my_company)

my_company = Company_Place("Bangladesh IT LTD","Emon Hossain Hira","Dhaka","Motijil")
company = Company("Bangladesh IT LTD","Emon Hossain Hira")
print(company)

print(my_company)
        