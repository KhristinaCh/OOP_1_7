class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.list_of_all_grades = []

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                lecturer.list_of_all_grades.append(grade)
            else:
                lecturer.grades[course] = [grade]
                lecturer.list_of_all_grades.append(grade)
        else:
            return 'Ошибка'

    def avg_rate(self):
        total = 0
        for grade in self.list_of_all_grades:
            total += grade
        return total / len(self.list_of_all_grades)

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

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_rate()}\n'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                student.list_of_all_grades.append(grade)
            else:
                student.grades[course] = [grade]
                student.list_of_all_grades.append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# ivan_ivanov = Student('Ivan', 'Ivanov', 'm')
# ivan_ivanov.courses_in_progress.append('Macroeconomics')
#
# alexey_alexeev = Lecturer('Alexey', 'Alexeev')
# alexey_alexeev.courses_attached.append('Macroeconomics')
#
# ivan_ivanov.rate_hw(alexey_alexeev, 'Macroeconomics', 10)
# ivan_ivanov.rate_hw(alexey_alexeev, 'Macroeconomics', 9)
#
# petr_petrov = Reviewer('Petr', 'Petrov')


some_reviewer = Reviewer('Some', 'Reviewer')
some_reviewer.courses_attached.append('Python')

another_reviewer = Reviewer('Another', 'Reviewer')
another_reviewer.courses_attached.append('Git')

some_lecturer = Lecturer('Some', 'Lecturer')
some_lecturer.courses_attached.append('Python')

another_lecturer = Lecturer('Another', 'Lecturer')
another_lecturer.courses_attached.append('Git')
another_lecturer.courses_attached.append('Введение в программирование')

some_student = Student('Ruoy', 'Eman', 'm')
some_student.courses_in_progress += ['Python','Git']
some_student.finished_courses += ['Введение в программирование']
another_student = Student('Another', 'Student', 'f')
another_student.courses_in_progress += ['Python','Введение в программирование']

some_student.rate_hw(some_lecturer, 'Python', 10)
some_student.rate_hw(another_lecturer, 'Git', 9)
another_student.rate_hw(another_lecturer, 'Введение в программирование', 5)
some_student.rate_hw(another_lecturer, 'Git', 7)
# another_student.rate_hw(another_lecturer, 'Git', 3)

some_reviewer.rate_hw(some_student, 'Python', 10)
another_reviewer.rate_hw(some_student, 'Git', 8)
# another_reviewer.rate_hw(some_student, 'Python', 6)
some_reviewer.rate_hw(another_student, 'Python', 4)
# some_reviewer.rate_hw(some_student, 'Git', 10)

# print(best_student.grades)
# print(alexey_alexeev.__dict__)
# print(petr_petrov.__dict__)
# print(alexey_alexeev.grades)
# print(some_student.__dict__)
# print(another_student.__dict__)
# print(some_lecturer.__dict__)
# print(another_lecturer.__dict__)
print(some_reviewer)
print(some_lecturer)
print(some_student)
print(some_lecturer.avg_rate() > another_lecturer.avg_rate())
print(some_student.avg_rate() > another_student.avg_rate())
