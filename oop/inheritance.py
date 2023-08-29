# example of python inheritance
class Animal:
    def eat(selt):
        print('i can eat')

    def sleep(selt):
        print('i can sleep')


class Dog(Animal):
    def age(self):
        print(6)

    # its method overridding
    def eat(self):
        print("Overridding")


dog = Dog()
dog.eat()
dog.sleep()


