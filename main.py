def calculate_average(score1, score2, score3):
  average = (score1 + score2 + score3) / 3
  return average

student = int(input("how many students? "))
if student < 3:
  student = 3
  print("At least 3 students.")

for student in range(1, 4):
  print("student", student)
  name = input("enter name: ")
  activity1 = float(input("activity 1: "))
  activity2 = float(input("activity 2: "))
  activity3 = float(input("activity 3: "))

average = calculate_average(activity1, activity2, activity3)

if average >= 95:
  
  status = "Excellent"
elif average>= 87:
  status = "vary good"
elif average >=75:
  status = "passed"
else:
  status = "failed"
  print("====Student Result====")
  print("Name:", name)
  print("activity1:", activity1)
  print("Activity2:", activity2)
  print("activity3:", activity3)
  print("average:", round(average, 2))
  print("status:", status)



5







