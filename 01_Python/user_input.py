name = input("enter your name: ")
level = int(input("enter your level: "))
score = int(input("enter your score: "))

print("player:" , name)
print("level:", level)
print("score", score)

if score >= 1500:
    print("high scorer")
else:
    print("regular scorer")

if level >= 5:
    print("advanced player")
else:
    print("beginner player")

