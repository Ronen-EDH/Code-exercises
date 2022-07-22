board = '_ | _ | _\n_ | _ | _\n_ | _ | _'

# print(len(board))
print('-=Welcome to my Tic-tac-toe game=-\nYou have the following options:\nPlay - Info - Quit')


while True:
    user_input = input().lower()
    if user_input == 'play':
        print(board)
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
    if position == '1st':
        position = '2nd'
    else:
        position = '1st'
    if player_input is '1':
