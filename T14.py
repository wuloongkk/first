class Student:
    def __init__(self, name, age, is_single):
        self.name = name
        self.age = age
        self.is_single = is_single
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def __str__(self):
        return f"姓名：{self.name}，平均分：{self.average_grade()}"

    def print_status(self):
        return f"姓名：{self.name}，年龄：{self.age}，单身：{self.is_single}"

student = Student("Alice", 20, True)
student.add_grade(90)
student.add_grade(85)
print(student)
print(student.print_status())