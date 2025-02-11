from datetime import datetime

class CodeGradeUser:
    def __init__(self, username, institute):
        self.username = username
        self.institute = institute

    def hello(self):
        print(f"Hello {self.username} from {self.institute}!")

class Student(CodeGradeUser):
    def __init__(self, username, institute, graduation_year=None):
        super().__init__(username, institute)
        self.graduation_year = graduation_year

    def graduated(self):
        if self.graduation_year is None:
            return False
        current_year = datetime.now().year
        return self.graduation_year <= current_year

    def handin(self, assignment):
        if self.graduated():
            print(f"Sorry {self.username}, you can only hand in if you haven't graduated yet!")
        else:
            print(f"Thanks, {self.username}! Your submission {assignment} was successfully handed in!")

class Teacher(CodeGradeUser):
    def teach(self):
        return "Python is named after the British comedy troupe Monty Python."

    def grade(self, student, grade):
        if self.institute == student.institute:
            print(f"Teacher {self.username} graded {student.username} with grade {grade}.")
        else:
            print(f"You cannot grade {student.username} as they are from another institute.")

if __name__ == "__main__":
    user = CodeGradeUser("John", "Code University")
    user.hello()

    devin = Student("Devin", "University of Amsterdam", 2018)
    devin.handin("Python Assignment")

    robin = Teacher("Robin", "Code University")
    print(robin.teach())
    robin.grade(devin, 90)

    peter = Student("Peter", "Code University")
    robin.grade(peter, 85)
