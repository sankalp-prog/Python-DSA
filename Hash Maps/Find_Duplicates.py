# My Solution:
def find_duplicates(input_list):
    my_dict = {}
    array_with_duplicates = []
    for item in input_list:
        if item in my_dict and item not in array_with_duplicates:
            array_with_duplicates.append(item)
        else:
            my_dict[item] = True
    return array_with_duplicates

# # Course Solution:
# def find_duplicates(nums):
#     num_counts = {}
#     for num in nums:
#         num_counts[num] = num_counts.get(num, 0) + 1
 
#     duplicates = []
#     for num, count in num_counts.items():
#         if count > 1:
#             duplicates.append(num)
 
#     return duplicates



print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

