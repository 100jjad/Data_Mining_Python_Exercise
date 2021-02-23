# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 12:47:28 2021

@author: 100jjad
"""

from __future__ import unicode_literals
import pandas as pd
from hazm import *


cd = pd.DataFrame()
df = pd.DataFrame()

good_atr_db = ['بهترین', 'ارزش' , 'عالی ' , 'بصرفه' , 'پسند' ,'عاشق','ممنون','راضی','خوشحال','سریع','واضح','قوی','محکم','خوش',
          'کیفیت','خوب','فوق','نظیر'
          ,'بالا','راحت','پایین','طبیعی',
        'دمت','جذاب','زیبا', 'توپ','احسنت','شگفت','بهتر','بهترین', 'دوست','صحت'
,'قدرت','تحسین','لذت','معمولی','ماندگار','جالب','کاربردی','دوس']

bad_atr_db = ['اصلا','پشیمان' , 'پشیمون' ,'ضعیف','بد','اذیت', 'گرون','گران','ناراحت','فاجعه' , 'متاسف','متأسف' ,
        'افتضاح', 'کند','کلافه','مشکل','تعمیر','دشوار','ناراضی','بدتر','خراب','بدترین']

negativ_atr_db = [ 'نیست' , 'ندار' ,'نداشت','نشد','نبود','بی','نمیش','نا','نمیاد','نیومد','نمیکن']



def Read_Data():
    file_name = "D:\software\Anaconda Project\Final Project\comment.xlsx"

    dfs = pd.read_excel(file_name, sheet_name=None)
    my_list = [1,2,3]

    cd = dfs['result']
    df = dfs['result']
    cd['atr1'] = [my_list] * len(cd)
    cd['atr2'] = [my_list] * len(cd)
    cd['ext_atr'] = [my_list] * len(cd)
    cd['emojo_label'] = [my_list] * len(cd)

    for i in cd.index:
        cd['atr1'][i] , cd['atr2'][i] , cd['ext_atr'][i] = Attribute_Extract(cd['comment'][i])
        
        
    for i in cd.index:
        cd['emojo_label'][i] = Emoji_Labeling(cd['ext_atr'][i])
    
    
    
    return cd


def Attribute_Extract(comment = ""):
    attribute_list = []
    words_list2 = []
    words_list3 = []
    
    
    words_list = word_tokenize(str(comment))
#    words_list3 = tagger.tag(words_list)
    for i in words_list:
        if i != "":
            if len(i) != 1:
                words_list2.append(i)
                
    for w in words_list2:
        for i in good_atr_db:
            if i in w:            
                attribute_list.append(i)
                
    for w in words_list2:
        for i in bad_atr_db:
            if i in w:            
                attribute_list.append(i)
                
    return words_list , words_list2 , attribute_list


def Emoji_Labeling(atr = []):
    emoji = ""
    if len(atr) == 0:
        emoji = "\U0001f610"
        return emoji
    
    for i in range(0 , len(atr)):
        if atr[i] == "گران" or atr[i] == "گرون" :
            emoji = "\U0001F911"
            return emoji
        if atr[i] == 'فاجعه' or atr[i] == "بدترین" or atr[i] == "افتضاح" or atr[i] == "کلافه" or atr[i] == "اصلا": 
            emoji = "\U0001F621"
            return emoji
        if atr[i] == 'نظیر' or atr[i] == "عاشق" or atr[i] == "بهترین" or atr[i] == "عالی" or atr[i] == "عالیه" or atr[i] == "توپ" or atr[i] == "فوق" or atr[i] == "فوق العاده" or atr[i] == "شگفت" or atr[i] == "تحسین" or atr[i] == "احسنت" or atr[i] == "دمت" or atr[i] == "جذاب": 
            emoji = "\U0001F60D"
            return emoji
        if atr[i] == 'متأسف' or atr[i] == "متاسف" or atr[i] == "ناراحت" or atr[i] == "پشیمون" or atr[i] == "پشیمان" or atr[i] == "ناراضی" : 
            emoji = "\U0001F614"
            return emoji
        if atr[i] == 'خوشحال' or atr[i] == "راضی" or atr[i] == "خوش" or atr[i] == "خوب" or atr[i] == "ممنون" or atr[i] == "بهتر" or atr[i] == "زیبا" or atr[i] == "لذت" or atr[i] == "دوست" or atr[i] == "دوس": 
            emoji = "\U0001F60A"
            return emoji
        if atr[i] == 'محکم' or atr[i] == "مستحکم" or atr[i] == "قوی" or atr[i] == "واضح" or atr[i] == "سریع" or atr[i] == "پایین" or atr[i] == "راحت" or atr[i] == "بالا" or atr[i] == "صحت" or atr[i] == "کاربردی" or atr[i] == "جالب" or atr[i] == "ماندگار" or atr[i] == "قدرت": 
            emoji = "\U0001F44C"
            return emoji
        if atr[i] == 'بصرفه' or atr[i] == "ارزش" : 
            emoji = "\U0001F4B0"
            return emoji
        if atr[i] == "خراب" or atr[i] == "دشوار" or atr[i] == "ضعیف" or atr[i] == "بد" or atr[i] == "اذیت" or atr[i] == "تعمیر" or atr[i] == "مشکل" or atr[i] == "کند": 
            emoji = "\U0001F612"
            return emoji
            
    
    emoji = "\U0001F615"
    return emoji
    return




def main():
    
     global cd , df
     cd = Read_Data()
     
     df1 = pd.DataFrame(cd)
     df1.to_excel("output.xlsx") 
    
if __name__ == "__main__":
    main()

