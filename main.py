from pyscript import document
import card_matrix
import random

# this array store all possible number the caller can call, and should be shuffled during reset
all_bingo_numbers = []
# this array stores the numbers that have been called this game.
called_numbers = []
#this array stores the 25 numbers generated for the bingo card
card_numbers = []

# EVENTS
def reset_game(event):
    global all_bingo_numbers, called_numbers, card_numbers  #   ACCESS to THAT global variable   #
    shuffle_caller()    #   shuffles numbers    #
    reset_calls()       #   resets the game     #
    document.querySelector("#current_call").innerHTML = ""
    document.querySelector("#called_numbers").innerHTML = ""
    generate_card()     #   new bingo card      #
    card_matrix.reset_card() #c\
    document.querySelector("#win_game").close()
    print("resetting")


def check_cell(event):
    global called_numbers
    cell_id = event.target.id               #   EXTRACTS unique ID of CLICKED cell from EVENT object    #
    cell_val = int(event.target.innerHTML)  #   EXTRACTS NUMBER values of CLICKED cell  #
    print(cell_val)
    x = int(cell_id.split("_")[1])
    y = int(cell_id.split("_")[2])
    if cell_val in called_numbers and not card_matrix.is_position_marked(x,y):  #   LOOP for checking called numbers    #
        highlight_card_cell("#" + cell_id)    #   Highlight's called number, USERS BINGO CARD   #
        Bingo = card_matrix.mark_position(x,y)
        if Bingo:
            document.querySelector("#win_game").showModal()

    print("CHECKING")


def call_next(event):
    global all_bingo_numbers, called_numbers
    next_number = all_bingo_numbers.pop()   #    PEZ dispenses 'number'    #
    add_called(next_number)

    print(f"NEXT Number : {next_number}")


# INTERNAL FUNCTIONS
def shuffle_caller():
    global all_bingo_numbers
    all_bingo_numbers = list(range(1, 76))  #   this creates THE list of numbers for BINGO card #
    random.shuffle(all_bingo_numbers)   # SHUFFLE Bingo Numbers #
    for x in all_bingo_numbers:
        cell_id = f"#cell_{x}"
        reset_caller_cell(cell_id)

    print("shuffling")

 
 
def reset_calls():   
    global called_numbers    #   ACCESS to THAT global variable   #
    called_numbers = []     #   this functions clears the array #



def generate_card():
    global card_numbers
    card_numbers = list(range(1, 76))   #   Generates a NEW Bingo Card and Numbers  #
    random.shuffle(card_numbers)
    card_numbers = card_numbers[:25]    # this (:##) grabs the first ## of entries from list    #

    for x in range(5):
        for y in range (5):
            cell_id =f"#cell_{y + 1}_{x + 1}"
            number = card_numbers.pop()        #    PEZ dispenses 'number'    #
            document.querySelector(cell_id).innerHTML = number
            reset_card_cell(cell_id)
    print("card generating")



def add_called(num):
    global called_numbers
    called_numbers.append(num)
    highlight_caller_cell(f"#cell_{num}")
    document.querySelector("#current_call").innerHTML = num     #   connects to .HTML , "#" classifies it   #
    #
    document.querySelector("#called_numbers").innerHTML =  ", ".join(str(x) for x in called_numbers)




# adds/removes highlight CSS classes from cells (these are complete, don't change)
def highlight_card_cell(cell_id):
    document.querySelector(cell_id).className += "highlight-card"


def reset_card_cell(cell_id):
    document.querySelector(cell_id).className = ""


def highlight_caller_cell(cell_id):
    document.querySelector(cell_id).className += "highlight-caller"


def reset_caller_cell(cell_id):
    document.querySelector(cell_id).className = ""


# initial setup
reset_game(0)
