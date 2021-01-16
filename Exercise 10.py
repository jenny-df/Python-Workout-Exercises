def mysum(*argv):
	if not argv:
		return("Can't sum none")
	for i in range(1,len(argv)):
		if type(argv[i]) != type(argv[i-1]):
			return("Can't sum different types")
	sum1 = argv[0]
	for item in range(1,len(argv)):
		sum1+=argv[item]
	return(sum1)
# print(mysum([1,123],["abc",True],["hi"]))

def sum_bigger_than(*argv):
	if not argv:
		return("Can't sum none")
	for i in range(1,len(argv)):
		if type(argv[i]) != type(argv[i-1]):
			return("Can't sum different types")
	sum1= argv[0]
	for item in range(1,len(argv)):
		if argv[0]<argv[item]:
			sum1+=argv[item]
	return(sum1)

# print(sum_bigger_than([10,50,20],[3,60]))

def sum_numeric(*argv):
	if not argv:
		return("Can't sum none")
	sum1=0
	for item in argv:
		try:
			sum1+= int(item)
		except:
			pass
	return(sum1)

# print(sum_numeric(1,2,3,4,"1","a",[1,2]))

def add_dicts(list1):
	final_dict= {}
	if str(type(list1))== "<type 'list'>":
		for dict1 in list1:
			for val,amount in list(dict1.items()):
				if val not in final_dict:
					final_dict[val]=amount
				else:
					if str(type(final_dict[val])) == "<type 'list'>":
						final_dict[val].append(amount)
					else:
						temp_list = [final_dict[val]]
						temp_list.append(amount)
						final_dict[val]=temp_list
	return final_dict
		
# print(add_dicts([{"name":"jennifer"}, {"name":"jennifer","age":2,"height":154}, {"name":"Kim","height":160}]))
