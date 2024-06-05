import random

hangmanPics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',

'''
 +---+
 |   |
 O   |
     |
     |
     |
=========''',
'''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''',
'''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''',
'''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''',
'''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''',
'''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

words = ('chedva', 'ayala', 'rina', 'shira', 'chani', 'ruti', 'hadasa')


def playAgain():
    playA = input("do you want to play agine?(yes or no)")
    if playA == "yes":
        return True
    elif playA == "no":
        return False
    else:
        print("worng")


def displayBoard(hangmanPics, missedLetters, shownWord):
    print(hangmanPics[len(missedLetters)])
    print("the secret word:")
    print(shownWord)
    print("missed letters:")
    print(missedLetters, sep=" ")


def getGuess(letter, alreadyGuessed):
    if not letter.isalpha():
        return '-1'
    if letter in alreadyGuessed:
        return '-2'
    return letter


def shown(letter, shownWord):
    for i in range(len(secretWord)):
        if letter == secretWord[i]:
            shownWord = (shownWord[:i] + letter + shownWord[i + 1:])
    return shownWord


gameIsDone = False
missedLetters = ''
correctLetters = ''
secretWord = words[int(random.random() * len(words))]
shownWord = '_' * len(secretWord)

# the beginning of the game
while not gameIsDone:
    displayBoard(hangmanPics, missedLetters, shownWord)

    guess = input("make a guess\n")  # e
    get = getGuess(guess, missedLetters + correctLetters)
    if get == '-1':
        print("invalid input")
    elif get == '-2':
        print("you have already guessed that letter")
    else:  # In case the letter is normal
        shownWord = shown(guess, shownWord)
        if guess in secretWord:  # If the guess is correct
            correctLetters += guess
            print("correct guess")
            if shownWord == secretWord:  # If the player has finished guessing the whole word
                print('Yes! The secret word is "' + secretWord + '". You have won!')
                gameIsDone = True

        else:  # If the guess is wrong
            missedLetters += guess
            print("wrong guess")
            if len(missedLetters) == len(hangmanPics) - 1:  # If the guesswork is over
                displayBoard(hangmanPics, missedLetters, shownWord)
                print('Game over!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                    len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

        # Does the player want to play again??
        # Initialize the variables and the game resumes...
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = words[int(random.random() * len(words))]
            shownWord = '_' * len(secretWord)
        else:
            break
