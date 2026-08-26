def recursive_match(lst1, lst2):
    if lst1 == [] or lst2 == []:
        return 0
    else:
        left_over_string_lst1 = lst1[0] 
        left_over_string_lst2 = lst2[0]
        partial_value = recursive_match(lst1[1:],lst2[1:])
        if left_over_string_lst1 == left_over_string_lst2:
            return partial_value + 1
        else:
            return partial_value
print(recursive_match([4, 2, 1, 6], [4, 3, 7, 6]))