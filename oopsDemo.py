"""
Python OOP Basics: Classes, Objects, Constructors, and Variables
---------------------------------------------------------------
Key Takeaways:
1. Classes are user-defined blueprints or prototypes for creating objects.
2. A class contains methods, class variables, instance variables, and constructors.
3. The `self` keyword is mandatory as the first parameter of instance methods
   to access instance variables and other methods within the same class.
4. Class variables are shared across all instances, whereas instance variables
   are unique to each object created from the class.
5. Unlike Java, Python does NOT require the `new` keyword when creating an object.
"""


class Calculator:
    # Class variable: shared across all instances of Calculator
    num = 100

    # Parameterized constructor: called automatically when an object is instantiated
    def __init__(self, a, b):
        # Instance variables: unique to each object instance
        self.a = a
        self.b = b
        print("Constructor called automatically when object is created")

    def get_data(self):
        print("Executing method inside Calculator class")

    def summation(self):
        # Access instance variables via `self` and class variable via `Calculator.num`
        return self.a + self.b + Calculator.num


# --- Object Instantiation & Method Calls ---

# Create first object (no `new` keyword needed in Python)
obj = Calculator(2, 3)
obj.get_data()
print(f"Summation for obj (2 + 3 + 100): {obj.summation()}")  # Output: 105

# Create second object with different instance values
obj1 = Calculator(4, 5)
obj1.get_data()
print(f"Summation for obj1 (4 + 5 + 100): {obj1.summation()}")  # Output: 109