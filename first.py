import random as rd

def user_function():
    user_pick=int(input('''Rock. Paper. Scissors. Shoot! Select what you're throwing! 
    1. Rock
    2. Paper
    3. Scissors\n'''))
    if user_pick == 1:
        user_hand='Rock'
    elif user_pick == 2:
        user_hand='Paper'
    elif user_pick == 3:
        user_hand='Scissors'
    else:
        print("That wasn't one of the options")
        user_hand='Game Over'
    return (user_hand)    

def opponent_function():
    opponent_pick=rd.randint(1,3)
    if opponent_pick == 1:
        opponent_hand='Rock'
    if opponent_pick == 2:
        opponent_hand='Paper'
    if opponent_pick == 3:
        opponent_hand='Scissors'
    return (opponent_hand)
x=0
while x<3:
    user_hand_main = user_function()
    opponent_hand_main = opponent_function()
    print('You have selected',user_hand_main)
    print('Your opponent has selected', opponent_hand_main)
    # print(user_hand_main)
    if user_hand_main==opponent_hand_main:
        print("It's a tie! Play again")
        x=x+1
        print("You guys now both have",x,"points")
    if x==3:
        print("Game Over")
        break
        

# for x in range(5):
#     print(x+1)
