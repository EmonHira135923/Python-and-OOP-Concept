class Library:
    book_list = []
    
    @classmethod
    def entry_book(Libary,book):
        Libary.book_list.append(book)

class Book:
    def __init__(self,book_id,title,author,availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability  
    
    def show_book_id(self,book_id):
       self.__book_id = book_id
        
    def __repr__(self):
        return (f"ID NO : {self.book_id},Title No : {self.title}, Author Name : {self.author}, Book's avilablable : {self.availability}")

    def borrow_book(self):
        if self.availability==True:
            self.availability = False
            print(f"The Book is {self.book_id} succesfully borrowed!")
        else:
            print(f"Sorry {self.book_id} Has Been Not Avilable")
                
    def return_book(self):
        if self.availability==False:
            self.availability = True
            print(f"The Book is {self.book_id} succesfully Retrun!")
        else:
            print(f"Sorry {self.book_id} Has Been Not Avilable")
            
    def view_book_info(self):
        print(self.__repr__()) 

Book_1 =  Book(101,"Python","Jhankar Mahbub",True)
Book_2 =  Book(102,"C","Rahat Khan Pathan",True)
Book_3  = Book(103,"C++","Piyas",True)
Book_4  = Book(104,"Java","Akbar Hossain",True)
Book_5  = Book(105,"Data Structure and Algorithom","Abdur Rahman Sifat",True)
Book_6  = Book(106,"DataBase","Ariful Islam",True) 

Library.entry_book(Book_1)
Library.entry_book(Book_2)
Library.entry_book(Book_3)
Library.entry_book(Book_4)
Library.entry_book(Book_5)
Library.entry_book(Book_6)

def Menu():

    while True:
        
        print("""
                1. View All Books
                2. Borrow Book
                3. Return Book
                4. Exit.
            """)
        
        input_user = int(input("Enter Your Choice : "))
        print()
        
        if input_user == 1:
            print("------------------ All Books in Library ------------------")
            for book in Library.book_list:
                book.view_book_info()
                
        elif input_user == 2:
            try:
                book_id = int(input("Enter Your BOOK_ID : "))
                flag = False
                for book in Library.book_list:
                    if book.book_id == book_id:
                        book.borrow_book()
                        flag = True
                        break
                if flag == False:
                    print(f"{book_id} is not return")
            except ValueError:
                print("User ValueError")
            except ZeroDivisionError:
                print("User ZeroDivison Error")
            finally:
                print("Everything Clear")     
            
        elif input_user == 3:
            try:
                book_id = int(input("Enter Your BOOK_ID : "))
                flag = False
                for book in Library.book_list:
                    if book.book_id == book_id:
                        book.return_book()
                        flag = True
                        break
                if flag == False:
                    print(f"{book_id} is not return")
            except ValueError:
                print("User ValueError")
            except ZeroDivisionError:
                print("User ZeroDivison Error")
            finally:
                print("Everything Clear")  
                
        elif input_user == 4:
            print("Thank You Sir ! For Visiting My Libary")
            break
        
        else:
            print("Invallid Input")  

Menu()
    




# cus = Library()
# cus.entry_book("Python")
# cus.entry_book("C")
# cus.entry_book("C++")
# cus.entry_book("Java")

# print(cus.book_list)

# person_1.borrow_book()
# person_1.return_book()

# print("------ All Books in Library ------")
# for book in Library.book_list:
#     book.view_book_info()

# print("\n")

# for book in Library.book_list:
#     print(book)
    





        
    