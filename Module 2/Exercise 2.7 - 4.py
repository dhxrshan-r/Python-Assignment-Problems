def value(n):
    if n % 2 == 0:
        print("Even") 
    else:
        if n >= 10:
            print("Large odd")
        else:
            print("Small odd")
    return n
print(value(13))
print(value(16))
print(value(3))