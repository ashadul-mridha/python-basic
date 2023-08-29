class Mammal:
    def __init__(self, name) -> None:
        print(name)

    def mammal_info(self):
        print("Mammals can give direct birth.")


class WingedAnimal:
    def __init__(self, roll) -> None:
        print(roll)

    def winged_animal_info(self):
        print("Winged animals can flap.")


class Bat(Mammal, WingedAnimal):
    def __init__(self, name, roll) -> None:
        Mammal.__init__(self, name)
        WingedAnimal.__init__(self, roll)


# create an object of Bat class
b1 = Bat('bat name', 34)

b1.mammal_info()
b1.winged_animal_info()
