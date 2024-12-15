# create emp class -emp.py
class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print('{:5d} {:15s} {:10.2f}'.format(self.id, self.name, self.sal))