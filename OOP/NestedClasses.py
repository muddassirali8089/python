

class Company:
    class Employee:
        def __init__(self , name , position):
            self.name = name
            self.position = position

        def getDetails(self):
             return {f"{self.name} {self.position}"}
    
    def __init__(self , companyName):
        self.companyName = companyName
        self.employees = []

    def addEmployee(self , name , position):
            newEmployee = self.Employee(name , position)
            self.employees.append(newEmployee)

    def displayEmployee(self):
            return [employee.getDetails() for employee in self.employees]


company = Company("Kodifly")

company.addEmployee("muddassir" , "mern")
company.addEmployee("khan" , "mean")
company.addEmployee("ali" , "node")




print(company.companyName)
print(company.displayEmployee())