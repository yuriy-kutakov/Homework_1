def _recalc_average(obj):
    all_grades = [g for gs in obj.grades.values() for g in gs]
    obj.average_score = round(sum(all_grades) / len(all_grades), 2) if all_grades else 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_score = 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Сравнивать можно только лекторов')
        return self.average_score < other.average_score

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Сравнивать можно только лекторов')
        return self.average_score > other.average_score

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_score == other.average_score

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_score}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            _recalc_average(student)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            _recalc_average(lecturer)

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Сравнивать можно только студентов')
        return self.average_score < other.average_score

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Сравнивать можно только студентов')
        return self.average_score > other.average_score

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_score == other.average_score

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_score}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


def average_grade_hw(students, course):
    all_grades = []
    for student in students:
        if course in student.grades:
            all_grades += student.grades[course]
    return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0


def average_grade_lecture(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]
    return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0


# --- полевые испытания (ваш блок без изменений) ---
abashev = Student('Денис', 'Абашев', 'м')
abashev.courses_in_progress += ['Математика', 'Электроника']
# ... и так далее