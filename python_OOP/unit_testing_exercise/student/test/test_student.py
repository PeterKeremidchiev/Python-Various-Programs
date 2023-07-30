import unittest

from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Pesho")
        self.student_with_course = Student("Gosho", {"math": ["some note"]})

    def test_initializing_without_courses(self):
        self.assertEqual("Pesho", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_initializing_with_courses(self):
        self.assertEqual("Gosho", self.student_with_course.name)
        self.assertEqual({"math": ["some note"]}, self.student_with_course.courses)

    def test_enroll_course_that_it_is_in_courses(self):
        result = self.student_with_course.enroll("math", ["asd"], "yy")

        self.assertEqual({"math": ["some note", "asd"]}, self.student_with_course.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_new_course_and_adding_notes_with_Y(self):
        result = self.student.enroll("physics", ["asd"], "Y")

        self.assertEqual({"physics": ["asd"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_new_course_and_adding_notes_without_Y(self):
        result = self.student.enroll("physics", ["asd"], "")

        self.assertEqual({"physics": ["asd"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enrolling_without_notes_that_need_to_be_appended(self):
        result = self.student.enroll("physics", ["asd"], "Yyy")

        self.assertEqual({"physics": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_try_to_add_notes_in_no_existing_course_raises(self):

        with self.assertRaises(Exception) as ex:
            self.student.add_notes("test", ["asd"])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_adding_notes_to_a_existing_course(self):
        result = self.student_with_course.add_notes("math", "asd")

        self.assertEqual({"math": ["some note", "asd"]}, self.student_with_course.courses)
        self.assertEqual("Notes have been updated", result)

    def test_try_to_leave_course_that_doesnt_exists_raises(self):

        with self.assertRaises(Exception) as ex:
            self.student.leave_course("test")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_to_leave_existing_course(self):
        result = self.student_with_course.leave_course("math")

        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual("Course has been removed", result)

if __name__ == "__main__":
    unittest.main()