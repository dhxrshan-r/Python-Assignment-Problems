def longest_digit_run(s):
    current_count=0
    max_count=0
    prev=0
    
    for num in s:
        if num==prev:
            current_count+=1
        else:
            current_count=1
        if current_count>max_count:
            max_count=current_count
        prev=num
    return max_count
print (longest_digit_run("99988777"))
print (longest_digit_run("12345678"))
print (longest_digit_run("99567443"))
print (longest_digit_run("0"))
print (longest_digit_run("-99988777"))