player = {
    "name": "abel",
    "level": 4,
    "health": 100,
    "score": 500,
    "xp": 634,
    "enemies_defeated": 5
}

for item in player:
    print(player["name"])
    print(player["score"])
    player["health"] -=25
    print("health after damage", player["health"])
    player["score"] += 500
    print("new score", player["score"])
    player["weapon"] = "riffle"
    print(player["weapon"])
    print(player)

