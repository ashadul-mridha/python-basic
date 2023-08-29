numbers = [1, 2, 3, 4, 5]
mine = 2
for number in numbers:
    if number == 3:
        if mine == 2:
            continue
        else:
            break

    print(number)
else:
    print('The loop is over')
