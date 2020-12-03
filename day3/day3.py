def treecount(grid, dx, dy):
    y = 0
    x = 0
    trees = 0
    while y < len(grid):
        if grid[y][x % len(grid[y])] == '#':
            trees += 1
        y += dy
        x += dx
    return trees

grid = list(list())
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break
t = 1
for pair in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    t *= treecount(grid, pair[0], pair[1])
# I accidentally wrote over part 1 to solve part 2
# print(treecount(grid, 3, 1)) should just answer for day 1
print(t)
