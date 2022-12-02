
fileData = open('d1data.txt', 
               'r')

largest = []
count = 0

for line in fileData:
  if line != '\n':
    count = count + int(line.strip('\n'))
      
  else:
    largest.append(count)
    count = 0


largest.sort(reverse=True)
print(largest[0])
print(largest[0] + largest[1] + largest [2])
