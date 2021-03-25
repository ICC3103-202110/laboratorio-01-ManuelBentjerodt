#ctrl k c 
#ctrl k u

import random

print()
print("WELCOME TO ¿M?E¿M?O¿R¿I?C¿E?")

#Generate cards
while True: #user have to write a positive number
    try:
        print()
        noc = int(input("Insert number of pairs of cards: ")) 
        print()

    except ValueError:
        print()
        print("You must write a positive number: ")
        continue

    if noc <= 1:
        print("You must write a positive number: ")
        
    else:
        break

cards = []
for i in range(1,noc+1):
    cards.append(i)
cards *= 2
random.shuffle(cards)

repeated_cord = [] #this list appends the coordinates in move (2 times player flipping a card) It's temporary
repeated_val = [] #this list appends the value of the coordinate. It's temporary
correct_fliped = [] #this list appends the card they cant be played again. It's permanent

end = 0 #if end == number of pair cards, game ends

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

def ask_for_coordinate(): #this function asks to user the coordinate of the board staring whit 1
#11 12 13 ..
#21 22 23 ..
#31 32 33 ..
#.. .. .. ..
    while True: #user have to write a positive number
        try:
            print()
            cord = input(f"Enter a tuple less than or equal to '{row},{column}': ")
            cord_ = cord
            cord = cord.split(",")

            if len(cord) < 2:
                cord.append("a")
            
            a = int(cord[0])
            b = int(cord[1])

        except ValueError:
            print()
            print("Invalid coordinate, make sure both numbers are positive and equal to or less than the board dimension")
            continue
            
        else:
            break

    print()

    if cord_ in repeated_cord or cord_ in correct_fliped:  #these are the conditions that makes player cant insert a coordinate actually used,
        print("Coordinate in use or unable")               #a card actually flipped succefuy or a coordinate out of the board
        return ask_for_coordinate()

    else:

        if (a > row or a <= 0 or b > column or b <= 0):
            print("Invalid coordinate, make sure both numbers are positive and equal to or less than the board dimension")
            return ask_for_coordinate()

        else:
            repeated_cord.append(cord_)
            return [a,b]
     
def flip_card_and_show(l): #function flip a card and show the board actualiced, l parameter will be the return of ask_for_coordinate function
    print("____________________________________________________________")
    card = board[l[0]-1][l[1]-1]
    board_hidden[l[0]-1][l[1]-1] = str(" ")*(len(str(noc))-len(str(card))) +str(card) +str(" ")
    repeated_val.append(card)

    for i in transform(board_hidden):
        print(i)

def player_move(n):  #This functions makes player have to flipp card twice, 
    print("____________________________________________________________")
    print(f"Player {n}    Points: {points[n-1]}")
    print()
    print(f"There are {row} ROWS and {column} Columns")

    n=n

    for i in transform(board_hidden):
        print(i)

    flip_card_and_show(ask_for_coordinate())  #here player flipp card twice
    flip_card_and_show(ask_for_coordinate()) 

    a = int(repeated_cord[0].split(",")[0]) #this variables saves the the two coordinates user have to insert
    b = int(repeated_cord[0].split(",")[1]) 
    
    c = int(repeated_cord[1].split(",")[0])
    d = int(repeated_cord[1].split(",")[1]) 

    for i in range(len(repeated_cord)): #delete the history of cards played in a turn
        repeated_cord.pop()
        repeated_val.pop()

    if board[a-1][b-1] == board[c-1][d-1]: #here, if user flipp the 2 equals cards, remove those cards of the board and play again
        correct_fliped.append(str(a)+str(",")+str(b))
        correct_fliped.append(str(c)+str(",")+str(d))

        board_hidden[a-1][b-1] = str(" ")*(len(str(noc))) + str(" ")
        board_hidden[c-1][d-1] = str(" ")*(len(str(noc))) + str(" ")
        
        points[n-1] += 1
        global end
        end += 1
        if end == noc:
            return True
        return player_move(n)
   
    elif board[a-1][b-1] != board[c-1][d-1]: #in the other hand, if user flipp 2 differents cards, return again those cards in the board (hidden)
        board_hidden[a-1][b-1] = str("*")*(len(str(noc))) + str(" ")
        board_hidden[c-1][d-1] = str("*")*(len(str(noc))) + str(" ")
    
def main(): #this function is the base of the game, switch between players and call other fuctions.
    #this hidden part of the code shows the board with all the cards flipped,
    txt = input("Show flipped board before starting? y/n: ")

    if  txt != str("y") and txt != str("n"):
        while txt != str("y") and txt != str("n"):
            txt = input("Show flipped board before starting? y/n: ")  
            print()

    if txt == "y":
        print()                                 
        print("The board filpped is:") 
        print()
        for i in transform(board):
            print(i)
    else:
        pass
    
    l = [1,2]

    for i in l:
        player_move(i)
        if end == noc:
            print()
            if points[0] > points[1]:
                print("The game is over ¡PLAYER 1 WINS!")
                print()
                print(f"Player 1    Points: {points[0]}")
                print(f"Player 2    Points: {points[1]}")
                print()
                break
            elif points[0] < points[1]:
                print("The game is over ¡PLAYER 2 WINS!")
                print()
                print(f"Player 1    Points: {points[0]}")
                print(f"Player 2    Points: {points[1]}")
                print()
                break
            else:
                print("The game is over ¡BOTH PLAYERS ARE WINNERS!")
                print()
                print(f"Player 1    Points: {points[0]}")
                print(f"Player 2    Points: {points[1]}")
                print()
                break
        else:
            pass

        if i%2 == 0:
            l.append(1)
            
        else:
            l.append(0)
        
main() #start the game
 
