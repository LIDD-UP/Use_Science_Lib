#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: line_graph.py
@time: 2018/7/10
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

file_path = os.path.dirname(os.getcwd())
print(file_path)
house_info_path = file_path+'\house_info.csv'
print(house_info_path)

# pandas有自带的日期转换的函数；#2017-07-08
house_info= pd.read_csv(house_info_path)
house_info['listingDate'] = pd.to_datetime(house_info['listingDate'])
print(house_info[['listingDate','price']].head())

#只取出12数
first_twelve = house_info[['listingDate','price']][0:12]
# 排序，不然图没有规律，其实还可以把下标reset一下
first_twelve = first_twelve.sort_values('listingDate')
first_twelve = first_twelve.reset_index(drop=True)
print(first_twelve)

# 画图，没有对图像的坐标轴进行处理，
# plt.plot(first_twelve['listingDate'],first_twelve['price'])
# plt.show()

# 对坐标进行变换
plt.plot(first_twelve['listingDate'],first_twelve['price'])
plt.xticks(rotation=45) #变换x坐标值显示形状，将他改为垂直与x轴的
plt.yticks(rotation=45)# 比那还y坐标形状将他改为与y轴成45度


#加上标题和x,y轴的含义：
plt.xlabel('listingDate')
plt.ylabel('price')
plt.title('datetime-price-graph')



plt.show()