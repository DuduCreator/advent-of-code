import re
ans = 0

with open("input.txt", "r") as f:
    file = f.read().strip()

matches = re.findall(r"((?:don't\(\))|(?:do\(\))).*?mul\((\d{1,3},\d{1,3})\)|mul\((\d{1,3},\d{1,3})\)", file)

enabled = True
for match in matches:
    if match[0]:
        enabled = True if match[0] == "do()" else False

    if enabled:
        try:
            a, b = map(int, match[1].split(","))
        except:
            a, b = map(int, match[2].split(","))
        ans += a * b

print(ans)