import random as rd

def user_function():
    user_pick=int(input('''\nRock. Paper. Scissors. Shoot! Select what you're throwing! 
    1. Rock
    2. Paper
    3. Scissors\n'''))
    if user_pick == 1:
        user_hand='Rocasdasdkjbqakefr vck'
    elif user_pick == 2:
        user_hand='Paper'
    elif user_pick == 3:
        user_hand='Scissors'
    else:
        print("That wasn't one of the options")
        return None
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

def main():
    y=0
    z=0
    while True:
        user_hand_main = user_function()
        if user_hand_main==None:
            print("Please try again")
            break
        opponent_hand_main = opponent_function()
        print('You have selected',user_hand_main)
        print('Your opponent has selected', opponent_hand_main)
        if user_hand_main=='Rock' and opponent_hand_main=='Scissors':
            print('You win! Rock beats Scissors')
            y=y+1
            print("You now have",y,"points")
        if user_hand_main=='Rock' and opponent_hand_main=='Paper':
            print('You lose! Paper beats Rock')
            z=z+1
            print("Your opponent now has ",z,"points")
        if user_hand_main=='Paper' and opponent_hand_main=='Rock':
            print('You win! Paper beats Rock')
            y=y+1
            print("You now have",y,"points")
        if user_hand_main=='Paper' and opponent_hand_main=='Scissors':
            print('You lose! Scissors beats Paper')
            z=z+1
            print("Your opponent now has ",z,"points")
        if user_hand_main=='Scissors' and opponent_hand_main=='Paper':
            print('You win! Scissors beats Paper')
            y=y+1
            print("You now have",y,"points")
        if user_hand_main=='Scissors' and opponent_hand_main=='Rock':
            print('You lose! Rock beats Scissors')
            z=z+1
            print("Your opponent now has",z,"points")

        if user_hand_main==opponent_hand_main:
            print("It's a tie! Play again")
        if y==3:
            print("You win! Congratulations!")
            print("Game Over")
            break
        if z==3:
            print("You lose! Better luck next time!")
            print("Game Over")
            break
        print("The score is now | You:",y,"Opponent:",z)
