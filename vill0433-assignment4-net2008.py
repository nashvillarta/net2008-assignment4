# Nash Edward Villarta Assignment 4 - NET2008
# Idea: Create an average grade calculator.
# It will continue asking for grades to input until reaching 5 total grades. Just like how much is in a semester.
# To then add them all up and divide it by how much was inputted.
# Was going to do a heat engine calculator but I do not have much use for that.
# Plan:
# Counter variable to count how much grades has been inputted
# Create a loop of input, stopping until it has gotten 5 grades.
# Once done with the loop, it should display the average of grades.
#https://github.com/nashvillarta/net2008-assignment4.git



print("Welcome to average grade calculator! Please input your 5 courses in here!")
totalGrades = 0
for i in range (0,5):
   print(f"[{i}] Grade")
   inputNum = input(" Input a float (Ex 88.8): ")
   try:
           inputNum = float(inputNum)
   except ValueError:
       print(" Not correct try again")
   else:
       if(inputNum < 0):
           print(" Invalid number, setting to zero and adding it.")
           inputNum = 0
       else:
           print(" Valid number... Adding it.")
       totalGrades +=inputNum
       print(f" Test case: Total Grades = {totalGrades}")
# Calculation for average grade
totalGrades /= 5
print(f"Your average grade across 5 courses is: {totalGrades}")


#Test case 1: 80, 80, 90, 90, 80
# 420 total = average of 84
# verified
#Test case 2: 50, 80, 90, 80, 80
# 380 total = average of 76
# verified
# Code works also for misinputs!

