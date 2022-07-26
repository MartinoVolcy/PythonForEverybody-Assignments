#We look at how Python executes some statements and skips others.

#3.1

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.

h = float(input("Enter Hours: "))
s = float(input("Enter Salary: "))
overtimeHours = 0
overtimeSalary = 0
overtimePay =0
if h > 40:
    overtimeHours = h - 40
    overtimeSalary = s*1.5
    overtimePay = overtimeHours*overtimeSalary
regularPay = 40*s
print(str(regularPay+overtimePay))


#3.3

#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

grade = float(input("Enter Grade: "))
if 0.0 > grade > 1.0:
  print("Not a valid grade!")
  quit()
elif grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
elif grade < 0.6:
    print("F")
