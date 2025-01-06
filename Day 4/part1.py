### Work in progress

import re

def check_horizontal(file):
    re.search("XMAS", file) # not done
    ...

def check_vertical(file):
    ...


def check_diagonal(file):
    ...

def main():
    with open("input.txt", "r") as f:
        file = f.read().strip().split("\n")
        ...

if __name__ == "__main__":
    main()