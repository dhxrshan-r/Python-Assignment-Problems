def sum_value(First):
    total_sum = 0
    for row in First:
        for number in row:
            total_sum += number
    return total_sum
        

First = [ [ 1,2,3 ],
          [ 4,5,6 ],
          [ 7,8,9 ] ]
print(sum_value(First))