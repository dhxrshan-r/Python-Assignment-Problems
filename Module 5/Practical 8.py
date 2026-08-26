def duplicate_col(L, index, n):
        for row in L:
                value = row[index]
                for i in range(n):
                        row.insert(index, value)
        return L
L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(duplicate_col(L, 0, 2))