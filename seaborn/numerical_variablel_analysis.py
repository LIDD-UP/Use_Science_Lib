#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: numerical_variablel_analysis.py
@time: 2018/7/10
"""
# 对于连续值的分析绘图；
# 对于类别值的绘制；

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
print(tips.head())

#对于类别我们可以使用stipplot 来画成散点图
# sns.stripplot(x='day',y='total_bill',data=tips)
# 但是不可取，这是由于数据量过大的时候容易导致图像变成一条直线
# sns.stripplot(x='day',y='total_bill',data=tips,jitter=True) #将点进行随机的偏动，可以清晰的看出

#化成一个树状的结构；
# sns.swarmplot(x='day',y='total_bill',hue='sex' ,data=tips) #hue是指定一个指标，进行分类，把属于sex下那一类的点进行分别用颜色表示
#还可以横着画图和竖着画图；

#盒图：IQR即统计学概念四分卫距，第一/四分位与第三/四分位之间的距离；
# n = 1.5LQR 如果一个值>Q3+n 或者《 Q-N则为离群点；

# sns.boxplot(x='day',y='total_bill',hue='time',data=tips)
#如果有小菱形，就是离群点；


# 小提琴图
# sns.violinplot(x='total_bill',y='day',hue='time',data=tips) #越胖的地方值越多；
# split=True 把左右两边分开
# sns.violinplot(x='total_bill',y='day',hue='sex',data=tips,split=True) #越胖的地方值越多；

#除此之外还能将两个图何在一起画；
# 如：/
# sns.violinplot(x='day',y='total_bill',data=tips,inner=None)
# sns.swarmplot(x='day',y='total_bill',data=tips,color='w',alpha=0.1)  # alpha指定的是透明度


# 条形图，不是直方图，显示的是单个特征值的计量；
# 对于条形图则如下：
# sns.barplot(x='class',y='survived',data=titanic)
#以船舱类别为变换因素，以获救率为结果，以性别为指标

# 各自的变换：点图：能很好地描述差异性；
# sns.pointplot(x='sex',y='survived',hue='class',data=titanic)
#可以指定颜色；palette;,指定线型，linestyles;
#

# 盒图可以横着画也可以竖着画


# 多层面板分类图factorplot 可以花很多图，只需要指定kind的类别，如kind=bar等
# 这相当于整合了这些图
#size,大小，aspect，长宽比；

# 常用的参数：
'''
x,y,hue数据集变量，变量名称，hue是指标，根据这个指标能干什么；
date数据集 数据集名；
row，col更多分类变量进行平铺显示，变量名；
col_wrap 每行的最高平铺数，整数；
estimator 在每个分类中进行矢量到标量的映射，矢量，
ci 执行区间，浮点数或None
n_boot：计算执行区间时使用的引导迭代次数，整数；
units：采样单元的表示符，用于执行多级引导和重复测量涉及，数据变量或变量数据；
order，hue_order 对应排序列表，字符串列表；
row_order,col_order 对应排序列表字符串列表；
kind：可选，point默认，bar柱状图，count，频次，box，盒图，violin提琴图trip：散点图，swarm，分闪电，四则，每个面的高度，标量aspect纵横比，标量orent方向，v/h ,color颜色，matplotlib颜色，palette调色板，seaborn颜色色板或者是字典，
        legend hue 的信息面板True/Fasle legend_out 是否扩展图形，并将信息绘制在中心右边True/Falseshare(x,y)共享轴线TrueFalse,



'''



plt.show()