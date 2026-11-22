"""Store and display student details using a Python class."""


class Student:
    """Represent a student with basic academic details."""

    def __init__(self, name: str, roll_number: str, course: str) -> None:
        self.name = name.strip()
        self.roll_number = roll_number.strip()
        self.course = course.strip()

    def display_details(self) -> None:
        """Print the student's details in a readable format."""
        print("\n--- Student Details ---")
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Course      : {self.course}")


def main() -> None:
    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()
    course = input("Enter course: ").strip()

    if not all((name, roll_number, course)):
        print("Invalid input: all fields are required.")
        return

    student = Student(name, roll_number, course)
    student.display_details()


if __name__ == "__main__":
    main()
