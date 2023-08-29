#  numeric data type 
num = 5;
print(num, 'data type is', type(num)) # int
num = 5.5;
print(num, 'data type is', type(num)) # float
num = 5 + 6j;
print(num, 'data type is', type(num)) # complex

#  sequence data type
name = 'Ashadul';
print(name, 'data type is', type(name)) # string
name = [1, 2, 3, 4, 5];
print(name, 'data type is', type(name)) # list
name = (1, 2, 3, 4, 5);
print(name, 'data type is', type(name)) # tuple

#  mapping data type
name = {'name': 'Ashadul', 'roll': 1};
print(name['name'], 'data type is', type(name)) # dictionary
