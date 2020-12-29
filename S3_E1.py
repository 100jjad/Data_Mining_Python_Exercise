# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 13:02:31 2020

@author: 100jjad


..........Sajjad Soheyli.........Series.....03.............Exercise....01...........


Preprocess for All Text Document

"""
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
    txt = re.sub("[1234567890~`!@#$%^&*()-_+={}\/:;'<>,.?]","",temp)
    
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


def Show_Words(matrix =[] , title = ""):

    print("\n\n" , title , "\n\n")
    print(matrix)   
    print("=============================================================")


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
    
    Show_Words(words1 , "PreProcced Text 1")
    Show_Words(words2 , "PreProcced Text 2")
    Show_Words(words3 , "PreProcced Text 3")
    Show_Words(words4 , "PreProcced Text 4")
    Show_Words(words5 , "PreProcced Text 5")
    Show_Words(words6 , "PreProcced Text 6")
    Show_Words(words7 , "PreProcced Text 7")
    Show_Words(words8 , "PreProcced Text 8")
    Show_Words(words9 , "PreProcced Text 9")
    Show_Words(words10 , "PreProcced Text 10")
    
    
if __name__ == "__main__":
    main()

