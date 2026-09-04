name = input("enter name: ")
level = int(input("enter level "))
score = int(input("enter score "))

with open("player_report.txt", "w") as file:
    file.write(f"player name: {name} \n")
    file.write(f"level: {level} \n")
    file.write(f"score: {score} \n")

with open("player_report.txt", "r") as file:
    content = file.read()

print("player report:")
print(content)