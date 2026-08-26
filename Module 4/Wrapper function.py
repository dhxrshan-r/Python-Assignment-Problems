def find_min(lst):
    smallest = lst[0]
    return find_min_helper(lst[1:], smallest)

def find_min_helper(lst, smallest):
    if lst == []:
        return smallest
    else:
        smaller_list = lst[1:]
        if lst[0] < smallest:
            new_smallest = lst[0]
        else:
            new_smallest = smallest
        result = find_min_helper(smaller_list, new_smallest)
        return result


assert(find_min([5, 2, 7, 3]) == 2)
assert(find_min([1, 2, 3, 4]) == 1)
assert(find_min([13, 19, 9, 20, 15, 6, 16, 7, 5, 9]) == 5)
assert(find_min([4, 4, 4, 4, 4]) == 4)
assert(find_min([10]) == 10)