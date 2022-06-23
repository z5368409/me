# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""

import math


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    guess = 0

    # Write your code in here

    my_dict = {"guess":guess, "tries":tries}

    while (low <= high):
        
        mid = low + (high - low)//2 # Huh //2 rounds the number
        #print(low, high, mid, actual_number)
        tries += 1

        if mid == actual_number:
            my_dict["guess"] = mid
            my_dict["tries"] = tries
            break
        elif mid < actual_number:
            low = mid + 1
        elif mid > actual_number:
            high = mid - 1


    return my_dict["guess"], my_dict["tries"]


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
