students = [
    ["Amit", [78, 85, 90]],
    ["Sita", [65, 70, 72]],
    ["Ravi", [35, 50, 50]],
    ["Neha", [88, 92, 95]]
]
total=0
pass_count=0
fail_count=0
max_total=0
topper=""
for student in students:
    name = student[0]
    marks = student[1]
    print(name, ":", marks)
    for mark in marks:
        total+=mark
    print("Total=",total)
    if(total>max_total):
        topper=name
    average=total/len(marks)
    print("Average= ",average)
    total=0
    if(average>=50):
        pass_count+=1
    else:
        fail_count+=1
print("No.of passed students= ",pass_count)
print("No.of failed students= ",fail_count)
print("TOPPER=",topper)