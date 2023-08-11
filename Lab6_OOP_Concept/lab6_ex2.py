class Student:
    def __init__(self):
        self.name = ""
        self.major = ""
        self.gpa = 0

    # display object attribute
    def studen_info(self):
        print(f'name:{self.name} major:{self.major} gpa:{self.gpa}')

s1 = Student()
#assign data to object attribute
s1.name = "Mind"
s1.major = "MIT"
s1.gpa = 3.0

# display student data
s1.studen_info()

# get data form user
# s2 = Student()
# s2.name = input("Enter name: ")
# s2.name = input("Enter major: ")
# s2.name = float(input("Enter gpa: "))
# s2.Studen_info()

std = []

n = int(input('How many student? : '))
for i in range (n):
    s = Student()
    print(f"Please, enter student info {n+1}:")
    s.name = input("Enter name: ")
    s.major = input("Enter major: ")
    s.gpa = float(input("Enter gpa: "))
    std.append(s)

#display all student in list
for i in std:
    i.student_info()

