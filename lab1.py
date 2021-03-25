#ctrl k c 
#ctrl k u

import random

#Generate cards
while True: #user have to write a positive number
    try:
        print()
        print("WELCOME TO ¿M?E¿M?O¿R¿I?C¿E? This program support up to 1000 cards")
        print()
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

repeated_cord = [] #this list appends the coordinates in move (2 times player flipping a card)
repeated_val = [] #this list appends the value of the coordinate
correct_fliped = [] #this list appends the card they cant be played again


points = [0,0] #points[0] are the points of player 1, and points[1] are the points of player 2


#Generate the Dimensions of the board
lowest_sum = 4*noc

for i in range(1,2*noc):
    for j in range(1,2*noc):
        if i*j == 2*noc:
            if i+j < lowest_sum:
                row = i
                column = j
                lowest_sum = i+j

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
    
def transform(board): #this function transform the rows of list type into string type
    new_board = []
    
    for i in board:
        new_row_board = ""

        for j in i:
            new_row_board += str(" ")*(len(str(noc))-len(str(j))) +str(j) +str(" ")
        new_board.append(new_row_board)

    return new_board

def ask_for_coordinate(): #thi function asks to user the coordinate of the board staring whit 1
#11 12 13 ..
#21 22 23 ..
#31 32 33 ..
#.. .. .. ..
    cord = input("Enter a tuple 'a,b': ")
    cord_ = cord
    cord = cord.split(",")
    
    a = int(cord[0])
    b = int(cord[1])

    if cord_ in repeated_cord or cord_ in correct_fliped:
        print("Coordinite in use or unable")
        return ask_for_coordinate()

    else:

        if (a > row or a <= 0 or b > column or b <= 0):
            print("Invalid coordinate, make sure both numbers are positive and equal to or less than the board dimension")
            return ask_for_coordinate()

        else:
            repeated_cord.append(cord_)
            return [a,b]
     

def flip_card_and_show(l): #l parameter will be the return of ask_for_coordinate function
    print("____________________________________________________________")
    card = board[l[0]-1][l[1]-1]
    board_hidden[l[0]-1][l[1]-1] = str(" ")*(len(str(noc))-len(str(card))) +str(card) +str(" ")
    repeated_val.append(card)

    for i in transform(board_hidden):
        print(i)

def player_move(n):
    print("____________________________________________________________")
    print(f"Player {n}    Points: {points[n-1]}")
    print()
    print(f"There are {row} ROWS and {column} Columnes")

    n=n

    for i in transform(board_hidden):
        print(i)

    flip_card_and_show(ask_for_coordinate())
    flip_card_and_show(ask_for_coordinate()) 

    a = int(repeated_cord[0].split(",")[0])
    b = int(repeated_cord[0].split(",")[1])
    
    c = int(repeated_cord[1].split(",")[0])
    d = int(repeated_cord[1].split(",")[1]) 

    for i in range(len(repeated_cord)):
        repeated_cord.pop()
        repeated_val.pop()

    if board[a-1][b-1] == board[c-1][d-1]:
        correct_fliped.append(str(a)+str(",")+str(b))
        correct_fliped.append(str(c)+str(",")+str(d))

        board_hidden[a-1][b-1] = str(" ")*(len(str(noc))) + str(" ")
        board_hidden[c-1][d-1] = str(" ")*(len(str(noc))) + str(" ")
        
        points[n-1] += 1
        return player_move(n)
   
    elif board[a-1][b-1] != board[c-1][d-1]:
        board_hidden[a-1][b-1] = str("*")*(len(str(noc))) + str(" ")
        board_hidden[c-1][d-1] = str("*")*(len(str(noc))) + str(" ")
    

def main():
    print()
    print("The board filpped is:")
    print()
    for i in transform(board):
        print(i)

    print()

    l = [1,2]*noc**noc
    for i in l:
        player_move(i)
        print(correct_fliped)
        
main()
 
