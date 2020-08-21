#!/usr/bin/env python3


filename = "words_alpha.txt"


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
	return hold


def check_file(word):
	# word length for comparison
	word_length = len(word)

	# Open file
	dict_file = open(filename, "r")
	print("opened " + dict_file.name) # pointless, really

	word_list = []

	for line in dict_file:
		# Remove newlines, make everything lowercase
		line = line.rstrip().lower()

		# Get item's len()
		line_length = len(line)

		# If the counts from each item and the user_input match, add word to list
		if word_length == line_length:
			# Make sorted split of word
			test = deconstruct(line)

			if test == word:
				# Add to the list
				word_list.append(line)
				# print(line)



	# Close file
	dict_file.close()
	print("closed " + dict_file.name) # pointless, really

	# return the list of matching words
	return word_list


def main():
	# take user input
	user_input = input("word: ")

	# deconstruct user input
	dictionary = deconstruct(user_input)

	# check if the word has an anagram counterpart
	words = check_file(dictionary)

	# print the list
	print(words)


if __name__ == "__main__":
	main()
