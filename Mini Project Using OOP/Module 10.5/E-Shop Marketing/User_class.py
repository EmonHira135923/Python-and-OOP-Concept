class User:
    
    verifay =  [] 
      
    def __init__(self,name,email,password):
        self.name = name
        self.__email = email
        self.__password = password
        
        if self.email in User.verifay:
            print("Please Insert New e-mail that's using")
        else:
            self.verifay.append(self.email)
            print("Email Implement")
        
    @property
    def email(self):
        return self.__email
    
    @property
    def password(self):
        return self.__password
    
    
    def set_email_pass(self,email,password):
        
        if  email in User.verifay:
            print("Please Insert New e-mail that's using")
        else:
            if self.email in User.verifay:
                User.verifay.remove(self.email)
                print("Delete Your Mail")
            
            self.__email = email
            self.__password = password
            self.verifay.append(self.email)
        
    def __repr__(self):
        return f"User Name : {self.name},User E-mail : {self.email},User Pass : {self.password}"           


     

    
        