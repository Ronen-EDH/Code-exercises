import random

words_file = open("hangman.txt")
words = [line.strip() for line in words_file if len(line.strip()) > 5]

word_to_guess = random.choice(words)

hidden = ["_" for letter in word_to_guess]
allowed_tries = 10
used_letters = set()
while allowed_tries > 0:
    print(" ".join(hidden))
    guess = input(f"Guess a letter ({allowed_tries} tries left): ").lower()

    if not guess.isalpha():
        print("Please enter a letter")
        continue

    if guess in used_letters:
        print("You already proposed that letter")
        continue

    used_letters.add(guess)

    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                hidden[i] = guess
    else:
        print("Wrong!")
        allowed_tries -= 1
    if "".join(hidden) == word_to_guess:
        print("You won!")
        break

if allowed_tries == 0:
    print("You lost!")
    print("The word was: " + word_to_guess)
