
""" Question 5: strip """
"""
Input: string s
Output: s with leading and trailing spaces removed
"""
def strip(s):
    start = 0
    end = len(s) - 1
    
    while start < len(s) and s[start] == " ":
        start += 1
    while end >= 0 and s[end] == " ":
        end -= 1
    return s[start:end + 1]

""" Test 5 """
def test_strip():
    print("Testing strip...", end='')
    assert(strip("Hello") == "Hello") 
    assert(strip(" Hello world ") == "Hello world") 
    assert(strip("      apple ") == "apple") 
    assert(strip("    ") == "") 
    print("... done!")

if __name__ == '__main__':
    test_strip()