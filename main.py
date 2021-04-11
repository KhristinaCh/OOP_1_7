list_of_students = {}
list_of_lecturers = {}


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.list_of_all_grades = []

    def add_course(self, course):
        self.courses_in_progress.append(course)
        if course in list_of_students:
            list_of_students[course] += [self]
        else:
            list_of_students[course] = [self]

    def finish_course(self, course):
        self.finished_courses.append(course)
        self.courses_in_progress.remove(course)
        if course in list_of_students:
            list_of_students[course].remove(self)
        else:
            'Ошибка'

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            lecturer.list_of_all_grades.append(grade)
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        total = 0
        for grade in self.list_of_all_grades:
            total += grade
        return total / len(self.list_of_all_grades)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() > other.avg_rate()
        else:
            return 'Сравнение невозможно'

    def avg_rate_per_course(self, course_calc):
        total = 0
        if course_calc in self.grades:
            for grade in self.grades[course_calc]:
                total += grade
        return total / len(self.grades[course_calc])

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_rate()}\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.list_of_all_grades = []

    def avg_rate(self):
        total = 0
        for grade in self.list_of_all_grades:
            total += grade
        return total / len(self.list_of_all_grades)

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() > other.avg_rate()
        else:
            return 'Сравнение невозможно'

    def avg_rate_per_course(self, course_calc):
        total = 0
        if course_calc in self.grades:
            for grade in self.grades[course_calc]:
                total += grade
        return total / len(self.grades[course_calc])

    def add_course(self, course):
        self.courses_attached.append(course)
        if course in list_of_lecturers:
            list_of_lecturers[course] += [self]
        else:
            list_of_lecturers[course] = [self]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}\n'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.list_of_all_grades.append(grade)
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_course(self, course):
        self.courses_attached.append(course)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


def avg_rate_per_student(course_calc):
    students_list = list_of_students[course_calc]
    total = 0
    for student in students_list:
       total += student.avg_rate_per_course(course_calc)
    return total / len(students_list)


def avg_rate_per_lecturer(course_calc):
    lecturers_list = list_of_lecturers[course_calc]
    total = 0
    for lecturer in lecturers_list:
        total += lecturer.avg_rate_per_course(course_calc)
    return total / len(lecturers_list)


some_reviewer = Reviewer('Adam', 'Adams')
some_reviewer.add_course('Python')

another_reviewer = Reviewer('Will', 'Willis')
another_reviewer.add_course('Git')

some_lecturer = Lecturer('Ben', 'Bens')
some_lecturer.add_course('Python')

another_lecturer = Lecturer('John', 'Johns')
another_lecturer.add_course('Git')
another_lecturer.add_course('Введение в программирование')

some_student = Student('Ruoy', 'Eman', 'm')
some_student.add_course('Python')
some_student.add_course('Git')
some_student.add_course('Введение в программирование')
some_student.finish_course('Введение в программирование')

another_student = Student('John', 'Smith', 'm')
another_student.add_course('Python')
another_student.add_course('Введение в программирование')

some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(some_lecturer, 'Python', 5)
some_student.rate_hw(another_lecturer, 'Git', 9)
some_student.rate_hw(another_lecturer, 'Git', 3)
some_student.rate_hw(another_lecturer, 'Git', 10)
another_student.rate_hw(another_lecturer, 'Введение в программирование', 5)
another_student.rate_hw(another_lecturer, 'Введение в программирование', 9)
some_student.rate_hw(another_lecturer, 'Git', 7)

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 1)
another_reviewer.rate_hw(some_student, 'Git', 8)
another_reviewer.rate_hw(some_student, 'Git', 6)
some_reviewer.rate_hw(another_student, 'Python', 4)
some_reviewer.rate_hw(another_student, 'Python', 10)

# print(some_student.__dict__)
# print(another_student.__dict__)
# print(some_lecturer.__dict__)
# print(another_lecturer.__dict__)
print(some_reviewer)
# print(another_reviewer)
print(some_lecturer)
# print(another_lecturer)
print(some_student)
# print(another_student)
print(some_lecturer.__lt__(another_lecturer))
print(some_student.__lt__(another_student))
print(some_student.__lt__(another_lecturer))
print(avg_rate_per_student('Git'))
print(avg_rate_per_lecturer('Python'))
print(some_student.avg_rate_per_course('Python'))
print(some_lecturer.avg_rate_per_course('Python'))