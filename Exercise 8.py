def strsort(word):
	return "".join(sorted(word))

# print(strsort("cba35"))

def sentencesort(sentence):
	new_sentence = []
	longest = ""
	for word in sentence.split(" "):
		if len(word)> len(longest):
			longest = word
		new_sentence.append("".join(sorted(word)))
	print("longest word is " + longest)
	return ", ".join(new_sentence)

# print(sentencesort("Tome harry"))

def lastword(sentence):
	last = "a"
	for word in sentence.lower().split():
		for letter in word:
			for letter2 in last.lower():
				if ord(letter) < ord(letter2):
					break
				elif ord(letter) > ord(letter2):
					last = word
					break
				else:
					pass
			break
	print(last)

# lastword("How are you my zzzz friend zero zp zzz?")