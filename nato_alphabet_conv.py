#!/usr/bin/env python3

nato_alphabet = {"a":"alpha", "b":"bravo", "c":"charlie", "d":"delta", "e":"echo", "f":"foxtrot", "g":"golf", "h":"hotel", "i":"india", "j":"juliet", "k":"kilo", "l":"lima", "m":"mike", "n":"november", "o":"oscar", "p":"papa", "q":"quebec", "r":"romeo", "s":"sierra", "t":"tango", "u":"uniform", "v":"victor", "w":"whiskey", "x":"x-ray", "y":"yankee", "z":"zulu"}

def nato_translate_word(word):
	for letter in word:
		if letter.isalpha() == False:
			print(letter, end=" ")
		elif letter.isalpha() == True:
			print(nato_alphabet[letter], end=" ")

def nato_translate_sentence(sentence):
	sentence = sentence.split()
	for word in sentence:
		print(nato_alphabet[word[0]], end=" ")

user_input = input("word: ")

if " " in user_input:
	nato_translate_sentence(user_input)
	print()
else:
	nato_translate_word(user_input)
	print()
