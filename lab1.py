#ctrl k c 
#ctrl k u

import random

#Generate cards
while True: #user have to write a psitive number
    try:
        noc = int(input("Insert number of pairs of cards: ")) 
        print()
    except ValueError:
        print("You must write a number ") 
        print()
        continue
    if noc <= 0:
        print("You must write a positive number ")
        print()
    else:
        break

cards = []
for i in range(1,noc+1):
    cards.append(i)
cards *= 2
random.shuffle(cards)

hidden_cards = []
for i in cards:
    hidden_cards.append("*")

#Generate Board, board as square as possible
lowest_sum = 4*noc

for i in range(1,2*noc):
    for j in range(1,2*noc):
        if i*j == 2*noc:
            if i+j < lowest_sum:
                row = i
                column = j
                lowest_sum = i+j

print(f"row: {row}, column: {column}")

#the idea of the board of the game, is that the players intectar with the board list type, but in the screen, for esthetic reazon, print the board string type.
#
row_board_string = ""  # this will be the rows who will be append in the boards (the type of the row is indicated)
row_board_list = [] 
row_board_hidden = ""

board_string = [] #this will be the board (a list that will contain all the rows)
board_list = [] 
board_hidden = []


for i in range(row):
    row_board_string = ""
    row_board_list = []
    row_board_hidden= ""
    for j in range(column):
        
        row_board_string += str(" ")*(len(str(noc))-len(str(cards[-1]))) +str(cards[-1])+str(" ")
        row_board_list.append(cards[-1])
        row_board_hidden +=  str("*")*len(str(noc))+str(" ")

        cards.pop()
    board_string.append(row_board_string)
    board_list.append(row_board_list)
    board_hidden.append(row_board_hidden)
    

for i in board_string:
    print(i)

for i in board_hidden:
    print(i)



