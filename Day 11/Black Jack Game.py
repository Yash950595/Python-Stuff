import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def calculate_score(cards):
    if sum==21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "You Lose"
    elif user_score==0:
        return "You Win"
    elif user_score>21:
        return "You Lose"
    elif computer_score>21:
        return "Computer loses"
    else:
        if user_score > computer_score:
            return "You Win"
        else:
            return "Computer wins"



user_cards = []
computer_cards = []
is_game_over=False


for _ in range(2):
    new_card=deal_card()
    user_cards.append(new_card)
    computer_cards.append(new_card)

while not is_game_over: 
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)

    print(f"Your first two cards are[{user_cards}] and the score is {user_score}")
    print(f"First card of computer is [{computer_cards}] and the score is {computer_score}")

    if user_score==0 or computer_score==0 or new_card>21:
        is_game_over=True
    else:
        user_should_deal=input("Type y to get another card or n to stop the game: ")
        if user_should_deal=="y":
            user_cards.append(deal_card())
        else:
            is_game_over=True

while computer_score !=0 and computer_score>17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)


print(f"Your cards in hand:{user_score} and final score:{user_score}")
print(f"Computer cards:{computer_cards} and final score:{computer_score}")


print(compare(user_score,computer_score))





