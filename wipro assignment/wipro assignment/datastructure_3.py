n = int(input())

student_marks = {}

for _ in range(n):
    line = input().split()
    name = line[0]
    
    marks = list(map(float, line[1:]))
    
    student_marks[name] = marks


query_name = input()

query_marks = student_marks[query_name]

average_marks = sum(query_marks) / len(query_marks)

print(f"{average_marks:.2f}")