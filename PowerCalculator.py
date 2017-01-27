from sys import stdout

def Power(NUMBER,POWER):
	# Declaring the Array and the Carry variable.
	theNumber = []
	Carry = 0

	# Setting the first number.
	theNumber.append(0)
	theNumber[0] = NUMBER

	# Loops based on the power given.
	for i in range(POWER - 1):

		# Loops based on how many elements there currently are in the array.
		for j in range(len(theNumber)):

			# Multiplying the current number by the original number.
			theNumber[j] = theNumber[j] * NUMBER

			# Adding on the carry if there was any from the last calculation.
			if (Carry != 0):
				theNumber[j] = theNumber[j] + Carry
				Carry = 0

			# Calculating the carry and taking it off the current number.
			if (theNumber[j] > 999999999):
				Carry = theNumber[j]/1000000000
				theNumber[j] = theNumber[j] - (Carry*1000000000)

			# Add another place in the array if there is a carry but no more space to put it.
			if ((Carry != 0) and (j == (len(theNumber) - 1))):
				theNumber.append(Carry)
				Carry = 0

	# Declaring reverse as the length of the final array.
	reverse = len(theNumber) - 1
	tmp = [0,0,0,0,0,0,0,0,0]

	# Printing out the Last array first to get rid of the leading zeros.
	stdout.write(str(theNumber[reverse]))
	reverse = reverse - 1


	# Printing out each element of the array backwards to form the result.
	for i in range(len(theNumber) - 1):

		tmp[0] = ((theNumber[reverse])/100000000)
		tmp[1] = ((theNumber[reverse] - (tmp[0] * 100000000)) /10000000)
		tmp[2] = ((theNumber[reverse] - (tmp[0] * 100000000) - (tmp[1] * 10000000)) /1000000)
		tmp[3] = ((theNumber[reverse] - (tmp[0] * 100000000) - (tmp[1] * 10000000) - (tmp[2] * 1000000))/100000)
		tmp[4] = ((theNumber[reverse] - (tmp[0] * 100000000) - (tmp[1] * 10000000) - (tmp[2] * 1000000) - (tmp[3] * 100000))/10000)
		tmp[5] = ((theNumber[reverse] - (tmp[0] * 100000000) - (tmp[1] * 10000000) - (tmp[2] * 1000000) - (tmp[3] * 100000) - (tmp[4] * 10000))/1000)
		tmp[6] = ((theNumber[reverse] - (tmp[0] * 100000000) - (tmp[1] * 10000000) - (tmp[2] * 1000000) - (tmp[3] * 100000) - (tmp[4] * 10000) - (tmp[5] * 1000))/100)
		tmp[7] = ((theNumber[reverse] - (tmp[0] * 100000000) - (tmp[1] * 10000000) - (tmp[2] * 1000000) - (tmp[3] * 100000) - (tmp[4] * 10000) - (tmp[5] * 1000) - (tmp[6] * 100))/10)
		tmp[8] = ((theNumber[reverse] - (tmp[0] * 100000000) - (tmp[1] * 10000000) - (tmp[2] * 1000000) - (tmp[3] * 100000) - (tmp[4] * 10000) - (tmp[5] * 1000) - (tmp[6] * 100) - (tmp[7] * 10))/1)

		for j in range(9):
			stdout.write(str(tmp[j]))
		reverse = reverse - 1
	stdout.write("\n")