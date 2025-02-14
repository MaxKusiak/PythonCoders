from family_composition.student import Student


class Participants:
    def __init__(self, list_of_students: list[Student]):
        self._list_of_students = list_of_students

    @property
    def list_of_students(self) -> list[Student]:
        return self._list_of_students

    @list_of_students.setter
    def list_of_students(self, value: list[Student]):
        if isinstance(value, list) and all(isinstance(student, Student) for student in value):
            self._list_of_students = value
        else:
            raise ValueError("list_of_students must be a list of Student objects")
