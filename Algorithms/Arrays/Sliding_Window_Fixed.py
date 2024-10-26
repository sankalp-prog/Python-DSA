# Q: Given an array, return true if there are two elements within a window of size k that are equal.


# Bruteforce: O(n * k)
def bruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


test_list = [1, 2, 3, 2, 3, 3]
# test_list = [1, 2, 3, 4, 5, 6]
print(bruteForce(test_list, 3))


# Sliding Window: O(n)
def slidingWindow(nums, k):
    window = set()
    L = 0
    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False
