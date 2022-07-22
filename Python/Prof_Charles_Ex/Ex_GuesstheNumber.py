from random import randint

value = randint(0, 100)
# print(value)

rounds = 5
while rounds > 0:
    user_input = input('Guess the number: ')
    try:
        guess = int(user_input)

    except:
        print("Error, please enter numeric input only")
        continue

    if guess == value:
        print("Victory")
        break
    elif guess > value:
        print("Smaller")
    else:
        print("Bigger")
    rounds = rounds - 1
    print(rounds, "number of gueses left")
    if rounds == 0:
        print("The number was:", value)
