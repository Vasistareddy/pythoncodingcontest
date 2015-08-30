def spliting(inputline):
	""" splits the inputline into listofwords"""
	if inputline[-1]==".":
		words = ""
		listofwords = []
		for i in line:
			if i == " " or i == ".":
				listofwords.append(words)
				words = ""
				
			else:	
				words = words + i

		listofwordswithoutextraspaces = []
		for i in listofwords:
			if i != '':
				listofwordswithoutextraspaces.append(i)

		#listofwordswithoutextraspaces.append(".")
		return listofwordswithoutextraspaces
	else:
		return "Please end the line with fullstop"

def revtheodd(splitlist):
	""" this function is to reverse the odd indexed words in the list"""

	output = ""

	for i in range(len(splitlist)):
		if len(splitlist[i])<=15:
			if i%2 == 1:
				length = len(splitlist[i]) - 1
				rev = revword(splitlist[i],length)
			else:
				rev = splitlist[i]
		else:
			return "each word should not exceed the length 15"
		output = output + " " + rev
	output = output + "."
	return output

def revword(word, length):
	"""reversing the word"""
	reverse = ''
        for i in range(length,-1,-1):
            reverse = reverse + word[i]
        return reverse


if __name__ == "__main__":
	line = raw_input("enter the srting")
	splitlist = spliting(line)
	#print splitlist
	reversingtheodd = revtheodd(splitlist)
	

	if len(line)>0:
		print reversingtheodd
	else:
		print "enter atleast a single word"
	
