def get_valid_score():
   
    while True:
        try:
            score = int(input("enter player score: "))
            
            if score < 0 :
                print("score cannot be negative")
            else:
                return score
                
        except ValueError:
            print("invalid number, try again")
    

    

player_score = get_valid_score()

print("score:", player_score)

if player_score >= 1500 :
    print("high scorer")
else:
    print("regular scorer")