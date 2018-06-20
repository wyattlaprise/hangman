# title				:hangman
# author			:wyatt laprise
# date				:20180620
# python_version	:3.6.4

import sys

if sys.version_info[0] < 3:
	raise 'You need to be using Python 3. Go to "https://www.python.org/downloads/" for more information'

import random #python module
import functions
import random_word

word = random_word.ans() # pulls random word from 'random_word.py'
count = len(word[1:]) # length of word
assemble = [] # assembles word
wrong = [] # compiles incorrect letters
num = 6 # number of tries left

if '\n' in word: # removes '\n' from word
	count -= 1

print('Welcome to the Hangman Game!')

print('\nThe word is {0} letters long, and you have {1} tries.\n'.format(count, num))

print('Word: {0}'.format(functions.word(assemble, word))) # prints word as it gets assembled

while count > 0: # while not fully assembled
	guess = input('\nWhat is your guess? ').lower() # asks user for guess

	if guess in word and guess not in assemble and len(guess) == 1: # if guess is correct
		assemble.append(guess)
		count -= functions.sub(guess, word) # number of letters in word left

		print('You are correct, now there are: {0} letters left, and you have {1} tries left.\n'.format(count, num))

		print('Word: {0}'.format(functions.word(assemble, word))) # prints word as it gets assembled
		print('Wrong: {0}'.format(functions.wrong(guess, word, wrong))) # prints incorrect letters
	elif len(guess) == 0: # if guess is null
		pass
	elif guess in assemble or guess in wrong: # if guess is already logged
		print('You already guessed that.\n')

		print('Word: {0}'.format(functions.word(assemble, word))) # prints word as it gets assembled
		print('Wrong: {0}'.format(functions.wrong(guess, word, wrong))) # prints incorrect letters
	elif len(guess) > 1: # if guess is too long
		print('That\'s too long')

		print('Word: {0}'.format(functions.word(assemble, word))) # prints word as it gets assembled
		print('Wrong: {0}'.format(functions.wrong(guess, word, wrong))) # prints incorrect letters
	elif guess not in word: # if guess is incorrect
		num -= 1 # number of tries left, - 1

		if num < 6 and num > 0: # if user is not out of tries
			print('That is not in the word, and you have {0} tries left.\n'.format(num))

			print('Word: {0}'.format(functions.word(assemble, word))) # prints word as it gets assembled
			print('Wrong: {0}'.format(functions.wrong(guess, word, wrong))) # prints incorrect letters
		elif num == 0: # if user is out of tries
			print('\n\n\tYou loose.\tThe word was: {0}\n\n'.format(word))
			break

if count == 0: # if correct
	 print('\n\n\tYou got it!\tThe word was: {0}\n\n'.format(word))
