def foo(x, y):
    x *= 2
    y += x
    z = x + y
    return z 
a = 5 
b = foo(a, a-2) // 2 
print(a,b)