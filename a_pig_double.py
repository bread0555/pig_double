import dice
import player
import sys

N_DICES = 2
GOAL_SCORE = 100
DEFAULT_LIMIT = 15


def setup_game():

    # Initialize two dice
    dices = [0] * N_DICES # list of dice
    i = 0
    while i < N_DICES:
        dices[i] = dice.Dice()
        i += 1

    # Initialize a list of players
    name = input("What is your name human? ")
    human_player = player.Player(name)
    computer_player = player.Player("Computer")
    print(f"Hi, {human_player}.")
    
    players = (human_player, computer_player)

    return dices, players

def quit_game():
    print("See you again.")

def print_dices(dices):
    str_out = ""
    for i in dices:
        str_out += str(i) + " "
    return str_out.strip()

def instructions():
    str_out = ""
    str_out += (f"The  first player that reaches {GOAL_SCORE} wins.\n")
    str_out += ("Enter 'r' to roll the dice.\n")
    str_out += ("-If you roll a '1', you lose all your points for the roll and your turn.\n")
    str_out += ("-If you roll two '1's, you lose all your score and your turn.\n")
    str_out += ("Enter 'h' to hold your points and pass the turn to the next player.\n")
    str_out += ("Enter 'q' at any time to quit the game.\n")
    str_out += ("Humans go first.")
    return str_out


def set_computer_limit(args):
    '''
    Updates the computer limit to second command line argument
    Parameters:
        args: list
    Returns:
        new_limit: int
    '''
    try:
        new_limit = args[1]
    except IndexError as e:
        print(f"ValueError: {e}")
        new_limit = DEFAULT_LIMIT

    try:
        new_limit = int(new_limit)
    except ValueError as e:
        print(f"ValueError: {e}")
        new_limit = DEFAULT_LIMIT
    
    if new_limit <= 0:
        raise ValueError("ValueError: Must be a postitive integer.")
        new_limit = DEFAULT_LIMIT

    return new_limit

def handle_player_decision(player, dices):
    decision = input("What do you want to do ('q' to quit game, 'r' to roll, 'h' to hold)? ").lower()

    if decision == "r":
        pass
    elif decision == "h":
        pass
    elif decision == "q":
        sys.exit(1)
    else:
        print("I don't understand")

def play_human_turn(player, dices):
    pass



def play_computer_turn(player, dices, computer_limit):
    pass


def check_win(player, goal_score):
    if player.score >= goal_score:
        return True
    else:
        return False


def play_two_dice_pig_game(players, dices, computer_limit, instructions_text):
    human_player, computer_player = players

    current_player = human_player
    human_player_score = 0
    computer_score = 0

    print(instructions_text)

    while True:
        print(f"Score: {human_player} - {human_player_score}, Computer - {computer_score}")
        print(f"It is now {current_player}'s turn...")

        if current_player == human_player:
            play_human_turn(current_player, dices)
        else:
            play_computer_turn(current_player, dices, computer_limit)

        if check_win(current_player, GOAL_SCORE):
            print(f"{current_player} wins!")
            break

        if current_player == human_player:
            current_player = computer_player
        else:
            current_player = human_player
        


def main(args):
    '''
    Implementation of Two-Dice Pig game.
    '''
    computer_limit = set_computer_limit(args)
    dices, players = setup_game()
    instructions_text = instructions()

    play_two_dice_pig_game(players, dices, computer_limit, instructions_text)

    # player.rolldices(dices)

    quit_game()
    

# DO NOT REMOVE
if __name__ == "__main__":
    main(sys.argv)