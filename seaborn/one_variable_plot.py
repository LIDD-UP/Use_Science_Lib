#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: one_variable_plot.py
@time: 2018/7/10
"""

#单特征的分析；

# 直方图，柱形图
# 把这份数据画出来；

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file_path = os.path.dirname(os.getcwd())
print(file_path)
house_info_path = file_path+'\house_info.csv'
print(house_info_path)
house_info= pd.read_csv(house_info_path)
house_info = house_info.dropna()
price = house_info['price']
# sns.distplot(price,kde=False)  #核密度估计，kde若是没有是一个折线图，有了才是柱状图（直方图）
#通过指定bins分成多少等分
# sns.distplot(price,bins=10,kde=False)
# 写入fit 显示分布情况
# sns.distplot(price,kde=False,fit=)

# 根据均值后协方差生成数据
mean,cov = [0,1],[(1,5),(5,1)]
# data = np.random.multivariate_normal(mean,cov,200) #根据均值和协方差生成200个点；
# df = pd.DataFrame(data,columns={'x','y'})
#
# print(df)

# 查看一个特征用直方图较好

# 查看特征与特征的关系用散点图比较好；
# jointplot不仅能画出两个特征之间的散点图，还能画出各自特征的直方图
# sns.jointplot(x='x',y='y',data=df) #相关系数也能计算出来；

#散点图每个点大小都是一样，要想看出那块多，哪块少就要用到hex图了；


#通过jointplot下的hex图来展示散点图的分散程度，数据量比较大的时候
x, y = np.random.multivariate_normal(mean,cov,1000).T
with  sns.axes_style('white'):
    sns.jointplot(x=x,y=y,kind='hex',color='k')









plt.show()



