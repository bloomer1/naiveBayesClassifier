import os

path1 = '/home/rahul/work/csci544-hw1/SPAM_training'
path2 = '/home/rahul/work/csci544-hw1/SENTIMENT_training'

listing1 = os.listdir(path1)
listing2 = os.listdir(path2)
handle_spam = open('spam_training.txt','w',errors='ignore' )
handle_sentiment = open('sentiment_training.txt', 'w',errors = 'ignore')


for infile in listing1:
	#print "filename " + infile
	if infile == '.DS_Store':
		continue
	file_handle = open(path1+'/'+infile,'r',errors='ignore')
	#handle.write("#@@#")
	name = infile.split(".")

	handle_spam.write(name[0] + ' ')
	content = file_handle.read()
	content = content.strip('\r')
	data = content.split("\n")
	for words in data:
		wordline = words.split(" ")
		for i in wordline:
			handle_spam.write(i + ' ')
	handle_spam.write("\n")

handle_spam.close()

for infile in listing2:
	#print "filename " + infile
	if infile == '.DS_Store':
		continue
	file_handle = open(path2+'/'+infile,'r',errors='ignore')
	#handle.write("#@@#")
	name = infile.split(".")

	handle_sentiment.write(name[0] + ' ')
	content = file_handle.read()
	content = content.strip('\r')
	data = content.split("\n")
	for words in data:
		wordline = words.split(" ")
		for i in wordline:
			handle_sentiment.write(i + ' ')
	handle_sentiment.write("\n")

handle_sentiment.close()
