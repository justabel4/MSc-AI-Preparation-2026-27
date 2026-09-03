scores = [1200, -50, 1800, -20, 900, 2100]

for number in scores:
    if number < 0:
        print("invalid score skipped")
        continue

    if number >= 1500:
        print("score:", number)
        print("high scorer")
    else:
        print("score:", number)
        print("regular scorer")