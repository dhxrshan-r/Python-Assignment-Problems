def count_char(s,c):
     count = 0
     for char in s:
          if char == c:
               count += 1
     return count


def are_anagrams(str1,str2):
    if len(str1) != len(str2):
        return False
    count1 = 0
    count2 = 0
    for c in str1:       
          count1 = count_char(str1,c)
          count2 = count_char(str2,c)
          if count1 != count2:
               return False
    return True
print(are_anagrams("listen", "silent",))