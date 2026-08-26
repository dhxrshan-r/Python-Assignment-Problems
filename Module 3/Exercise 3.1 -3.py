def total_input():
    user_input = 1
    total = 0
    while (user_input != 0):
        user_input = int(input("Enter a number:"))
        total +=user_input
    return total
print(total_input())
