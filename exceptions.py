#exception example
'''def program11():
    try:
        print('Open files')
        a = int (input('Enter a num1: '))
        b = int (input('Enter a num2: '))
        c = a/b
        print('Result of division: ', c)
    except ZeroDivisionError:  #except block is executed when there is error.
        print('Division by zero happened.')
        print('Please do not enter zero in inputs ')
    finally:
        print('close files')      #if we do not close the file all data in file is gone.
program11()
'''

'''def program12():
    try:
        print('Open files')
        a = int (input('Enter a num1: '))
        b = int (input('Enter a num2: '))
        c = a/b
        print('Result of division: ', c)
    except ZeroDivisionError:  #except block is executed when there is error.
        print('Division by zero happened.')
        print('Please do not enter zero in inputs ')
    except ValueError:
        print('Enter integer number in inputs')
    finally:
        print('close files')      #if we do not close the file all data in file is gone.
program12()'''

'''def program13():
    try:
        print('Open files')
        a = int (input('Enter a num1: '))
        b = int (input('Enter a num2: '))
        c = a/b
        print('Result of division: ', c)
    except Exception as obj:
        print(obj)
    finally:
        print('close files')      #if we do not close the file all data in file is gone.
program13()'''

def program14():
    try:
        print('Open files')
        a = int (input('Enter a num1: '))
        b = int (input('Enter a num2: '))
        c = a/b

    except ZeroDivisionError:  #except block is executed when there is error.
        print('Division by zero happened.')
        print('Please do not enter zero in inputs ')
    except ValueError as ve:
        print(ve)

    else:                       #When there is no exception else part will be executed
        print('Result of division: ', c)
    finally:
        print('close files')
program14()