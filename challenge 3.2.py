class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage
if __name__ == "__main__":
    students = [
        Student("Alice", "A101", 3.9),
        Student("Bob", "B102", 3.7),
        Student("Charlie", "C103", 4.0),
        Student("David", "D104", 3.5),
    ]

    sorted_students = sort_students(students)

    print("Students sorted by CGPA (descending order):")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")