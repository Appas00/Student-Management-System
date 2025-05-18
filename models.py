class Student:
    def __init__(self, st_id, st_name, st_marks):
        self.st_id = st_id
        self.st_name = st_name
        self.st_marks = st_marks

class StudentManagement:
    students = []

    @classmethod
    def add_student(cls, st_id, st_name, st_marks):
        for student in cls.students:
            if student.st_id == st_id:
                return False
        cls.students.append(Student(st_id, st_name, st_marks))
        return True

    @classmethod
    def get_all_students(cls):
        return cls.students

    @classmethod
    def get_student_by_id(cls, st_id):
        for student in cls.students:
            if student.st_id == st_id:
                return student
        return None

    @classmethod
    def delete_student(cls, st_id):
        student = cls.get_student_by_id(st_id)
        if student:
            cls.students.remove(student)
            return True
        return False

    @classmethod
    def update_student(cls, st_id, new_name, new_marks):
        student = cls.get_student_by_id(st_id)
        if student:
            student.st_name = new_name
            student.st_marks = new_marks
            return True
        return False
