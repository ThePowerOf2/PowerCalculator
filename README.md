# PowerCalculator
A python program that has 2 modules 'Big_Power(x,y)' and 'Print_Power(z)'.  
The first module takes in 2 integers x and y. x = Number that is going to be used. y = Power to use on x. It returns an Array of the Result in 1-9 digit integers.  
The Second module takes in the array that was formed in the First Module and the prints it out into an acctual number.  

### Theoretical Numbers
Max output = [MAX ARRAY SIZE = 536,870,912] * [MAX NUM IN ARRAY = 9] = 4831838208 Digit Number.  
Max Number that can be used = SquareRoot(999,999,999,999,999,999) = 1,000,000,000.  
Max Power = ?.  
**_I say Theoretical as i don't have the computer power to reach these numbers nor do i have an in depth knowledge of the real limits of python. But i'm very happy to get feedback and corrections on my equations!_**

### How it Works 
The first chuck of code is to initialise an Array and a Carry variable. It then appends the NUMBER given to that array.
```python
# Declaring the Array and the Carry variable.
	theNumber = []
	Carry = 0

	# Setting the first number.
	theNumber.append(0)
	theNumber[0] = NUMBER
```