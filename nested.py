#inner class/ nested class
'''class Student:
    def __init__(self):
        self.rno = 100
        self.name = 'vijay'
    def display(self):
        print('rno: ', self.rno)
        print('Name: ',self.name)

    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 12
            self.yy = 2001

        def display(self):
            print('Dob= %d-%d-%d' %(self.dd, self.mm, self.yy))

#crate an object
st = Student()
st.display()    #calling display method from above

d = st.Dob()        #shows only date of birth
d.display()

d = Student().Dob()    #2nd method to show inner class
d.display()'''

#abstraction of a loan amount in a bank account
class Bank:
    def __init__(self):
        self.accno = 10
        self.name = 'vijay'
        self.addr = 'Aurangabad'
        self.phone = 7029980917
        self.bal  = 6000.75
        self.__loan = 1500000.00    #__ before variable means it is private not visible to all

    def display_to_clerk(self):             #only add that data which a user should view
        print('account no: ',self.accno)
        print('Name: ', self.name)
        print('Address: ',self.addr)
        print('Phone; ', self.phone)
        print('Balance amount: Rs.%.2f'% self.bal)

b = Bank()
b.display_to_clerk()
print(b._Bank__loan)        #name mangling



