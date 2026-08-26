class Course:
    def __init__(self, title, semester):
        self.title = title
        self.semester = semester
        self.students = dict()
        self.tas = dict()
        self.grade_map = dict()

    def add_student(self, student):
        self.students[student.id] = student
        student.course = self

    def add_ta(self, ta):
        self.tas[ta.id] = ta
        ta.course = self

    def get_student(self, student_id):
        if student_id in self.students:
            return self.students[student_id]
        return "No student available"

    def get_ta(self, ta_id):
        if ta_id in self.tas:
            return self.tas[ta_id]
        return "No TA available"

    def add_grades(self, grades, weight, grade_type):
        self.grade_map[grade_type] = weight / 100
        lines = grades.strip().splitlines()[1:]
        for row in lines:
            student_id, grade = row.strip().split(",")
            student = self.get_student(student_id)
            if student != "No student available":
                student.grades[grade_type] = int(grade)

    def get_average_for_course(self):
        if not self.students:
            return 0

        total = 0
        for student in self.students.values():
            total += student.get_average()
        return total / len(self.students)


""" Test 4 """
def test_Course_class():
    print("Testing Course class...", end='')
    # ignore this part - just reinitializing variables
    stu1 = Student("stu1", "Stu1_First", "Stu1_Last")
    stu2 = Student("stu2", "Stu2_First", "Stu2_Last")
    stu3 = Student("stu3", "Stu3_First", "Stu3_Last")
    stu4 = Student("stu4", "Stu4_First", "Stu4_Last")

    ta1 = TA("ta1", "TA1_First", "TA1_Last")
    ta2 = TA("ta2", "TA2_First", "TA2_Last")

    ta1.add_student(stu1)
    ta1.add_student(stu2)
    ta2.add_student(stu3)
    ta2.add_student(stu4)

    # each course has students and TAs
    course = Course("Introduction to Programming", "Spring 2022")
    assert((course.title == "Introduction to Programming") and (course.semester == "Spring 2022"))

    course.add_student(stu1)
    course.add_student(stu2)
    course.add_student(stu3)
    course.add_student(stu4)
    course.add_ta(ta1)
    course.add_ta(ta2)

    assert((stu1.course == course) and (stu2.course == course) and (stu3.course == course) and (stu4.course == course))
    assert((ta1.course == course) and (ta2.course == course))

    assert(course.students == {"stu1": stu1, "stu2": stu2, "stu3": stu3, "stu4": stu4})
    assert(course.tas == {"ta1": ta1, "ta2": ta2})

    assert(course.get_student("stu1") == stu1)
    assert(course.get_student("stu5") == "No student available")
    assert(course.get_ta("ta1") == ta1)
    assert(course.get_ta("ta7") == "No TA available")

    csv_hw_grades = """
    ID,homework
    stu1,100
    stu2,90
    stu3,80
    stu4,70
    """

    csv_exam_grades = """
    ID,exam
    stu4,80
    stu3,80
    stu2,70
    stu1,70
    """

    # add_grades parses the data and records the grades to the relevant student
    course.add_grades(csv_hw_grades, 40, "homework") # the weight of hw is 40
    assert(course.grade_map == {"homework": 0.4})
    assert(stu1.grades == {"homework": 100})
    assert(stu2.grades == {"homework": 90})
    # need to weight and normalize the grades
    assert(stu1.get_average() == (100*0.4) / 0.4)
    assert(stu2.get_average() == (90*0.4) / 0.4)

    course.add_grades(csv_exam_grades, 60, "exam") # the weight of exam is 60
    assert(course.grade_map == {"homework": 0.4, "exam": 0.6})

    assert(stu3.grades == {"homework": 80, "exam": 80})
    assert(stu3.get_average() == (80*0.4 + 80*0.6)/(0.4 + 0.6))

    assert(stu4.grades == {"homework": 70, "exam": 80})
    assert(stu4.get_average() == (70*0.4 + 80*0.6)/(0.4 + 0.6))

    assert(ta1.get_average_of_students() == ((100*0.4 + 70*0.6)/(0.4 + 0.6) + (90*0.4 + 70*0.6)/(0.4 + 0.6)) / 2)
    assert(course.get_average_for_course() == (stu1.get_average() + stu2.get_average() + stu3.get_average() + stu4.get_average()) / 4)
    print("... done!")

if __name__ == '__main__':
    test_Course_class()