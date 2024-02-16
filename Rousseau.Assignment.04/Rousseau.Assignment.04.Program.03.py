# Program #03:

# Design and implement an object-oriented program for a simple game of blackjack that provides for one
# player and a dealer (the computer).

# Console

# Blackjack
# DEALER'S SHOW CARD:
# 9 of Clubs
# YOUR CARDS:
# 2 of Hearts
# Queen of Clubs
# Hit or stand? (h/s): h
# YOUR CARDS:
# 2 of Hearts
# Queen of Clubs
# 7 of Clubs
# Hit or stand? (h/s): s
# DEALER'S CARDS:
# 9 of Clubs
# 7 of Spades
# Queen of Spades
# YOUR POINTS: 19
# DEALER'S POINTS: 26
# Yay! The dealer busted. You win!
# Play again? (y/n): n
# Come back soon!
# Specifications
# • Design and implement the classes for the business tier.
# • Use functions to implement the user interface tier.
# • Store the code for each tier in its own file.
# • If necessary, learn the rules of Blackjack by researching it on the web.
# • Use a standard 52-card deck of playing cards.
# • The dealer must continue taking cards until the dealer’s hand has at least 17 points.
# • Don’t implement betting.
# • Don’t allow a player to “split” a hand or “double down.” (16-1)

def blackjack():
    import cards

    deck = cards.Deck()
    
    player_hand = cards.Hand()
    dealer_hand = cards.Hand()

    dealer_hand.add_card(deck.draw_card())
    player_hand.add_card(deck.draw_card())
    player_hand.add_card(deck.draw_card())

    print("\n\n\nDealer's Show Card:")
    print(dealer_hand)
    dealer_hand.add_card(deck.draw_card())

    print("Your Cards:")
    print(player_hand)

    

    while(True):
        hit_value = input("Hit or stand? (h/s): ")

        match hit_value: 
            case "h":
                hit(player_hand, deck)
                print("\nYOUR CARDS:")
                print(player_hand)
            case "s":
                break
            case _:
                print("Invalid input")

                continue

        if(player_hand.total() > 21):
            print("You busted! Game Over\n")
            print(f"YOUR POINTS {player_hand.total()}")
            print(f"DEALER's POINTS: {dealer_hand.total()}")
            again()

    dealer_ai(dealer_hand, deck)

    print("\nDealer's Cards")
    print(dealer_hand)

    if(dealer_hand.total() > 21):
        print("The Dealer Busted! You win!")
    elif(player_hand.total() > dealer_hand.total()):
        print("You win! Congrats!")
    else:
        print("The Dealer wins. Better luck next time!")

    print(f"YOUR POINTS {player_hand.total()}")
    print(f"DEALER's POINTS: {dealer_hand.total()}")

    again()

def dealer_ai(hand, deck):
    
    while(True):
        if(hand.total() > 16):
            break
        else:
            hit(hand, deck)



def hit(hand, deck):
    hand.add_card(deck.draw_card())

def again():
    while(True):
        again = str(input("Continue? (y/n): "))

        match again: 
            case "y":
                blackjack()
            case "n":
                print("Come back soon!")
                exit()
            case _:
                print("Invalid Entry")
                continue


def main():
    print("\nBlackjack")
    blackjack()

if __name__ == "__main__":
    main()