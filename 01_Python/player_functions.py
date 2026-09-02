player_name = "Alex"
health = 100
score = 2400
current_xp = 320
xp_required = 1000
point_earned = 129

def show_player():
    print("player name:", player_name, "health:", health, "score:", score)



def add_score(current_score, point_earned):
    new_score = current_score + point_earned
    return new_score

def calculate_xp_needed(current_xp, xp_required):
    xp_remain = xp_required - current_xp
    return xp_remain

show_player()

new_score = add_score(2400,129)
xp_remain = calculate_xp_needed(1000,320)

print("new score:", new_score)
print("xp remaining:", xp_remain)
