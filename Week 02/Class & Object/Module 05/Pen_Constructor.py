class Pen_Update:
    pass
    def __init__(self,Company,Manager,Pen_name,Price):
        self.Company = Company
        self.Manager = Manager
        self.Pen_name = Pen_name
        self.Price = Price

res = Pen_Update("Real Boss","Emon Hossain Hira","Magic Pen",500)
res_1 = Pen_Update("I gell IT","Jillu Vai","Gell Pen",250)
res_2 = Pen_Update("Mayer Doya Pen Supplay","Maruf","Mattador Pen",400)

print(res.Company,res.Manager,res.Pen_name,res.Price)
print(res_1.Company,res_1.Manager,res_1.Pen_name,res_1.Price)
print(res_2.Company,res_2.Manager,res_2.Pen_name,res_2.Price)