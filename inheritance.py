class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_vehicle_details(self):
        print("Mileage of Vehicle is",self.mileage)
        print("Cost of vehicle is",self.cost)
        print("I am a vehicle")
class Car(Vehicle):
    def show_car_details(self):
        print("I am a Car")
class Car1(Vehicle):
    def __init__(self,mileage,cost,tyre,hp):
        super().__init__(mileage,cost)
        self.tyre=tyre
        self.hp=hp
    def show_car_details(self):
        print("No of tyres",self.tyre)
        print("Horse Power",self.hp)
        print("I am a Car")
