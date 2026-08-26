def sequence(n):
    if (n==0):
        return 0
    else:
        return sequence(n-1) + 3 
print(sequence(10))