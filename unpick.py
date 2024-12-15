#Unpickling
def unpick():
    import pickle
    f = open('F:/Avd/Python/Pythonproject/emp.dat', 'rb')

    while True:  #while 1:
        try:
            e = pickle.load(f)
            e.display()
        except EOFError:
            print('End of file reached ...')
            break
    f.close()
