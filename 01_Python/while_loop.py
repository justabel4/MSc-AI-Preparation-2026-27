player_health = 100
enemy_damage = 20

while player_health > 0:
    print("health:", player_health)
    player_health -= enemy_damage 

    if player_health == 0:
        print("player defeated")