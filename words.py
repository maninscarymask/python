#!/usr/bin/env python3

user_input = input("word: ")

letter_count = len(user_input)

dictionary = {}

# Split and sort words to letter, counting each letter each time it occurs
def deconstruct(word):
	hold = {}
	for letter in word:
		if letter in hold:
			# If letter key exists, increment
			hold[letter] += 1
		else:
			# If letter key !exists, add it
			hold[letter] = 1

	# Take the items, make them sortable, then sort them
	hold_items = hold.items()
	hold = sorted(hold_items)
	dictionary = hold
	return hold

def check_file(word):
	# Open file
	dict_file = open("dict.txt", "r")
	print("opened dict.txt")

	word_list = []

	for line in dict_file:
		# Remove newlines, make everything lowercase
		line = line.rstrip().lower()

		# Get item's len()
		line_length = len(line)

		# If the counts from each item and the user_input match, add word to list
		if letter_count == line_length:
			# Make sorted split of word
			test = deconstruct(line)

			if test == dictionary:
				# Add to the list
				word_list.append(test)
				print(test)
	

	# complete list of length-matched words
	#print(word_list)
	
	# Close file
	dict_file.close()
	print("closed dict.txt")


def main():
	# Split the user_input to a dictionary
	ui = deconstruct(user_input)

	# Print the deconstructed user input
	print(ui)

	check_file(ui)

if __name__ == "__main__":
	main()

