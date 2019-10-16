from employees import Employee
class Developer(Employee):
    salary_raise_amount = 1.15
    
    def __init__(self,name,salary,empid,prgm_lang):
        super().__init__(name,salary,empid)
        # Employee.__init__(self,name,salary,empid)
        self.prgm_lang = prgm_lang
    
    def details(self):
        print("{} {} {} {}".format(
            self.name,
            self.salary,
            self.empid,
            self.prgm_lang
        ))

print(Developer.numberofemp)
print(Developer.salary_raise_amount)

dev_1 = Developer("ayan",120000,45,"GO")
dev_1.details()
