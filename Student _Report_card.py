class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = {}

    def get_marks(self):
        return self.__marks

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    def calculate_average(self):
        if not self.__marks:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)

    def is_passed(self):
        has_passed = all(i > 35 for i in self.__marks.values())
        if has_passed:
            return f"{self.name} has passed"
        else:
            return f"{self.name} has failed"

    def calculate_grade(self):
        percentage = self.calculate_average()
        print("Grade: ", end="")
        if percentage >= 90:
            print("A")
        elif percentage >= 80:
            print("B+")
        elif percentage >= 70:
            print("B")
        elif percentage >= 50:
            print("C")
        else:
            print("D")

class ReportCards:
    @staticmethod
    def generate(student: Student):
        print(f"\nName: {student.name}\tRoll No: {student.roll_no}")
        print("-------Marks--------")
        for subject, marks in student.get_marks().items():
            print(f"{subject} - {marks}")
        print("--------------------")
        print(f"Average: {student.calculate_average():.2f}")
        print(f"Result: {student.is_passed()}")
        student.calculate_grade()


class ClassRoom:
    def __init__(self,grade,section):
        self.grade  = grade
        self.section = section
        self.__student = []

    def add_student(self,Student):
        self.__student.append(Student)

    def calculate_class_average(self):
        if not self.__student:
            print("No student in the class")
            return
        total = sum(i.calculate_average() for i in self.__student)
        print(f"Class Average: {total / len(self.__student):.2f}")

    def get_student(self):
        print(f"\n--- Students of Grade {self.grade} Section {self.section} ---")
        for j in self.__student:
            print(f"{j.roll_no}. {j.name}")

        


def menu():
    print("\n---Student Report Card System---")
    print("1. Add Student")
    print("2. Show Report Cards")
    print("3. ClassRoom")
    print("4. Exit")




grade = int(input("Enter your grade: "))
section = input("Enter your Section: ")
c = ClassRoom(grade,section)

r = []
while True:
    menu()
    n = int(input("Enter your choice: "))
    if n == 1:
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter your Name: ")
        student = Student(roll_no, name)

        while True:
            subject = input("Enter subject name (or 'done' to finish): ")
            if subject.lower() == "done":
                break
            marks = int(input(f"Enter marks for {subject}: "))
            student.add_marks(subject, marks)

        r.append(student)
        c.add_student(student)
        print(f"✅ Student {name} added successfully.")

    elif n == 2:
        if not r:
            print("⚠️ No student added yet.")
        else:
            for k in r:
                ReportCards.generate(k)

    elif n == 3:
        c.get_student()
        c.calculate_class_average()
        
    

    elif n == 4:
        print("👋 Exiting program. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")

