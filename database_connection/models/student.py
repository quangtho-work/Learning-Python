class Student:
    def __init__(self, name, age, gender, student_id=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f"Student: id: {self.student_id} {self.name} ({self.age} years old, {self.gender})"
    