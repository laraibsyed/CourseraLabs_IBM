class Car:
    colour = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None
    
    def assign_seating(self, seating_capacity):
        self.seating_capacity = seating_capacity
    
    def display(self):
        print("Properties")
        print("Colour: ", self.colour)
        print("Max Speed: ", self.max_speed)
        print("Mileage: ", self.mileage)
        print("Seating Capacity: ", self.seating_capacity)

Car1 = Car(200, 20)
Car1.assign_seating(5)
Car1.display()

print("-------------------------")

Car2 = Car(180, 25)
Car2.assign_seating(4)
Car2.display()