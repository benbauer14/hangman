#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
solution = word_list[random.randint(0, len(word_list) -1)]
print(solution)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input(f"Please guess a letter.\n")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.