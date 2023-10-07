import dice
import player
import sys

N_DICES = 2
GOAL_SCORE = 100
DEFAULT_LIMIT = 15


def setup_game():

    # Initialize two dice
    dices = [0] * N_DICES
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
    sys.exit(1)


def print_dices(dices):
    '''
    Converts the results of the dice into a string.
    Parameters:
        dices:
    Returns:
        str_out: string
    '''
    str_out = ""
    for i in dices:
        str_out += " " + str(i)
    str_out.strip()
    str_out = "You have rolled:" + str_out
    print(str_out)


def instructions():
    '''
    Prints the instructions at the start of the match
    '''
    str_out = ""
    str_out += (f"The  first player that reaches {GOAL_SCORE} wins.\n")
    str_out += ("Enter 'r' to roll the dice.\n")
    str_out += ("-If you roll a '1', you lose all your points for the roll and your turn.\n")
    str_out += ("-If you roll two '1's, you lose all your score and your turn.\n")
    str_out += ("Enter 'h' to hold your points and pass the turn to the next player.\n")
    str_out += ("Enter 'q' at any time to quit the game.\n")
    str_out += ("Humans go first.")
    return str_out


def set_computer_limit(args: list) -> int:
    '''
    Updates the computer limit to second command line argument
    Parameters:
        args: list
    Returns:
        new_limit: int
    '''
    new_limit = int(args[1])

    if new_limit <= 0:
        raise ValueError("Must be a positive integer.")

    return new_limit


def play_human_turn(player, dices):
    temp = 0
    while True:
        decision = input("What do you want to do ('q' to quit game, 'r' to roll, 'h' to hold)? ").lower()
        if decision == "r":
            player.roll_dice(dices)
            dice_1 = int(dices[0].top_face)
            dice_2 = int(dices[1].top_face)
            print_dices(dices)
            if dice_1 == 1 and dice_2 == 1:
                player.score = 0
                break
            elif dice_1 == 1 or dice_2 == 1:
                break
            else:
                temp += dice_1 + dice_2
        elif decision == "h":
            if temp == 0:
                print("You have not rolled the dice yet.")
            else:
                player.update_score(temp)
                break
        elif decision == "q":
            quit_game()
        else:
            print("I don't understand...")


def play_computer_turn(player, dices, computer_limit):
    temp = 0
    while True:
        player.roll_dice(dices)
        dice_1 = dices[0].top_face
        dice_2 = dices[1].top_face
        print_dices(dices)
        if dice_1 == 1 and dice_2 == 1:
            player.score = 0
            break
        elif dice_1 == 1 or dice_2 == 1:
            break
        else:
            temp += dice_1 + dice_2

        if temp >= computer_limit:
            player.update_score(temp)
            break


def check_win(player, goal_score):
    '''
    Checks if current_player has reached the goal score
    '''
    if player.score >= goal_score:
        return True
    else:
        return False


def play_two_dice_pig_game(players, dices, computer_limit, instructions_text):
    human_player, computer_player = players

    current_player = human_player

    print(instructions_text)

    while True:
        print(f"Score: {human_player} - {human_player.score}, Computer - {computer_player.score}")
        print(f"It is now {current_player} turn...")

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

    computer_limit = DEFAULT_LIMIT

    try:
        computer_limit = set_computer_limit(args)
    except ValueError as e:
        print(f"ValueError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")

    dices, players = setup_game()
    instructions_text = instructions()

    play_two_dice_pig_game(players, dices, computer_limit, instructions_text)


# DO NOT REMOVE
if __name__ == "__main__":
    main(sys.argv)