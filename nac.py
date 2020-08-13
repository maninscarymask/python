#!/usr/bin/env python3
# Jamie McLaughlin (C) 2020/08/12

from tkinter import *

# Dictionary of NATO letters
nato_alphabet = {"a":"alpha", "b":"bravo", "c":"charlie", "d":"delta", "e":"echo", "f":"foxtrot", "g":"golf", "h":"hotel", "i":"india", "j":"juliet", "k":"kilo", "l":"lima", "m":"mike", "n":"november", "o":"oscar", "p":"papa", "q":"quebec", "r":"romeo", "s":"sierra", "t":"tango", "u":"uniform", "v":"victor", "w":"whiskey", "x":"x-ray", "y":"yankee", "z":"zulu"}

# Translate a word or acronym
def nato_translate_word(word):
	output=[]
	for letter in word:
		if letter.isalpha() == False:
			output.append(letter)
			
		elif letter.isalpha() == True:
			output.append(nato_alphabet[letter])
	lbl02.configure(text=output, background='white')
	print(output)
	return output


# Translate a set of words or a phrase
def nato_translate_sentence(sentence):
	output=[]
	sentence = sentence.split()
	for word in sentence:
		output.append(nato_alphabet[word[0]])
	lbl02.configure(text=output, background='white')
	print(output)
	return output


def main():
	# If there's a space, it's a phrase, otherwise it's a word or acronym
	user_input = e01.get()
	if " " in user_input:
		nato_translate_sentence(user_input)
	else:
		nato_translate_word(user_input)

# background color (useful if .Xresources is something unusable in Tk)
bgc="#cccccc"

# Window
window=Tk()
window.configure(background = bgc)

# Labels
lbl01=Label(window, text="output", background = bgc, foreground='black')	# "output" label
lbl02=Label(window, text="", background = bgc, foreground='black')		# text from functions
lbl03=Label(window, text="input", background = bgc, foreground='black')		# "input" label

# Buttons
btn01=Button(window, text="Convert", background=bgc, foreground='black', command=main)		# convert button
btn02=Button(window, text="Quit", background=bgc, foreground='black', command=window.quit)	# quit button

# Text entry
e01 = Entry(window, background = 'white', foreground='black')			# text entry

# Placement
lbl01.grid(row=0, column=0)
lbl02.grid(row=0, column=1)

e01.grid(row=1, column=1)
lbl03.grid(row=1, column=0)

btn01.grid(row=2, column=0)
btn02.grid(row=2, column=1)

# Window configuration
window.title('NATO Alphabet Converter')
window.mainloop()

if __name__ == "__main__":
	main()
