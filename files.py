'''#create a textffiles
r = open('d:/py/Myfile.txt','a+',4096)
#r is file handling object
chars = input('Enter data ')
r.write(chars)
r.close()

import os,sys
files = input('Enter filename:')
if os.path.isfile(files):
    f = open(files,'r')
    print('Files is exists')
else:
    print('Files is not exists')
    sys.exit()


#to read data from text file
try:
    files = input('Enter files name ')
    r = open(files,'r')
    d = r.read()
    print(d)
    r.close()
except FileNotFoundError:
    print('You have entered the wrong filename')'''

# to read data from text file
try:
    files = input('Enter files name ')
    r = open(files, 'r')
    d = r.read()
    print(d)
    r.close()
except FileNotFoundError:
    print('You have entered the wrong filename')