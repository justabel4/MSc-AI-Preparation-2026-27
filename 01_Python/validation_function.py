def get_valid_score():
    valid_input = False
    while valid_input == False:
        try:
            score = int(input("enter player score: "))
            if score < 0 :
                print("score cannot be negative")
            else:
                print("score:", score)
                valid_input = True
                break
        except ValueError:
            print("invalid number, try again")
    
    return score
    

player_score = get_valid_score()

if player_score >= 1500 :
    print("high scorer")
else:
    print("regular scorer")