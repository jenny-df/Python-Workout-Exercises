from decimal import *

def running_time():
	values = []
	total = 0
	while True:
		ans = input("How many minutes did it take you to run 10km today?  (Press ENTER if you are done)")
		if ans != '':
			try:
				values.append(float(ans))
			except:
				print("Please enter a number\n\n\n")
		else:
			break
	for number in values:
		total+=number
	average= total/len(values)
	print("Average of "+str(round(average,2))+", over "+str(len(values))+" runs")

# running_time()

def cutting_float(float_num, before, after):
	float_num2 = str(float_num)
	num= float_num2.split(".", 1)
	before = before* -1 -1
	print(num[0][before:-1] +"."+num[1][0:after])
	
cutting_float(1234.5678,2,3)


def adding_decimals():
	number1 = input("Please enter a decimal")
	number2 = input('Please enter another decimal')
	total = Decimal(number1) + Decimal(number2) 
	print(total)

adding_decimals()