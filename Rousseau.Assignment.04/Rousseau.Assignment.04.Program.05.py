# Program #05:
# Create an object-oriented program that creates a deck of cards, shuffles them, and deals
# the specified number of cards to the player.

# Console

# Card Dealer
# I have shuffled a deck of 52 cards.
# How many cards would you like?: 7
# Here are your cards:
# Jack of Hearts
# Jack of Diamonds
# 2 of Diamonds
# 6 of Spades
# Jack of Spades
# 6 of Hearts
# King of Diamonds
# There are 45 cards left in the deck.
# Good luck!
# Specifications

# • Use a Card class to store the rank and suit for each card. In addition, use a method to get a string
# representation for each card such as “Ace of Spades”, “2 of Spades”, etc.
# • Use a Deck class to store the 52 cards in a standard playing deck (one card for each rank and
# suit):
# ranks: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace
# suits: Clubs, Diamonds, Hearts, Spades
# • The Deck class should include a method that shuffles the deck, a method that counts the number
# of cards in the deck, and a method that deals a card from the deck, which should reduce the
# count of the cards in the deck by 1.
# • When the program starts, it should get a new deck of cards, shuffle them, and display a message
# that indicates the total number of cards in the deck. To shuffle the cards, you can use the shuffle
# function of the random module described in chapter 6.
# • The program should prompt the user for the desired number of cards. Then, it should deal the
# user the desired number of cards and display a message that indicates the number of cards left in
# the deck. (14-2)

def main():
    import cards
    print("Card Dealer")

    deck = cards.CardDeck()
    hand = cards.CardHand()


    print(f"\nI have a shuffled deck of {deck.count} cards")

    count = int(input("\nHow many cards would you like?: "))

    while(count > 0):
        hand.add_card(deck.draw_card())
        count = count - 1

    print("Here are your cards")
    print(hand)

    print(f"\nThere are {deck.count} cards left in the deck")
    print("\nGood luck!")



if __name__ == "__main__":
    main()