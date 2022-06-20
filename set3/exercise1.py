# -*- coding: UTF-8 -*-
"""Set 3.

Modify each function until the tests pass.
"""


from pickle import NONE


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Using a while loop make a list of numbers that goes from the start number up
    to, but not including, the stop number, in increments of step. E.g.:
        start: 3
        stop: 10
        step: 2
        will return: [3, 5, 7, 9]
    Look up for how range() works in the python docs. You could  answer this
    with just the range function, but we'd like you to do it the long way.
    """
    # range(start: starting value, stop: stop at value, step: increment)
    num_list = []
    counter = start

    while counter < stop:
        num_list.append(counter)
        counter = counter + step

    return num_list


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2

    You can either reuse loop_ranger, or the range function that in the standard library
    """

    #num_list = []

    #num_list.append(loop_ranger(start,stop,2))

    return loop_ranger(start,stop,2)


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for a function called "input"
    """
    num_input = int(input("Give me a number between " + str(low) + " and " + str(high) + ": "))

    while num_input > high or num_input < low:
        #print(str(num_input)+ " is not in range.")
        num_input = int(input("Give me another number between " + str(low) + " and " + str(high) + ": "))

    #if num_input <= high and num_input >= low:
        #print(str(num_input)+ " is in range")

    return num_input


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    # You can't use .isnumeric() unless its on str()

    inputter = input("Gimme number: ")

    while str(inputter).isnumeric() == False:
        inputter = input("Gimme number: ")

    return inputter


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """
    # Checks if its between low and high
    def low_high_checker(message, low, high):
        #print("low_high: " + str(message)) #print debugger
        if message >= low and message <= high:
            return True
        else:
            return False

    # Checks if its a number
    def number_checker(message, low, high):
        #print("num checker: " + str(message)) #print debugger
        if str(message).isnumeric() == True:
            if low_high_checker(int(message), low, high) == True:
                return True
            else:
                return False
        else:
            return False

    message = input("Give me a number between " + str(low) + " and " + str(high) + ": ")
    while number_checker(message, low, high) == False:
        message = input("Give me a number between " + str(low) + " and " + str(high) + ": ")
    
    return message


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
