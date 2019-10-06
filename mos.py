# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
letter={"a":"．-","b":"-．．．","c":"-．-．","d":"-．．","e":"．","f":"．．-．","g":"--．","h":"．．．．","i":"．．","j":"．---","k":"-．-","l":"．-．．","m":"--","n":"-．","o":"---","p":"．--．","q":"--．-","r":"．-．","s":"．．．","t":"-","u":"．．-","v":"．．．-","w":"．--","x":"-．．-","y":"-．--","z":"--．．","1":"．----","2":"．．---","3":"．．．--","4":"．．．．-","5":"．．．．．","6":"-．．．．","7":"--．．．","8":"---．．","9":"----．","0":"-----"}
print("要輸入幾個字")
n=input(">>")
print("請輸入")
d=list(input())
for i in range(0,int(n)):
    print(letter[d[i]])
