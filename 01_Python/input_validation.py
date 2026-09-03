name = input("enter player name:")

try:
    level = int(input("enter level:"))
    score = int(input("enter score:"))
    print("name:", name)
    print ("level:", level)
    print ("score:", score)
    
except ValueError:
    print("please enter a number")

