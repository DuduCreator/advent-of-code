def x_max(lines):
    ret = 0
    for i in range(len(lines)-1)[1:]:
        for j in range(len(lines[0])-1)[1:]:
            if lines[i][j] == "A" and ((lines[i-1][j-1] == "M" and lines[i+1][j+1] == "S") or (lines[i-1][j-1] == "S" and lines[i+1][j+1] == "M")) \
            and ((lines[i-1][j+1] == "M" and lines[i+1][j-1] == "S") or (lines[i-1][j+1] == "S" and lines[i+1][j-1] == "M")):
                ret += 1
    return ret


def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    print(x_max(lines))


if __name__ == "__main__":
    main()