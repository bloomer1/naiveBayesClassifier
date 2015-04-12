from sys import argv
import math
#import string


script, trainingfile, modelfile = argv

#for linux
#trainingfile_handle = open(trainingfile,'r',errors='ignore')
trainingfile_handle = open(trainingfile,'r',errors='ignore')
content = trainingfile_handle.read()
#exclude = set(string.punctuation)
#content = ''.join(ch for ch in content if ch not in exclude)
content = content.strip('\r')

   
count = 0
hamCount = 0
hamWordCount = 0
spamWordCount = 0
unique_words = 0

unique_list = []
sentence = content.split("\n")
listDictCount = {}
clList = []
clDocCountList = {}
priorProb = {}
classwordCount = {}
classProbDic = {}

total_docs =  len(sentence)

#countDictionary
for doc in sentence:
	words = doc.split(" ")
	d ={}
	countDictName = words[0] + "CountDict"
	if countDictName in listDictCount:
		d = listDictCount[countDictName]
	else:
		listDictCount[countDictName] = {}
		d = listDictCount[countDictName]
	if words[0] not in clList:
		clList.append(words[0])
		#countDictName = word[0] + "CountDict"
        
	for word in words[1:]:
		word = word.rstrip('\r')
		if word not in unique_list:
			unique_list.append(word)
			unique_words +=  1
		# listDictCount[countDictName][word] = 1
	
		d[word]= d.get(word,0) + 1
	listDictCount[countDictName] = d
	#print listDictCount[countDictName]

clList.remove("")
del listDictCount["CountDict"]

     
#hamWordCount = sum(listDictCount["HAMCountDict"].values())

# Individual Docs as per the class
for i in clList:
	for doc in sentence:
		words = doc.split(" ")
		if words[0] == i:
			count = count + 1
	clDocCountList[i] =  count
	count = 0





#Prior Probabilities
for i in clList:
	pb = float(clDocCountList[i])/total_docs
	priorProb[i] = pb


#class word count
for i in listDictCount:
	k = i + "words"
	classwordCount[k] = sum(listDictCount[i].values())



#Probabilities of each word

finalDict = {}
for key,value in listDictCount.items():
	classProbDic = {}
	for k,v in value.items():
		classProbDic[k] = math.log(float(v+1)/( sum(listDictCount[key].values())+ unique_words))
	finalDict[key] = classProbDic
	


	
#modelfile_handle = open(modelfile,'w',errors='ignore')
modelfile_handle = open(modelfile,'w',errors='ignore')

modelfile_handle.write("Prior Probabilities")
modelfile_handle.write("\n")
modelfile_handle.write(str(priorProb))
modelfile_handle.write("\n")

modelfile_handle.write("ClassWordCount")
modelfile_handle.write("\n")
modelfile_handle.write(str(classwordCount))
modelfile_handle.write("\n")


modelfile_handle.write("UniqueWords")
modelfile_handle.write("\n")
modelfile_handle.write(str(unique_words))
modelfile_handle.write("\n")

modelfile_handle.write("Word Probabilities of class")
modelfile_handle.write("\n")
modelfile_handle.write(str(finalDict))
modelfile_handle.write("\n")









