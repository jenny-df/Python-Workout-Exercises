def firstlast(sequence):
	return sequence[:1]+sequence[-1:] #SUPER IMPORTANT

# print(firstlast((1,2,3)))

def even_odd_sums(nums):
	even = 0
	odd = 0
	for i in range(len(nums)):
		if i%2 == 0:
			even+=nums[i]
		else:
			odd+=nums[i]
	return [even,odd]

# print(even_odd_sums([10,20,30,40,50,60]))

def plus_minus(nums):
	final = nums[0]
	for i in range(1,len(nums)):
		if i%2 == 0:
			final-=nums[i]
		else:
			final+=nums[i]
	return final

# print(plus_minus([10,20,30,40,50,60]))

def myzip(list1,list2):
	final = []
	for i in range(len(list1)):
		final.append((list1[i],list2[i]))
	return final

# print(myzip([1,2,3],"abc"))