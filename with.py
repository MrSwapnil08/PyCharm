#to read data with stmt
'''with open('F:/Avd/Python/programs/myfile.txt', 'r')
    data = f.read()
    print(data)'''

#Random accessing of a binary file.
'''with open('test.bin', 'w+b') as f:
    n = f.tell()
    print(n)                    #inittially file handler will be at zeroth position

    f.write(b'Core Python')         #b will make it binary file
    print(f.tell())'''

#i want to move the file handler to beginning of the file
with open('test.bin', 'w+b') as f:
    n = f.tell()
    print(n)                    #inittially file handler will be at zeroth position

    f.write(b'Core Python')         #b will make it binary file
    print(f.tell())
    f.seek(0, 0)
    data = f.read(4)
    print(data.decode())    #to convert binary data into string
#reading string at end 'Python'.
    f.seek(-6, 2)
    data = f.read(6)
    print(data.decode())