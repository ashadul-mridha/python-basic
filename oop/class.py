class Parrot:
    name = ''
    color = ''


# create 1st parrot
parrot1 = Parrot()
parrot1.name = 'Lal Tia'
parrot1.color = 'red'

# create 2nd parrot
parrot2 = Parrot()
parrot2.name = 'sobuj tia'
parrot2.color = 'green'


print(f" 1st {parrot1.name} is and color is {parrot1.color}")
print(f" 1st {parrot2.name} is and color is {parrot2.color}")

# class with constructor


class Boy():
    def __init__(self, name):
        self.name = name


boy1 = Boy('fahim')
print(boy1.name)
