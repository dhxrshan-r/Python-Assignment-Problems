def sum_from_m_to_n(m, n):
   if (m == n):
     return n
   else:
      smaller_value = m + 1
      partial_value = sum_from_m_to_n(smaller_value, n)
      result = m + partial_value
      return result
print(sum_from_m_to_n(2,5))