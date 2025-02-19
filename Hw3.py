class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        self.attendance = 0

    def mark_attendance(self):
        self.attendance += 1

    def get_attendance(self):
        return self.attendance

    def display_info(self):
        print(f"Student Name: {self.name}, ID: {self.student_id}, GPA: {self.gpa}")


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to {self.course_name}.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student.name} has been removed from {self.course_name}.")
                return
        print(f"Student with ID {student_id} not found in {self.course_name}.")

    def list_students(self):
        print(f"Students enrolled in {self.course_name}:")
        for student in self.students:
            student.display_info()
