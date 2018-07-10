#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: head_map.py
@time: 2018/7/10
"""

import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 绘制热度图：heat map

# 离散的数据：
# 在那个点值比较大，哪个店值比较小，用颜色的深浅来表示；

unifom_data=np.random.rand(3,3)
print(unifom_data)
# 二维点的情况,查看值的大小,一眼就看出来了;
# heatmap = sns.heatmap(unifom_data)
#调色板最大和最小的设置:vmin,vmax
# heatmap = sns.heatmap(unifom_data,vmin=0.2,vmax=0.5) #这样就可以得到,超过某个最大值就大于跟最大值一个颜色,低于最小值,就跟最小值一个颜色;

# heatmap = sns.heatmap(unifom_data,center=0) #指定中心值

flights = sns.load_dataset('flights')
flights.head()
flights = flights.pivot('month','year','passengers')
print(flights)
# ax = sns.heatmap(flights)

# 显示热度图中的的值;
# ax = sns.heatmap(flights,annot=True,fmt='d') #把 热度图里面的值显示值,fmt ='d' 默认的时科学计算法,直接用数字表示;
#还可以指定格子之间的间距:linewidths
# ax = sns.heatmap(flights,annot=True,fmt='d',linewidths=5)
# 可以指定自己的调色板:cmap
# ax = sns.heatmap(flights,annot=True,fmt='d',cmap='YlGnBu') #把 热度图里面的值显示值,fmt ='d' 默认的时科学计算法,直接用数字表示;
#还可以隐藏cbar
ax  = sns.heatmap(flights,cbar=False)# 显示不显示colorbar
#最好不要隐藏他,

#可以使用pandas求出相关系数之后再用热度图画出来,相关系数可以是变量之间的也可以是变量和因变量之间的;










plt.show()
