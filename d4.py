input = open('d4data.txt').read().split('\n')

out = 0

for line in input:
    a, b = line.split(",")
    x0, y0 = map(int, a.split('-'))
    x1, y1 = map(int, b.split('-'))

    
    """if x0 >= x1 and y0 <= y1:
        out += 1
    elif x1 >= x0 and y1 <= y0:
        out += 1
      ^ D1"""

    """if max(x0, x1) <= min(y0, y1):
        out += 1
      ^ D2"""
    
print(out)
