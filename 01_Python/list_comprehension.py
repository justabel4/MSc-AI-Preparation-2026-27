scores = [1200, -50, 1800, -20, 900, 2100]


valid_scores = [number for number in scores if number >= 0]
high_scores = [ number for number in scores if number >= 1500]
doubled_scores = [number * 2 for number in valid_scores]

print("valid scores: ", valid_scores)
print("high scores: ", high_scores)
print("doubled scores: ", doubled_scores)
