# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 16:47:01 2022

@author: Clemira
"""

import pandas as pd

data = pd.read_csv("Negara.csv")

df = pd.DataFrame(data)
mean = df.groupby(["Benua"]).mean()
std = df.groupby(["Benua"]).std()

print(data)
print(mean)
print(std)
