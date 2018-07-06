import json
from tkinter import *
from difflib import get_close_matches

window = Tk()
window.title("Dictionary")

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:  # The title() convert the first letter to uppercase
        return data[w.title()]
    elif w.upper() in data:  # in case users enter word like USA
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        similar_word = get_close_matches(w, data.keys())[0]
        answer = input("Did you mean %s instead?, Type (Y/y) if yes, (N/n) if not: " % similar_word)
        answer_lower = answer.lower()
        if answer_lower == "y":
            return data[similar_word]
        elif answer_lower == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We did not understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

w = input("Enter word: ")
list_of_output = translate(w)

if type(list_of_output) == list:
    for value in list_of_output:
        print(value)
else:
    print(list_of_output)


