a = [1, 3, 5] 
def foo(L): 
    L = L + [12] 

foo(a) 
print(a)

b = [2, 4, 6] 
def bar(M): 
    M += [8] 
    
bar(b) 
print(b) 