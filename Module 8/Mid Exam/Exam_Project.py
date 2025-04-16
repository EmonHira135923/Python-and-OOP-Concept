class Library:
    book_list = []
    @classmethod
    def entry_book(Libary,book):
        Libary.book_list.append(book)
        
class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id = book_id
        self._title = title
        self._author = author
        self._availability = availability  
        
    @property
    def book_id(self):
        return self.__book_id
    
    @property
    def title(self):
        return self._title
    
    @property
    def author(self):
        return self._author
    
    @property
    def availability(self):
        return self._availability
    
    @availability.setter
    def availability(self,value):
        self._availability = value
        
    def __repr__(self):
        return (f"ID NO : {self.book_id},Title No : {self.title}, Author Name : {self.author}, Book's avilablable : {self.availability}")

    def borrow_book(self):
        if self.availability==True:
            self.availability = False
            print(f"The Book is {self.book_id} succesfully borrowed!")
        else:
            print(f"Sorry {self.book_id} Has Been Already Booked")
                
    def return_book(self):       
        if self.availability==False:
            self.availability = True
            print(f"The Book is {self.book_id} succesfully Retrun!")
        else:
            print(f"{self.book_id} This Book is Avilable ")
            
    def view_book_info(self):
        print(f"ID NO : {self.book_id},Title No : {self.title}, Author Name : {self.author}, Book's avilablable : {self.availability}")
        
        
        
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
            ------------------  Welcome To Libary Projects ------------------
                
                    1. View All Books
                    2. Borrow Book
                    3. Return Book
                    4. Exit.
            
        """)
        
        input_user = int(input("Enter Your Choice : "))
        
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
            except TypeError:
                print("User Type Error")
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
            except TypeError:
                print("User Type Error")  
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