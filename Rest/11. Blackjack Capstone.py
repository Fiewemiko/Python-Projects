import random
cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

player_hand = []
computer_hand = []

blackjack = True

# sum of cards
def sum_cards(hand):
    sum_player = 0
    for card in hand:
        if card == 'J' or card =='Q' or card =='K':
            sum_player += 10
        elif card == 'A':
            if sum_player <= 11:
                sum_player += 10
            else:
                sum_player += 1
        else:
            sum_player += card
    return sum_player


def game():

    # First two cards
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))

    # computer card
    computer_hand.append(random.choice(cards))

    print("Welcome in the blackjack game! ")
    print(f"Your hand is {player_hand}. Kasyno hand is {computer_hand}")
    hit_or_stand = input("What would you like to do? Type 'hit' to hit or type 'stand' to stand: ").lower()
    if hit_or_stand == 'hit':
        player_hand.append(random.choice(cards))

    if sum_cards(player_hand) > 21:
        print(f"Your hand is {player_hand} with a sum of {sum_cards(player_hand)}. You lose...")
        return blackjack == False

    print(f"Your hand is {player_hand}. \nNow it's casyno move...")
    while sum_cards(computer_hand) <= 17:
        computer_hand.append(random.choice(cards))
        print(f"Casyno get {computer_hand[-1]}. The Casyno hand is {computer_hand}. ")

    if sum_cards(computer_hand) >  21 or sum_cards(player_hand) > sum_cards(computer_hand):
        print("Casyno lose, go get your money $$$")
    else:
        print("You lose...")



while blackjack:
        game()
        y_n = input("Would you like to play again? type 'y' or 'n': ").lower()
        if y_n == 'n':

            print("Good bye! ")
            break
        else:
            player_hand = []
            computer_hand = []
            print("Let's goo!!")

