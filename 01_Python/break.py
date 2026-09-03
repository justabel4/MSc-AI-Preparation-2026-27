valid_input = True

while valid_input == True:

    try:
        score = int(input("enter score: "))

        if score < 0:
                print("score cannot be neagtive")
        else:
             print("score:", score)
             break
        
    except ValueError:
        print("invalid number, try again")

print("loop finished")