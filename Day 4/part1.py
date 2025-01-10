import re


def check_horizontal(lines):
    ret = 0
    for line in lines:
        if match := re.findall("XMAS", line):
            ret += len(match)
        if match := re.findall("XMAS", line[::-1]):
            ret += len(match)
    return ret


def check_vertical(lines):
    ret = 0
    for i in range(len(lines[0])):
        for j in range(len(lines)-3):
            if lines[j][i] == "X" and lines[j+1][i] == "M" and lines[j+2][i] == "A" and lines[j+3][i] == "S":
                ret += 1
            if lines[j][i] == "S" and lines[j+1][i] == "A" and lines[j+2][i] == "M" and lines[j+3][i] == "X":
                ret += 1
    return ret


def check_diagonal(lines):
    ret = 0 
    for i in range(len(lines[0])):
        for j in range(len(lines)-3):
            if i + 3 < len(lines[0]) and lines[j][i] == "X" and lines[j+1][i+1] == "M" and lines[j+2][i+2] == "A" and lines[j+3][i+3] == "S":
                ret += 1
            if i + 3 < len(lines[0]) and lines[j][i] == "S" and lines[j+1][i+1] == "A" and lines[j+2][i+2] == "M" and lines[j+3][i+3] == "X":
                ret += 1
            if i - 3 > 0 and lines[j][i] == "X" and lines[j+1][i-1] == "M" and lines[j+2][i-2] == "A" and lines[j+3][i-3] == "S":
                ret += 1
            if i - 3 > 0 and lines[j][i] == "S" and lines[j+1][i-1] == "A" and lines[j+2][i-2] == "M" and lines[j+3][i-3] == "X":
                ret += 1
    return ret


def main():
    ans = 0
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    ans = check_horizontal(lines) + check_vertical(lines) + check_diagonal(lines)
    print(ans)


if __name__ == "__main__":
    main()