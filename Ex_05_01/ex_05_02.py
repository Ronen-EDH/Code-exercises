largest_so_far = None
smalest_so_far = None
while True:
    num = input('Enter a number: ')
    print(num)
    if num == 'done':
        break
    else:
        try:
            num = float(num)
        except:
            print('Invalid input')
            continue

    if largest_so_far == None or num > largest_so_far:
        largest_so_far = num
    if smalest_so_far == None or num < smalest_so_far:
        smalest_so_far = num

    print('Largest', largest_so_far)
    print('Smalest', smalest_so_far)
