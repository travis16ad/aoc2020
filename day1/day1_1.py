nums = set()
while True:
    n = int(input())
    if 2020 - n in nums:
        print(n * (2020 - n))
        break
    nums.add(n)
