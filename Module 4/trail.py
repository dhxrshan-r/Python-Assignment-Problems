def sum_list(lst):
    total = 0
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            total += lst[i][j]
    return total
lst   = [ [ 1,2,3 ],
          [ 4,5,6 ],
          [ 7,8,9 ] ]
print(sum_list(lst))