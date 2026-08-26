""" Question 9: get_averages_from_csv """
"""
Input: two strings, one representing a csv and one representing a header
Output: average of csv entries under header
        None if header does not appear in csv or if values in column are not integers
"""
csv = """University,Number of Students,Tuition
Carnegie Mellon University,13961,76760
Stanford University,16914,78218
Harvard University,22947,75891
University of California Berkeley,45057,41528"""

def row_to_list(row):
    L = row.split(",")
    for i in range(len(L)):
        if (L[i].isdigit()):
            L[i] = int(L[i])
    return L

def csv_str_to_list(s):
    s = s.strip()
    stu_list = list()
    for row in s.splitlines():#s.split("\n")
        row_as_list = row_to_list(row)
        stu_list.append(row_as_list)
    return stu_list

def get_averages_from_csv(csv_str,header):
    stu_list = csv_str_to_list(csv_str)
    headers=stu_list[0]
    data=stu_list[1:]
    if headers[0]==header:
        return None
    if header in headers:
        idx=headers.index(header)
        value=0
        for c in data:
            value+=c[idx]
    else:
        return None
    return value/len(data)

# print(get_averages_from_csv(csv,"Number of Students"))

""" Test 9 """
def test_get_averages_from_csv():
    print("Testing get_averages_from_csv...", end='')
    csv = """University,Number of Students,Tuition
Carnegie Mellon University,13961,76760
Stanford University,16914,78218
Harvard University,22947,75891
University of California Berkeley,45057,41528"""
    assert(get_averages_from_csv(csv, "Number of Students") == 24719.75)
    assert(get_averages_from_csv(csv, "University") == None)
    assert(get_averages_from_csv(csv, "Tuition") == 68099.25)
    assert(get_averages_from_csv(csv, "Undergrad Population") == None)
    print("... done!")

if __name__ == '__main__':
    test_get_averages_from_csv()