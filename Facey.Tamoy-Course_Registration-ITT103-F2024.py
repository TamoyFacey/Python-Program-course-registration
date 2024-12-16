class Course:

    def __init__(self, course_id, name, tuition):
        self.course_id = course_id
        self.name = name
        self.tuition = tuition


class Student:

    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0.0

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            self.balance += course.tuition
            print(f"{self.name} has been enrolled in {course.name}.")
        else:
            print(f"{self.name} is already enrolled in {course.name}.")


class RegistrationSystem:

    def __init__(self):
        self.courses = []
        self.students = {}

    def add_course(self, course_id, name, tuition):
        self.courses.append(Course(course_id, name, tuition))
        print(f"Course {name} added successfully.")

    def register_student(self, student_id, name, email):
        self.students[student_id] = Student(student_id, name, email)
        print(f"Student {name} registered successfully.")

    def enroll_student(self, student_id, course_id):
        student = self.students.get(student_id)
        course = next((c for c in self.courses if c.course_id == course_id),
                      None)
        if student and course:
            student.enroll(course)
        else:
            print("Student or Course not found.")

    def check_balance(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"{student.name}'s balance is: ${student.balance:.2f}")
        else:
            print("Student not found.")

    def calculate_payment(self, student_id, amount):
        student = self.students.get(student_id)
        if student:
            if amount > student.balance:
                print("Payment exceeds the balance.")
            else:
                student.balance -= amount
                print(
                    f"Payment of ${amount:.2f} processed for {student.name}. Remaining balance: ${student.balance:.2f}"
                )
        else:
            print("Student not found.")

    def show_courses(self):
        if not self.courses:
            print("No courses available.")
            return
        print("Available Courses:")
        for course in self.courses:
            print(f"{course.course_id}: {course.name} - ${course.tuition:.2f}")

    def show_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id),
                      None)
        if not course:
            print("Course not found.")
            return
        enrolled_students = [
            s.name for s in self.students.values() if course in s.courses
        ]
        if enrolled_students:
            print(
                f"Students enrolled in {course.name}: {', '.join(enrolled_students)}"
            )
        else:
            print(f"No students enrolled in {course.name}.")


while True:
    print("\nMenu:")
    print("1. Add Course")
    print("2. Register Student")
    print("3. Enroll Student in Course")
    print("4. Check Student Balance")
    print("5. Calculate Payment")
    print("6. Show Courses")
    print("7. Show Students in Course")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        course_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        tuition = float(input("Enter Course Fee: "))
        print("course added successfully")

    elif choice == '2':
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        email = input("Enter Student Email: ")
        print("student registered successffully")

    elif choice == '3':
        student_id = input("Enter Student ID: ")
        course_id = input("Enter Course ID: ")
        print("course not found")

    elif choice == '4':
        student_id = input("Enter Student ID: ")
        print("student balance not found")

    elif choice == '5':
        student_id = input("Enter Student ID: ")
        amount = float(input("Enter payment amount: "))
        print("student not registered")

    elif choice == '6':
        course_id = input("Enter Course ID")
        course_name = input("Enter Course Name")
        print("no available courses found")

    elif choice == '7':
        course_id = input("Enter Course ID")
        course_name = input("Enter Course Name")
        print("no students enrolled")

    elif choice == '8':
        print("Exiting")
        break

    else:
        print("invalid try again")
