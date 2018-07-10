#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: box_figure.py
@time: 2018/7/10
"""

# 图：figure,digram,plot,graph

import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = os.path.dirname(os.getcwd())
file_name = '\house_info.csv'
house_info_path = file_path + file_name

house_info = pd.read_csv(house_info_path)
# print(house_info)
house_info.sort_values('price')



fig, ax = plt.subplots()
ax.boxplot(house_info['price'])
# ax.set_xticklabels(['price'])
# ax.set_ylim(0,5)
plt.show()