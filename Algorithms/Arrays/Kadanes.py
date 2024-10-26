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



# Q: Return the left and right index of the max subarray sum, assuming there's exactly one result (no ties).


# Sliding Window Variation of Kadane's: O(n) 
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
        L = R 

        curSum += nums[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]