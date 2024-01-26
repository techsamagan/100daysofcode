import random, art, game_data


print(art.logo)
def person_information(index):
    return f'{game_data.data[index]["name"]} a {game_data.data[index]["description"]}, from {game_data.data[index]["country"]}.'

def compare(a,b):
    if a > b:
        return "A"
    elif a < b:
        return "B"
    else:
        return "A", "B"

score = 0
is_game_over = False


while not is_game_over:
    a_person_index = random.randint(0, len(game_data.data)+1)
    b_person_index = random.randint(0, len(game_data.data)+1)
    print(f"\nCompare A: {person_information(a_person_index)}")
    print(art.vs)
    print(f"\nAgains B: {person_information(b_person_index)}")

    answer = input("\n\nWho has more followers? Type 'A'or 'B': ")
    if answer in compare(game_data.data[a_person_index]["follower_count"], game_data.data[b_person_index]["follower_count"]):
        
        score += 1
        print(f"\nYou're right. Your score is {score}")
    else:
        is_game_over = True
        print(f"\nLoose. Your score is {score}")
        print(score)
