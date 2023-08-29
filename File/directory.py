# working with directory
import os

print(os.listdir())

os.rename('python.txt', 'new_one.txt')

print(os.listdir())

os.remove("new_one.txt")
