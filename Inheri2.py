class Father:
    def height(self):
        print('Height is 6ft')
class Mother:
    def color(self):
        print('Complexion is tan')

class Child(Father, Mother):
    pass

ch= Child()
print('Child Qualities: ')
ch.height()
ch.color()