import random

# Project: Hangman Game
# Author: Muhammad Saeed
# Internship: CodeAlpha - Python Programming Internship
# Description: A simple console-based Hangman game using Python.

# Step 1: Word list
words = ["python", "programming", "developer", "hangman", "internship"]

# Step 2: Random word choose karo
word = random.choice(words)
guessed_letters = []
lives = 5

print(" Welcome to Hangman Game! ")
print("_ " * len(word))

# Step 3: Game loop
while lives > 0:
    guess = input(" Enter a letter : ").lower()

    if guess in guessed_letters:
        print(" You already guessed that letter! ")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" Correct guess! ")
    else:
        lives -= 1
        print(f" Wrong guess! Lives left : {lives}")

    # Display word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word)

    # Check if user won
    if "_" not in display_word:
        print(" Congratulations! You guessed the word : ", word)
        break

# Out of lives
if lives == 0:
    print(" Game Over! The word was : ", word)
