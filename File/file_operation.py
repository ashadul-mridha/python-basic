# print('File Operation')

# Hence, in Python, a file operation takes place in the following order:

# Open a file
# Read or write (perform operation)
# Close the file

# open file and  read and close
try:
    # open a file in reading mode
    file1 = open('../main.txt')

    # file read
    content = file1.read()
    print(content)

except:
    print("Something went wrong")

finally:
    # close file
    file1.close()

# use with open syntax
with open('test.txt', 'r') as file2:
    read_file2 = file2.read()
    print(read_file2)


# write a file
with open('test2.txt', '+w') as text2:
    text2.write('write file test2')

# open text2 file
with open('test2.txt') as test2open:
    read2 = test2open.read()
    print(read2)
