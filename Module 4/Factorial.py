def factorial(x):
    if x == 1:
        return 1
    else:
        smaller_problem = x-1
        leftover_part = x
        smaller_result = factorial(smaller_problem)
        return leftover_part * smaller_result
print(factorial(5))