numbercount = 0
total = 0.0
rounds = 0
while rounds > -1:
    guess = input('Enter a number: ')
    if guess == 'done':
        print(total, numbercount, average)
        break
    else:
        try:
            guess = float(guess)
        except:
            print('Invalid input')
            continue

        rounds = rounds + 1
        numbercount = rounds
        total = guess + total
        average = total / float(numbercount)
