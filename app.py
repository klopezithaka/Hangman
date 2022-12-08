print("Welcome to Hangman!")

word = "Beautiful"
guess1 = input("Guess your first letter: ")

if guess1 in word:
    print("That letter is located at space: ", word.find(guess1))
else:
    print("No match found")


