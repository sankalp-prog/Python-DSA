# def bubble_sort(my_list):
#     for i in range(len(my_list)-1, 0, -1):
#         for j in range(i):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
#         print(my_list)
#     return my_list

def bubble_sort(my_list):
    for i in range(len(my_list)):
        for j in range(i):
            if my_list[i] < my_list[j]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
        print(my_list)
    return my_list

# print(bubble_sort([4,2,6,5,1,3]))
print(bubble_sort([5, 10,3,8,2,7,9,4,1,6]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """