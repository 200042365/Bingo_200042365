# a 2-D list (or a list of lists) that stores 
# the 'marked' state of the bingo card
card_matrix = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]


# reset the card matrix back to zero
def reset_card():
    global card_matrix
    card_matrix = [[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0]]


# check if the card position is already marked
def is_position_marked(x, y):
    return card_matrix[x-1][y-1]


# mark the position on the card and
# checks if a line has been created.
# returns True if a line has been
# created or False otherwise
def mark_position(x, y):
    global card_matrix
    card_matrix[x-1][y-1] = 1

    # Check for any lines
    # Check rows
    for row in card_matrix:
        if all(cell == 1 for cell in row):
            return True

    # Check columns
    for col in range(5):
        if all(row[col] == 1 for row in card_matrix):
            return True

    # Check top-left to bottom-right diagonal
    if all(card_matrix[i][i] == 1 for i in range(5)):
        return True

    # Check top-right to bottom-left diagonal
    if all(card_matrix[i][4 - i] == 1 for i in range(5)):
        return True

    return False


