logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''                  
print(logo)

# TODO-1: Ask the user for input



# TODO-2: Save data into dictionary {name: price}


# TODO-3: Whether if new bids need to be added
def finding_highest_bidder(bidding_dictonary):
            highest_bid=0
            winner=""
            
            max(bidding_dictonary)

            for bidder in bidding_dictonary:
                bid_amount=bidding_dictonary[bidder]
                if int(bid_amount) > int(highest_bid):
                    highest_bid=bid_amount
                    winner=bidder

            print(f"The winner of bidding is {winner} with a bidding amount of ${highest_bid}")
            





bid={}
continue_bidding= True
while continue_bidding:
    name=input("Enter your name: ")
    amount=input("Enter your bidding amount: $ ")
    move_ahead=input("Are there any more bids? Type yes or no \n").lower()
    bid[name]=amount

    if move_ahead=="no":
          continue_bidding=False
          finding_highest_bidder(bid)
    elif move_ahead=="yes":
          print("\n" * 20)


# TODO-4: Compare bids in dictionary
        
