def main():
    safes = 0

    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n")

    for line in lines:
        nums = list(map(int, line.split()))
        safes += 1 if safe(nums, 1) or safe(nums[::-1], 1) else 0

    print(safes)


def safe(data, tries=0):
    print(data)

    for i in range(len(data)-1):
        diff = data[i] - data[i+1]
        if not 1 <= diff <= 3:
            return tries and any(safe(data[j-1:j] + data[j+1:]) for j in (i, i+1))
    return True

if __name__ == "__main__":
    main()
