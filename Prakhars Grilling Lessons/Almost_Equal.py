def almost_equal(string1, string2, n) -> bool:
    if len(string1) != len(string2): 
        return False
    counter = 0
    for i in range(string2):
        if string1[i] != string2[i]:
            counter += 1
    if counter > n: 
        return False
    return True