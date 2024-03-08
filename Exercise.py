TREASURE_ASCII_CODE = '''
             __________
            /\____;;___\ \t
           | /         /
           `. ())oo() .
            |\(%()*^^()^\
           
           \ | %  ))   |
            \|%________|
'''
welcome_note = 'Welcome To Treasure Game'
task = 'Your Mission is find the trasure'
print(TREASURE_ASCII_CODE)
print(welcome_note)
print(task)
choice1 = input('In this island where you go left or right? : ')
if choice1 == 'right':
    print('Game Over')
elif choice1 == 'left':
    choice2 = input('There is a pond in the middle of island Swim or Wait : ')
    if choice2 == 'swim':
        print('Game Over')
    elif choice2 == 'wait':
        choice3 = input('In front You there is 3 door\' this are Red, Blue, Yellow : ')
        if choice3 == 'red':
            print('Game Over')
        elif choice3 == 'blue':
            print('Game Over')
        elif choice3 == 'yellow':
            print('Game Win')
