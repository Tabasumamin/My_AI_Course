#python# Student Grade Checker — Python

students = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 67,
    "Ayesha": 54,
}

def get_grade(marks):
    if marks >= 90: return "A+"
    elif marks >= 80: return "A"
    elif marks >= 70: return "B"
    elif marks >= 60: return "C"
    else: return "Fail"

for name, marks in students.items():
    grade = get_grade(marks)
    print(f"{name}: {marks} marks → Grade: {grade}")

# Output:
# Ali: 85 marks → Grade: A
# Sara: 92 marks → Grade: A+
# Ahmed: 67 marks → Grade: C
# Ayesha: 54 marks → Grade: Fail