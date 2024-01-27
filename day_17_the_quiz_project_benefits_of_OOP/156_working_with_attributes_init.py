# class User:
#     pass


# user1 = User()
# user1.id = 100
# user1.username = "samagan"
# user1.followers = 0
# print()

# user2 = User()
# user2.id = 100
# user2.username = "erzhigit"
# user2.followers = 0

class User:
    def __init__(self, user_id, user_name, followers):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = followers

user1 = User(100, "samagan", 803)

print(user1.user_name)