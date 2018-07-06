import json
from tkinter import *
from difflib import get_close_matches

window = Tk()
window.title("Auto Correcting Dictionary")

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
        global similar_word
        similar_word = get_close_matches(w, data.keys())[0]
        x = str("Did you mean %s instead?, click (Yes) if yes, (No) if not: " % similar_word)
        return x
    else:
        return "The word doesn't exist. Please double check it."

def search_word():
    word = enter_word.get()
    check_if_list_or_not(translate(word))

def search_similar_word():
    check_if_list_or_not(translate(similar_word))
    enter_word.set(similar_word)  # change the word in Entry

def check_if_list_or_not(list_of_output):
    if type(list_of_output) == list:
        definition.delete(1.0, END)
        for value in list_of_output:
            definition.insert(END, value + '\n')
    else:
        definition.delete(1.0, END)
        definition.insert(END, list_of_output)

def cannot_find():
    definition.delete(1.0, END)
    definition.insert(END, "The word doesn't exist. Please double check it.")

def reset():
    e.delete(0, 'end')

# enter form
enter_word = StringVar()
entry = Entry(window, textvariable=enter_word)
entry.grid(row=0, column=0)

# search button
b_search = Button(window, text="Search", command=search_word)
b_search.grid(row=0, column=1)

# yes button
b_yes = Button(window, text="Yes", command=search_similar_word)
b_yes.grid(row=1, column=1)
b_yes.configure(bg="red")

# no button
b_no = Button(window, text="No", command=cannot_find)
b_no.grid(row=1, column=2)

# reset button
b_reset = Button(window, text="Reset", command=reset)
b_reset.grid(row=0, column=2)

# output form
definition = Text(window, height=8, width=50)
definition.grid(row=3, column=0)
definition_lable = Label(window, text="definition")
definition_lable.grid(row=2, column=0)


window.mainloop()