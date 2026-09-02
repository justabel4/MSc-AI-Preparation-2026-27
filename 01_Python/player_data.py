player = {
    "name": "abel",
    "health": 500,
    "level": 4,
    "score": 1000,
    "inventory": ["key", "phone", "wallet", "coffee"]
}

print(player["name"])
print(player["health"])
print(player["inventory"])

for item in player["inventory"]:
    print(item)

player["inventory"].append("mug")
player["inventory"].remove("phone")

for item in player["inventory"]:
    print(item)

print(len(player["inventory"]))
