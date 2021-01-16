def ubbi_dubbi(word):
	extra = 0
	final_string = word
	for i in range(len(word)):
		if word.lower()[i] in 'aeiou':
			final_string = final_string[:i+extra] + "ub" + final_string[i+extra:]
			extra+=2
	print(final_string.lower().capitalize())

# ubbi_dubbi("Octupus")

def author(title, names):
	print(title.capitalize() +" by", end=" ")
	for name in names[:-1]:
		print(name[0]+".,", end=" ")
	print("& "+names[-1][0]+".")

# author("kim", ["Jennifer","Lopez","Paula"])

def encoder(url):
	final_url= []
	for letter in url:
		if letter not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
			letter = hex(ord(letter)).replace("0x", "%")
		final_url.append(letter)	
	print("".join(final_url))
	
# encoder("https://www.programiz.com/python-programming/methods/built-in/ord")		
