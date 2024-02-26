"""EX03 - Functional Battleship Battleship."""
 
__author__ = "730476889"

import random

# Defining the box colors
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


# Prompting for a guess from the user
def input_guess(grid_size: int, guess_type: str) -> int:
    """Prompting and returning the user's row or column guess."""
    assert guess_type == "row" or guess_type == "column"

    player_guess: int = int(input(f"Guess a {guess_type}: "))
    if 1 <= player_guess <= grid_size:
        return player_guess
    else:
        while 1 > player_guess or player_guess > grid_size:
            player_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
            if 1 <= player_guess <= grid_size:
                guess_type = str(player_guess)
        return player_guess


# Printing a grid of boxes that will be my playing board
def print_grid(grid_size: int, grid_row: int, grid_column: int, correct_guess: bool) -> None:
    """Function will print a grid to represent the gameboard."""
    rcounter: int = 1
    while rcounter <= grid_size:
        row_string: str = ""
        ccounter: int = 1
        if grid_row == rcounter:
            while ccounter <= grid_size:
                if grid_column == ccounter:
                    if correct_guess is True:
                        row_string += RED_BOX
                    elif correct_guess is False:
                        row_string += WHITE_BOX 
                else:
                    row_string += BLUE_BOX  
                ccounter += 1
        else:
            while ccounter <= grid_size:
                row_string += BLUE_BOX
                ccounter += 1
        print(row_string)
        rcounter += 1


# Figuring out if the guess was correct(red) or wrong(blue)
def correct_guess(secret_boat_row: int, secret_boat_column: int, player_r_guess: int, player_c_guess: int) -> bool:
    """Function will return whether the user was correct or not."""
    if secret_boat_row == player_r_guess and secret_boat_column == player_c_guess:
        return True
    else:
        return False 
    

# Creating the main function which will act as the Battleship's "game loop"
def main(grid_size: int, secret_boat_row: int, secret_boat_column: int) -> None:
    """This function will tie the whole program together."""
    turn_number: int = 1
    win: bool = False
    while turn_number <= 5 and win is False:
        print(f"=== Turn {turn_number}/5 ===")
        player_r_guess = input_guess(grid_size, "row")
        player_c_guess = input_guess(grid_size, "column")
        if correct_guess(secret_boat_row, secret_boat_column, player_r_guess, player_c_guess) is True:
            print_grid(grid_size, player_r_guess, player_c_guess, True)
            print("Hit!")

            print(f"You have won in {turn_number}/5 turns!")
            win = True
        else:
            print_grid(grid_size, player_r_guess, player_c_guess, False)
            print("Miss!")
            turn_number += 1
    if turn_number > 5:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))