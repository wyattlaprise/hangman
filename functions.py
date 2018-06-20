import bisect

def sub(guess, word):
	'''
	Returns number of letters in guess to main.py

	:Param word: random word assigned to user
	:Return:
	:Rtype: int
	'''

	sub = word.count(guess)

	return sub

def word(assemble, word):
	'''
	Collects user's correct inputs and compiles them

	:Param assemble: collects user's correct inputs and compiles them
	:Return: returns word as it gets created
	:Rtype: array
	'''

	create = []
	for letter in word:
		if letter != '\n':
			if letter in assemble:
				create.append(letter)
			elif letter not in assemble:
				create.append('_')

	return create

def wrong(guess, word, wrong):
	'''
	Collects user's incorrect inputs and compiles them

	:Param guess: user's guess
	:Param word: random word from sting to assign user
	:Param wrong: user's incorrect guesses
	:Return: wrong guesses alphabetically
	:Rtype: array
	'''

	if guess not in word and guess not in wrong and len(guess) == 1:
		bisect.insort(wrong, guess)

	return wrong
