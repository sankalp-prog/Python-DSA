# Bottom Up Approach
def unique_paths(row, column):
    previous_row = [0] * 4
    
    for r in range(row-1, -1, -1):
        current_row = [0] * 4
        current_row[-1] = 1

        for c in range(column - 2, -1, -1): 
            current_row[c] = current_row[c+1] + previous_row[c]
        previous_row = current_row
    
    return previous_row[0]


print(unique_paths(4, 4))