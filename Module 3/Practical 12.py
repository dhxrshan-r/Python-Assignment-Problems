def longest_bit_run(s):
    if len(s) == 0:
        return 0
    
    current_count=0
    max_count=0
    prev=-1
    
    for bit in s:
        if bit==prev:
            current_count+=1
        else:
            current_count=1
        if current_count>max_count:
            max_count=current_count
        prev=bit
    return max_count
print (longest_bit_run("11000111101010111"))