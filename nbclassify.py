from sys import argv
import ast

import math

script, modelfile, testfile = argv


model_handle = open(modelfile,'r',errors='ignore')
learning = model_handle.read();

learnComponents = learning.split("\n");

PriorProbDict = dict()
PriorProbDict = ast.literal_eval(learnComponents[1])

classWordCount = dict()
classWordCount = ast.literal_eval(learnComponents[3])

uniqueWords = learnComponents[5]

wordProbOfClass = dict()
wordProbOfClass = ast.literal_eval(learnComponents[7])

listOfDicClass = []
'''
for k,v in wordProbOfClass.items():
	listOfDicClass.append(wordProbOfClass[k])
'''
name = modelfile.split(".")
ofile = name[0] + ".out"
outputhandle = open(ofile,'w',errors='ignore')
#outputhandle.write(str(listOfDicClass))
#print listOfDicClass



classList = []
for key in PriorProbDict:
	classList.append(key)



test_handle = open(testfile,'r',errors='ignore')
testcontent = test_handle.read()
docmts = testcontent.split("\n")
docmts.remove('')


finalpb = {}
#listOfDicClass

for d in docmts:
	doc = d.split(" ")
	for iclass in classList:
		dic = wordProbOfClass[iclass + "CountDict"]
		
		pb = float(PriorProbDict[iclass])
		#print pb
		for word in doc:
			if word in  dic:
				pb += dic[word]
			else:
				pb += math.log(1.0/(int(classWordCount[iclass + "CountDictwords"]) + int(uniqueWords)))
		finalpb[iclass] = pb
		
	maxval = float("-inf")
	classified = ""
	for k,v in finalpb.items():

		if(v > maxval):
			maxval = v
			classified = k
	outputhandle.write(classified)
	outputhandle.write("\n")
	finalpb = {}

outputhandle.close()

	 	







