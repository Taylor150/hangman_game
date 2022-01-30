# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript']

word = random.choice(words)

guessed_correctly = []
guessed_incorrectly = []
lives = 8

print('H A N G M A N')
menu = input('Type "play" to play the game, "exit" to quit: ').lower()

if menu == 'play':
    while lives > 0:
        output = ''
        for letter in word:
            if letter in guessed_correctly:
                output += letter
            else:
                output += '-'
        if output == word:
            break

        guess = input(f'\n{output}\nInput a letter: ')

        if guess.islower() is False or guess.isalpha() is False:
            if len(guess) != 1:
                print('You should input a single letter')
            else:
                print('Please enter a lowercase English letter')

        if guess not in word and guessed_incorrectly.count(guess) == 0 and guess.isalpha() and guess.islower():
            if len(guess) != 1:
                print('You should input a single letter')
            else:
                print("That letter doesn't appear in the word")
                lives -= 1
                guessed_incorrectly.append(guess)

        elif guessed_incorrectly.count(guess) > 0:
            print("You've already guessed this letter")

        if guess in word and guessed_correctly.count(guess) == 0 and guess.isalpha() and guess.islower():
            guessed_correctly.append(guess)
        elif guessed_correctly.count(guess) > 0:
            print("You've already guessed this letter")

elif menu == 'exit':
    menu = input('Type "play" to play the game, "exit" to quit: ').lower()

if lives > 0:
    print()
    print(word)
    print('You guessed the word!')
    print("You survived!")
elif lives == 0:
    print("You lost!")
else:
    print("You lost!")
