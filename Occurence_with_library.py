# How to read a text file and print the occurences of words in it using library

from collections import Counter

print("\nReading characters from a file and print their occurence using  library")
text_file=open("read_txt.txt","r")
wordcount= Counter(text_file.read().split())
print(wordcount)
text_file.close();