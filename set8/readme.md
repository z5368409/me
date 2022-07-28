TODO: Reflect on what you learned this week and what is still unclear.

"With" function holds any action inside it ready for use, accompanied at the end with an "As" function
which renames the "With" for easier usage.
e.g: 
with open(file_path, mode, encoding) as history_book
history_book.write("yay")

F-string allows the string to replace any attribute inside {} whenever the function called.
e.g:
def FUNCTION(name)
    with open(file_path, mode, encoding) as book
    book.write(f"{name} is great")

File path functions include
- .open() Opens file
- .read() Reads entire file as 1 single string
- .readline() Each line read are separately done. Use While or For to iterate.
- .readlines() Same as readline but idk

Exceptions uses try and except:
for _ in range(10):
    try:
        print(4/random.randrange(0 , 4))
    except Exception as z:
        print(z) #This will print error type.
    finally: # Fires every time after try and except. Not necessary.
        print("Finished")