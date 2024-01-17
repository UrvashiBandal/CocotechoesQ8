import random
def student_data(student_number):
    subjects = ["English", "Hindi", "Math 1", "Math 2", "Science"]
    total_marks = [100, 100, 70, 70, 100]
    student_data = {
        "name": f"Student{student_number}",
        "subjects": {subject: {"total_marks": total, "marks_scored": random.randint(0, total)} 
        for subject, total in zip(subjects, total_marks)}
    }
    return student_data
    students = [student_data(i) for i in range(1, 21)]
    def calculate_total_marks(student):
        return sum(subject_info["marks_scored"] for subject_info in
        student["subjects"].values())
        students.sort(key=lambda student: calculate_total_mark
        (student), reverse=True)
        
        print("Top Five Students:")
        for i, student in enumerate(students[:5]):
            total_marks = calculate_total_marks(student)
            print(f"{i+1}. {student['name']}: Total Marks{total_marks}")
            for subject, marks_info in student["subjects"].items():
                print(f"{subject}: Total Marks - {marks_info['total_marks']}, Marks Scored - {marks_info['marks_scored']}")
    print()

