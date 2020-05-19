#!/usr/bin/python3
class User:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
user = User("seif", "16061995")
print(user.name)
print(user.birthday)
user1 = User("mohamed", "565974")
print(user1.name)
print(user1.birthday)
help(User)
