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
    print("calling 'reset_game'")
    #complete me

def check_cell(event):
    print("calling 'check_cell'")
    # use event to get the cell id that
    # was clicked and it's value
    cell_id = event.target.id
    cell_val = int(event.target.innerHTML)

    # complete me

def call_next(event):
    global all_bingo_numbers
    print("calling 'call_next'")

    #complete me


# INTERNAL FUNCTIONS
def shuffle_caller():
    global all_bingo_numbers
    print("Calling 'shuffle_caller'")

    # complete me
 
 
def reset_calls():   
    global called_numbers
    print("Calling 'reset_calls'")

    # complete me


def generate_card():
    global card_numbers
    print("Calling 'generate_card'")

    # complete me


def add_called(num):
    global called_numbers
    print("Calling 'add_called'")

    # complete me


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
