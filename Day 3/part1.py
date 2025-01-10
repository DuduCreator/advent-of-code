import re
ans = 0

with open("input.txt", "r") as f:
    file = f.read().strip()

matches = re.findall(r"mul\((\d{1,3},\d{1,3})\)", file)

for match in matches:
    a, b = map(int, match.split(","))
    ans += a * b

print(ans)