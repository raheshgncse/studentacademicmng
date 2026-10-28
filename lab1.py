name = input("Enter student name:")
n = int(input("Enter number of subject:"))
total = 0

for i in range(1, n+1):
    mark = float(input(f"Enter mark for Subject {i}:"))
    total+=mark
    percentage = total/n

    if percentage >= 90:
        grade = "A+"
        performance = "Outstanding"
    elif percentage >= 80:
        grade = "A"
        performance = "Exellent"
    elif percentage >= 70:
        grade = "B"
        performance = "Very Good"
    elif percentage >= 60:
        grade = "C"
        performance = "Good"
    elif percentage >= 50:
        grade = "D"
        performance = "Average"
    else:
        grade = "F"
        performance = "Needs Improvement"

print("\n---Academic Performance---")
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Performance: {performance}")