valid = 0
while True:
    try:
        line = input().split()
    except EOFError:
        break
    first, last = [int(x) for x in line[0].split('-')]
    char = line[1][0]
    word = line[2]
    if word[first - 1] == char and word[last - 1] != char:
        valid += 1
    elif word[last - 1] == char and word[first - 1] != char:
        valid += 1
print(valid)
