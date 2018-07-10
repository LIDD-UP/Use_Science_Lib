#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: linear_regression_plot.py
@time: 2018/7/10
"""

# 鸢尾花数据集做回归问题,seaborn自己内置了鸢尾花数据集
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# iris =sns.load_dataset('iris')
# sns.pairplot(iris) #他会统计出单个特征，特征与特征之间的分布情况；
# # 图画出来之后就是4*4形状的图；一共有16个图，对角线上是直方图，也就是自己和自己就是直方图，其他就是散点图；
#
# # kind = 'hex'比较好的了 ，当点过多之后需要显示点的分布情况；
#
# plt.show()


tips = sns.load_dataset('tips')

print(tips.head())

#规范不多，但是功能少，implot规范多但是功能多，
# sns.regplot(x='total_bill',y='tip',data=tips)
# 画图，x是那个，y轴是那个；data:是相应的数据；

#对于不太适合做回归分析的数据可以给他加上一个抖动，(x_jitter)小范围的浮动操作；
sns.regplot(x='size',y='tip',data=tips,x_jitter=1)





plt.show()


