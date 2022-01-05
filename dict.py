#!/usr/bin/env python3

# # open the file in read mode

# text = open('text.txt', 'r')

# #create an empty dictionary
# dictionary = dict()

# #loop through the lines in the file
# for line in text:
#     #split the line into words
#     words = line.split()
#     #loop through the words
#     for word in words:
#         #if the word is in the dictionary
#         if word in dictionary:
#             #increment the count
#             dictionary[word] += 1
#         #if the word is not in the dictionary
#         else:
#             #add the word to the dictionary
#             dictionary[word] = 1
    
# #print the dictionary
# for key in dictionary:
#     print(key, dictionary[key])

import os
import pandas as pd 

book_dir = './Books'
os.listdir(book_dir)

stats = pd.DataFrame(columns=['Language', 'Author', 'Title', 'Length'])

title_count = 1

for language in os.listdir():
    if not os.path.isdir(language):
        continue
    os.chdir(language)
    for author in os.listdir():
        if not os.path.isdir(author):
            continue
        os.chdir(author)
        for title in os.listdir():
            if not title.endswith('.txt'):
                continue
            with open(title, 'r') as f:
                text = f.read()
            stats.loc[title_count] = [language, author.capitalize(), title[:-4], len(text)]
            title_count += 1
        os.chdir('..')
    os.chdir('..')

print(stats.groupby('Language').Language.count())