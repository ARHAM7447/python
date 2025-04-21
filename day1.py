# # THIS IS THE FIRST PROGRAM OF DAY 1
# # This program is to create a class and object for student details
# class Student:
#     def __init__(self, name,roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Roll No: {self.roll_no}")
#         print(f"marks: {self.marks}")

#     #create the object for the program
# s1 = Student("arham",101,88)  
# s1.display() 

# # THIS IS THE SECOND PROGRAM OF DAY 1
# # this program is based on the non-input program 
# class Student:
#     def __init__(self, name,marks):
#         self.name = name
#         self.marks = marks
    
#     def check_pass(self):
#         if self.marks >= 40:
#             return "pass"
#         else:
#             return "fail"
        
# s1= Student("Arham", 35)
# print(f"{s1.name} - {s1.check_pass()}")

# # this is the third program of day 1
# # this program is based on the input program
# class student:
#     def __init__(self, name, marks):
#         self.name = name 
#         self.marks = marks 
    
#     def check_pass(self):
#         if self.marks >= 40:
#             return "pass"
#         else:
#             return "fail"
# name = input("Enter the student's name: ")
# marks = int(input("Enter the student's marks: "))

# s1 = student(name, marks)
# print(f"{s1.name} - {s1.check_pass()}")