class Subject:
    def __init__(self, name, subject_id=None):
        self.subject_id = subject_id
        self.name = name
    def __str__(self):
        return f"Subject: {self.name}"