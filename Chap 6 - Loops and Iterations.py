#We look at how Python repeats statements using looping structures.

#5.2

# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
#Enter 7, 2, bob, 10, and 4 and match the output below.

small=None
large=None
while True:
    sval = input('Enter a number:')
    if (sval=='done'):
        break
    try:
        val = int(sval)
    except:
        print('Invalid input')
        continue
    if small is None and large is None:
        small = val   
        large = val
    elif(small>val):
        small = val
    elif(large<val):
        large=val   
print ("Maximum is", large)
print ("Minimum is", small)
