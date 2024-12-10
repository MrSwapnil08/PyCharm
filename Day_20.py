'''A accessor and mutator methods.
class Student:
    def __init__(self):
        self.rno = 10
        self.name = 'Shrinu'

    def getRno(self):
        return self.rno

    def getName(self):
        return self.name

st = Student()              #st is object reference variable
rno = st.getRno()
print(rno)

name = st.getName()
print(name)'''

#from random import sample

''' A accessor and mutator methods.
class Student:
    def __init__(self):
        self.rno = 10
        self.name = 'Shrinu'

    def getRno(self):
        return self.rno

    def getName(self):
        return self.name

    def setRno(self,rno):
        self.rno = rno
    def setName(self, name):
        self.name =name

st = Student()
st.setRno(88)
st.setName("Laxmi")

print('rno = ', st.setRno())
print('name = ',st.getName())'''


#Class variable and class method.

class Sample:
    x = 10   #this is class or static variable

    @classmethod
    def modify(cls):
        cls.x+=1

s1 = Sample()
s2 = Sample()

print(s1.x, s2.x)

Sample.modify()   #s1.modify()
print(s1.x, s2.x)

s1.x+=1
print(s1.x, s2.x)

