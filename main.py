#Step 1 
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
solution = word_list[random.randint(0, len(word_list) -1)]
solutionArray = []
guessArray = []
attempts = 0

for letter in range(0, len(solution)):
    solutionArray.append(solution[letter])
    guessArray.append("_")
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
def checkLetters(guess):
    found = False
    for letterIndex in range(0,len(solutionArray)):
        if(guess == solutionArray[letterIndex]):
            guessArray[letterIndex] = guess
            found = True
        else:
    print(guessArray)

    if(found == False):
        global attempts
        attempts += 1

    for guess in guessArray:
        if(guess == "_"):
            if(attempts >5):
                buildHangMan()
                print("Game Over!")
                break

def buildHangMan():
    if(attempts == 6):
        print("      _______")
        print("      |     |")
        print("      0     |")
        print("     \|/    |")
        print("      /\    |")
        print("      ______|")
    elif(attempts == 5):
        print("      _______")
        print("      |     |")
        print("      0     |")
        print("     \|/    |")
        print("      /     |")
        print("      ______|")
    elif(attempts == 4):
        print("      _______")
        print("      |     |")
        print("      0     |")
        print("     \|/    |")
        print("            |")
        print("      ______|")
    elif(attempts == 3):
        print("      _______")
        print("      |     |")
        print("      0     |")
        print("     \|     |")
        print("            |")
        print("      ______|")
    elif(attempts == 2):
        print("      _______")
        print("      |     |")
        print("      0     |")
        print("      |     |")
        print("            |")
        print("      ______|")
    elif(attempts == 1):
        print("      _______")
        print("      |     |")
        print("      0     |")
        print("            |")
        print("            |")
        print("      ______|")
    elif(attempts == 0):
        print("      _______")
        print("      |     |")
        print("            |")
        print("            |")
        print("            |")
        print("      ______|")

while attempts < 6:
    buildHangMan()
    guess = input(f"Please guess a letter.\n").lower()
    checkLetters(guess)

