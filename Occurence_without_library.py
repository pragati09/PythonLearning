# How to read a text file and print the occurences of words in it without using library

print("Reading characters from a file and print their occurence without using a library")
text_file=open("read_txt.txt","r")
wordcount={}
for word in text_file.read().split():
	if word not in wordcount:
		wordcount[word] = 1
	else:
	   wordcount[word] += 1
print(word,wordcount)
text_file.close();

