"""Main program for CSC350 Lab 1."""


class Student:
    """Represent one student and their marks."""

    def __init__(self, name, marks):
        """Store the student's name and marks."""
        self.name = name
        self.marks = marks

    def passed(self):
        """Return True when the student has at least 50 marks."""
        return self.marks >= 50

    def __str__(self):
        """Return the student's result as readable text."""
        result = "Pass" if self.passed() else "Fail"
        return f"{self.name} ({self.marks}): {result}"


from course import Course, InvalidMarksError, load_course


def main():
    """Run the tests for Tasks 1 to 5."""
    # Task 1: Student class
    print("TASK 1")
    students = [
        Student("Ali", 72),
        Student("Sara", 45),
        Student("Omar", 50),
    ]
    for student in students:
        print(student)

    # Task 2: Course class
    print("\nTASK 2")
    course = Course("Programming for AI")
    course.add_student("Ali", 88)
    course.add_student("Sara", 92)
    course.add_student("Omar", 75)
    print(len(course))
    print(course.average())
    print(course.top_student())


    c = Course("X"); c.add_student("Ali" , 88)
    c.remove_student("Ali")
    print(len(c))
    try:
        c.remove_student("Zara")
    except KeyError as e:
        print("KeyError:", e)

    



    # Task 3: Custom exception and readable Course output
    print("\nTASK 3")
    try:
        course.add_student("Bilal", 120)
    except InvalidMarksError as error:
        print("Error:", error)
    print(course)

    # Task 4: Load students from marks.txt
    print("\nTASK 4")
    loaded_course = load_course("Programming for AI", "marks.txt")
    print(loaded_course)
    print("Top student:", loaded_course.top_student())
    load_course("Programming for AI", "mark.txt")

    # Task 5: Modules are used through the import above.
    # Course logic is in course.py; this file contains the tests.
    print("\nTASK 5")
    print("Module import is working.")


if __name__ == "__main__":
    main()


