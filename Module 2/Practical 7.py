def get_grade(grade1, grade2, grade3, grade4, grade5, curve=0):
    all_grades = grade1 + grade2 + grade3 + grade4 + grade5
    all_grades_minus_min = all_grades - min(grade1, grade2, grade3, grade4, grade5)
    average = all_grades_minus_min / 4
    print("Average grade pre-curve:", average)
    return average + curve