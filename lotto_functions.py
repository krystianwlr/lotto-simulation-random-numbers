#!/usr/bin/env python3

"""
Module which consists of functions for basic number operations.
1. Drawing a set  of random numbers.
2. Putting numbers to a coupon.
"""

import random
import pygal

def draw_numbers_imp():
    line = set(random.sample(range(1,50),6))
    return line

def user_numbers():
    """
    Function which lets a user pick a valid set of 6 numbers
    :return: a set of 6 integers
    """
    coupon = set()
    while len(coupon) < 6:
        try:
            to_add = int(input("Please pick a number between 1-49: "))
            if to_add < 1 or to_add > 49 or to_add in coupon:
                raise ValueError
        except ValueError:
            print("Not a valid number")
        else:
            coupon.add(to_add)
            print("Number added!")
            print(coupon)
    return coupon


def classify_results(have, drawn):
    prizes = {0: 0, 1: 0, 2: 0, 3: 24, 4: 258, 5: 9500, 6: 2000000}
    hit = len(have.intersection(drawn))
    prize = prizes[hit]
    return hit, prize


def main():
    n = 4500
    have = user_numbers()
    money_lost = n * 3
    money_won = 0
    histogram = {}

    # simmulation
    print("Starting simulation:\n")
    for i in range(n):
        if i % 500 == 0:
            print(i)
        drawn = draw_numbers_imp()

        # cummulative functions
        x = classify_results(have, drawn)
        histogram[x[0]] = histogram.get(x[0], 0) + 1
        money_won += x[1]

    # print the results\n
    print("\nSimulation complete for {:d} number of draws".format(n))
    print("*" * 40)
    print("\nMoney spent on lottery: {:d} PLN".format(money_lost))
    print("Money won in the loterry: {:d} PLN".format(money_won))
    print("*" * 40)
    for key, value in histogram.items():
        if key >= 3:
            print("You've correctly picked {:d} numbers {:d} times".format(key, value))

    # create a bar chart
    print("\nWould you like to create a chart? Type 'y' to confirm")
    choice = str(input("\nType 'y' to confirm "))
    if choice == "y":
        line_chart = pygal.Bar()
        line_chart.title = "Results of " + str(n) + " lotto draws"
        line_chart.x_labels = ['1', '2', '3', '4', '5', '6']
        line_chart.x_title = "Numbers matching the draw"
        line_chart.y_title = "Frequency of result"

        line_chart.add('', histogram.values())
        line_chart.render_to_png('chart.png')
    else:
        pass

if __name__ == main():
    main()
