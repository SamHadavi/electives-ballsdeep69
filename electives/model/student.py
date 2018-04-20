

class Student:
    def __init__(self ,student_number='student_number', name='name', level='level'):
        self._student_number = student_number
        self._name = name
        self._level = level
        self.electives = []

    @property
    def student_number(self):
        return self._student_number

    @student_number.setter
    def student_number(self, student_number):
        self._student_number = student_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    def add_elective(self, crn):
        #check if right level
        self.electives.append(crn)

    def remove_elective(self, crn):
        self.electives.remove(crn)
