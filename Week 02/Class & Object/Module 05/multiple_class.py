class Student:
    def __init__(self,Name,Roll,Class):
        self.Name = Name
        self.Roll = Roll
        self.Class = Class
    def __repr__(self) -> str:
        return f'Student Name : {self.Name},Roll : {self.Roll},Class : {self.Class}'
class Teacher:
    def __init__(self,Name,Subject,Id):
        self.Name = Name
        self.Subject = Subject
        self.Id = Id
    def __repr__(self) -> str:
        return f'Teacher Name : {self.Name},Roll : {self.Subject},Class : {self.Id}'

class School:
    def __init__(self,Name) -> None:
        self.Name = Name
        self.Teacher = []
        self.Student = []

    def add_teacher(self,name,subject):
        id = len(self.Teacher) + 101
        teachers = Teacher(name,"Python",id)
        self.Teacher.append(teachers)
        print(f'{name} Welcome Sir')
    
    def add_student(self,name,fee):
        if fee < 6500:
            print(f"{6500-fee} Please Insert Some Money For Enroll")
        else:
            id = len(self.Student) + 1
            Students = Student(name,id,'python')
            self.Student.append(Students)
            print(f"{name} Welcome Phitron For Enrollment. Your Money Recive {fee-6500}")
    
    def __repr__(self):
        for teacher in self.Teacher:
            print(teacher)
        for student in self.Student:
            print(student)


# Emon = Student("Emon Hossain Hira",189123,7)
# print(Emon)    

# Emon_Teacher = Teacher("Jhankar Mahbub","Python",101)
# print(Emon_Teacher)

phitron = School("Phitron")
phitron.add_student("Emon Hossain Hira",6500)
phitron.add_student("Akbar Hossain",6650)
phitron.add_student("EH Hira",5000)
phitron.add_teacher("Sifat","Python")

