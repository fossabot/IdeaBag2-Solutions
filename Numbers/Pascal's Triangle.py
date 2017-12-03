#!/usr/bin/env python3
"""
Title:
Pascal's Triangle

Description:
Create a program to print the Pascal's Triangle representation for a number N
where N is an integer specified by the user.
For more info on OasÄs Triangle,
look here: https://en.m.wikipedia.org/wiki/Pascal's_triangle
Submitted by Imperial_Squid
"""


def pascals_triangle(rows: int) -> tuple:
    """Return tuple containing pascals triangle up to specified length
    """
    result = []
    next_numbers = [1]
    for _ in range(0, rows):
        # move row
        current_numbers = next_numbers
        next_numbers = []
        result.append(tuple(current_numbers))
        for index, number in enumerate(current_numbers):
            # check whether it is the first or last number
            if index == 0:
                next_numbers.append(number)
            if index == len(current_numbers) - 1:
                next_numbers.append(number)
            else:
                next_numbers.append(number + current_numbers[index + 1])
    return tuple(result)


if __name__ == "__main__":
    while True:
        ROWS = int(input("Please input the number of rows"
                         " the program should print out: "))
        for row in pascals_triangle(ROWS):
            print(*row)
