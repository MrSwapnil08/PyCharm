# class and objects
class Person:
    #properties = vars
    def __init__(self, n, a):
        self.name = n
        self.age = a
    #actions = methods
    def talk(self):
        print('hello, i am', self.name)
        print('my age is', self.age)

#create an objects
p1 = Person('ram', 22)
p1.talk()
p2 = Person('sita', 22)
p2.talk()

'''class Student:
    def __init__(self):
        self.rno = 10
        self.name = 'Swapnil'
        self.add = 'Aurangabad'
        self.marks = [87,88,94]

    def display(self):
        print('Roll no: ', self.rno)
        print('Student name is', self.name)
        print('Address: ',self.add)
        tot = sum(self.marks)
        print('Total marks of all subjects', tot)
        percentage = tot/len(self.marks)
        print('Percentage :%2.f ' % percentage)

st=Student()
st.display()'''

'''class Student:
    def __init__(self, rno, name, add, marks):
        self.rno = rno
        self.name = name
        self.add = add
        self.marks = marks

    def display(self):
        print('Roll no: ', self.rno)
        print('Student name is', self.name)
        print('Address: ',self.add)
        tot = sum(self.marks)
        print('Total marks of all subjects', tot)
        percentage = tot/len(self.marks)
        print('Percentage :%2.f ' % percentage)

st = Student(8, 'Aditya', 'beed', [76, 76, 98])
st.display()'''

'''class Student:
    def __init__(self, rno, name, add, marks):
        self.rno = rno
        self.name = name
        self.add = add
        self.marks = marks

    def display(self):
        print('Roll no: ', self.rno)
        print('Student name is', self.name)
        print('Address: ',self.add)
        tot = sum(self.marks)
        print('Total marks of all subjects', tot)
        percentage = tot/len(self.marks)
        print('Percentage :%2.f ' % percentage)

rno = int(input('Enter rno: '))
name = input('Enter a name: ')
add = input('Enter address: ')
marks = int(input(''))

st = Student(rno, name, add, marks)
st.display()'''
