nums = [43,21,5,32,52,83,67,67,55]
target = 60
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
print(two_sum(nums, target))
