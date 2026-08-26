def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) , 1):
        if num % i == 0:
            return False
    return True

def average_of_primes(n):
    sum = 0
    count = 0
    for num in n:
        if is_prime(num):
            sum += num
            count += 1
    if count == 0:
        return 0
    return sum / count
print(average_of_primes([2, 3, 5, 7]))