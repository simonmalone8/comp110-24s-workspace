"""EX01 - One Shot Battleship."""
 
__author__ = "730476889"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# setting the location of my ship
grid_size = int(4)
secret_row = int(3)
secret_column = int(2)

# asking the player to guess a row, and telling them it is wrong if it is outside the 4 by 4 box
p_input_row = int(input("Guess a row: "))
while p_input_row > grid_size or p_input_row < 1:
    p_input_row = int(input("The grid is only 4 by 4. Try again: "))

# asking the player to guess a column, and telling them it is wrong if it is outside the 4 by 4 box
p_input_column = int(input("Guess a column: "))
while p_input_column > grid_size or p_input_column < 1:
    p_input_column = int(input("The grid is only 4 by 4. Try again: "))

# Figuring out result based on player guess
result_box = RED_BOX if p_input_column == secret_column and p_input_row == secret_row else WHITE_BOX

# Using while loops to print out the 4 by 4 grid
row_counter = 1
while row_counter <= grid_size:
    row_string = ""
    column_counter = 1
    while column_counter <= grid_size:
        if row_counter == p_input_row:
            if column_counter == p_input_column:
                row_string += result_box 
            else:
                row_string += BLUE_BOX  
        else:
            row_string += BLUE_BOX  

        column_counter += 1

    print(row_string)  
    row_counter += 1   

# printing Hit! or Miss! depending on the result of the guess. As well as giving the player a hint if they are close
if p_input_column == secret_column and p_input_row == secret_row:
    print("Hit!")
elif p_input_column == secret_column:
    print("Close! Correct column, wrong row. ")
elif p_input_row == secret_row:
    print("Close! Correct row, wrong column. ")
else:
    print("Miss!")