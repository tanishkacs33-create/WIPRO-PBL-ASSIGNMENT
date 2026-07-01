# 10 buckets for ranges: 0-10, 11-20, 21-30, ..., 91-100
range_counts = [0] * 10

print("Enter examination marks for 30 students (0 to 100):")
for i in range(30):
    while True:
        mark = int(input(f"Student {i+1} Mark: "))
        if 0 <= mark <= 100:
            # Determine the index bucket
            if mark == 0:
                bucket_idx = 0
            else:
                # Math ceiling logic to group 1-10 into index 0, 11-20 into index 1, etc.
                bucket_idx = (mark - 1) // 10
            
            range_counts[bucket_idx] += 1
            break
        print("Invalid input! Marks must be between 0 and 100.")

# Display the final range distributions
print("\nDistribution of marks across ranges:")
ranges_labels = [
    "0% to 10%", "11% to 20%", "21% to 30%", "31% to 40%", "41% to 50%",
    "51% to 60%", "61% to 70%", "71% to 80%", "81% to 90%", "91% to 100%"
]

for i in range(10):
    print(f"{ranges_labels[i]}: {range_counts[i]} student(s)")