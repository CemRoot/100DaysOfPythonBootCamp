#Average Hight
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total = 0
reapeter = 0

for student in student_heights:
  reapeter += 1
  total+= student
  full= total
  
total_heights = full / reapeter
print(round(total_heights))






