#!/usr/bin/env python3

# open the file in read mode

text = open('text.txt', 'r')

#create an empty dictionary
dictionary = dict()

#loop through the lines in the file
for line in text:
    #split the line into words
    words = line.split()
    #loop through the words
    for word in words:
        #if the word is in the dictionary
        if word in dictionary:
            #increment the count
            dictionary[word] += 1
        #if the word is not in the dictionary
        else:
            #add the word to the dictionary
            dictionary[word] = 1
    
#print the dictionary
for key in dictionary:
    print(key, dictionary[key])

