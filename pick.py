#pickling or serialization

import pickle, emp, unpick
f = open('F:/Avd/Python/Pythonproject/emp.dat','ab')

n = int(input('How many employees: '))
for i in range(n):
    id = int(input('Enter id: '))
    name = input('Enter a name: ')
    sal = float(input('Enter a salary: '))
    e = emp.Emp(id, name, sal)
    pickle.dump(e, f)

f.close()
unpick.unpick()