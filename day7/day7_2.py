from sys import stdin
def count(dic, x, parent):
    if x not in dic:
        print ("leaf", x, parent)
        return parent
    print(x, parent)
    total = 0
    for child in dic[x]:
        total += count(dic, child[1], parent*child[0])
    return parent + total

data = [line[:-1].split(' contain ') for line in stdin]
bags = dict()
for line in data:
    key = line[0].split(' bag')[0]
    s = line[1][:-1].split(', ')
    if s[0] == 'no other bags':
        continue
    bags[key] = [(int(bag.partition(' ')[0]), bag.partition(' ')[2].split(' bag')[0]) for bag in s]
print(count(bags, 'shiny gold', 1) - 1) #remove the shiny gold back itself with the -1
