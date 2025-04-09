# duplicate

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

# print(has_dup(nums))


# is Anagram

# def isAnagram(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     else:
#         for i in range(len(str1)):
#             if str1.count(str1[i]) != str2.count(str1[i]):
#                 return False
#         return True
# s = 'racecar'
# t = 'carrace'

# print(isAnagram(s, t))


def twoSum(nums, target):
    for index, num in enumerate(nums):
        leftover = target - num
        if leftover in nums[index+1:]:
            return [index, nums.index(leftover, index+1)]

nums=[1,3,4,2]
target = 6

print(twoSum(nums, target))