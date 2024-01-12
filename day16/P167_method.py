class Car: 
    def __init__(self, seats):
        self.seats = seats
    
    def enter_race_mode():
        self.seats = 2


my_car = Car(5)   # initialize a car object with seats of 5 

class User:
    def __init__(self,user_id, username):
        print("Construct a new object ..")
        self.id = user_id
        self.username = username
        self.followers = 0 
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Angela")

user_2 = User("002", "Tao Wu")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
