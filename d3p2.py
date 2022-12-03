from string import ascii_lowercase, ascii_uppercase

input = open('d3data.txt').read().split('\n')


currentdata = [] 
pri = 0

group = range(0,len(input),3)

for num, line in enumerate(input):
  if num in group:
    
    dupes = set(input[num]).intersection(set(input[num+1])).intersection(set(input[num+2]))

    for x in dupes:
      if x in ascii_lowercase:
        pri += ascii_lowercase.index(x) + 1
      else:
        pri += ascii_uppercase.index(x)+27
    
print(pri)
