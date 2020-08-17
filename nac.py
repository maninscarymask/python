#!/usr/bin/env python3
# Jamie McLaughlin (C) 2020/08/17

from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Tk

# Dictionary of NATO letters
nato_alphabet = {
    "a": "alpha",
    "b": "bravo",
    "c": "charlie",
    "d": "delta",
    "e": "echo",
    "f": "foxtrot",
    "g": "golf",
    "h": "hotel",
    "i": "india",
    "j": "juliet",
    "k": "kilo",
    "l": "lima",
    "m": "mike",
    "n": "november",
    "o": "oscar",
    "p": "papa",
    "q": "quebec",
    "r": "romeo",
    "s": "sierra",
    "t": "tango",
    "u": "uniform",
    "v": "victor",
    "w": "whiskey",
    "x": "x-ray",
    "y": "yankee",
    "z": "zulu"
}


# Translate a word or acronym
def nato_translate_word(word):
    output = []
    for letter in word:
        if letter.isalpha() == False:
            output.append(letter)

        elif letter.isalpha() == True:
            output.append(nato_alphabet[letter])
    label_display.configure(text=output, background='white')
    #print(output)
    #return output


# Translate a set of words or a phrase
def nato_translate_sentence(sentence):
    output = []
    sentence = sentence.split()
    for word in sentence:
        output.append(nato_alphabet[word[0]])
    label_display.configure(text=output, background='white')
    #print(output)
    #return output


def main():
    # If there's a space, it's a phrase, otherwise it's a word or acronym
    user_input = text_entry.get()
    if " " in user_input:
        nato_translate_sentence(user_input)

    else:
        nato_translate_word(user_input)


# background color (useful if .Xresources is something unusable in Tk)
background_color = "#cccccc"

# Window
window = Tk()
window.configure(background=background_color)

# Labels
label_output = Label(window,
                     text="output",
                     background=background_color,
                     foreground='black')  # "output" label
label_display = Label(window,
                      text="",
                      background=background_color,
                      foreground='black')  # text from functions
label_input = Label(window,
                    text="input",
                    background=background_color,
                    foreground='black')  # "input" label

# Buttons
button_convert = Button(window,
                        text="Convert",
                        background=background_color,
                        foreground='black',
                        command=main)  # convert button
button_quit = Button(window,
                     text="Quit",
                     background=background_color,
                     foreground='black',
                     command=window.quit)  # quit button

# Text entry
text_entry = Entry(window, background='white',
                   foreground='black')  # text entry

# Placement
label_output.grid(row=0, column=0)
label_display.grid(row=0, column=1)

text_entry.grid(row=1, column=1)
label_input.grid(row=1, column=0)

button_convert.grid(row=2, column=0)
button_quit.grid(row=2, column=1)

# Window configuration
window.title('NATO Alphabet Converter')
window.mainloop()

if __name__ == "__main__":
    main()
