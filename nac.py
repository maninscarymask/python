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
	lbl.configure(text=output)
	return output


# Translate a set of words or a phrase
def nato_translate_sentence(sentence):
	output=[]
	sentence = sentence.split()
	for word in sentence:
		output.append(nato_alphabet[word[0]])
	lbl.configure(text=output)
	return output

#user_input = input("word: ")

def main():
	# If there's a space, it's a phrase, otherwise it's a word or acronym
	user_input = e01.get()
	if " " in user_input:
		output = nato_translate_sentence(user_input)
		#print(output)
	else:
		output = nato_translate_word(user_input)
		#print(output)

bgc="#cccccc"

# Window
window=Tk()
window.configure(background = bgc)

# Labels
lbl=Label(window, text="Word or Sentence")
lbl.configure(background = 'white', foreground='black')

# Buttons
btn01=Button(window, text="Convert", background=bgc, foreground='black', command=main)
btn02=Button(window, text="Quit", background=bgc, foreground='black', command=window.quit)

# Text entry
e01 = Entry(window)
e01.configure(background = 'white', foreground='black')
#e01.bind("<Return>", main)
#e01.pack()

# Placement
btn01.place(x=60, y=100)
btn02.place(x=120, y=100)
e01.place(x=50, y=50)
lbl.place(x=50, y=150)

# Window configuration
window.title('NATO Alphabet Converter')
window.geometry("300x200+10+10")
window.mainloop()

if __name__ == "__main__":
	main()

