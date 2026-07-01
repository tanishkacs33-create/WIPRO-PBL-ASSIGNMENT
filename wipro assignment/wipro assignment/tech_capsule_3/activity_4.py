# Create a frequency list for scores 0 to 100 initialized to 0
marks_count = [0] * 101

print("Enter examination marks for 30 students (0 to 100):")
for i in range(30):
    while True:
        mark = int(input(f"Student {i+1} Mark: "))
        if 0 <= mark <= 100:
            marks_count[mark] += 1
            break
        print("Invalid input! Marks must be between 0 and 100.")

# Display counts for marks that appeared at least once
print("\nFrequency of each obtained mark:")
for score in range(101):
    if marks_count[score] > 0:
        print(f"Mark {score}: {marks_count[score]} student(s)")