#!/usr/bin/python3

#import difflib
#from difflib import ndiff
#import itertools
from itertools import permutations
import re

# Anagrams are words split into the component letters, rearranged.  length>len(2) and length<=len(letters)
# to create other known words.  Example:  Tea: ate, eat, at.  Wrong: grow, now, nor, row, won, on, go, or.

# Take user input
word = input("Enter word: ")
#word = "draw"

def check_if_string_in_file(file_name, string_to_search):
	with open(file_name, 'r') as read_obj:
		for line in read_obj:
			if re.search('^' + string_to_search + '$', line, re.I):
				line = line.rstrip("\n")
				word_list.append(line)

scramble = []

# make all permutations from 2 characters to the size of the word
for i in range(2,len(word)+1):
	# concatenating the list items, since we don't want a list of lists
	scramble = scramble + [''.join(p) for p in permutations(word, i)]
	# sorting so we know if we have duplicates or not
	scramble.sort()
	# removing duplicates by converting from a list to a dictionary to a list again
	scramble = list(dict.fromkeys(scramble))

print(scramble)

# a new list for the actual words
word_list = []

def main():
	# within the scramble list
	for element in scramble:
		#print(element)
		# check to see if the element exists on a line
		if check_if_string_in_file('dict.txt', element):
			# add the matching word to the word_list
			word_list.append(element)
			print("found: " + element)
		else:
			print("", end="")

	print(word_list)

if __name__ == "__main__":
	main()
