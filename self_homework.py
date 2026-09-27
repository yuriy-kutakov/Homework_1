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
            all_grades = [g for gs in lecturer.grades.values() for g in gs]
            lecturer.average_score = round(sum(all_grades) / len(all_grades), 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Сравнивать можно только студентов')
        return self.average_score < other.average_score

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_score}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_score = 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Сравнивать можно только лекторов')
        return self.average_score < other.average_score

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
            all_grades = [g for gs in student.grades.values() for g in gs]
            student.average_score = round(sum(all_grades) / len(all_grades), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


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


# --- полевые испытания ---
abashev = Student('Денис', 'Абашев', 'м')
abashev.courses_in_progress += ['Математика', 'Электроника']

kondratiev = Student('Дмитрий', 'Кондратьев', 'м')
kondratiev.courses_in_progress += ['Электроника']
kondratiev.finished_courses += ['Математика']

strapenin = Lecturer('Григорий', 'Страпенин')
strapenin.courses_attached += ['Электроника']

bautin = Lecturer('Петр', 'Баутин')
bautin.courses_attached += ['Математика']

sadov = Reviewer('Андрей', 'Садов')
sadov.courses_attached += ['Математика']

lisin = Reviewer('Валерий', 'Лисин')
lisin.courses_attached += ['Электроника']

sadov.rate_hw(abashev, 'Математика', 3)
sadov.rate_hw(abashev, 'Математика', 2)
sadov.rate_hw(abashev, 'Математика', 3)
sadov.rate_hw(kondratiev, 'Математика', 5)

lisin.rate_hw(abashev, 'Электроника', 3)
lisin.rate_hw(abashev, 'Электроника', 4)
lisin.rate_hw(abashev, 'Электроника', 5)
lisin.rate_hw(kondratiev, 'Электроника', 3)
lisin.rate_hw(kondratiev, 'Электроника', 3)
lisin.rate_hw(kondratiev, 'Электроника', 3)

abashev.rate_lecture(strapenin, 'Электроника', 7)
abashev.rate_lecture(strapenin, 'Электроника', 8)
abashev.rate_lecture(strapenin, 'Электроника', 5)
kondratiev.rate_lecture(strapenin, 'Электроника', 2)
kondratiev.rate_lecture(strapenin, 'Электроника', 1)
kondratiev.rate_lecture(strapenin, 'Электроника', 1)

abashev.rate_lecture(bautin, 'Математика', 9)
abashev.rate_lecture(bautin, 'Математика', 7)
abashev.rate_lecture(bautin, 'Математика', 6)
kondratiev.rate_lecture(bautin, 'Математика', 8)

students = [abashev, kondratiev]
lecturers = [strapenin, bautin]

print(abashev);     print()
print(kondratiev);  print()
print(bautin);      print()
print(strapenin);   print()
print(sadov);       print()
print(lisin);       print()

print("Средний балл за ДЗ по Электронике:", average_grade_hw(students, 'Электроника'))
print("Средний балл за лекции по Математике:", average_grade_lecture(lecturers, 'Математика'))
print()
print("strapenin > bautin:", strapenin > bautin)
print("kondratiev > abashev:", kondratiev > abashev)