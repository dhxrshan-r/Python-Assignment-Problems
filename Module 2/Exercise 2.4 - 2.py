def second():
    x = "my name is "
    return x 
def first(name):
    return second() + name 
name = "Greg" 
print("Hello,", first(name))