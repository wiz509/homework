# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
s=list(range(1,50))
print("要買幾張電腦選號")
n=input(">>")
for i in range(0,int(n)):
    sh=random.sample(s,6)
    print(sh)
