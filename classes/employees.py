# class Employee:
#     def __init__(self,name,salary,empid):
#         self.name = name
#         self.salary = salary
#         self.empid = empid


# emp1 = Employee()
# emp2 = Employee()

# instamce variable
# emp1.name = "kevin"
# emp1.salary = "25000"
# emp1.id = "789"

# emp2.name = "james"
# emp2.salary = "35000"
# emp2.id = "780"

# emp1 = Employee("kevin",25000,789)
# emp2 = Employee("james",20000,780)


# print(emp1.name,emp1.salary,emp1.empid)
# print(emp2.name,emp2.salary,emp2.empid)

# class variable
class Employee:

    # class variable
    numberofemp = 0
    salary_raise_amount = 1.04

    def __init__(self,name,salary,empid):
        self.name = name
        self.salary = salary
        self.empid = empid

        # Employee.numberofemp
        Employee.numberofemp += 1

    def details(self):
        print("{} {} {}".format(self.empid, self.name ,self.salary))

    def print_numberofemp(self):
        print(self.numberofemp)
        print(Employee.numberofemp)

    def raiseAmount(self):
        self.salary = self.salary * self.salary_raise_amount 

    @classmethod
    def fromstring(cls,emp_string):
        name,salary,empid = emp_string.split("_")
        return cls(name,int(salary),int(empid))

    @staticmethod
    def is_weekend(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        else:
            return False

import datetime

my_date = datetime.date(2019,6,28)

# print(Employee.is_weekend(my_date))

# emp_1_details = "ram_45454564_788"
# emp_2_details = "sita_545464_798"

# new_emp1 = Employee.fromstring(emp_1_details)
# new_emp2 = Employee.fromstring(emp_2_details)




emp1 = Employee("kevin",25000,789)
emp2 = Employee("james",20000,780)

# print(Employee.numberofemp)
# Employee.salary_raise_amount = 1.06

# print(emp1.__dict__)

# emp1.salary_raise_amount = 1.04

# print(emp1.__dict__)

# emp1.details()
# emp1.raiseAmount()
# emp1.details()

# emp2.details()
# emp2.raiseAmount()
# emp2.details()

# print(emp2.numberofemp)

# alternative constructror
# new_emp1.details()
# new_emp2.details()

