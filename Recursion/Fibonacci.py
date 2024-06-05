# sum of preceding 2 numbers -
# nth = nth-1 + nth - 2
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(4))