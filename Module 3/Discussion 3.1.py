def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    guess = 1
    while count <= n:
        guess += 1
        if is_prime(guess):
            count += 1 
    return guess
print(nth_prime(3))