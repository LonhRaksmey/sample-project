from student import Student

# Create student objects
student1 = Student("Alice", 15, 9)
student2 = Student("Bob", 16, 10)

# Print student details
print(student1.get_details())
print(student2.get_details())

# Promote a student
print(student1.promote())

# Check updated grade
print(f"{student1.name}'s new grade: {student1.grade}")