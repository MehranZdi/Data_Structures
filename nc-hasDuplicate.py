class Solution:
    def hasDuplicate(self, nums) -> bool:
        for item in nums:
            if nums.count(item) > 1:
                return True
        return False

### ----------Best Solution
# def hasDuplicate(self, nums) -> bool:
#     return len(set(nums) < len(nums))


## ------------First solution

# nums = [1, 2, 3, 4]
# instance = Solution()
# print(instance.hasDuplicate(nums))
# print(instance.hasDuplicate(nums))
# nums.count()
# hash = dict()
# for item in nums:
#     count = 0
#     if hash[item]:
#         count += 1
#         hash[item] = count
#     else:
#         has



## ------------- Second Solution

# from collections import defaultdict

# dup = defaultdict()

# nums = [1, 2, 3, 3]

# def has_dup(nums):
#     for i in range(len(nums)):
#         if nums[i] not in dup.keys():
#             dup[nums[i]] = 1
#         else:
#             return True
#     return False


