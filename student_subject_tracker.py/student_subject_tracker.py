students=[
    (("Lavanya",101),{"DBMS","Python","webdev"}),
    (("Sandhya",102),{"UI/UX","java"}),
    (("Sathvika",103),{"Python"})
    ]
#print(student)
for i in students:
    print("Name:",i[0][0])
    print("Roll no:",i[0][1])
    print("Subjects:",i[1])
    print()
all_subjects=set()
for i in students:
    all_subjects.update(i[1])
print("All unique subjects:",all_subjects)
print("Total no.of subjects:",len(all_subjects))
print("Common subjects:",students[0][1]&students[2][1])
for student in students:
    print(student[0][0],":",len(student[1]))
max_count=0
max_student=""
for student in students:
    if(len(student[1])>max_count):
        max_count=len(student[1])
        max_student=student[0][0]
print(f"The student who has maximum subjects is:{max_student}({max_count})")
min_count=len(students[0][1])
min_student=students[0][0][0]
for student in students:
    if len(student[1])< min_count:
        min_count=len(student[1])
        min_student=student[0][0]
print(f"The student who has minimum subjects is:{min_student}({min_count})")
for student in students:
    if len(student[1]) < 2:
        print(f"Warning:Student {student[0]} attended less subjects")