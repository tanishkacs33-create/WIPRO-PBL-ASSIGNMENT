# Sample student marks
marks = [75, 28, 42]
pass_count = 0

for mark in marks:
    if mark >= 35:
        pass_count += 1

print(f"Number of students who passed: {pass_count}")