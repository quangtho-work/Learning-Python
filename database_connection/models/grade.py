class Grade :
    def __init__(self,student_id, subject_id, score, grade_id =None):
        self.grade_id = grade_id
        self.student_id = student_id
        self.subject_id = subject_id
        self.score = score

    def __str__(self):
        return f" {self.score}"