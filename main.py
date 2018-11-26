import os
"""
Phillip chatbot made by @neodymium
Starts completely from scratch and must be trained
*Note: All saved files will be cleared when the page is closed/refreshed.
"""
prompts = [["hello", "there"]]
res = ["Hi"]
inp = ""
words = []
name = "Phillip"
version = "0.1"


#Method to write a txt file to a
#multidimensional list
def strToList(arr2):
	item = ""
	outList = []
	inList = []
	for i in arr2:
		if not (i == "[" or i == "," or i == "'" or i == "]" or i == " "):
			item = "%s%s" % (item, i)
		elif i == ",":
			if len(item) > 0:
				inList.append(item)
			item = ""
		elif i == "]":
			if len(inList) > 0 or len(item) > 0:
				inList.append(item)
				outList.append(inList)
			inList = []
			item = ""
	return outList


#Method to write a txt file to
#a normal list
def normStrToList(arr3):
	item2 = ""
	newList = []
	for i in arr3:
		if not (i == "[" or i == "," or i == "]" or i == "'" or i == "\""):
			item2 = "%s%s" % (item2, i)
		elif i == ",":
			newList.append(item2)
			item2 = ""
	newList.append(item2)
	return newList


if os.path.isfile("promptData.txt"):
	#Write saved prompts
	f = open("promptData.txt", "r")
	if f.mode == "r":
		data = f.read()
		prompts = strToList(data)
	else:
		print "Error reading prompts file."
	f.close()
	#Write saved responses
	f = open("responsesData.txt", "r")
	if f.mode == "r":
		data = f.read()
		res = normStrToList(data)
	else:
		print "Error reading responses file."
	f.close()
else:
	#For first time program use
	checkFile = open("promptData.txt", "w+")
	checkFile.close()
	checkFile = open("responsesData.txt", "w+")
	checkFile.close()

#Small bug fix
if res[0] == "":
	res.pop(0)


#Contains method for list
def cont(array, item):
	ret = False
	for i in array:
		if i == item:
			ret = True
	return ret


#Parses words into list
def parsed(txt):
	i = ""
	iii = []
	for ii in txt:
		if ii == " ":
			iii.append(i)
			i = ""
		else:
			i = "%s%s" % (i, ii)
	iii.append(i)
	return iii


#Method for finding appropriate response
#based on user input


def findRes(arr):
	sim = []
	match = []
	g = 0
	gi = 0
	c = 0
	for i in prompts:
		#Determines how much a sentence matches
		#to its response
		matches = 0
		for ii in i:
			if cont(arr, ii):
				matches += 1
		if matches > 0:
			sim.append(i)
			match.append(matches)
	if len(match) > 0:
		for iii in match:
			if iii > g:
				g = iii
				gi = c
			c += 1
		return res[prompts.index(sim[gi])]
	else:
		#If no matches, return Null
		return "Null"


print name
print "%s%s" % ("Version ", version)
print "Type \'help\' for list of commands."

while True:
	inp = raw_input("READY: ")
	if inp == "break":
		break
	elif inp == "train":
		inp = raw_input("ENTER PROMPT:")
		prompts.append(parsed(inp))
		inp = raw_input("ENTER RESPONSE:")
		res.append(inp)
		print "DONE"
	elif inp == "stats":
		print prompts
		print res
	elif inp == "clear":
		inp = raw_input("ENTER PASSCODE:")
		if inp == "531224":
			f = open("promptData.txt", "w+")
			f.write("")
			f.close()
			f = open("responsesData.txt", "w+")
			f.write("")
			f.close()
			print "WRITTEN DATA CLEARED."
			print "-->The \'break\' command will rewrite all data."
		else:
			print "INCORRECT PASSCODE."
	elif inp == "save":
		f = open("promptData.txt", "w+")
		string = str(prompts)
		f.write(string)
		f.close()
		f = open("responsesData.txt", "w+")
		string = str(res)
		f.write(string)
		f.close()
		print "DATA SAVED."
	elif inp == "help":
		print "break: stops program."
		print "train: asks for a prompt and response to train the program."
		print "stats: shows current prompts and responses."
		print "clear: clears all chatbot memory after asking for passcode."
		print "save: saves data at that point."
		print "Type anything else to talk to chatbot."
	else:
		words = parsed(inp)
		if findRes(words) == "Null":
			resp = raw_input("UNKOWN. ENTER RESPONSE:")
			prompts.append(words)
			res.append(resp)
		else:
			print findRes(words)

#Save lists into txt file
f = open("promptData.txt", "w+")
string = str(prompts)
f.write(string)
f.close()
f = open("responsesData.txt", "w+")
string = str(res)
f.write(string)
f.close()

print "DATA SAVED."
