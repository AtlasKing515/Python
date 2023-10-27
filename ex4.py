num_students = int(input("Enter the number of students who took the exam: "))

theory_marks = []
problem_marks = []

for i in range(num_students):
    theory_mark = float(input(f"Enter the theory mark for student {i}: "))
    problem_mark = float(input(f"Enter the problem mark for student {i}: "))
    theory_marks.append(theory_mark)
    problem_marks.append(problem_mark)

total_marks = []
for i in range(num_students):
    total_mark = (theory_marks[i] * 0.4) + (problem_marks[i] * 0.6)
    total_marks.append(total_mark)

print("Student\tTheory\tProblem\tTotal")
for i in range(num_students):
    print(f"{i}\t{theory_marks[i]}\t{problem_marks[i]}\t{total_marks[i]}")

max_total_mark = max(total_marks)
min_total_mark = min(total_marks)
avg_total_mark = sum(total_marks) / num_students
print(f"Maximum total mark: {max_total_mark}")
print(f"Minimum total mark: {min_total_mark}")
print(f"Average total mark: {avg_total_mark}")

max_total_mark_index = total_marks.index(max_total_mark)
print(f"Index of maximum total mark: {max_total_mark_index}")
