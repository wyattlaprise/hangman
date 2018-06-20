import random

def ans():
	'''
	Takes pseudo random word from text file and presents it to the user to guess

	:Return: pseudo random word
	:Rtype: string
	'''
	try:
		text = open('random_words.txt', 'r')
	except FileNotFoundError:
		print('File not found')

	max = len(text.readline()) # max param in random number

	count = 0 # counter
	rand_int = random.randint(1, max)

	while True:
		curr_word = text.readline()
		count += 1

		if count == rand_int:
			return curr_word # returns word
			break

	text.close()
