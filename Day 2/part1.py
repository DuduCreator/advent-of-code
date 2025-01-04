with open("input.txt", "r") as input:
    for line in input:
        nums = map(int, line.split())
        if nums == sorted(nums) or sorted(nums, reversed=True):
            for i in len(nums):
                diff = abs(nums[i + 1] - nums[i])
                safe = True
                if not 1 <= diff <= 3:
                    safe = False
        safes = 0
        if safe == True:
            safes += 1