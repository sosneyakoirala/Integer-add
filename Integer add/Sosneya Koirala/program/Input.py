from Conversion import *

def decimal():
	loop = True
	print("")
	print("The decimal number should be positive and less than 256")
	print("")

	while loop == True:
		try:
			fstNumber = int(input("Enter first decimal number: "))# taking input as int dataType from user
			if fstNumber > 255:
				print("")
				print("The number should be less than 256")
				print("")
				continue
			elif fstNumber < 0:
				print("")
				print("The number should be positive")
				print("")
				continue

		except ValueError:# value error exception is handled
			print("")
			print("Please enter decimal number")
			print("")
			continue
		while loop == True:
			try:
				sndNumber = int(input("Enter second decimal number: "))
				if sndNumber > 255:
					print("")
					print("The number should be less than 256")
					print("")
					continue
				elif sndNumber < 0:
					print("")
					print("The number should be positive")
					print("")
					continue
			except ValueError:# value error exception is handled
				print("")
				print("Please enter decimal number")
				print("")
				continue
			break
		if fstNumber + sndNumber > 255:
			print("")
			print("The sum of two decimal number should be less than 256")
			print("")
			continue
		else:
			break
	return fstNumber, sndNumber

def binary():
	loop = False
	print("")
	print("The binary number should not be more than 8-bits")
	print("")
	while loop == False:
		fstNumber = input("Enter first binary number: ")
		if len(fstNumber) > 8:
			print("")
			print("The number should be not more than 8-bits")
			print("")
			continue
		try:
			intNumber = int(fstNumber)
			setnumber = stringToSet(fstNumber)
			if setnumber == {0} or setnumber == {0,1} or setnumber == {1}:
				pass
			else:
				print("")
				print("Please enter binary number 0 - 1")
				print("")
				continue

		except ValueError:# value error exception is handled
			print("")
			print("Please enter binary number")
			print("")
			continue

		while loop == False:
			sndNumber = input("Enter second binary number: ")
			if len(sndNumber) > 8:
				print("")
				print("The binary number should be not more than 8-bits")
				continue
			try:
				intNumber = int(sndNumber)
				setnumber = stringToSet(sndNumber)# string to set function is called from conversion class
				if setnumber == {0} or setnumber == {0,1} or setnumber == {1}:
					pass
				else:
					print("")
					print("Please enter binary number 0 - 1")
					print("")
					continue

			except ValueError:# value error exception is handled
				print("")
				print("Please enter binary number")
				print("")
				continue
			break
		binary1 = stringToList(fstNumber)# string to list function is called from conversion class
		binary2 = stringToList(sndNumber)

		decimal1 = binaryToDecimal(binary1)# binary to decimal function is called from conversion class
		decimal2 = binaryToDecimal(binary2)
		if decimal1 + decimal2 > 255:
			print("")
			print("The sum of the input binary number should not be more than 8-bits")
			print("")
			continue
		else:
			loop = True

	return fstNumber, sndNumber


