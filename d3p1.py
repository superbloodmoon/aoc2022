from string import ascii_lowercase, ascii_uppercase

input = open('d3data.txt').read().split('\n')


currentdata = [] 
pri = 0

for line in input:
  first, second = line[:len(line)//2], line[len(line)//2:]
  currentdata = [first, second]

  dupes = set(first).intersection(set(second))

  for x in dupes:
    if x in ascii_lowercase:
      pri += ascii_lowercase.index(x) + 1
    else:
      pri += ascii_uppercase.index(x)+27
        
print(pri)
