# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
things=[]
thingsold=[]
prize=[]
cost=[]
real=[]
thing=input(">>你有幾項商品\n")
for i in range(0,int(thing)):
    things.append(0)
    thingsold.append(0)
    prize.append(0)
    cost.append(0)
    real.append(0)
for i in range(0,int(thing)):
    things[i]=input("商品名稱:")
    thingsold[i]=input("商品售出幾個:\n")
    prize[i]=input("商品售價:\n")
    cost[i]=input("商品成本:\n")
    a=int(prize[i])-int(cost[i])
    b=int(thingsold[i])*a
    real[i]=b
for i in range(0,int(thing)):
    print(("%s賺了%d元")%(things[i],real[i]))
