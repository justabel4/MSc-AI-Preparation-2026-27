player_name = "alex"
health = 70
score = 1600
level = 5

#health condition
if health >= 70:
    print("player healthy")
elif health <= 69 and health >= 31:
    print("player is injured")
else:
    print("player is critical")

#score condtion
if score >= 1500:
    print("high score")
elif score >= 1000 and score <=1499:
    print("medium score")
else:
    print("low score")

#level condtion
if level >= 5:
    print("advanced player")
else:
    print("beginner player")