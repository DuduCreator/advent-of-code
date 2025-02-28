import re

def main():
    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    print(lines)


if __name__ == "__main__":
    main()