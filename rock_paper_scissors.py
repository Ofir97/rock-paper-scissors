import random


def letter_to_tool(letter):
    switcher = {
        'R': "rock",
        'P': "paper",
        'S': "scissors",
    }

    return switcher.get(letter, 'invalid')


def play():
    player = letter_to_tool(input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors: ").upper())
    computer = random.choice(('rock', 'paper', 'scissors'))
    if is_player_choice_invalid(player):
        print('invalid player input')
    elif player == computer:
        print(f"It's a tie! Both you and opponent chose {player}")
    elif is_win(player, computer):
        print(f"You win! Opponent choice: {computer}")
    else:
        print(f"You lose! Opponent choice: {computer}")


def is_player_choice_invalid(player):
    return player == 'invalid'


def is_win(player, opponent):
    return (player == 'rock' and opponent == 'scissors') \
        or (player == 'paper' and opponent == 'rock') \
        or (player == 'scissors' and opponent == 'paper')


play()
