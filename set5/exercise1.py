# -*- coding: UTF-8 -*-

import requests

"""REFACTORING

Refactoring is the process of making your code better. You are usually looking 
to make it more readable or easier to maintain. Usually you'll do this by 
pulling out bits of code that encapsualte one idea, especially if that idea is 
used in several places.

We've talked already about 
    ↱red→green→refactor↴
    ↜←←←←←←←←←←←←←←←←←←↩

Where red means make sure the test fails if you haven't done anything, green 
means make the test pass, however you can, now this is the reafactor part.

The function below works fine, but it's long and hard to read. Identify the 
parts that are repeated, and pull them out into their own functions. I've made 
that easier for you by making the function stubs for the bits you need to do.

Modify this function, don't write a whole new one.
"""


def wordy_pyramid():
    
    pyramid_list = []
    for i in range(3, 21, 2):
        word = get_a_word_of_length_n(i)
        pyramid_list.append(word)
        

    for i in range(20, 3, -2):
        word = get_a_word_of_length_n(i)
        pyramid_list.append(word)

    return pyramid_list


def get_a_word_of_length_n(length):
    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/"
        "give_me_a_word?wordlength={length}"
    )
    url = baseURL.format(length=length)
    r = requests.get(url)
    if r.status_code == 200:
        message = r.text
    else:
        print("failed a request", r.status_code, length)

    return message

# hmm, idk how to use
def list_of_words_with_lengths(list_of_lengths):
    if len(list_of_lengths) == 1:
        return list_of_lengths[0]
        


    return


if __name__ == "__main__":
    pyramid = wordy_pyramid()
    for word in pyramid:
        print(word)
