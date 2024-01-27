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
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user1 = User(100, "samagan")
user2 = User(1001, "erzhigit")

user1.follow(user2)


print(f'{user1.followers}   {user1.following}')
print(f'{user2.followers}   {user2.following}')