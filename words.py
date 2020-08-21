#!/usr/bin/env python3


filename = "words_alpha.txt"
user_input = input("word: ")
letter_count = len(user_input)

# Clean up the user input word
dictionary = {}
for letter in user_input:
	if letter in dictionary:
		dictionary[letter] += 1
	else:
		dictionary[letter] = 1
dictionary_items = dictionary.items()
dictionary = sorted(dictionary_items)


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
	# Open file
	dict_file = open(filename, "r")
	print("opened " + dict_file.name)

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

			if test == word:
				# Add to the list
				word_list.append(test)
				print(line)

	# Close file
	dict_file.close()
	print("closed " + dict_file.name)


def main():
	# Print the deconstructed user input
	#print(dictionary)

	check_file(dictionary)


if __name__ == "__main__":
	main()
