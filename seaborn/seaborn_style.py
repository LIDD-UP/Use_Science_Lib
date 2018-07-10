#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: seaborn_style.py
@time: 2018/7/10
"""

import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# % matplotlib inline #直接显示在图上

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*5)*(7-i)*flip)

# sns.set() #默认的

# seaborn 五种主题和风格
'''
darkgrid
whitegrid
dark
white
ticks :在上下左右加上一些线段；精确刻度
'''

sns.set_style('ticks')


data = np.random.normal(size=(20,4)) + np.arange(4)/2
# data = np.random.normal(size=(20,4))

print(data)
sns.boxplot(data=data)



sinplot()
sns.despine() #在画了之后才能去掉 ，去掉某些轴

#设置距离轴线的距离
sns.violinplot(data)
sns.despine(offset=10)

sns.despine(left=True) # 左边的轴隐藏

# 可以用with来指定风格，在with里面的是同一个风格，
# 其他的是不同


# 只能不同的大小；
# sns.set_context(font_scale)指定字体；


plt.show()


# 自己可以指定风格，最好用with打开，在这个with里面可以使用自己想要的风格其他的可以用其他的风格；

#默认值也比较好


