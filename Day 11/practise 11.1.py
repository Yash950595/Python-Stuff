import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

user_cards = []
computer_cards = []

for _ in range(2):
    new_card=deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)




