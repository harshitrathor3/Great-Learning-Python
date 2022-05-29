class Employee:
    inc = 1.5
    n=0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.n+=1
        # self.inc = 1.2
    
    def increase(self):
        self.salary = self.salary * self.inc

    @classmethod
    def changeincreament(cls, amt):
        cls.inc = amt
    
    @classmethod
    def from_str(cls, emp_string):
        name, sal = emp_string.split("-")
        return cls(name, sal)

    @staticmethod
    def isopen(day):
        if day=="sunday":return False
        else:return True

class Programmer(Employee):
    def __init__(self, name, salary, lang, exp):
        super().__init__(name, salary)
        self.lang = lang
        self.exp = exp
    
    def increase(self):
        self.salary = self.salary * (self.inc+.2)

    def __add__(this, other):
        return this.salary + other.salary
    
    def __repr__(self) :
        return "Employee({}, {})".format(self.name, self.salary)
        

    def __str__(self):
        return "This is {}".format(self.name)
    


harry = Programmer("Harry", 20000, "Python", 5)
e1= Employee("EMPL", 20000)

print(repr(harry))
print(harry.__repr__())
print(harry.__str__())
# print(harry.lang)
# print(harry.exp)

# harry.increase()
# print(harry.salary)

# e1.increase()
# print(e1.salary)

# help(Programmer)

# print(Employee.isopen("sunday"))

# print(Employee.n)
# e1 = Employee("Anuj", 10000)
# print(e1.isopen("monday"))
# print(Employee.n)
# e2 = Employee("Vijay", 20000)
# print(e2.isopen("sunday"))
# print(Employee.n)

# e3 = Employee.from_str("Lovish-20000")
# print(e3.name)
# print(e3.salary)


# print(e1.salary)
# Employee.changeincreament(7)
# e1.increase()
# print(e1.salary)



# e1.name = "Anuj"
# e2.name = "Sanju"

# e1.salary = 10000
# e2.salary = 10000

# print(e1.__dict__)
# e1.var = 10
# print(e1.__dict__)

# print(Employee.__dict__)

# print(e1.salary)
# e1.increase()
# print(e1.salary)
# print(e1, e2)