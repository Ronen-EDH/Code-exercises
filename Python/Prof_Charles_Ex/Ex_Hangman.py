# Importing a .txt file
import os
import random
inputlist = open('hangman.txt')

# Making a list that strips and contains the words from
#  the .txt file
guesslist = list()
for line in inputlist:
    wds = line.rstrip()
    guesslist.append(wds)

# Making a list for the hidden word, than choose a random
# word from the guesslist, than making a loop that goes
# through the letters and for each letter there put a '_'
# in the "hiddenw" list
hiddenw = []
the_word = random.choice(guesslist)
print(the_word)
for letter_in_the_word in the_word:
    hiddenw.append('_')

print(" ".join(hiddenw))

all_letters = []
gletters = 10
while gletters > 0:
    user_input = input('Guess the letter: ').lower().strip()
    if not user_input.isalpha():
        print('Error, Please enter a letter')
        continue

    if len(user_input) > 1:
        print('Error, please input only one letter at the time')
        continue

    if user_input not in all_letters:
        all_letters.append(user_input)
    else:
        print('This letter already been guessed')
        continue

    if user_input in the_word:
        sameletters = the_word.count(user_input)
        pos = the_word.find(user_input)
        hiddenw[pos] = user_input
        while sameletters > 1:
            pos = the_word.find(user_input, pos+1)
            hiddenw[pos] = user_input
            sameletters -= 1
    else:
        gletters -= 1

    if '_' not in hiddenw:
        print('Well done, you won :)')
        quit()

    os.system("cls")
    print('You got:', gletters, 'more guesses.')
    print(" ".join(hiddenw))
    # print(hiddenw)
print('The word was:', the_word)
