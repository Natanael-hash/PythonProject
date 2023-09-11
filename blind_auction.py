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

blind_dictionary = {} 

def find_highest_bidder(bidding_record):
    highest_bidder = 0
    for biddder in bidding_record:
        bid_amount = bidding_record[biddder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = biddder
    print(f"The winner is {winner} with a bid of ${bid_amount}!")

while True:
    player_name = input(" What is your name? ")
    bid = int(input("What is your bid? $"))

    blind_dictionary[player_name] = bid
    
    biders = input("Are there any other biders? Type 'yes' or 'no' ")
    if biders == 'yes':
        continue
        
    else:
        find_highest_bidder(blind_dictionary)
        print("See you at the next time!")
        break
    
