import sys
import numpy as np
import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

#add vowel/consonant ending code


#input char DF
char_df = pd.read_csv('charTableEdited.csv', index_col = 0)

#input suffix DF
suf_df = pd.read_csv('sufTable.csv', index_col = 0)

#drop eth from all tables when it fails a criterium
def dropEth(index):
    char_df.drop(index=i, inplace=True)               
    suf_df.drop(index=i, inplace=True)
    
print("Welcome to the last name identifier. Type in a last name and see its origin.")
name = input().lower() #make lowercase
name = ''.join(name.split())  #remove whitespace

c = 0 #counter for current index in name
for letter in name:
    if (letter not in name[0:c]):  #skip if we already have seen this letter
        for i in char_df.index:
            if char_df.loc[i][letter] != letter:
                #print("dropped " + i + " due to: " + letter)  #drop eth if it doesn't have letter,
                dropEth(i)                                    #print little report each time
                
    c += 1
    #return if char df len = 1
    
    
    
for c in suf_df.columns:
    if name.endswith(c):
        for i in suf_df.index:
            if pd.isnull(suf_df.loc[i][c]):
                dropEth(i)
        break
print(suf_df.index[0])
