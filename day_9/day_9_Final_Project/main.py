import art

print(art.logo)
print("Welcome to the aucion program!")

bidders_dict = {}

finish = False

def finding_highest_bid(dict):
    key = ""
    highest_bid = 0
    for i in dict:
        if dict[i] > highest_bid:
            highest_bid = dict[i]
            key = i
        else:
            highest_bid = 0     

    print(f"{key} has the highest bid amount of {highest_bid}.")

while not finish:
    name = str(input("What's your name? "))
    bid = int(input("What's your bid?: $"))
    bidders_dict[name] = bid
    
    quiz = input("Are there any bidders? Type 'yes' or 'no'. \n")
    if quiz == "yes":
        finish = False
    elif quiz == "no":
        finish = True


finding_highest_bid(bidders_dict)



