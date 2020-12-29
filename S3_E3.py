# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:32:06 2020

@author: 100jjad


..........Sajjad Soheyli.........Series.....03.............Exercise....03...........


Entropy Calculation for Each Text Document File 


"""
import math
import re
from nltk.stem import PorterStemmer

txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10 = "","","","","","","","","",""
words1,words2,words3,words4,words5,words6,words7,words8,words9,words10 = [] , [] , [] , [] , [] , [] , [] , [] , [] , []

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


def Entropy_Calculation(words = [] , size = 1 , title = "" , words_number =1):
    
    Entropy = 0;
    
    print("\n\n" , title , "\n\n")
    
    for i in range(size-1):
        pi = words[1][i]/words_number
        logpi = math.log10(pi)
        temp = pi*logpi
        Entropy += temp
        
    Entropy = Entropy * (-1)
    
    print("\n\n",Entropy , "\n\n")
    print("\n\n====================================================================================\n\n")
    return Entropy



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
    
    
    Entropy_Calculation(unique_words1 , size1 , "Entropy For Text Document 1 : " , len(words1))
    Entropy_Calculation(unique_words2 , size2 , "Entropy For Text Document 2 : " , len(words2))
    Entropy_Calculation(unique_words3 , size3 , "Entropy For Text Document 3 : " , len(words3))
    Entropy_Calculation(unique_words4 , size4 , "Entropy For Text Document 4 : " , len(words4))
    Entropy_Calculation(unique_words5 , size5 , "Entropy For Text Document 5 : " , len(words5))
    Entropy_Calculation(unique_words6 , size6 , "Entropy For Text Document 6 : " , len(words6))
    Entropy_Calculation(unique_words7 , size7 , "Entropy For Text Document 7 : " , len(words7))
    Entropy_Calculation(unique_words8 , size8 , "Entropy For Text Document 8 : " , len(words8))
    Entropy_Calculation(unique_words9 , size9 , "Entropy For Text Document 9 : " , len(words9))
    Entropy_Calculation(unique_words10 , size10 , "Entropy For Text Document 10 : " , len(words10))
    
    
if __name__ == "__main__":
    main()

