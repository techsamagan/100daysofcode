#Day 7 - Final Project - Hangman Game
import random

word_list = ["apple", "banana", "orange", "grape", "kiwi", "melon", "pear", "pineapple", "strawberry", "watermelon", "dog", "cat", "bird", "elephant", "giraffe", "lion", "tiger", "zebra", "monkey", "penguin", "sunflower", "rose", "tulip", "daisy", "lily", "orchid", "cactus", "maple", "oak", "pine", "car", "bicycle", "train", "airplane", "ship", "bus", "motorcycle", "truck", "helicopter", "subway", "book", "pen", "notebook", "pencil", "marker", "eraser", "scissors", "glue", "ruler", "calculator"]

logo = ''' 
 _                                             
| |                                            
| |    _ _     _ _  _   __ _ _ __  
| '_ \ / _ | '_ \ / _ | '_  _ \ / _ | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
hangman_pics = ['''
     +---+
        |
        |
        |
       ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
    O   |
   /|   |
         |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
           +---+
    O   |
   /|\  |
   / \  |
       ==='''
       ]
mistake = -1
word = random.choice(word_list)
#print(word)

display = ["_"] * len(word)
print(display)

complete = False

while not complete and mistake < len(hangman_pics) - 1:
    guess = str(input("Enter guess: \n"))
    found = False  
    
    for i, letter in enumerate(word):
        if letter == guess:
            display[i] = guess
            found = True
            
    if "".join(display) == word:
        complete = True
        print("Congratulations! You guessed the word.")
    elif not found:
        mistake += 1
        print(hangman_pics[mistake])
    
    print(display)
print("Game Over! You are loooooooser!!!!!")
