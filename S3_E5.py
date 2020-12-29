# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:53:01 2020

@author: 100jjad


..........Sajjad Soheyli.........Series.....03.............Exercise....05...........


Frequency Term Matrix for All Text Document File Together 

"""
import math
import re
from nltk.stem import PorterStemmer



def Data_Read():
    global txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10
    temp = open("D:/software/Anaconda Project/Project 2/data/1.txt", "r")
    txt1 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/2.txt", "r")
    txt2 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/3.txt", "r")
    txt3 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/4.txt", "r")
    txt4 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/5.txt", "r")
    txt5 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/6.txt", "r")
    txt6 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/7.txt", "r")
    txt7 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/8.txt", "r")
    txt8 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/9.txt", "r")
    txt9 = temp.read()
    temp = open("D:/software/Anaconda Project/Project 2/data/10.txt", "r")
    txt10 = temp.read()
    
    return


def Text_Cleaning(txt = ""):
    txt = txt.lower()
    temp = txt.strip()
    txt = re.sub("[1234567890~`!@#$%^&*()-_+={}\/:;'<>,.?]"," ",temp)
    
    return txt


def Word_Detection(txt = ""):
    stop_words = ["a","about"
,"above","after","again","against","all","am","an","and","any","are","aren't,","as","at","be","because","been"
,"before","being","below,","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't"
,"doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having"
,"he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd"
,"i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most"
,"mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours"
,"ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such",
"than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd",
"they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we",
"we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who",
"who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours",
"yourself","yourselves","vs"]
    
    
    words , temp = [] , []
    temp = txt.split(" ")
    for w in temp:
        if w not in stop_words:
            if w != "":
                if len(w) != 1:
                    words.append(PorterStemmer().stem(w))
    
    
    return words


def Counting_Words(words = []):
    
    temp = []
    
    for w in words:
        if w not in temp:
            temp.append(w)
    
    
    temp_size = len(temp)
    word_size = len(words)
    
    unique_words = [[0 for x in range(temp_size-1)] for y in range(2)] 
    
    
    for i in range(temp_size-1):
        num = 0
        for j in range(word_size-1):
            if temp[i] == words[j]:
                num +=1
                
        unique_words[0][i] = temp[i]
        unique_words[1][i] = num
        
    return unique_words , temp_size


def Calculate_Frequency_Matrix(words1 = [] , words2 = [] , words3 = [] , words4 = [] , words5 = [] , words6 = [] , words7 = [] , words8 = [] , words9 = [] , words10 = [], size1=1 , size2=1 , size3=1 , size4=1 , size5=1 , size6=1 , size7=1 , size8=1 , size9=1 , size10=1):
    temp = []
    
    for w in words1[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words2[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words3[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words4[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words5[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words6[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words7[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words8[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words9[0]:
        if w not in temp:
            temp.append(w)
            
    for w in words10[0]:
        if w not in temp:
            temp.append(w)
            
    temp_size = len(temp)   

            
    Frequency_Matrix = [[0 for x in range(temp_size-1)] for y in range(11)] 
    
    for i in range(temp_size-1):
        Frequency_Matrix[0][i] = temp[i]
        
        
    for i in range(temp_size-1):
        for j in range(size1-1):
            if words1[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[1][i] = words1[1][j]
                
    for i in range(temp_size-1):
        for j in range(size2-1):
            if words2[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[2][i] = words2[1][j]
                
                
    for i in range(temp_size-1):
        for j in range(size3-1):
            if words3[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[3][i] = words3[1][j]
                
    for i in range(temp_size-1):
        for j in range(size4-1):
            if words4[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[4][i] = words4[1][j]
                
    for i in range(temp_size-1):
        for j in range(size5-1):
            if words5[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[5][i] = words5[1][j]
                
    for i in range(temp_size-1):
        for j in range(size6-1):
            if words6[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[6][i] = words6[1][j]
                
    for i in range(temp_size-1):
        for j in range(size7-1):
            if words7[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[7][i] = words7[1][j]
                
    for i in range(temp_size-1):
        for j in range(size8-1):
            if words8[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[8][i] = words8[1][j]
                
    for i in range(temp_size-1):
        for j in range(size9-1):
            if words9[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[9][i] = words9[1][j]
                
    for i in range(temp_size-1):
        for j in range(size10-1):
            if words10[0][j] == Frequency_Matrix[0][i]:
                Frequency_Matrix[10][i] = words10[1][j]
                
    return Frequency_Matrix


def main():
        
    global txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10,words1,words2,words3,words4,words5,words6,words7,words8,words9,words10
    
    Data_Read()
    
    txt1 = Text_Cleaning(txt1)
    txt2 = Text_Cleaning(txt2)
    txt3 = Text_Cleaning(txt3)
    txt4 = Text_Cleaning(txt4)
    txt5 = Text_Cleaning(txt5)
    txt6 = Text_Cleaning(txt6)
    txt7 = Text_Cleaning(txt7)
    txt8 = Text_Cleaning(txt8)
    txt9 = Text_Cleaning(txt9)
    txt10 = Text_Cleaning(txt10)
    
    words1 = Word_Detection(txt1)
    words2 = Word_Detection(txt2)
    words3 = Word_Detection(txt3)
    words4 = Word_Detection(txt4)
    words5 = Word_Detection(txt5)
    words6 = Word_Detection(txt6)
    words7 = Word_Detection(txt7)
    words8 = Word_Detection(txt8)
    words9 = Word_Detection(txt9)
    words10 = Word_Detection(txt10)
    
    
    unique_words1 , size1 = Counting_Words(words1)
    unique_words2 , size2 = Counting_Words(words2)
    unique_words3 , size3 = Counting_Words(words3)
    unique_words4 , size4 = Counting_Words(words4)
    unique_words5 , size5 = Counting_Words(words5)
    unique_words6 , size6 = Counting_Words(words6)
    unique_words7 , size7 = Counting_Words(words7)
    unique_words8 , size8 = Counting_Words(words8)
    unique_words9 , size9 = Counting_Words(words9)
    unique_words10 , size10 = Counting_Words(words10)
    

    matrix = Calculate_Frequency_Matrix(unique_words1 , unique_words2 , unique_words3 , unique_words4 , unique_words5 , unique_words6
                                         , unique_words7 , unique_words8 , unique_words9 , unique_words10 , size1 , size2 , size3
                                          , size4 , size5 , size6 , size7 , size8 , size9 , size10)
    
    print(matrix)
    
if __name__ == "__main__":
    main()

