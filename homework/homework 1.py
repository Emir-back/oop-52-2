
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marriage_status = "Married" if self.is_married else "Not Married"
        print(f"Name: {self.full_name}, Age: {self.age}, Marital Status: {marriage_status}")

class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_grade(self):
        if self.marks:
            return sum(self.marks.values()) / len(self.marks)
        return 0

    def introduce_myself(self):
        super().introduce_myself()
        print("Marks: ")
        for subject, grade in self.marks.items():
            print(f"  {subject}: {grade}")
        print(f"Average Grade: {self.average_grade()}")

class Teacher(Person):
    base_salary = 30000

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience
    def calculate_salary(self):
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * Teacher.base_salary
            total_salary = Teacher.base_salary + bonus
        else:
            total_salary = Teacher.base_salary
        return total_salary

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Experience: {self.experience} years")
        print(f"Salary: {self.calculate_salary()}")

def create_students():
    students = [
        Student("Alia", 16, False, {"Math": 5, "English": 4, "Physics": 5}),
        Student("Danya", 17, False, {"Math": 4, "English": 3, "Biology": 4}),
        Student("Doni", 16, False, {"Math": 5, "History": 4, "Chemistry": 5}),
    ]
    return students


teacher = Teacher("Anna", 40, True, 7)
teacher.introduce_myself()

students = create_students()

for student in students:
    student.introduce_myself()