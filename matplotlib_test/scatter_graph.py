#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: scatter_graph.py
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
house_info= pd.read_csv(house_info_path)
print(house_info[['province','price']])

## 简单的散点图
# fig, ax = plt.subplots()
#
# ax.scatter(house_info['expectedDealPrice'],house_info['price'])
# ax.set_xlabel('province')
# ax.set_ylabel('price')
# plt.show()

## 加子图的闪电图； 相同的道理，只不过需要用到add_subplot



# DataFrame 相当于一个矩阵
#Series相当于DataFrame的一部分


# fig 和ax的区别； ax实际上是我们的具体操作；
# 而fig一般是设置一些参数的；
# 用ax画图的时候用fig来控制整体的形状

