csv = '''
Student 1,50,60,70,80
Student 2,100,100,100,100
Student 3,0,10,20,30
Student 4,100,90,80,70
'''
s = "Student 1,50,60,70,80"

def row_to_list(row):
    L = row.split(",")
    for i in range(1,len(L)):
        if L[i].isdigit():
            L[i] = int(L[i])
        else:
            L[i] = 0
    return L
print(row_to_list(s))

def stu_score_avg(stu):
    scores = stu[1:]
    return sum(scores) / len(scores)

s1 = "Student 1,50,60,70,80"
s1_list = row_to_list(s1)
print(stu_score_avg(s1_list))

def csv_str_to_list(s):
    s = s.strip()
    stu_list = list()
    for row in s.splitlines():
        row_as_list = row_to_list(row)
        stu_list.append(row_as_list)
    return stu_list

stu_list = csv_str_to_list(csv)
print(stu_list)

def get_max_avg(stu_list):
    current_max_avg = 0
    for stu in stu_list:
        stu_avg = stu_score_avg(stu)
        if (stu_avg > current_max_avg):
            current_max_avg = stu_avg
    return current_max_avg

import copy

def bump_scores(stu_list, index, amount):
    stu_list_copy = copy.deepcopy(stu_list)
    for stu in stu_list_copy:
        stu[index] += amount
    return stu_list_copy

new_stu_list = bump_scores(stu_list, 1, 10)

print(stu_list)
print(new_stu_list)