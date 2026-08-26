def is_linear_pattern(lst):
    if len(lst) < 2:
        return True
    diff = lst[1] - lst[0]
    for i in range(1, len(lst)-1):
        if lst[i+1] - lst[i] != diff:
            return False
    return True
print(is_linear_pattern([1, 3, 5, 7]))