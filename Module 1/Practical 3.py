def find_root(a, b, c):
    square_root = (b**2 - 4*a*c)**0.5
    return (-b + square_root) / (2*a)
print(find_root(1, -2, 1))