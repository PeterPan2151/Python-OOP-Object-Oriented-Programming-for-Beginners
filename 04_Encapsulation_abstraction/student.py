class Student:

    def __init__(self, student_id, name, age, gpa):
        self.studetn_id = student_id
        self.name = name
        self._age = age
        self. gpa = gpa


student_nora = Student('245Afs', 'Nora Nav', 15, 3.96)
# Error
print(student_nora.age)

# No error
print(student_nora._age)
