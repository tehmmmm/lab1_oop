"""Course management classes and file-loading function for Lab 1."""


class InvalidMarksError(Exception):
    """Raised when a student's marks are outside the range 0 to 100."""


class Course:
    """Store student marks and calculate basic course information."""

    def __init__(self, name):
        """Create a course with a name and an empty marks dictionary."""
        self.name = name
        self.marks = {}

    def add_student(self, student: str, marks: int) -> None:
        """Add a student after checking that marks are between 0 and 100."""
        if not 0 <= marks <= 100:
            raise InvalidMarksError(f"Invalid marks for {student}: {marks}")
        self.marks[student] = marks

    def average(self):
        """Return the average marks, or 0.0 if there are no students."""
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        """Return the name of the student with the highest marks."""
        if not self.marks:
            return None
        return max(self.marks, key=self.marks.get)

    def __len__(self):
        """Return the number of students in the course."""
        return len(self.marks)

    def __str__(self):
        """Return a readable summary of the course."""
        count = len(self)
        student_word = "student" if count == 1 else "students"
        return (
            f"{self.name}: {count} {student_word}, "
            f"average {self.average():.1f}"
        )

    def remove_student(self,name: str)  ->None :
        """Remove a student, or raise KeyError if missing."""
        if name not in self.marks:
            raise KeyError(f"No student named {name}")
        del self.marks[name]


def load_course(name: str, filename: str) -> Course:
    """Load valid student marks from a text file and skip invalid lines."""
    course = Course(name)

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                try:
                    student, mark = line.split(",", 1)
                    student = student.strip()
                    marks = int(mark.strip())
                    course.add_student(student, marks)
                except ValueError:
                    # Handles a mark such as "abc" and malformed lines.
                    student_name = line.split(",", 1)[0].strip()
                    print(f"Skipping {student_name}: marks is not a number")
                except InvalidMarksError as error:
                    print(f"Skipping: {error}")

    except FileNotFoundError:
        print(f"File not found: {filename}")

    return course


if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)
