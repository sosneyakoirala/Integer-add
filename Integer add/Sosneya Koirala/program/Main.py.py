from Conversion import *
from Input import *
from Adder import *

loop = True
print("------WELCOME-------")

while loop == True:
	dataType = input("Enter 'B' or 'b' for binary number system and 'D' or 'd' for decimal number system: ")#taking input from user
	dataType = dataType.lower()#changing the datatype letter to lower case
	if dataType == "b":
		num1, num2 = binary()
		fnumber = stringToList(num1)
		snumber = stringToList(num2)

	elif dataType == "d":
		num1, num2 = decimal()
		fnumber = decimalToList(num1)
		snumber = decimalToList(num2)

	elif dataType == "" or dataType == " ":
		print("")
		print("Please fill the field")
		print("")
		continue

	else:
		print("")
		print("Please enter the appropriate value")
		print("")
		continue

	sumResult = adder(fnumber, snumber)#adder function is called from adder class
	binary1 = listToString(sumResult)
	inputBinary1 = listToString(fnumber)
	inputBinary2 = listToString(snumber)

	decimal1 = binaryToDecimal(sumResult)# binary to decimal function is called from conversion class
	inputDecimal1 = binaryToDecimal(fnumber)
	inputDecimal2 = binaryToDecimal(snumber)

	print("")
	print(" The binary number     The decimal number")
	print("    ",inputBinary1, "             ", inputDecimal1)
	print("    ",inputBinary2, "             ", inputDecimal2)
	print("   ------------          -------")
	print("    ", binary1, "             ", decimal1)

	while loop == True:
		a = input("Do you want to continue the program? \n Enter 'y' to continue or 'n' to exit: ")
		a = a.lower()
		if a == "y" or a == "n":
			break
		else:
			print("")
			print("Please enter the appropriate value")
			print("")
			continue

	if a == "y":
		continue
	else:
		loop = False