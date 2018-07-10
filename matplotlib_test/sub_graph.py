#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: sub_graph.py
@time: 2018/7/10
"""
#数据获取
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
house_info['listingDate'] = pd.to_datetime(house_info['listingDate'])
print(house_info[['listingDate','price']].head())

#只取出12数
first_twelve = house_info[['listingDate','price']]
# 排序，不然图没有规律，其实还可以把下标reset一下
first_twelve = first_twelve.sort_values('listingDate')
first_twelve = first_twelve.reset_index(drop=True)
print(first_twelve)





# 添加子图，在子图中画图
# 需要画出子图，一个图不能完全表示自己所需要的所有的意义；
# fig = plt.figure() #指定一个默认画图的区间，画图域
# fig = plt.figure(figsize=(3,3)) # 指定画图域大小
# ax1 = fig.add_subplot(2,1,1) #一维的是从上到下的
# ax2 = fig.add_subplot(2,2,2) # 二维的是从左到右，从上到下的图的组织结构；
# # ax3 = fig.add_subplot(3,3,9) #这三个参数：前两个是图片的区域，后一个是第几块图
# ax1.plot(np.random.randint(10,400,5),np.arange(5))
# ax2.plot(np.arange(10)*3,np.arange(10))
# plt.show()



# 在一个图中画两个折线图,并标明不同颜色先的标签，
# 比较完善的列子
fig = plt.figure(figsize=(10,6))
colors = ['red','blue','green','orange','black']

for i in range(5):
    start_index = i*12
    end_index = (i+1) * 12
    subset = first_twelve[start_index:end_index]
    label = str(2017+i)
    plt.plot(subset['listingDate'],subset['price'],c=colors[i],label = label)

plt.legend(loc='center')  # 用于显示不同颜色线的标签
plt.xlabel('price')
plt.ylabel('data')
plt.title('data-price')
plt.show()
