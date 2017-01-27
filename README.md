# PowerCalculator
A python program that has 2 modules 'Big_Power(x,y)' and 'Print_Power(z)'.  
The first module takes in 2 integers x and y. x = Number that is going to be used. y = Power to use on x. It returns an Array of the Result in 1-9 digit integers.  
The Second module takes in the array that was formed in the First Module and the prints it out into an acctual number.  

## How it Works
*Throughout i will be showing how the variables are affected based on NUMBER = 2 and POWER = 32. And these do not Change.*  
#### Module 1 (Big_Power):
The first chuck of code is to initialise an Array and a Carry variable. It then appends the NUMBER given to that array.  
```python
	# Declaring the Array and the Carry variable.
	theNumber = []
	Carry = 0

	# Setting the first number.
	theNumber.append(0)
	theNumber[0] = NUMBER
```
*After this chuck of code this is how the variables would look:*  
* theNumber = [2]
* Carry = 0  

The next chunk of code contains 2 for loops. The first one loops based on the POWER variable.  
```python
# Loops based on the power given.
for i in range(POWER - 1):

	# Loops based on how many elements there currently are in the array.
	for j in range(len(theNumber)):
```
*So using hte NUMBER and POWER values above this is initially what the for loops would read:*  
* `for i in range(31):`
* `for j in range(1):`  

The next chunk of code multiplys the current part of the array(Based on the value of 'j' from the for loop) by NUMBER.
```python
# Multiplying the current number by the original number.
	theNumber[j] = theNumber[j] * NUMBER
```
*After this chuck of code this is how the variables would look:*  
* theNumber = [4]
* Carry = 0  

The next chunk of code checks whether there was a remainder (Carry) from the last calculation and then adds it onto the current part of the array.
```python
# Adding on the carry if there was any from the last calculation.
if (Carry != 0):
	theNumber[j] = theNumber[j] + Carry
	Carry = 0
```
*After this chuck of code this is how the variables would look:*  
* theNumber = [4]  
(This has not changed as Carry = 0 but if the Carry was = 3 lets say. theNumber = [7])
* Carry = 0  






## Theoretical Numbers
Max output = [MAX ARRAY SIZE = 536,870,912] * [MAX NUM IN ARRAY = 9] = 4831838208 Digit Number.  
Max Number that can be used = SquareRoot(999,999,999,999,999,999) = 1,000,000,000.  
Max Power = ?.  
**_I say Theoretical as i don't have the computer power to reach these numbers nor do i have an in depth knowledge of the real limits of python. But i'm very happy to get feedback and corrections on my equations!_**