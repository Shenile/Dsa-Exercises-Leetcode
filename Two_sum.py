def twoSum(nums, target):
    num_index_map = {}
    
    for i, value in enumerate(nums):
        compliment = target - value
        if compliment in num_index_map:
            return [num_index_map[compliment][0], i]
        else:
            num_index_map[value] = [i]

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
