import numpy as np

# Raw data
marks = np.array([78, 85, 92, 67, 88, 95, 72])

# Display data
print("Marks:", marks)

# Calculate statistics
print("Average:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))

# Add 5 grace marks
updated_marks = marks + 5
print("Updated Marks:", updated_marks)

# Find students scoring above 80
high_scores = marks[marks > 80]
print("Marks above 80:", high_scores)

# Sort marks
sorted_marks = np.sort(marks)
print("Sorted Marks:", sorted_marks)