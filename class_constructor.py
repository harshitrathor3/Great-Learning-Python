class Employee():
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def emp_detail(self):
        print("Name of Employee is",self.name)
        print("Age of Employee is",self.age)
        print("Salary of Employee is",self.salary)
        print("Gender of Employee is",self.gender)
