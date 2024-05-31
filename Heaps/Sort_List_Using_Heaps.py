import heapq

input_list = [95, 75, 80, 55, 60, 50, 65]
output_list = []
        
heapq.heapify(input_list)
while len(input_list) > 0:
    output_list.append(heapq.heappop(input_list))

print(input_list)
print(output_list)



