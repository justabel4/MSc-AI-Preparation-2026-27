players = [
    {
        "name": "alex",
        "level": 5,
        "score": 200,
        "hours_played": 40
    },
    {
        "name": "bob",
        "level": 3,
        "score": 1800,
        "hours_played": 80
    },
    {
        "name": "lisa",
        "level": 8,
        "score": 1600,
        "hours_played": 30
    },
    {
        "name": "mark",
        "level": 4,
        "score": 1400,
        "hours_played": 20
    },
    {
        "name": "marie",
        "level": 10,
        "score": 290,
        "hours_played": 45
    }
]

for item in players:
    print("player name and score:", item["name"], item["score"])

for score in players:
    if score["score"] >= 1500:
        print("high scorer", score["name"])
    else:
        print("regular scorer", score["name"])

def count_level_player(players):
    advanced_player=0 

    for count in players:
        if count["level"] >= len(players):
            advanced_player += 1

    return advanced_player

advanced_player = count_level_player(players)
print("advanced players:", advanced_player)
