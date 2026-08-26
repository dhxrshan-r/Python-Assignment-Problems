lst  = [ ['0', '1', 'a'],
         ['2', 'c', 'e'],
         ['3', '4', '5'] ]

def get_alpha_string(lst):
    result = ""
    for row in lst:
            for c in row:
                if ("a" <= c<= "z" or "A" <= c <= "Z"):
                    result += c
    return result
print(get_alpha_string(lst))