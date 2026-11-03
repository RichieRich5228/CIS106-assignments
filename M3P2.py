last_name = input("Enter student last name: ")
midterm = float(input("Enter midterm score (0-100): "))
final = float(input("Enter final exam score (0-100): "))

total_points = midterm * .4 + final * .6

print(f"Student: {last_name}")
print(f"Total exam points: {total_points:.2f}")