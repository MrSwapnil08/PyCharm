#user defined exception is raised when balance is <2000

class MyException(Exception):
    def __init__(self, str):
        self.str = str

def check(bank):
    for k, v  in bank.items():
        print('Name= %s Balance=  %.2f' %(k, v))
        if v<2000:
            raise MyException("Balance amount is less")

bank =  {'Vinod': 4500, 'Ajay': 6700.75, 'Rani': 5000, 'Anil': 3400, 'Raj': 1200}
try:
    check(bank)
except MyException as me:
    print(me)