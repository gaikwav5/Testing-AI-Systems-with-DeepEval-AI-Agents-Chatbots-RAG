"""
Python OOP: Inheritance and Calling Parent Constructors
-------------------------------------------------------
Key Takeaways:
1. Inheritance allows a child class (`ChildImpl`) to inherit all attributes,
   class variables, and methods from a parent class (`Calculator`).
2. Syntax: Pass the parent class in parentheses -> `class ChildImpl(Calculator):`
3. Calling Parent Constructor: If the parent class defines a parameterized
   `__init__`, the child class must explicitly invoke it so parent instance
   variables (`self.a`, `self.b`) are initialized.
   - Modern Pythonic way: `super().__init__(2, 10)` (no `self` needed).
   - Explicit parent way: `Calculator.__init__(self, 2, 10)` (requires `self`).
4. Inside the child class, `self` can access both child attributes (`self.num2`)
   and inherited parent attributes/methods (`self.num`, `self.summation()`).
"""

from OopsDemo import Calculator


class ChildImpl(Calculator):
    # Child class variable
    num2 = 200

    def __init__(self):
        # Invoke parent constructor so `self.a` and `self.b` are initialized
        super().__init__(2, 10)
        # Alternative explicit call: Calculator.__init__(self, 2, 10)

    def get_complete_data(self):
        # Combines child variable (200) + inherited class variable (100)
        # + inherited summation method (2 + 10 + 100 = 112) -> Total: 412
        return self.num2 + self.num + self.summation()


# --- Object Instantiation & Execution ---
obj = ChildImpl()
print(f"Complete Data Output: {obj.get_complete_data()}")  # Output: 412