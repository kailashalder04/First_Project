# Step 1: Define the Employee class with class variable
class Employee:
    new_id = 1   # class variable

    # Step 2: __init__ method to assign unique id
    def __init__(self):
        self.id = Employee.new_id
        Employee.new_id += 1   # increment class variable for next employee

    # Step 3: Method to output the instance id
    def say_id(self):
        print("My id is", self.id)

class Admin(Employee):
    def say_id(self):
        super().say_id()
        print("i am an Admin")

class Manager(Employee):
    def say_id(self):
        super().say_id()
        print("i am a Manager")

# Step 4: Create 2 employees and display their ids
e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()
e1.say_id()   # Output: My id is 1
e2.say_id()   # Output: My id is 2
e3.say_id()   # Output: My id is 3
e4.say_id()   # Output: My id is 4 # Output: my id is 3
