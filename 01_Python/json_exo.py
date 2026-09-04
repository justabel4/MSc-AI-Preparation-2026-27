import json
player = { 
    "name": "alex",
    "level": 6,
    "score": 1800,
    "inventory": ["key", "wallet", "phone"]
    }

with open("player_data.json", "w") as file:
    json.dump(player, file)

with open("player_data.json", "r") as file:
    loaded_player = json.load(file)

print("Player:", loaded_player["name"])
print("Level:", loaded_player["level"])
print("Score:", loaded_player["score"])

for item in loaded_player["inventory"]:
    print(item)