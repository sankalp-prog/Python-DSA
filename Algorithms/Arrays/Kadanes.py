# Q: Find the largest non-empty subarray with the largest sum


# Bruteforce: O(n^2)
def bruteforce(nums):
    maxSum = nums[0]
    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum


# Kadane's Algorithm: O(n)
def kadanes(nums):
    # Can also initialize maxSum to float('-inf')
    maxSum = nums[0]
    curSum = 0
    for n in nums:
        # below 2 lines can be condensed to: curSum = max(curSum, 0) + n
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum


test_list = [4, -1, 2, -7, 3, 4]
print(bruteforce(test_list))
print(kadanes(test_list))
