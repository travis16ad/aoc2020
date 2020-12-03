valid = 0
while True:
    try:
        line = input().split()
    except EOFError:
        break
    minimum, maximum = [int(x) for x in line[0].split('-')]
    char = line[1][0]
    word = line[2]
    t = 0
    for c in word:
        if c == char:
            t += 1
    if minimum <= t <= maximum:
        valid += 1
print(valid)
