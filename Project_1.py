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

atr_db = ['بهترین', 'ارزش' , 'عالی ' , 'بصرفه' , 'پسند' ,'عاشق','ممنون','راضی','خوشحال','سریع','واضح','قوی','محکم','خوش',
          'گرون','گران','کیفیت','خوب','فوق','ضعیف','بد','اذیت','پشیمون','پشیمان','نظیر'
          ,'راحت','متاسف','متأسف','خراب','بالا','راحت','ناراحت','فاجعه','پایین','طبیعی',
          'شگفت','اصلا','بدتر','بهتر','بدترین','بهترین', 'دوست','دشوار','ناراضی','صحت'
,'قدرت','کلافه','کند','تحسین','لذت','معمولی','ماندگار','جالب','تعمیر','مشکل','کاربردی','دوس']

negativ_atr_db = [ 'نیست' , 'ندار' ,'نداشت','نشد','نبود','بی','نمیش','نا','نمیاد','نیومد','نمیکن']



def Read_Data():
    file_name = "D:\software\Anaconda Project\Final Project\comment2.xlsx"

    dfs = pd.read_excel(file_name, sheet_name=None)
    my_list = [1,2,3]

    cd = dfs['result']
    df = dfs['result']
    cd['atr1'] = [my_list] * len(cd)
    cd['atr2'] = [my_list] * len(cd)
    cd['ext_atr'] = [my_list] * len(cd)


    for i in cd.index:
        cd['atr1'][i] , cd['atr2'][i] , cd['ext_atr'][i] = Attribute_Extract(cd['comment'][i])
    
    
    
    return cd


def Attribute_Extract(comment = ""):
    attribute_list = []
    words_list2 = []
    words_list3 = []
    
    
    words_list = word_tokenize(comment)
#    words_list3 = tagger.tag(words_list)
    for i in words_list:
        if i != "":
            if len(i) != 1:
                words_list2.append(i)
                
    for w in words_list2:
        for i in atr_db:
            if i in w:            
                attribute_list.append(i)
    
    for w in attribute_list:
        if w == "فوق":
            w = "فوق العاده"
        else if w == "دوس":
            w = "دوست"
        
                
                
    return words_list , words_list2 , attribute_list



def main():
    
     global cd , df
     cd = Read_Data()
     
     df1 = pd.DataFrame(cd)
     df1.to_excel("output.xlsx") 
    
if __name__ == "__main__":
    main()

