import random

#Generate cards
noc = int(input("Insert number of cards: ")) #noc = number of cards
cards = []
for i in range(1,noc+1):
    cards.append(i)
cards *= 2
random.shuffle(cards)

print(cards)
