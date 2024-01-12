class Car: 
    def __init__(self, seats):
        self.seats = seats


my_car = Car(5)   # initialize a car object with seats of 5 

class User:
    def __init__(self,user_id, username):
        print("Construct a new object ..")
        self.id = user_id
        self.username = username
        self.follower = 0 


user_1 = User("001", "Angela")

user_2 = User("002", "Tao Wu")

print(user_1)
print(user_1.id)
print(user_2.id)
print(user_2.follower)


