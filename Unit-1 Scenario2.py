class Vehicle:
    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price

    def category(self):
        if self.price >= 1000000:
            return "Luxury"
        return "Economy"

    def display(self):
        print("\nVehicle Number :", self.number)
        print("Brand :", self.brand)
        print("Price :", self.price)
        print("Category :", self.category())


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self):
        number = input("Enter Vehicle Number: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: "))
        self.vehicles.append(Vehicle(number, brand, price))
        print("Vehicle Added Successfully!")

    def display_vehicles(self):
        if len(self.vehicles) == 0:
            print("No vehicles available.")
        else:
            i = 0
            while i < len(self.vehicles):
                self.vehicles[i].display()
                i += 1


showroom = Showroom()

while True:
    print("\n1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        showroom.add_vehicle()
    elif choice == 2:
        showroom.display_vehicles()
    elif choice == 3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
