# Name:             Senal Dampiya Dolage
# Student Number:   10609526

import random


# The word list.
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER', 'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER', 'BECKET', 'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED', 'BELIES', 'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER', 'BOBBER', 'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER', 'BOSKER', 'BOTHER', 'BOWYER', 'BRACER', 'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN', 'DEAFER', 'DEARER', 'DELVER', 'DENSER', 'DEXTER', 'EVADER',
                  'GELDED', 'GELDER', 'HEARER', 'HEIFER', 'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER', 'LEANER', 'LEAPER', 'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER', 'MEANER', 'MENDER', 'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER', 'PEWTER', 'PODDED', 'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER', 'RELIER', 'RENDER', 'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR', 'TEENER', 'TEMPER', 'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED', 'YONDER']


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


# Function to print the wordList.
def printWordList():
    print("Password is one of the follwing words: \n")
    for index, word in enumerate(wordList):
        print("(" + str(index + 1) + ")." + word)
    print("\n")


# Getting users answer(guess)
def getUserAnswer():
    guessesRemaining = 4
    count = 1
    won = False
    try:
        while count <= 4:
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
                printWordList()
                continue
    except ValueError:
        print("Invalid input")
        pass
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
        print("Thank you for playing")


# Welcome message to the user.
print("Welcome to the word game!!")

# Choosing 8 random words from the candidateWords and storing it in variable wordList.
global wordList
wordList = random.sample(candidateWords, 8)

# Choosing a password from the wordList and storing in variable password.
global password
password = random.choice(wordList)
# print("Password is ->", password)

# Reusable function to print the words in wordList.
printWordList()

# The main function of the program, to get users guess and show the result.
getUserAnswer()
