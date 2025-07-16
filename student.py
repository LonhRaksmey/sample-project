class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.is_on_probation = False

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def promote(self):
        self.grade += 1
        return f"{self.name} promoted to grade {self.grade}"