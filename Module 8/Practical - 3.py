class CoursePerson(object):
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
class Student(CoursePerson):
    def __init__(self, id, first_name, last_name):
        super().__init__(id, first_name, last_name)
        self.ta = None
        self.course = None
        self.grades = dict()

    def get_average(self):
        if not self.grades or self.course is None:
            return 0

        weighted_total = 0
        total_weight = 0
        for grade_type, grade in self.grades.items():
            weight = self.course.grade_map.get(grade_type, 0)
            weighted_total += grade * weight
            total_weight += weight

        if total_weight == 0:
            return 0
        return weighted_total / total_weight

class TA(CoursePerson):
    def __init__(self, id, first_name, last_name):
        super().__init__(id, first_name, last_name)
        self.students = []
        self.course = None

    def add_student(self, student):
        self.students.append(student)
        student.ta = self

    def get_average_of_students(self):
        if not self.students:
            return 0
        return sum(student.get_average() for student in self.students) / len(self.students)


""" Test 3 """  
def test_CoursePerson_class():
    print("Testing Student, TA, CoursePerson classes...", end="")
    stu1 = Student("stu1", "Stu1_First", "Stu1_Last")
    stu2 = Student("stu2", "Stu2_First", "Stu2_Last")
    stu3 = Student("stu3", "Stu3_First", "Stu3_Last")
    stu4 = Student("stu4", "Stu4_First", "Stu4_Last")

    assert((stu1.id == "stu1") and (stu1.first_name == "Stu1_First") and (stu1.last_name == "Stu1_Last"))
    assert((stu2.id == "stu2") and (stu2.first_name == "Stu2_First") and (stu2.last_name == "Stu2_Last"))
    assert((stu3.id == "stu3") and (stu3.first_name == "Stu3_First") and (stu3.last_name == "Stu3_Last"))
    assert((stu4.id == "stu4") and (stu4.first_name == "Stu4_First") and (stu4.last_name == "Stu4_Last"))

    ta1 = TA("ta1", "TA1_First", "TA1_Last")
    ta2 = TA("ta2", "TA2_First", "TA2_Last")

    assert((ta1.id == "ta1") and (ta1.first_name == "TA1_First") and (ta1.last_name == "TA1_Last"))
    assert((ta2.id == "ta2") and (ta2.first_name == "TA2_First") and (ta2.last_name == "TA2_Last"))

    assert(stu1.get_full_name() == "Stu1_First Stu1_Last")
    assert(ta1.get_full_name() == "TA1_First TA1_Last")

    # Student and TA are subclasses of the class CoursePerson
    assert(isinstance(stu1, Student) and isinstance(stu1, CoursePerson))
    assert(isinstance(ta1, TA) and isinstance(ta1, CoursePerson))

    # Each student is assigned to a TA
    ta1.add_student(stu1)
    ta1.add_student(stu2)
    ta2.add_student(stu3)
    ta2.add_student(stu4)

    # These are the actual student instances, not just their ids
    assert(ta1.students == [stu1, stu2])
    assert(ta2.students == [stu3, stu4])

    assert((stu1.ta == ta1) and (stu2.ta == ta1) and (stu3.ta == ta2) and (stu4.ta == ta2))
    print("... done!")

if __name__ == '__main__':
    test_CoursePerson_class()