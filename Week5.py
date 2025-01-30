#ASSIGNMENT 1
# Parent class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand            # Public attribute
        self.model = model            # Public attribute
        self.__price = price          # Private attribute (Encapsulation)

    def get_info(self):
        """Returns smartphone details"""
        return f"{self.brand} {self.model} costs ${self.__price}"

    def set_price(self, new_price):
        """Allows updating the price"""
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")

# Child class inheriting from Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, price, refresh_rate):
        super().__init__(brand, model, price)  # Call parent constructor
        self.refresh_rate = refresh_rate       # Additional attribute

    def gaming_mode(self):
        return f"Gaming mode enabled! {self.refresh_rate}Hz refresh rate for smooth performance."

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S23", 999)
gaming_phone = GamingPhone("Asus", "ROG Phone 7", 1299, 144)

# Using methods
print(phone1.get_info())                     # Output: Samsung Galaxy S23 costs $999
phone1.set_price(899)                         # Update price
print(phone1.get_info())                      # Output: Samsung Galaxy S23 costs $899

print(gaming_phone.get_info())                # Output: Asus ROG Phone 7 costs $1299
print(gaming_phone.gaming_mode())             # Output: Gaming mode enabled! 144Hz refresh rate


#ASSIGNMENT 2


# Parent class
class Vehicle:
    def move(self):
        pass  # Defined in child classes

# Child classes with different implementations
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())  # Each object calls its own version of move()
