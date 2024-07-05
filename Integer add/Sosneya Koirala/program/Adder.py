from Gate import *

def adder(num1, num2):
	sum1 = [0,0,0,0,0,0,0,0]# as list
	i = 7
	c = 0
	while i >= 0:
		sum1[i] = xorGate(xorGate(num1[i], num2[i]),c)# xor Gate is used to obtained the final sum

		c1 = andGate(num1[i], num2[i])
		c2 = andGate(xorGate(num1[i], num2[i]),c)
		c = orGate(c1,c2)# orGate is used to obtain the new carry value
		i = i - 1
	return sum1	

