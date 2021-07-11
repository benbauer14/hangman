#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
solution = word_list[random.randint(0, len(word_list) -1)]
solutionArray = []
guessArray = []
for letter in range(0, len(solution)):
    solutionArray.append(solution[letter])
    guessArray.append("_")
print(solution)
print(solutionArray)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input(f"Please guess a letter.\n")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
def checkLetters(guess):
    found = False
    for letterIndex in range(0,len(solutionArray)):
        if(guess == solutionArray[letterIndex]):
            print("Found it!")
            guessArray[letterIndex] = guess
            found = True
        else:
            print("Nope")
    print(guessArray)
    if(found == False):
        print("Strike!")

checkLetters(guess)