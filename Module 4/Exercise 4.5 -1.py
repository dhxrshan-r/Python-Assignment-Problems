def sequence(n):
    if (n == 0):
        return 0 
    else: 
        return sequence(n-1) + 3 
print(sequence(12))
    
sequence(3) == 9 
sequence(0) == 0 
sequence(1) == 3 
sequence(10) == 30 