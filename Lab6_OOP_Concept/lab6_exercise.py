class Notebook:
    def __init__(self):
        self.CPU = ""
        self.GPU = ""
        self.RAM = ""
        self.DISPLAY = ""
        self.STORAGE = ""
        self.OS = ""

    def Notebook_info(self):
            print(f'CPU:{self.CPU} GPU:{self.GPU} RAM:{self.RAM} DISPLAY:{self.DISPLAY} STORAGE:{self.STORAGE} OS:{self.OS}')

nb = []

n = int(input('How many Notebook? : '))
for i in range(n):
    s = Notebook()
    print(f"Please, enter Notebook info {i+2}:")
    s.name = input("Enter CPU: ")
    s.GPU = input("Enter GPU: ")
    s.RAM = input("Enter RAM: ")
    s.DISPLAY = input("Enter DISPLAY: ")
    s.OS = input("Enter OS: ")
    nb.append(s)

for i in nb:
    i.Notebook_info()