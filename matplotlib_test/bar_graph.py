#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: bar_graph.py
@time: 2018/7/10
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = os.path.dirname(os.getcwd())
print(file_path)
house_info_path = file_path+'\house_info.csv'
print(house_info_path)

# pandas有自带的日期转换的函数；#2017-07-08
house_info= pd.read_csv(house_info_path)

cols = ['province','price','expectedDealPrice']
num_cols  = cols[1:]
print(house_info[cols])

# 还简单的条形图
# 定义条形图的高度
# bar_heights = house_info.ix[0,num_cols].values
# print(bar_heights)
# #定义条形图的位置
# bar_position = np.arange(2)+0.75 #arange是默认产生从0，到4的整数 #定义有多少个条形；以及他的位置
# # print(np.arange(4))
# print(bar_position)
# fig,ax = plt.subplots()
# # print(help(plt.subplots()))
# ax.bar(bar_position,bar_heights,0.4)
# plt.show()

# 定义较为完善的条形图
bar_heights = house_info.ix[0,num_cols].values
print(bar_heights)
#定义条形图的位置
bar_position = np.arange(2)+0.75
#定义tick_postions
tick_postion = np.arange(2)+0.75
fig,ax = plt.subplots()

# ax.bar(bar_position,bar_heights,0.3) #画出条形图
ax.barh(bar_position,bar_heights,0.3) #横着画，但是要注意y——label和x_label已经变换了，要重新设置一下标签；
ax.set_yticks(tick_postion) # 该条条形x坐标轴的名称
ax.set_yticklabels(num_cols,rotation=45) # 设置名称的显示

ax.set_xlabel('price') #设置x 轴的名称
# ax.set_ylabel('price')
plt.ylabel('price_cate')
ax.set_title('average pice 0f price_category') #这只y 轴的名称

plt.show()