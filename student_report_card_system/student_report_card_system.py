def get_grade(marks):
    if 90 <= marks <= 100:
        return "A+"
    elif 80 <= marks <= 89:
        return "A"
    elif 70 <= marks <= 79:
        return "B"
    elif 60 <= marks <= 69:
        return "C"
    else:
        return "Fail"
def calculate_average(marks_list):
    total = 0
    for mark in marks_list:
        total = total + mark
    avg = total / len(marks_list)
    return avg
def is_passed(marks_list):
    for marks in marks_list:
        if marks < 60:
            return False
    return True
def print_report(student):
    print("\n=============================")
    print("        REPORT CARD")
    print("=============================")
    print("Name     :", student["name"])
    print("Roll No  :", student["roll_no"])
    print("-----------------------------")
    print("Subject       Marks   Grade")
    print("-----------------------------")
    for subject, marks in student["marks"].items():
        grade = get_grade(marks)
        print(f"{subject:<13} {marks:<6} {grade}")
    print("-----------------------------")

    marks_list = list(student["marks"].values())
    avg = calculate_average(marks_list)
    print("Average      :", round(avg, 1))
    final_grade = get_grade(avg)
    print("Final Grade  :", final_grade)
    if is_passed(marks_list):
        print("Result       : PASS")
    else:
        print("Result       : FAIL")

    print("=============================")
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
subjects = ["Math", "Science", "English", "Telugu", "Hindi"]
marks = {}
for subject in subjects:
    m = int(input(f"Enter marks for {subject}: "))
    marks[subject] = m
student = {
    "name": name,
    "roll_no": roll,
    "marks": marks
}
print_report(student)