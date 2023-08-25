from replit import clear
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]


def deal():
    return cards[random.randint(0, 11)]


def keep_drawing():
    decision = input("Type 'y' to get another card, 'n' to pass:\n")

    if decision == 'y':
        continue_playing(user_deck, dealer_deck)
    else:
        start_game()  

def convert_ace(hand):
    """ Function that converts an ace (11) to a 1"""
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1
        return hand

    return hand


def final_hand():
    """Function that shows final game screen before restart. """

    print(f"  Your final hand: {user_deck}, final score: {sum(user_deck)}")
    print(
        f"  Computer's final hand: {dealer_deck}, final score: {sum(dealer_deck)}"
    )
    start_game()


def show_score():
    print(f"  Your cards: {user_deck}, current score: {sum(user_deck)}")
    print(f"  Computer's first card: {dealer_deck[0]}")


def start_game():
    """Checks if user wants to play."""

    play_check = input(
        "\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")

    if play_check == 'y':
        clear()
        print(art.logo)
        start_playing()


def make_decision():
    """Function to see if user wants to draw another card. """
    decision = input("\nType 'y' to get another card, 'n' to pass: ")
    print("\n")

    if decision == 'y':
        continue_playing(user_deck, dealer_deck)
    else:
        dealer_draw(user_deck, dealer_deck)


def determine_winner():
    """Function to see who wins. """
    if sum(dealer_deck) < sum(user_deck):
        print("You win.")
        final_hand()

    elif sum(dealer_deck) > sum(user_deck):
        print("You lose.")
        final_hand()

    else:
        print("Push")
        final_hand()


def start_playing():
    """Initializes the deck. """

    global user_deck, dealer_deck
    user_deck = []
    dealer_deck = []
    for i in range(2):
        user_deck.append(deal())
        dealer_deck.append(deal())

    if sum(user_deck) > 21:
        user_deck = convert_ace(user_deck)

    if sum(dealer_deck) > 21:
        dealer_deck = convert_ace(dealer_deck)

    show_score()

    if sum(user_deck) == 21 or sum(dealer_deck) == 21:

        if sum(user_deck) == 21 and sum(dealer_deck) == 21:
            print('Push.')

        elif sum(user_deck) == 21:
            print('Blackjack. You win!')

        elif sum(dealer_deck) == 21:
            print('Blackjack. The dealer wins!')

        final_hand()

    make_decision()


def continue_playing(user_deck, dealer_deck):
    """Function for when the user continues drawing after receiving the initial deck"""

    user_deck.append(deal())

    if sum(convert_ace(user_deck)) > 21:
        print("You busted. You lose :(")
        final_hand()

    else:
        user_deck = convert_ace(user_deck)
        show_score()
        make_decision()


def dealer_draw(user_deck, dealer_deck):
    while sum(convert_ace(dealer_deck)) < 17:
        dealer_deck.append(deal())
        dealer_deck = convert_ace(dealer_deck)

    if sum(convert_ace(dealer_deck)) > 21:
        print("The dealer busted. You win.")
        final_hand()

    else:
        determine_winner()


start_game()