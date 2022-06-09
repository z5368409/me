"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# All values within the [] are definded within the list "some_words"
some_words = ["what", "does", "this", "line", "do", "?"]

# I think this will print every values within the list "some_words"
for word in some_words:
    print(word) # It printed each individual word in the terminal seperately

# I think this will mimic the previous iteration above
for x in some_words:
    print(x) # It printed each individual word in the terminal seperately
    # this proves that "word" and "x" can be replaced with other variables

# I think this will print the whole list as 1 line
print(some_words) # It printed the whole list, including the commas and []

# I think this is a condition that activates if string length > 3
if len(some_words) > 3:
    print("some_words contains more than 3 words") # This statement was printed

# This defined and named the function "usefulFunction"
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # This will print the system and software versions and machine name
    print(platform.uname())

# This will run the function "usefulFunction"
usefulFunction() # Print runs
