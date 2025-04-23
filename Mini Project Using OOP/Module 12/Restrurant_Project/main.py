from Admin_class import Admin
from Customer import Customer
from Restrurant import Restrurant

rest = Restrurant("Khaiya jaa")

def Admin_Menu():
    try:
        name = str(input("Enter Admin Name : ")) 
        admin = Admin(name=name)
        while True:           
            print(f"\nWelcome Admin : {admin.name}")
            print()
            print(f"----- {admin.name}  Menu ------")
            print("1.Create Customer Account")
            print("2.Remove Customer Account")
            print("3.View All Customers")
            print("4.Manage Restrurant Menu")
            print("5.Exit") 
        
            try :
                op = int(input("Enter Your Option: "))
            except ValueError:
                print("Invalid Input")
                continue 
        
            if(op==1):
                cus_name = str(input("Enter Customer Name :"))
                cus_email = str(input("Enter Customer email :"))
                cus_address = str(input("Enter Customer address :"))
                customer = Customer(name=cus_name,email=cus_email,address=cus_address)
                Admin.add_customer(admin,rest,customer)
            elif(op==2):
                remove_name = str(input("Enter remove Customer Name : "))
                Admin.remove_customer(admin,rest,remove_name)
            elif(op==3):
                Admin.show_customer(admin,rest)
            elif(op==4):
                while True:
                    print("1. Item Added")
                    print("2. Item Delete")
                    print("3. Item View")
                    print("4. Price Update")
                    print("5. Exit")
                    
                    try :
                        op = int(input("Enter Your Option: "))
                    except ValueError:
                        print("Invalid Input")
                        continue 
                    
                    if(op==1):
                        item_name = str(input("Enter Item Name : "))
                        item_price = int(input("Item Price : "))
                        item_quen = int(input("Enter item quentity : "))
                        admin.add_item(rest,item_name,item_price,item_quen)
                    elif(op==2):
                        del_item_name = str(input("Deleted Item name : "))
                        admin.remove_item(rest,del_item_name)
                    elif(op==3):
                        admin.view_item(rest)
                    elif(op==4):
                        item_name_update = str(input("Enter Item name for update price : "))
                        item_price_update = int(input("Enter Update Price : "))
                        admin.update_price(rest,item_name_update,item_price_update)
                    elif(op==5):
                        print("Every Think Done")
                        break
                    else:
                        print(f"Invallid Input")   
                    
            elif(op==5):
                print("Thank You Sir,See You Again")
                break
            else:
                print(f"{name} Invallid Input\n") 
    except:
        print("Input vallid input")           
                      
def Customer_Menu():
    try:
        customer_name = str(input("Enter Customer Name : "))
        customer = None
        for cus in rest.list_customer:
            if cus.name == customer_name:
                customer = cus
                break
        if not customer:
            print("No Customar Here")
            return            
        
        while True:
            print(f"Welcome Customer : {customer_name}")
            print()
            print(f"----- {customer_name} Menu ------")
            print("1.View Restrurant Menu")
            print("2.View Balance")
            print("3.Add Balance")
            print("4.Place Order")
            print("5.Past Order")
            print("6.Exit") 
            
            try :
                op = int(input("Enter Your Option: "))
            except ValueError:
                print("Invalid Input")
                continue 
            
            if(op==1):
                Customer.view_Menu_item(customer,rest)
            elif(op==2):
                Customer.view_balance(customer)
            elif(op==3):
                Taka = int(input("Enter Your Money : "))
                Customer.add_money(customer,Taka)
            elif(op==4):
                while True:
                    print("1. Add To Cart")
                    print("2. Checkout")
                    print("3. View Cart")
                    print("4. View Menu Cart")
                    print("5. Exit")
                    
                    try :
                        op = int(input("Enter Your Option: "))
                    except ValueError:
                        print("Invalid Input")
                        continue 
                    if(op==1):
                        order_food_item = str(input("Enter Your Food Item : "))
                        order_food_quentity = int(input("Enter Your Item Quentity : "))
                        Customer.Order(customer,rest,order_food_item,order_food_quentity)
                    elif(op==2):
                        Customer.check_out(customer)
                    elif(op==3):
                        Customer.show_cart(customer)
                    elif(op==4):
                        Customer.view_Menu_item(customer,rest)                  
                    elif(op==5):
                        print("Every Think Done")
                        break
                    else:
                        print(f"Invallid Input")                             
            elif(op==5):
                Customer.past_order(customer)
            elif(op==6):
                print("Thank You Sir,See You Again")
                break
            else:
                print(f"{customer_name} Invallid Input\n")
    except:
        print("print value error")
          

def Menu():
    while(True): 
        try:
            print(f"------ Welcome to Restrurant Managment System --------")
            print("1.Admin Login")
            print("2.Customer Login")
            print("3.Exit Login")
            
            try :
                option = int(input("Enter Your Option: "))
            except ValueError:
                print("Invalid Input")
                continue    
            
            if(option==1):  
                Admin_Menu()  
            elif(option==2):
                Customer_Menu()      
            elif(option==3):
                print("Thank You sir,See You again") 
                break   
            else:
                print("Invallid Input\n")
        except:
            print("Please vallid input")        

Menu()   

 

   