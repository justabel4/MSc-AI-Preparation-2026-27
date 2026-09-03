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
    
    if item["score"] >= 1500:
        print(item["name"], item["score"])
        print("high scorer")
    else:
        print(item["name"], item["score"])
        print("regular scorer")

def count_level_player(players):
    advanced_player=0 

    for count in players:
        if count["level"] >= len(players):
            advanced_player += 1

    return advanced_player

advanced_player = count_level_player(players)
print("advanced players:", advanced_player)
