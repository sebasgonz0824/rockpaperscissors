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

        

# for x in range(5):
#     print(x+1)