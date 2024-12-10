# Write a python program to count the number of object created for a class.
'''class Myclass:
    x = 0  #static var
    def __init__(self):
        Myclass.x+=1
    @staticmethod
    def display():
        print( " number of objects created: ", Myclass.x)

m1 = Myclass()
m2 = Myclass()
m3 = Myclass()

Myclass.display()   #m1.display()'''

#create a static method to calculate square root value.

class Sample:
    @staticmethod
    def sroot(x):
        res = x ** 0.5
        return res

result = Sample.sroot(16)
print(result)

import math
result = math.sqrt(16)
print(result)






