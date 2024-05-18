# My Solution:
def item_in_common(list1, list2):
    my_set = set()
    my_set.update(list1 + list2)
    if len(my_set) != len(list1) + len(list2):
        return True
    return False

# Course Solution: The requirements mentioned using a dictionary so my solution is not ideal
# def item_in_common(list1, list2):
#     my_dict = {}
#     for i in list1:
#         my_dict[i] = True
 
#     for j in list2:
#         if j in my_dict:
#             return True
 
#     return False

list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""