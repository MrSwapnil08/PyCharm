#Create Child class from Father and Mother classes.
# Define property in the Father class as Rs. 500000 and in Mother class as Rs. 400000.
# Now, write a method display() in the Child class that displays child property as sum of the properties of its parents.

class Father:
    def __init__(self):
        self.property1 = 500000
class Mother:
    def __init__(self):
        self.property2 = 400000

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def display(self):
        total_property =  self.property1 + self.property2
        print('child property :Rs.  ', total_property)
child = Child()
child.display()