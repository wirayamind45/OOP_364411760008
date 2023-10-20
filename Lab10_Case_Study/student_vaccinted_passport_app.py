from model import Student, Vaccine, Vaccine_Passport



def display_vaccines():
    print("Vaccines list: ")
    n = 1
    for x in Vaccine.all_Vaccines:
        print(f'{n}. {x}')
        n = n+1

# # get student info
id = int(input("Enter student id? : "))
name = input("Enter student name ?: ")
major = input("Enter your major? : ")
age = int(input("How old are you? : "))
weight  = float(input("Enter your weight(kg.): "))
height  = int(input("Enter your height(cm.): "))

s = Student(id,name,major,age,weight,height)
# s.info()

#create vaccinated passport object

s_passport = Vaccine_Passport(s)

n = int(input("How many are you vaccinated?: "))
for x in range(n):

    display_vaccines()

    v = int(input(f'select 1- {len(Vaccine.all_Vaccines)}: '))
    s_passport.add_vaccinated(Vaccine(Vaccine.all_Vaccines[v-1]))

    date = input("Date(dd/mm/yyyy): ")
    s_passport.add_date(date)

s_passport.info()