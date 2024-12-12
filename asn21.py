
#Write a method in the super class to calculate square value.
# Override this method in the sub class to calculate cube value.

class SuperClass:
    def calculate(self, value):
        return value ** 2

class SubClass(SuperClass):
    def calculate(self, value):
        return value ** 3

# Example usage
super_obj = SuperClass()
sub_obj = SubClass()

print("Square value:", super_obj.calculate(3))
print("Cube value:", sub_obj.calculate(3))
