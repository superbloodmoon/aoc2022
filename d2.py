input = open('d2data.txt').read().split('\n')

score = 0

for line in input:
  opp, you = line.split()

  if you == "X":
        if opp == "A":
            score += 3
        if opp == "B":
            score += 1
        if opp == "C":
            score += 2
        
        score += 0

  if you == "Y":
        if opp == "A":
            score += 1
        if opp == "B":
            score += 2
        if opp == "C":
            score += 3
        score += 3

  if you =="Z":
        if opp == "A":
            score += 2
        if opp == "B":
            score += 3
        if opp == "C":
            score += 1
        score += 6

print(score)
