import os

def pl_sentence():
	sentence = input("Please enter a sentence to translate to Pig Latin:   ")
	words = sentence.split()
	complete_sentence = []
	print(words)
	for word in words:
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
		complete_sentence.append(new_word)
	final = " ".join(complete_sentence)

	return final.capitalize()

# print(pl_sentence())

def transposer(txt_file):
	current_dir = os.getcwd()
	opened_txt = open(current_dir+"/"+txt_file, "r")
	new_sentence = []
	lines = opened_txt.readlines()
	for line in lines:
		new_sentence.append(line.split(" ")[len(lines)].strip("\r\n"))
	print(" ".join(new_sentence))

# transposer("/Needed_extra_files/text.txt")

def sorter(listing):
	listing2 = []
	
	for string in listing:
		num = len(string.split())
		for item in string.split():
			listing2.append(item)
	print(listing2)

# sorter(['abc def ghi hjk','jkl mno pqr jhk','tuv wxj jil hjk'])

