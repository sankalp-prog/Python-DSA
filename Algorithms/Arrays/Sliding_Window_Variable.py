# Q: Find the length of the longest subarray, with the same value in each position.

# Bruteforce: O(n)
def longestSubarray(nums):
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        length = max(length, R - L + 1)
    return length

test_list = [4, 2, 2, 3, 3, 3]
print(longestSubarray(test_list))


# Q: Find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive

def minSubarray(nums, target):
    L, total = 0, 0
    length = float('inf')

    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(length, R - L + 1)
            total -= nums[L]
            L += 1
    return 0 if length == float('inf') else length


test_list = [2, 3, 1, 2, 4, 3]
print(minSubarray(test_list, 6))
