
class Student:
    '''класс студента'''

    def __init__(self, name, last_name, sex):
        self.name = name
        self.last_name = last_name
        self.sex = sex
        self.end_courses = []  # законченный курс
        self.courses_now = []  # не законченный курс
        self.grades = {}
        self._grades_list = []

    def _avg_rate(self):
        '''вычисляем среднюю оценку за домашние задания'''

        grades_list = []
        for grades in self.grades.values():
            for grade in grades:
                grades_list.append(grade)
                if len(grades_list) == 0:
                    self.avg_rate = 0
                else:
                    self.avg_rate = sum(grades_list) / len(grades_list)
                return self.avg_rate

    def __str__(self):

        return f'Имя: {self.name}' \
               f'\nФамилия: {self.last_name}' \
               f'\nСредняя оценка за Д/З: {self._avg_rate()}' \
               f'\nКурсы в процессе обучения: {", ".join(self.courses_now)}' \
               f'\nЗавершённые курсы: {", ".join(self.end_courses)}'

    def __gt__(self, other):
        '''Метод сравнения'''

        if isinstance(other, Student):
            return self.avg_rate < other.avg_rate
        else:
            return "error"

    def lector_rate(self, lector, course, grade):
        if (isinstance(lector, Lector)
                and course in self.courses_now
                and course in lector.courses):
            if course in lector.rate_lector:
                lector.rate_lector[course] += [grade]
            else:
                lector.rate_lector[course] = [grade]
        else:
            return "error"


class Mentor:
    '''Класс Ментора'''

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.courses_attached = []  # закреплённый курс


class Lector(Mentor):
    '''Класс Лектора'''

    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.courses = []
        self.rate_lector = {}

    def _avg_rate(self):
        '''средняя оценка за лекции'''
        rates_list = []
        for rates in self.rate_lector.values():
            for rate in rates:
                rates_list.append(rate)
        if len(rates_list) == 0:
            self.avg_lector = 0
        else:
            self.avg_lector = sum(rates_list) / len(rates_list)
        return self.avg_lector


    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.last_name}" \
               f"\nСредняя оценка за лекции: {self._avg_rate()}"

    def __gt__(self, other):
        '''Метод сравнения'''
        if isinstance(other, Lector):
            return self.avg_lector < other.avg_lector
        else:
            return "error"


class Reviewer(Mentor):
    '''класс эксперты, проверяющие, домашние, задания'''

    def __init__(self, name, last_name):
        super().__init__(name, last_name)

    def __str__(self):
        return f"Имя: {self.name}" \
               f"\nФамилия: {self.last_name}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_now:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "error"


# Студенты
student1 = Student("Alex", "Efimchik", "man")
student1.courses_now = ['Stepik', 'Python', 'English']
student1.end_courses = ['SQL']

student2 = Student("Mikha", "Egorof", "man")
student2.courses_now = ['Mashin', 'Python', 'English']
student2.end_courses = ['SQL']

# Лекторы
lector1 = Lector("Vitaly", "Veselof")
lector1.courses = ['SQL', 'Python']

lector2 = Lector("Oleg", "Batka")
lector2.courses = ['English', 'Python', 'Java']

# Проверяющие Д/З
reviewer1 = Reviewer("Naruto", "Yzumaki")
reviewer1.courses_attached = ['Stepik', 'Python']
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 3)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student1, 'Stepik', 7)
reviewer1.rate_hw(student1, 'Stepik', 4)
reviewer1.rate_hw(student1, 'Stepik', 6)

reviewer2 = Reviewer("Mikhail", "Gorshenef")
reviewer2.courses_attached = ['Python', 'SQL', 'Java']

student1.lector_rate(lector1, 'Python', 7)
student1.lector_rate(lector2, 'English', 5)
student2.lector_rate(lector1, 'SQL', 3)
student2.lector_rate(lector2, 'English', 10)

print(student1, "\n")
print(student2, "\n")
print(lector1, "\n")
print(lector2, "\n")
print(reviewer1, "\n")
print(reviewer2, "\n")

print(student1 > student2)
print(lector1 > lector2)

