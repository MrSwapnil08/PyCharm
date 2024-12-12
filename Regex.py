#Regular Expression
'''str = 'hello \n world'
print(str)'''
from os import lstat

#A regular expression to search for a string starting with
# m and having total 3 characters.
def program1():
    str = 'man sun mop run cat rat mat get'
    import re
    lst = re.findall(r'm\w\w',str)     #r is raw string
    print(lst)
#it will search the total string but will show first matching string.
program1()


def program2():
    str = 'sun kmp run cat rat mat get'
    import re
    obj = re.search(r'm\w\w', str)
    if obj:
        print(obj.group())
    else:
        print('No matching string')

program2()

#write a regex to retrieve id numbers
def program3():
    str = 'gopi 222 vinay 444 subba 433 rao 332 sri devi 3322'
    import re
    obj = re.findall(r'\D+', str)
    print(obj)
program3()

#write a regex to retrieve all words starting with 'an' or 'ak'
def program4():
    str = 'anil akhil anant arun arati arundhati abhijit ankur amar akruti'
    import re
    lst = re.findall(r'a[nk]\w*',str)
    print(lst)

program4()

#write a regex ton retrieve only birth dates
def program5():
    str = 'Vijat 20 1-5-2000, Rohit 21 22-12-1990, Sita 22 15-09-2000'
    import re
    lst = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
    print(lst)

program5()

#find all id number
def program6():
    str = 'Vijat 20 1-5-2000, Rohit 21 22-12-1990, Sita 22 15-09-2000'
    import re
    lst = re.findall(r'\s\d+\s',str)
    print(lst)

program6()

#a regex to split the string where id nos are found
def program7():
    data = 'Vijay 20  Rohit 21 Sita 22 ganesh 232'
    import re
    lst = re.split(r'\d+',data)
    print(lst)

program7()


#a regex to replace ahemdabad to hyderabad
def program8():
    data = 'kumbhmela is conducted in ahemdabad and ahemdabad is a holy place'
    import re
    lst = re.sub(r'ahemdabad', r'hyderabad',data)
    print(lst)

program8()

#write a regex to search in the beginning
def program9():
    str = 'Hello World'
    import re
    obj = re.search(r'^He', str)
    if obj:
        print('Found in the beginning')
    else:
        print('not found')
program9()

#write a regex to search in the ending

def program10():
    str = 'Hello World'
    import re
    obj = re.search(r'ld$', str)
    if obj:
        print('Found in the ending')
    else:
        print('not found')
program10()
