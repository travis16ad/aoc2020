num_list = []
nums = set()
while True:
    try:
        n = int(input())
    except EOFError:
        break
    num_list.append(n)
    nums.add(n)
two_sums = set()
for i,x in enumerate(num_list):
    for j,y in enumerate(num_list):
        if i == j:
            continue
        if 2020 - (x + y) in nums:
            print(x * y * (2020 - (x+y)))
            break
        two_sums.add(i+j)
