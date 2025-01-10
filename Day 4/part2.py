def x_max(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "A" and ((lines[i-1][j-1] == "M" and lines[i+1][j+1] == "S") or (lines[i-1][j-1] == "S" and lines[i+1][j+1] == "M")) \
            and ((lines[i-1][j+1] == "M" and lines[i+1][j-1] == "S") or (lines[i-1][j+1] == "D" and lines[i+1][j-1] == "M")):
                return 1


def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

        print(sum(x_max))


if __name__ == "__main__":
    main()