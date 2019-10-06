# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
print("輸入你出生日期")
for i in range(1,2):
    mo=input("月:")
    day=input("日:")
    if "十" and "10" in mo :
        if int(day) <23:
            print("天秤座")
        else:
            print("天蠍座")
    if "十一" and "11" in mo :
        if int(day) <22:
            print("天蠍座")
            break
        else:
            print("射手座")
            break
    if "十二" and "12" in mo :
        if int(day) <22:
            print("射手座")
            break
        else:
            print("魔羯座")
            break
    if "一" and "1" in mo :
        if int(day) <20:
            print("摩羯座")
        else:
            print("水瓶座")
    if "二" and "2" in mo :
        if int(day) <19:
            print("水瓶座")
        else:
            print("雙魚座")
    if "三" and "3" in mo :
        if int(day) <21:
            print("雙魚座")
        else:
            print("牡羊座")
    if "四" and "4" in mo :
        if int(day) <20:
            print("牡羊座")
        else:
            print("金牛座")
    if "五" and "5" in mo :
        if int(day) <21:
            print("金牛座")
        else:
            print("雙子座")
    if "六" and "6" in mo :
        if int(day) <21:
            print("雙子座")
        else:
            print("巨蟹座")
    if "七" and "7" in mo :
        if int(day) <23:
            print("巨蟹座")
        else:
            print("獅子座")
    if "八" and "8" in mo :
        if int(day) <23:
            print("獅子座")
        else:
            print("處女座")
    if "九" and "9" in mo :
        if int(day) <23:
            print("處女座")
        else:
            print("天秤座")
