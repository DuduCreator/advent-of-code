right = []
left = []
counter = {}
res1 = 0
res2 = 0

# Part 1
with open("input.txt", "r") as file:
    for line in file:
        l, r = line.split()
        l = int(l)
        r = int(r)
        left.append(l)
        right.append(r)
        counter[r] = counter[r] + 1 if r in counter else 1

left.sort()
right.sort()

for i in range(len(left)):
    res1 += abs(left[i] - right[i])

print(f"Part 1: {res1}")

# Part 2
for i in left:
    try:
        res2 += i * counter[i]
    except KeyError:
        pass 

print(f"Part 2: {res2}")
