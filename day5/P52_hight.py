student_heights = input().split()
sum = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum = sum + student_heights[n]

print (f"the average height is: {sum/(n+1)}")
