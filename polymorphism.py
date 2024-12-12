#1.Operator overloading – same operator performs many tasks.
a = 10
b = 15
print(a+b)  #addition

a = 'auranga'
b = 'bad'
print(a+b)   #concatenation

#2. Method overloading, same method performs many tasks             
class Myclass:
    @staticmethod
    def add_all(*x):    #(*x) it is variable arguments it can take 0 to many values in tuple.
        res = sum(x)
        print('total =', res )

Myclass.add_all(10, 11)
Myclass.add_all(11,33,34)

#3.Method overriding i.e. writing same method in the sub class.
class Super:
    def display(self):
        print('Super class method')
class Sub(Super):
    def display(self):          #taken same method display
        print('sub class method')

s = Sub()
s.display()

#4. Duck typing = executing a method without knowing its type(classname)
class Duck:
    def talk(self):
        print('Quack, Quack!')

class Dog:
    def talk(self):
        print('Bhow wow!')

def call_talk(obj):            #creating a function
    obj.talk()           #duck typing
d = Duck()
call_talk(d)
d= Dog()
call_talk(d)