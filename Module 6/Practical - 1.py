def convert_string_to_numbers(s):
    s = s.lower()
    count = 0 
    for c in s:
        value = ord(c) - 96
        count += value
    return count
print(convert_string_to_numbers("ramya"))