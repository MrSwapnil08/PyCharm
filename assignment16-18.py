#Create a class by the name Circle. Display its area by accepting its radius.
# Write this class with default and parameterized constructors.

'''class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def display_area(self):
        area = 3.14 * self.radius ** 2     #Taken pie value as 3.14
        print("Area of the circle with radius " + str(self.radius) + " is: " + str(round(area, 2)))


circle1 = Circle()  # Default radius
circle1.display_area()

circle2 = Circle(8)  # Custom radius
circle2.display_area()'''


#Write a static method that accepts a number and returns its factorial value.

'''class Fact:
    @staticmethod
    def factorial(number):
        if number < 0:
            return "Factorial is not defined"
        result =1
        for i in range(1, number + 1):
            result *= i
        return result

print(Fact.factorial(9))
print(Fact.factorial(0))
print(Fact.factorial(-4))'''

#Implement the following Manager class with getter and setter methods.
#Class Manager: id, name, deptname, salary, gender (M or F)

class Manager:
    def __init__(self, id, name, deptname, salary, gender):
        self._id = id
        self._name = name
        self._deptname = deptname
        self._salary = salary
        self._gender = gender

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_deptname(self):
        return self._deptname

    def set_deptname(self, value):
        self._deptname = value

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        self._salary = value

    def get_gender(self):
        return self._gender

    def set_gender(self, value):
        if value in ('M', 'F'):
            self._gender = value
        else:
            raise ValueError("Gender must be 'M' or 'F'")


manager = Manager(101, "Saurav", "IT", 60000, "M")

print(manager._id)        # Output: 101
print(manager._name)      # Output: Alice
print(manager._deptname)  # Output: IT
print(manager._salary)    # Output: 75000
print(manager._gender)
