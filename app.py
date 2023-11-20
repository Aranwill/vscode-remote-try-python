#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

score = {"Player": 0, "Computer": 0}
rounds_played = 0

def play():
    global rounds_played
    user = ""
    while user not in ['rock', 'paper', 'scissors']:
        user = input("What's your choice? 'rock', 'paper', 'scissors': ")
        user = user.lower()
        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose 'rock', 'paper' or 'scissors'.")
    user = user.lower()

    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        print('It\'s a tie!')
    elif is_user_winner(user, computer):
        print('You won!')
        score["Player"] += 1
    else:
        print('You lost!')
        score["Computer"] += 1

    rounds_played += 1
    print(f"Score: Player - {score['Player']}, Computer - {score['Computer']}")
    print(f"Rounds Played: {rounds_played}")

def is_user_winner(player, opponent):
    if (player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True

if __name__ == '__main__':
    while True:
        play()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print(f"Your final score is: {score['Player']}")
            print(f"Total rounds played: {rounds_played}")
            break
