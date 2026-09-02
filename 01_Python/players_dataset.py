players = [
    {
        "name": "alex",
        "level": 4,
        "score": 1200,
        "hours_played": 40,
        "deaths": 2
    },
    {
        "name": "sam",
        "level": 6,
        "score": 1800,
        "hours_played": 20,
        "deaths": 4
    },
    {
        "name": "lisa",
        "level": 3,
        "score": 100,
        "hours_played": 87,
        "deaths": 4
    },
    {
        "name": "jean",
        "level": 8,
        "score": 1400,
        "hours_played": 35,
        "deaths": 5
    },
    {
        "name": "bobby",
        "level": 2,
        "score": 800,
        "hours_played": 10,
        "deaths": 2
    }
]

print(players)
print("first player's neame:", players[0]["name"])
print("third player's score:", players[2]["score"])

for name in players:
   print("every player's name:", name["name"])

for item in players:
    print("name and score:", item["name"], item["score"])


def add_score(players):
   total_score = 0
   for player in players:
      total_score += player["score"]
      return total_score

total_score = add_score(players)
print("total score:", total_score)

def avg_score(players):
   average = total_score / len(players)

average = avg_score(players)
print("average score:", average)

