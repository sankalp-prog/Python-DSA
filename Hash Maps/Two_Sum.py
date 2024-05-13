# # My solution: Didn't think of any solution to use dictionaries or sets
# def two_sum(nums, target):
#     index_list = []
#     for num in nums:
#         # added condition to give just the first possibility and not all
#         if len(index_list) < 2:
#             if target - num in nums:
#                 # to remove duplicates and repetitions
#                 if num != target - num and nums.index(num) < nums.index(target - num):
#                     index_list.append(nums.index(num))
#                     index_list.append(nums.index(target - num))
#     return index_list
    
# Course Solution:
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
    
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


