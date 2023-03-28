import unittest

from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.student = Student("Grigor")
        self.student_with_courses = Student("Georgi", {"python": ["practice testing"]})

    def test_constructor(self):
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Grigor", self.student.name)
        self.assertEqual({"python": ["practice testing"]}, self.student_with_courses.courses)

    def test_enroll_with_already_added(self):
        result = self.student_with_courses.enroll("python", ["new note"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student_with_courses.courses["python"], ["practice testing", "new note"])

    def test_enroll_add_course_with_notes_y_as_optional(self):
        result = self.student.enroll("python", ["note"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["python"], ["note"])

    def test_enroll_add_course_with_notes_empty_optional(self):
        result = self.student.enroll("python", ["note"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(self.student.courses["python"], ["note"])

    def test_enroll_add_empty_course(self):
        result = self.student.enroll("python", ["note"], "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(self.student.courses["python"], [])

    def test_add_notes_successful(self):
        result = self.student_with_courses.add_notes("python", "new note")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student_with_courses.courses["python"], ["practice testing", "new note"])

    def test_add_notes_error(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes("python", "new note")
        self.assertEqual(str(error.exception), "Cannot add notes. Course not found.")

    def test_leave_course_successful(self):
        result = self.student_with_courses.leave_course("python")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(self.student_with_courses.courses, {})

    def test_leave_course_error(self):
        with self.assertRaises(Exception) as error:
            self.student_with_courses.leave_course("java")
        self.assertEqual(str(error.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    unittest.main()
