valid_input = False

while valid_input == False:
    try:
        level = int(input("enter level:"))
        print("level:", level)
        valid_input = True
    except:
        print("invalid number, try again")