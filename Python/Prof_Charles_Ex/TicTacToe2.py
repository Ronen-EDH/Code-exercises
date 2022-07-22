# def board():
#     print(" | ".join(bottomline))
#     print(" | ".join(midline))
#     print(" | ".join(topline))
# Do it with for loop


# bottomline = ['_', '_', '_']
# midline = ['_', '_', '_']
# topline = ['_', '_', '_']

theboard = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
userboard = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

for line2 in userboard:
    print(" | ".join(line2))

# board()
print('-=Welcome to my Tic-tac-toe game=-\nYou have the following options:\nPlay - Info - Quit')

# for list in theboard:
#     for number in list:
#         print(number, end=' ')

# print(number)

# 000 if word_to_guess[i] == gue1ss:
#     hidden[i] = guess
# print(theboard[0:1])

while True:
    user_input = input().lower()
    if user_input == 'play':
        for line2 in userboard:
            print(" | ".join(line2))
        break
    if user_input == 'info':
        print('This is a 2 player Tic-tac-toe game.\nThe 1st player is X, the 2nd is O\nUse the NumPad to mark your space.')
        continue
    if user_input == 'quit':
        quit()
    else:
        print('Error, Thats not a valid command.\nType in "Play","Info" or "Quit."')
        continue

position = '1st'
while True:
    player_input = input(f" ({position} Player move): ").lower()
    if not player_input.isdigit():
        print("Please use only single digits")
        continue
    if player_input == '1':
        if userboard[2][0] == '_':
            if position == '1st':
                userboard[2][0] = 'X'
            if position == '2nd':
                userboard[2][0] = 'O'
            for line2 in userboard:
                print(" | ".join(line2))
        else:
            print("This position has been already taken")
    if position == '1st':
        position = '2nd'
    else:
        position = '1st'
