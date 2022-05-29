class Parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        return self.name
class Child(Parent):
    def get_age(self,age):
        self.age=age
    def show_age(self):
        return self.age
class GrandChild(Child):
    def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender
