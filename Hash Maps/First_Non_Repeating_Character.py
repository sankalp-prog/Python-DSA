from collections import Counter

# Couldn't think of the answer so looked at the solution - 
def first_non_repeating_char(string):
    counts = Counter(string)
    for char in string:
        if counts[char] == 1:
            return char
    return None
    


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )

print( first_non_repeating_char('leetcodel'))

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""

