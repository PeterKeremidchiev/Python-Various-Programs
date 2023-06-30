from inheritance_lab.teacher_project.employee import Employee
from inheritance_lab.teacher_project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

