input = open('d6data.txt').read()

for i in range(len(input)):
    if len(set(input[i:i+14])) == 14:
        print(i + 14)
        exit()

#d1 = replace 14 with 4. No logic is changed.
