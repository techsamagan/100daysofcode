import art, random

def sum_cards(cards):
    sum = 0
    for i in cards:
        sum += i
    return sum

def show_card(user_cards, computer_cards):
    print(f"Your cards are {user_cards}. You score is {sum_cards(user_cards)}")
    print(f"First computer's card is {computer_cards[0]}")

def start_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    show_card(user_cards, computer_cards)
    add = "y"
    while add == "y":
        add = input("Do you want to add card? Type 'y' or 'n'.: ")
        if add == "y":
            user_cards.append(random.choice(cards))
            show_card(user_cards, computer_cards)
        elif add == "n":
            print(f"Your cars are {user_cards}")
            print(f"Computers cards are {computer_cards}")
            if (sum_cards(user_cards) == sum_cards(computer_cards)) or (sum_cards(user_cards) >21 and sum_cards(computer_cards) > 21):
                print("Push")
           
            elif sum_cards(user_cards) > 21 or sum_cards(computer_cards) == 21:
                print("You lose.")
            elif sum_cards(computer_cards) > 21 or sum_cards(user_cards) == 21:
                print("You win.")

            elif sum_cards(user_cards) > sum_cards(computer_cards):
                print("You win.")
            elif sum_cards(user_cards) < sum_cards(computer_cards):
                print("You lose.")

    

play = "y"
while play == "y":
    play = input("Do you want to play blackjack game? Type 'y' or 'n'. : ")
    if play == "y":
        start_game()

    elif play == "n":
        print("Choose again to play")
        play = 'n'

