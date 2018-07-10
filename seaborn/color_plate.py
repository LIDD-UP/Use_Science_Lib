#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: color_plate.py
@time: 2018/7/10
"""

import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize':(6,6)})

# 颜色也有离散性或者连续型的
# 渐变色来描述数据的重要性

# color_palette() 能传入任何matplotlib所支持的颜色；

# color_palette()不写参数则是默认颜色

# set_paplette() 设置所有图的颜色

# 分类色板
# current_palette = sns.color_palette()
# sns.palplot(current_palette)
# # current_palette 默认的6个颜色色板
# #普遍的是深色调；
#
# # 圆形画板：颜色主题多余6个时候需要使用
# # 最常用的方法是使用hls的颜色空间，这是TGB值的简单转换；
#
# sns.palplot(sns.color_palette('hls',8)) # 指定8个颜色分类；
#
# sns.palplot(sns.color_palette('hls',12))

# 如： 在实际画图的时候可以将color_palette传进去；
# data = np.random.normal(size=(20,8))+np.arange(8)/2
# sns.boxplot(data=data,palette=sns.color_palette('hls',8))
# # 分类画板的简单操作


# 指定亮度和饱和度
# l:lightness
#s 饱和度：saturation
#调整饱和度有问题：ValueError: RGBA values should be within 0-1 range

# sns.palplot(sns.hls_palette(2,l=2,s=1))

# 让颜色成对出现
# sns.palplot(sns.color_palette('Paired',8))

# 需要用颜色还是要看实际的需求





# --------------------------------》》》调色板设置
# 使用xkcd来命名颜色
# xkcd包含了一套众包努力的针对随机TGB色的命名，产生了954个可以随时通过xdcd_rgb字典中调用的命名颜色；

# 这一一套颜色命名方式，通过颜色命名来调用
# plt.plot([0,1],[0,1],sns.xkcd_rgb['pale red'],lw=3)

# 连续型的画板
# 即色彩岁数据变换，比如数据越来越重要则颜色越来越深

sns.palplot(sns.color_palette('Blues'))
#在color_palette中传入一个颜色就可以了，
# 这是由浅到深的过程
#如果想要调转过来则需要在颜色后面加入一个_r后缀
# 可以应用的数据的浮动情况，


#线性的调色板：
# sns.palplot(sns.color_palette('cubehelix',8))
#
# sns.palplot(sns.cubehelix_palette(8,start=5,rot=75))
# # 颜色的分布情况

# 颜色的深浅：
# light_palette('green')
# dart_palette('purple')

# reverse 反转颜色的变换情况


#画出一个等高线的颜色由深到浅的例子；
# x, y = np.random.multivariate_normal([0,0],[[1,-5],[-5,1]],size=300).T
# pal = sns.dark_palette('green',as_cmap=True)
# sns.kdeplot(x,y,cmap=pal)




plt.show()