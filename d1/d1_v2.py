lines = open('d1data.txt').read().split('\n\n')
content = [sum(list(map(int, line.split()))) for line in lines]

print(max(content))
