#ctrl k c 
#ctrl k u

import random

#Generate cards
while True: #user have to write a positive number
    try:
        noc = int(input("Insert number of pairs of cards: ")) 
        print()
    except ValueError:
        print("You must write a number: ") 
        print()
        continue
    if noc <= 0:
        print("You must write a positive number: ")
        print()
    else:
        break

cards = []
for i in range(1,noc+1):
    cards.append(i)
cards *= 2
random.shuffle(cards)

#Generate the Dimensions of the board
lowest_sum = 4*noc

for i in range(1,2*noc):
    for j in range(1,2*noc):
        if i*j == 2*noc:
            if i+j < lowest_sum:
                row = i
                column = j
                lowest_sum = i+j

print(f"row: {row}, column: {column}")

#Generate the board with cards, and another with the card hidden 
#the idea of the board of the game, is that the players intectar with the board list type, but in the screen, for esthetic reazon, print the board string type.

board = [] 
board_hidden = []

for i in range(row):
    row_board = []
    row_board_hidden = []

    for j in range(column):
        row_board.append(cards[-1])
        row_board_hidden.append(str("*")*len(str(noc))+str(" "))

        cards.pop()

    board.append(row_board)
    board_hidden.append(row_board_hidden)

def ask_for_coordinate():
    cord = input("Enter a tuple 'a,b': ")
    cord = cord.split(",")
    a = int(cord[0])
    b = int(cord[1])

    if a > row or a <= 0 or b > column or b <= 0:
        print("Invalid coordinate, make sure both numbers are positive and equal to or less than the board dimension")
        ask_for_coordinate()
    else:
        return [a,b]

def transform(board): #this function transform the rows of list type into string type
    new_board = []
    
    for i in board:
        new_row_board = ""

        for j in i:
            new_row_board += str(" ")*(len(str(noc))-len(str(j))) +str(j) +str(" ")
        new_board.append(new_row_board)

    return new_board

def flip_card_and_show(l): #l parameter will be the return of ask_for_coordinate function,
    card = board[l[0]-1][l[1]-1]
    board_hidden[l[0]-1][l[1]-1] = str(card) +str(" ")

    for i in transform(board_hidden):
        print(i)

    board_hidden[l[0]-1][l[1]-1] = str("*")*len(str(noc)) #this command makes that the board state equals 
    
    

flip_card_and_show(ask_for_coordinate())
