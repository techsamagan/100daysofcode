import random
from art import logo
while input("Do you want to play guessing game? Type 'y' or 'n'. ") == "y":
    print(logo)

    print("Welcome to the Guessing game!")

    print("I'm thinking of a number between 1 and 100. ")

    difficulty = str(input("Choose the dificulty. Type 'easy' or 'hard' : "))

    if difficulty == "hard":
        attempt = 5
    else:
        attempt = 10
    number = random.randint(1, 100)

    while attempt != 0:
        if attempt < 1:
            print("You loose!.")
        else:
            print(f"You have {attempt} attempt. ")
            user_number = int(input("Guess the number between 1 and 100: "))

            if user_number == number:
                print("Win")
                guess = True
                attempt = 0 
            elif user_number > number:
                print("High")
                guess = False
                attempt -= 1
            elif user_number < number:
                print("Low")
                guess = False
                attempt -= 1