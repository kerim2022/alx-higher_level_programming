#!/usr/bin/python3
for numbers in range(0, 10):
    for number in range(numbers + 1, 10):
        if numbers == 8 and number == 9:
            print("{}{}".format(numbers, number))
        else:
            print("{}{}".format(numbers, number), end=", ")
