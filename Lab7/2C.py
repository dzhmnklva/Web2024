answer_system = int(input())
student_answer = int(input())

if answer_system == 1 and student_answer != 1:
    print("NO")
elif answer_system != 1 and student_answer == 1:
    print("NO")
else:
    print("YES")
