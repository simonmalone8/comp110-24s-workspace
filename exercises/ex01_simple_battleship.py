"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730476889"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
emoji_string: str = ""

# p1 picking boat location
p1_input = int(input("Pick a secret boat location between 1 and 4:"))
if int(p1_input) > 4:
    print(f"Error! {p1_input} too high!")
    exit()
if int(p1_input) < 1:
    print(f"Error! {p1_input} too low!")
    exit()

# p2 guessing boat location
p2_guess = int(input("Guess a number between 1 and 4:"))
if int(p2_guess) > 4:
    print(f"Error! {p2_guess} too high!")
    exit()
if int(p2_guess) < 1:
    print(f"Error! {p2_guess} too low!")
    exit()
if p2_guess == p1_input:
    if p2_guess == 1:
        emoji_string = RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
        print(emoji_string)
    if p2_guess == 2:
        emoji_string = BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX
        print(emoji_string)
    if p2_guess == 3:
        emoji_string = BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX
        print(emoji_string) 
    if p2_guess == 4: 
        emoji_string = BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX
        print(emoji_string)        
    print("Correct! You hit the ship.")    
else:
    if p2_guess == 1:
        emoji_string = WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX
        print(emoji_string)
    if p2_guess == 2:
        emoji_string = BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX
        print(emoji_string)
    if p2_guess == 3:
        emoji_string = BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX
        print(emoji_string) 
    if p2_guess == 4: 
        emoji_string = BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX
        print(emoji_string) 
    print("Incorrect! You missed the ship.")