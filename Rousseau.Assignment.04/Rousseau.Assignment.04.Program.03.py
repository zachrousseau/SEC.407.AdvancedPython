def main():
    import cards

    deck = cards.CardDeck()
    playerHand = cards.CardHand()

    playerHand.add_card(deck.draw_card())
    playerHand.add_card(deck.draw_card())


    print(playerHand)

if __name__ == "__main__":
    main()