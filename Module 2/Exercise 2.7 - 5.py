n = 6 
b = (n % 2 == 0) 
if b == True:
   n //= 2 
if n % 2 == 0:
   n += 1 
else:
   n -= 1
print(n)