name = input("enter player name:")
print("name:", name)
try:
    level = int(input("enter level:"))
    print ("level:", level)
    score = int(input("enter score:"))
    print ("score:", score)
except ValueError:
    print("please enter a number")
