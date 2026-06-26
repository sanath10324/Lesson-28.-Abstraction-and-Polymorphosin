class BMW():
    def max_speed(self):
        print("280")
    
    def fuel_type(self):
        print("Petrol")
    
class Ferrari():
    def max_speed(self):
        print("260")
    
    def fuel_type(self):
        print("Petrol")

obj_bmw = BMW()
obj_ferrari = Ferrari()

for Car in (obj_bmw, obj_ferrari):
    Car.max_speed()
    Car.fuel_type()
