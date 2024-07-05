def stringToSet(num1):
	num2 = [0,0,0,0,0,0,0,0]
	i = 0
	while i < len(num1):
		num2[i] = int(num1[i])
		i = i + 1

	num3 = set(num2)
	return num3

def decimalToList(num1):
	num2 = [0,0,0,0,0,0,0,0]
	i = 7
	
	while num1 > 0:
		num2[i] = num1 % 2# remainder is checked
		num1 = int(num1/2)

		i = i - 1

	return num2

def stringToList(num1):
	num2 = [0,0,0,0,0,0,0,0]
	a = 7

	for i in range(len(num1)-1,-1,-1):
		num2[a] = int(num1[i])
		a = a - 1

	return num2

def listToString(num1):
	num2 = ""
	for i in range (len(num1)):
		num2 = num2 + str(num1[i])
	return num2

def binaryToDecimal(num1):
	num2 = 0
	i = 7
	a = 0
	while i >= 0:
		num2 = num2 + (num1[i]*2**a)
		a = a + 1
		i = i - 1
	return num2
