"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    # This function checks if boundaries are valid
    def BoundaryValidity(upper, lower):
      Bool = False
      if str(upper).isnumeric() == True and str(lower).isnumeric() == True:
        if int(upper) >= int(lower):
          Bool = True
        else:
          print("Your Upper boundary is smaller than Lower boundary!")
      else:
        print("Your boundaries are NOT values!")
      return Bool

    # This function checks if your guess are valid
    def GuessValidity(Actual, Guess, Upper, Lower):
      Bool = False
      if str(Guess).isnumeric() == True:
        intGuess = int(Guess)
        intActual = int(Actual)

        if intGuess >= int(Lower) and intGuess <= int(Upper):
          if intGuess == intActual:
            Bool = True
          elif intGuess < intActual:
            print("Higher")
          elif intGuess > intActual:
           print("Lower")
        else:
          print("Your guess is outside the boundaries!")
      else:
        print("You didn't give me a number!")
      return Bool

    print("\nWelcome to this game!")
    print("You must guess numbers between upper and lower boundary.")

    Upper_value = input("Gimme upper boundary: ")
    Lower_value = input("Gimme lower boundary: ")
    #print(str(Upper_value)+ " " + str(Lower_value))

    while BoundaryValidity(Upper_value, Lower_value) == False:
      Upper_value = input("Gimme upper boundary: ")
      Lower_value = input("Gimme lower boundary: ")
      #print(str(Upper_value)+ " " + str(Lower_value))

    # Number Randomiser
    if int(Lower_value) == int(Upper_value):
      Actual_Num = int(Lower_value)
    else:
      Actual_Num = random.randint(int(Lower_value), int(Upper_value))
    
    # Guessing Game
    Guess_num = input("Guess the number: ")

    while GuessValidity(Actual_Num, Guess_num, Upper_value, Lower_value) == False:
      Guess_num = input("Guess the number: ")

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
