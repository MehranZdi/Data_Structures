# -------- Best Solution
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for index, num in enumerate(nums):
        leftover = target - num
        if leftover in nums[index+1:]:
            return [index, nums.index(leftover, index+1)]

nums=[1,3,4,2]
target = 6

print(twoSum(nums, target))



# First Solution
# 
# def twoSum(nums: list[int], target: int) -> list[int]:
    # index = list()
    # for i in range(len(nums)):
        # diff = target - nums[i]
        # if diff in nums[i+1:]:
            # nums.remove(nums[i])
            # index.extend([i, nums.index(diff)+1])
            # return index
# 
# nums = [5, 5]
# target = 7
# print(twoSum(nums, target))
# 


# Second Solution

# def twoSum(nums: list[int], target: int) -> list[int]:
#     prevMap = {}  # val -> index
#     for i, n in enumerate(nums):
#         diff = target - n
#         if diff in prevMap:
#             return [prevMap[diff], i]
#         prevMap[n] = i


# nums = [3, 4, 5, 5]
# target = 10
# result = twoSum(nums, target)
# print(result)