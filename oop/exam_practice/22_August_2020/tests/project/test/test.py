import unittest

from project.student_report_card import StudentReportCard


class TestStudentReportCard(unittest.TestCase):

    def setUp(self) -> None:
        self.card = StudentReportCard("Ivan", 12)

    def test_constructor(self):
        self.assertEqual(self.card.student_name, "Ivan")
        self.assertEqual(self.card.school_year, 12)
        self.assertEqual(self.card.grades_by_subject, {})

    def test_with_year_one(self):
        self.card.school_year = 1
        self.assertEqual(self.card.school_year, 1)

    def test_student_name_error(self):
        with self.assertRaises(ValueError) as error:
            self.card.student_name = ""
        self.assertEqual(str(error.exception), "Student Name cannot be an empty string!")

    def test_school_year_error_more_than_12(self):
        with self.assertRaises(ValueError) as error:
            self.card.school_year = 16
        self.assertEqual(str(error.exception), "School Year must be between 1 and 12!")

    def test_school_year_error_less_than_1(self):
        with self.assertRaises(ValueError) as error:
            self.card.school_year = 0
        self.assertEqual(str(error.exception), "School Year must be between 1 and 12!")

    def test_add_grade_with_already_existing_subject(self):
        self.card.grades_by_subject = {"biology": [5], "english": [5, 5, 6]}
        self.card.add_grade("biology", 6)
        self.assertEqual(self.card.grades_by_subject, {"biology": [5, 6], "english": [5, 5, 6]})

    def test_add_grade(self):
        self.card.add_grade("biology", 5)
        self.card.add_grade("english", 6)
        self.assertEqual(self.card.grades_by_subject["biology"], [5])
        self.assertEqual(self.card.grades_by_subject, {"biology": [5], "english": [6]})
        self.card.add_grade("biology", 6)
        self.assertEqual(self.card.grades_by_subject["biology"], [5, 6])

    def test_average_grade_by_subject(self):
        self.card.grades_by_subject = {"biology": [6, 6, 6], "english": [5, 6]}
        result = self.card.average_grade_by_subject()
        expected = f"biology: 6.00\n" \
                   f"english: 5.50"
        self.assertEqual(result, expected)

    def test_grade_for_all_subjects(self):
        self.card.grades_by_subject = {"biology": [6, 6, 6], "english": [5, 6]}
        result = self.card.average_grade_for_all_subjects()
        self.assertEqual(result, f"Average Grade: 5.80")

    def test_repr(self):
        self.card.grades_by_subject = {"biology": [6, 6, 6], "english": [5, 6]}
        expected = f"Name: Ivan\n" \
                   f"Year: 12\n" \
                   f"----------\n" \
                   f"biology: 6.00\nenglish: 5.50\n" \
                   f"----------\n" \
                   f"Average Grade: 5.80"
        self.assertEqual(self.card.__repr__(), expected)


if __name__ == '__main__':
    unittest.main()
