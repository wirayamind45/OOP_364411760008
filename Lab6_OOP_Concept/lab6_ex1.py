
# class creation
class Student:
    #clas attribute
    faculty = "MT"
    #niit mettod
    def __init__(self,name,major,gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    # display object attribute
    def studen_info(self):
        print(f'name:{self.name} major:{self.major} gpa:{self.gpa}')

# object creation
s1 = Student("Mind","MIT",3.00)
s2 = Student("Film","DBM",3.55)
# s3 = Student()

#display attribut
print(s1.name, s1.major,s1.gpa)
print(s2.name, s2.major,s2.gpa)

# display with
print(f'name:{s1.name} major:{s1.major} gpa:{s1.gpa}')
print(f'name:{s2.name} major:{s2.major} gpa:{s2.gpa}')

print(s1.faculty,s2.faculty)

# change data in object attribute
print(s1.major)

s1.major = "MG"
print(s1.major)

#object call method in class
s1.studen_info()
s2.studen_info()

#list

std_list = [] # std_list = [s1,s2]
std_list.append(s1)
std_list.append(s2)
# display number of object in list
print(len(std_list))

# for loop and list
for x in  std_list:
    x.studen_info()