def random_gcd():
    import random, math
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print("x y:", x, y)
    result = math.gcd(x, y)
    return result
print(random_gcd())