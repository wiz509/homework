# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
b = random.randint(4,30)
print("這個遊戲會隨機生成4到30的一個數字，最少減一最多減三，成功最後減為零的為贏家")
input("了解嗎?")
print(("有%d個")%(b))
if b%4 == 0 :
    print("你先拿")
    while b != 0 :
        a=input(">>")
        b=b-int(a)
        print(f"剩{int(b)}個")
        c=b%4
        print(f"電腦拿{int(c)}個")
        b=b-c
        print(f"剩{int(b)}個")
else:
    print("電腦先拿")
    while b != 0 :
        d=b%4
        print(f"電腦拿{int(d)}個")
        b=b-d
        print(f"剩{int(b)}個")
        if b == 0 :
            break
        a=input(">>")
        b=b-int(a)
        print(f"剩{int(b)}個")
print("你輸了")      
    
