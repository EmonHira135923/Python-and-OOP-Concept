class Bank_Syestem:
    def __init__(self,Client_name,balance):
        self.Client_name = Client_name
        self.balance = balance
    def avilable_balance(self):
        return self.balance
    def deposit_amount(self,Id_name,deposit_money):
        self.Id_name = Id_name
        self.deposit_money = deposit_money
        if deposit_money > 0:
            self.balance += deposit_money
            print("Your Total Amount : ",self.avilable_balance())
        else:
            print("Your Balance Amount is low",self.avilable_balance())
    def withdraw_amount(self,Id_name,withdraw_money):
        if(self.balance<=0):
            # print(self.avilable_balance())
            print("No money Here")
        else:
            print("Your Avilable money : ",self.avilable_balance())
            self.balance -= withdraw_money
            print("Here Your Money",withdraw_money)
            print("after withdraw your avilable money",self.avilable_balance())




Bank_name = Bank_Syestem("Emon Hossain Hira",50)
# print(Bank_name.Client_name,Bank_name.balance)
# Bank_name.deposit_amount("Emon Hossain Hira",0)
if(Bank_name.balance>=0):
    Bank_name.withdraw_amount("Emon Hossain Hira",10)
else:
    print("No money is not withdraw")    
