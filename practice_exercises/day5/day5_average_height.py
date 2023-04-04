# Find Average Height without using sum() or len() function

# Turn input into a list and convert to integer type

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# For loop to sum heights and number of entries

sum_of_heights = 0
total_entries = 0

for height in student_heights:
    sum_of_heights += height
    total_entries += 1

# Evaluate to rounded average height

average_height = round(sum_of_heights / total_entries)
print(average_height)