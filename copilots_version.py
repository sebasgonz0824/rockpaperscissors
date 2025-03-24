import random as rd

def user_function():
    try:
        user_pick = int(input('''\nRock. Paper. Scissors. Shoot! Select what you're throwing! 
        1. Rock
        2. Paper
        3. Scissors\n'''))
        if user_pick in [1, 2, 3]:
            return ['Rock', 'Paper', 'Scissors'][user_pick - 1]
        else:
            print("That wasn't one of the options")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def opponent_function():
    return ['Rock', 'Paper', 'Scissors'][rd.randint(0, 2)]

def determine_winner(user_hand, opponent_hand):
    if user_hand == opponent_hand:
        return 'tie'
    elif (user_hand == 'Rock' and opponent_hand == 'Scissors') or \
         (user_hand == 'Paper' and opponent_hand == 'Rock') or \
         (user_hand == 'Scissors' and opponent_hand == 'Paper'):
        return 'user'
    else:
        return 'opponent'

def main():
    user_score = 0
    opponent_score = 0

    while True:
        user_hand = user_function()
        if user_hand is None:
            print("Game Over")
            break

        opponent_hand = opponent_function()
        print(f'You have selected {user_hand}')
        print(f'Your opponent has selected {opponent_hand}')

        result = determine_winner(user_hand, opponent_hand)
        if result == 'tie':
            print("It's a tie! Play again")
        elif result == 'user':
            print(f'You win! {user_hand} beats {opponent_hand}')
            user_score += 1
        else:
            print(f'You lose! {opponent_hand} beats {user_hand}')
            opponent_score += 1

        print(f"The score is now | You: {user_score} Opponent: {opponent_score}")

        if user_score == 3:
            print("You win! Congratulations!")
            print("Game Over")
            break
        if opponent_score == 3:
            print("You lose! Better luck next time!")
            print("Game Over")
            break

if __name__ == "__main__":
    main()