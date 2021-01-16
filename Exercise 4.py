def hexToDecCalculator(Hex):
	digits = "0123456789ABCDEF"
	DecValue = 0
	for i in Hex:
		digitsInt = digits.find(i)
		DecValue = 16 * DecValue + digitsInt
	return DecValue

print(hexToDecCalculator("4B5"))

def hex_output():
	hexnum = input("Please enter a hexidecimal number:  ")
	rev_enum_hexnum = enumerate(reversed(hexnum))
	number = 0
	for power, num in rev_enum_hexnum:
		number += (16**power *int(num, 16))
	return number

print(hex_output())

# "FACE"
# 16^3 x 15 +16^2 x 10 + 16^1 x 12 + 16^0 x 14

# 16* (16* (16* (16*0 +15) +10) +12) +14

# 5120
# 5000 +100 +20 +0
# 10^3 x 5 + 10^2 x 1 + 10^1 x 2 +10^0 x 0


# 20 = 1+2+4+8+16+.... = 0+0+4+0+16
# 10100

def manual_transformation():
	number = 0
	valid= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	while True:
		try:
			base = int(input("Please enter a base number:   "))
			break
		except:
			print("Please enter a valid number")
	while True:
		num = input("Please enter a number (in that base) to convert to decimal (base 10):  ")
		correct = True
		for char in num:
			if char in valid[0:base]:
				pass
			else:
				correct = False
		if correct==True:
			break
	for power, num in enumerate(reversed(num)):
		number += (base**power *valid.find(num))
	return number

print(manual_transformation())

def name_triangle(name):
	name = input("What's your name?")
	for i in range(len(name)+1):
		for letter_index in range(i):
			print(name[letter_index], end='')
		print()

name_triangle()
