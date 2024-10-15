def divisibility_quest(list: [int], limit: int, divisor: int) -> int:
    result = set()
    for i in range(len(list)):
        curr_sublist = []
        for j in range(i, len(list)):
            if list[j] % divisor != 0:
                break
            if len(curr_sublist) < limit:
                curr_sublist.append(list[j])
            if curr_sublist != []:
                result.add(tuple(curr_sublist))
    return result


# list = [6, 9, 9, 6, 6]
# # ANS: [6] [6, 9] [6, 9, 9] [9] [9, 9] [9, 9, 6] [9, 6] [9, 6, 6] [6, 6]
# limit = 3
# divisor = 3
# print(divisibility_quest(list, limit, divisor))

# list = [5, 10, 15, 20]
# # ANS: [5], [5, 10], [5, 10, 15], [5, 10, 15, 20], [10], [10, 15], [10, 15, 20], [15], [15, 20], [20]
# limit = 4
# divisor = 5
# print(divisibility_quest(list, limit, divisor))

list = [2, 3, 3, 2, 2]
limit = 2
divisor = 2
print(divisibility_quest(list, limit, divisor))