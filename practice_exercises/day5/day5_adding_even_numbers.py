# Add all the even numbers between 1 and (including) 100

total_sum = 0

for number in range(0, 101, 2):
    total_sum += number    

print(total_sum)