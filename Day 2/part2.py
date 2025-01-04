safes = 0

with open("input.txt", "r") as file:
    lines = file.read().strip().split("\n")

for line in lines:
    index = 0
    safe = True
    nums = list(map(int, line.split()))
    is_sorted = nums == sorted(nums) or nums == sorted(nums, reverse=True)

    for i in range(len(nums)-1):
        diff = abs(nums[i+1] - nums[i])
        if not 1 <= diff <= 3:
            safe = False
            index = i
            break

    if not safe:
        safe = True
        nums.remove(nums[index])
        is_sorted = nums == sorted(nums) or nums == sorted(nums, reverse=True)
        for i in range(len(nums)-1):
            diff = abs(nums[i+1] - nums[i])
            if not 1 <= diff <= 3:
                safe = False


    if safe and is_sorted:
        safes += 1

print(safes)
