def average_and_show_work(x, y, z):
    mid_result = x + y + z
    final_result = round(mid_result / 3, 2)
    first_str = "(" + str(x) + " + " + str(y) + " + " + str(z) + ") / 3"
    second_str = str(mid_result) + " / 3"
    final_str = str(final_result)
    print(first_str + " = " + second_str + " = " + final_str)
    return final_str
print(average_and_show_work(2, 2, 2))
