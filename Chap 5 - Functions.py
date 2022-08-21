#Take a brief look at how Python implements the 'store and use later' programming pattern.

#4.6

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
#Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
#The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
#Do not name your variable sum or use the sum() function.

def computepay(hours,salary):
    h = float(hours)
    s = float(salary)
    overtimeHours = 0
    overtimeSalary = 0
    overtimePay =0
    if h > 40:
        overtimeHours = h - 40
        overtimeSalary = s*1.5
        overtimePay = overtimeHours*overtimeSalary
    regularPay = 40*s
    finalPay = regularPay + overtimePay
    return finalPay
hour = input("enter hours ")
wage = input("enter wage ")
pay = computepay(hour, wage)
print("Pay", str(pay))
