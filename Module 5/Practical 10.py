def list_to_csv_str(L):
    for i in range(len(L)):
        for j in range(len(L)):
           L[i][j] = str(L[i][j])
    for sep in range(len(L)):
        L[sep] = ",".join(L[sep])
    joined = "\n".join(L)
    return joined