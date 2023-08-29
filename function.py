# function in python
def greet(name):
    print('Hello ', name)


# greet('Ashadul')

# function with abritary


def numbers(*numbers):
    for number in numbers:
        print(number)


# numbers(1, 2, 3, 4, 5, 6)

# annomius function or lamda
# syntax  = lambda arguments() : expression


def greet_user(name): return 'Hello',


greet_user('Zerin')
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)

# Output: [4, 6, 8, 12]

# nonlocal variable
name = 'global'


def outer():
    global name
    name = 'nonglobal'

    def inner():
        global name
        # name = 'inner name'
        print('inner', name)
    inner()
    print('outer', name)


outer()
