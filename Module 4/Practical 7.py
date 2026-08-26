def generate_inputs(n):
    if n == 0:
        return [[]]
    else:
        result = []
        partial_value = generate_inputs(n-1)
        for lst in partial_value:
            result.append(lst + [0])
            result.append(lst + [1])
        return result
print(generate_inputs(5))