# My Solution: Passed 6/9 test cases
# Yet to see the Solution
def longest_consecutive_sequence(nums):
    lookup_set = set()
    answer_set = set()
    for num in nums:
        before = num - 1 
        after = num + 1
        if before in lookup_set: 
            answer_set.update([before, num])
        elif after in lookup_set:
            answer_set.update([num, after])
        lookup_set.add(num)
    return len(answer_set)
        


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""