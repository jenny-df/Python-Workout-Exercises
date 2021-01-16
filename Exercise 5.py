def pig_latin():
	word = input("Please enter a word to translate to Pig Latin:   ")
	if word[0].lower() in "aeiou":
		if word[-1] in ".,:;!?)}]'\"":
			new_word = word[:-1]+"way"+word[-1]
		else:
			new_word = word+"way"
	else:
		i=0
		for letter in word:
			if letter in "aeiou":
				i+=1
		if i>=2:
			if word[-1] in ".,:;!?)}]'\"":
				new_word = word[:-1]+"way"+word[-1]
			else:
				new_word = word+"way"
		else:
			if word[-1] in ".,:;!?)}]'\"":
				new_word = word[1:-1]+word[0].lower()+"ay"+word[-1]
			else:
				new_word = word[1:]+word[0].lower()+"ay"
	return new_word.capitalize()

print(pig_latin())