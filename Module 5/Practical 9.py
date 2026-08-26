csv = """University,Number of Students,Tuition
Carnegie Mellon University,13961,76760
Stanford University,16914,78218
Harvard University,22947,75891
University of California Berkeley,45057,41528"""

def row_to_lst(row):
    L = row.split(",")
    for i in range(len(L)):
        if L[i].isdigit():
            L[i] = int(L[i])
    return L

def str_to_lst(L):
    L = L.strip()
    stu_lst = []
    for row in L.splitlines():
        list = row_to_lst(row)
        stu_lst.append(list)
    return stu_lst

def get_averages_from_csv(csv_str, header):
    stu_lst = str_to_lst(csv_str)
    headers = stu_lst[0]
    data = stu_lst[1:]
    if headers[0] == header:
        return None
    if header in headers:
        i = headers.index(header)
        value = 0
        for c in data:
            value += c[i]
    else:
        return None
    return value / len(data)