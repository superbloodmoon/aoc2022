data = open('input.txt').read().splitlines()


currentCycle = 0
x = 1
signalStrengths = []

def checkCycle(current):
  if current in (20, 60, 100, 140, 180, 220):
    signalStrengths.append(current * x)


for i in data:
  if i == "noop": currentCycle += 1; checkCycle(currentCycle)
  else:
    currentCycle += 1
    checkCycle(currentCycle)
    i = int(i.split(' ')[1])
    currentCycle += 1
    checkCycle(currentCycle)
    x += i

print(signalStrengths)
print(sum(signalStrengths))
