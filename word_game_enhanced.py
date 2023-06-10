# Name:  Senal Dampiya Dolage
# Student Number:  10609526

import random
import sys


# The word list.
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER',
                  'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']


# Reusable function to print the words in wordList.
def printWordList():
    print("Password is one of the follwing words: \n")
    for index, word in enumerate(wordList):
        print("(" + str(index + 1) + ")." + word)
    print("\n")


# Setting the game difficulty level and set it to global variable difficulty.
def selectDifficulty():
    try:
        global difficulty
        difficulty = input("Select difficulty level (Easy, Medium or Hard): ").lower()
    except:
        print("Invalid input")


# Choosing a varying amount of random words from the candidateWords depending on difficulty level.
def selectWordList():
    try:
        global wordList
        if (difficulty == "easy"):
            wordList = random.sample(candidateWords, 6)
        elif (difficulty == "medium"):
            wordList = random.sample(candidateWords, 7)
        elif (difficulty == "hard"):
            wordList = random.sample(candidateWords, 8)
        else:
            print("Difficulty level is not defined.")
            sys.exit(0)
        printWordList()
    except:
        print("Invalid input")


# Choosing a password from the wordList and storing in variable password.
def choosePassword():
    global password
    password = random.choice(wordList)
    # print("Password is ->", password)


# This function receives two words as parameters should return the number of matching characters between them.
# Parameters:
#   "password": String.
#   "userGuess": String.
# Returns matched characters: Integer.
def compareWords(pwd, userGuess):
    i = 0
    match = 0
    while i < len(pwd):
        if userGuess[i] == pwd[i]:
            match = match + 1
        i = i + 1
    return match


# Re-run the game if user wishes to keep playing
def reRunGame():
    try:
        userInput = input("Do you wish to play again (y or n): ").lower()
        if (userInput == "y"):
            selectDifficulty()
            selectWordList()
            choosePassword()
            getUserAnswer()
        elif (userInput == "n"):
            print("Thank you for playing")
        else:
            print("Not a valid response.")
    except ValueError:
        print("Invalid input")


# The main function of the program, to get users guess and show the result.
def getUserAnswer():
    won = False
    count = 1

    if (difficulty == "easy"):
        guessesRemaining = 5
        iterations = 5
    elif (difficulty == "medium"):
        guessesRemaining = 4
        iterations = 4
    elif (difficulty == "hard"):
        guessesRemaining = 3
        iterations = 3

    try:
        while count <= iterations:
            print("Guesses remaining: ", guessesRemaining)
            userInput = int(input("Which number is your guess (enter 1-8)? "))
            print(wordList[userInput - 1])
            matches = compareWords(password, wordList[userInput - 1])
            guessesRemaining = guessesRemaining - 1
            count = count + 1
            if (matches == len(password)):
                won = True
                print("Password Correct")
                break
            else:
                print("Password Incorect. Try again.")
                print(str(matches) + "/" + str(len(password)) + " correct" + "\n")
                wordList[userInput - 1] = wordList[userInput - 1] + " " + str(matches) + "/" + str(len(password))
                printWordList()
                continue
    except ValueError:
        print("Invalid input")
    except IndexError:
        print("Invalid guess. Please use the given range.")
        pass
    except:
        print("An error has occured.")
        pass
    finally:
        if won:
            print("Congratulations, you win!")
        else:
            print("Sorry, you lost :(")
        reRunGame()


# Welcome message to the user.
print("Welcome to the word game!!")

# Setting difficulty level.
selectDifficulty()

# Select random words from the provided cadidateWords.
selectWordList()

# Choosing a password from the randomly picked words.
choosePassword()

# Getting users guess and showing the result.
getUserAnswer()
