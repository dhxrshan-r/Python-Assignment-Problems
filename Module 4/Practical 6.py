def recursive_mirror(s):
     if s == "":
        return ""
     else:
         smaller_value = s[0]
         partial_value = recursive_mirror(s[1:])
         result = smaller_value + partial_value + s[0]
         return result
print (recursive_mirror("python"))