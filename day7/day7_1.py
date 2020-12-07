from sys import stdin
def gold(dic, x):
    if x not in dic:
        return False
    if 'shiny gold' in dic[x]:
        return True
    for value in dic[x]:
        if gold(dic, value):
            return True
    return False
data = [line[:-1].split(' contain ') for line in stdin]
bags = dict()
canhold = set()
for line in data:
    key = line[0].split(' bag')[0]
    s = line[1][:-1].split(', ')
    if s[0] == 'no other bags':
        continue
    bags[key] = [bag.partition(' ')[2].split(' bag')[0] for bag in s]
for k in bags:
    if gold(bags, k):
        canhold.add(k)
print(bags)
print(len(canhold))
