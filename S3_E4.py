# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:40:34 2020

@author: 100jjad


..........Sajjad Soheyli.........Series.....03.............Exercise....04...........


WordCloud Plot for Each Text Document File 



"""
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt


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



def WordCloud_Plot(txt = ""):
     wordcloud = WordCloud(max_font_size=50 , max_words=2000 , background_color="white").generate(txt)
     
     plt.figure()
     plt.imshow(wordcloud , interpolation = "bilinear")
     plt.axis("off")
     plt.show()


def main():
        
    global txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10,words1,words2,words3,words4,words5,words6,words7,words8,words9,words10
    
    Data_Read()
    
    WordCloud_Plot(txt1)
    WordCloud_Plot(txt2)
    WordCloud_Plot(txt3)
    WordCloud_Plot(txt4)
    WordCloud_Plot(txt5)
    WordCloud_Plot(txt6)
    WordCloud_Plot(txt7)
    WordCloud_Plot(txt8)
    WordCloud_Plot(txt9)
    WordCloud_Plot(txt10)
    
    
    
if __name__ == "__main__":
    main()

