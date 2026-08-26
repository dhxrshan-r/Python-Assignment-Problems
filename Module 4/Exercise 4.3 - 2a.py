a = 0 
for i in range(5): 
     if i > 2: 
          a += i
     elif i > 1: 
          continue 
     else:
         pass 
     a += 1 
print(a)