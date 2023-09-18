def Task1(numbers):
    for item in numbers:
        if item % 2 == 0:
            print(item)
        elif item == 237:
            print("found 237, stop")
            return


def Task2(number, edge):
    if number > edge:
        print('number > edge')
        if number >= edge * 3:
            print('number > edge in 3+ times')
    elif number < edge:
        print('edge > number')
    else:
        print('equal')


def main():
    Task1([0, 2, 6, 4, 10, 15, 27, 19, 28, 545, 313, 1523, 515, 421, 236, 237, 248])
    number = int(input('input number '))
    edge = int(input('input edge '))
    Task2(number, edge)


main()
