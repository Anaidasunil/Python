def get_student_details():
    students = {}
    n = int(input("Enter the number of students: "))
    
    for _ in range(n):
        name = input("Enter the student's name: ")
        roll_no = input("Enter the student's roll number: ")
        total_mark = float(input("Enter the student's total mark: "))
        students[roll_no] = {"name": name, "total_mark": total_mark}
    
    return students

def find_top_student(students):
    top_student = None
    highest_mark = -1

    for roll_no, details in students.items():
        if details["total_mark"] > highest_mark:
            highest_mark = details["total_mark"]
            top_student = {"roll_no": roll_no, "name": details["name"], "total_mark": details["total_mark"]}
    
    return top_student

def main():
    students = get_student_details()
    top_student = find_top_student(students)
    
    if top_student:
        print("\nDetails of the student with the highest total mark:")
        print(f"Name: {top_student['name']}")
        print(f"Roll Number: {top_student['roll_no']}")
        print(f"Total Mark: {top_student['total_mark']}")
    else:
        print("No student details found.")

if __name__ == "__main__":
    main()
