def sum(*argv):
	total=0
	for number in argv:
		total+= number
	print(total)

sum(3,6,7,100.5)

def weird_sum(numbers, starting=0):
	total = starting
	for number in numbers:
		total+= number
	print(total)

weird_sum([1,2,3],6)

def average(*argv):
	total=0
	for number in argv:
		total+=number
	mean = total / len(argv)
	print(mean)

average(3,4,2,9)

def word_processor(*argv):
	shortest = argv[0]
	longest = ""
	mean = 0
	for word in argv:
		letters=len(word)
		mean+=letters
		if len(shortest)> letters:
			shortest = word
		if len(longest)<letters:
			longest = word
	mean/=len(argv)
	return(shortest,longest,mean)

print(word_processor("Jennifer", "Hi", "Iphone"))

def number_selector(item_list):
	total = 0
	for item in item_list:
		try:
			x = int(item)
			total+=x
		except:
			pass
	print(total)

number_selector([9,3,"hi","9"])