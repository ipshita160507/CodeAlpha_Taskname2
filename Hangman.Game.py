import random

# WORDS PREDEFINED
words = ["RAIN", "NIGHT", "CLOUD", "MORNING","BRIGHT"]

# CHOOSE A RANDOM WORD
hidden_word = random.choice(words)

# GAME VARIABLE
wrong_guess = 0
guessed_letters=[]
max_wrong = 6

# DISPLAY THE HIDDEN WORD
space = ["_"] * len(hidden_word)

print("=== Welcome to Hangman ===")
print("Guess the word one letter at a time.")
print( "You have {max_wrong} incorrect guesses allowed.\n")

# GAME LOOP
while wrong_guess < max_wrong and "_" in space:
    print("Word: ", " ".join(space))
    print("Guessed letters: ", " ".join(guessed_letters))
    
    guess = input("Enter a letter: ").upper()
    
    # CHECK INPUT
    if len(guess) != 1 or not guess.isalpha():
        print("enter a single letter.\n")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue
    
    guessed_letters.append(guess)
    
    # Check if guess is correct
    if guess in hidden_word:
        for j, letter in enumerate(hidden_word):
            if letter == guess:
                space[j] = guess
        print("Good guess!\n")
    else:
        wrong_guess += 1
        print("Wrong guess! {max_wrong - wrong_guess} guesses left.\n")

# Game result
if "_" not in space:
    print(" CONGRATS! You guessed the word: {hidden_word}")
else:
    print("GAME OVER! The word was:", {hidden_word})
