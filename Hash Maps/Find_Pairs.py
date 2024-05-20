def find_pairs(arr1, arr2, target):
    set2 = set(arr2)
    answer_list = []
    for num in arr1:
        if target - num in set2:
            answer_list.append((num, target-num))
    return answer_list
    




arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""