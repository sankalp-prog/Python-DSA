import heapq

input_list = [95, 75, 80, 55, 60, 50, 65]
output_list = []
        
while len(input_list) > 0:
    # if I used my max_heap class then I wouldn't need to use the below line after every pop
    heapq._heapify_max(input_list)
    output_list.append(heapq.heappop(input_list))

print(input_list)
print(output_list)

"""
    EXPECTED OUTPUT:
    ----------------
    [95, 75, 80, 55, 60, 50, 65]
    [80, 75, 65, 55, 60, 50]
    [75, 60, 65, 55, 50]

"""

