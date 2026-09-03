valid_input = True

while valid_input == True:
    try:
        score = int(input("enter 5:"))

        if score == 5:
            break
        else:
            if score < 0:
                print("score cannot be neagtive")
    except ValueError:
        print("invalid number, try again")
print("loop finished")