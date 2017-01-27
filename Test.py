# Importing the Calculator.
import PowerCalculator

# Declaring variables.
Number = 0
Power = 0

# Asking the user to input a number.
print "Please enter the Number you wish to use: ",
while not Number: # If they enter anything other than an integer it will return 'Invalid Number'.
    try:
        Number = int(raw_input())
    except ValueError:
        print 'Invalid Number'
print "Please enter the Power you wish to use: ",
while not Power: # If they enter anything other than an integer it will return 'Invalid Number'.
    try:
        Power = int(raw_input())
    except ValueError:
        print 'Invalid Number'

# Printing out the result to the user.
print "Result = ",
PowerCalculator.Print_Power(PowerCalculator.Big_Power(Number,Power))