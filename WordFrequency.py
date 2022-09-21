# 7) WordFrequency.py - Write a program that reads the contents of a text file (you can use this file - sometext.txt   Download sometext.txt ). 
# The program should create a dictionary in which the keys are the individual words found in the file and the values are the number of times 
# each word appears. For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as 
# the value. The program should display the frequency of each word.

infile = open('sometext.txt', 'r')

for line in infile:
    text = line.strip()
    text_list = text.split()

word_count = {list: text_list.count(list) for list in text_list}

for word in text_list:
    print(word, '-', text_list.count(word))