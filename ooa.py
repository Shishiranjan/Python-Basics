# Lecture 1 of object oriented programming in python
'''
class program():
   def __init__(self, *args, **kwargs):  # Here init is the method which have three properties namely self, args and kwargs.
       self.lang = input("What language?:")
       self.version = float(input("Which version?:"))
       self.skill = input("What skill you have?:")

       
The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function.What *args allows you to do is take in
 more arguments than the number of formal arguments that you previously defined.For example : we want to make a multiply function that takes any number of arguments
 and able to multiply them all together. It can be done using *args.
 

   def upgrade(self):
        new_version = float(input("What is the new version?:"))
        print("We have upgraded the version for", self.lang)
        self.version = new_version                        

p1 = program()# Here we call the class program.

The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double
The reason is because the double star allows us to pass through keyword arguments (and any number of them).One can think of the kwargs as being a dictionary that
maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed
out.
'''


class Student():
   def Student_details(self, *args, **kwargs):
     self.student_name = ("What is the name of student?:")
     self.student_rollno = ("What is the rollno of student?:")
     self.student_address = ("Where does the student live?:")

p2 = Student()
