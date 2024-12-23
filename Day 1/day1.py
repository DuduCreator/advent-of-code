right = []
left = []
res = 0

with open("input.txt", "r") as file:
    for line in file:
        l, r = line.split("    ")
        l = int(l)
        r = int(r)
        left.append(l)
        right.append(r)

left = left.sort()
right = right.sort()

for i in range(len(left)):
    res += abs(left[i] - right[i])

print(res)
