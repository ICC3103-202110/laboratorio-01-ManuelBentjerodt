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

l = ""

for i in range(row):
    l = ""
    for j in range(column):
        
        l+= str(" ")*(len(str(noc))-len(str(cards[-1]))) +str(cards[-1])+str(" ")
        cards.pop()
    print(l)


