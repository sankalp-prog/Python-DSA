# Q: Check if an array is a palindrome

## My Solution-
# def isPalindrome(nums) -> bool:
#     R = len(nums) - 1
#     for L in range(int(len(nums) / 2)):
#         if nums[L] != nums[R]:
#             return False
#         R -= 1
#     return True


# Course Solution-
def isPalindrome(word):
    L, R = 0, len(word) - 1
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1
    return True


test_list = [1, 2, 7, 7, 2, 1]
print(isPalindrome(test_list))


# Q Given a sorted input array, return the two indices of two elements which sum up to the target value. Assume there's exactly one solution.


def solution(nums, target):
    L, R = 0, len(nums) - 1

    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            # Since the problem guarantees exactly one solution
            return [L, R]


test_list = [-1, 2, 3, 4, 8, 9]
k = 17
print(solution(test_list, k))