#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: genneric_pre_precess_data_way.py
@time: 2018/7/9
"""
'''
数据的预处理：
'''

# 如果没有进行数据预测里，比如算平均值在做除法操作的时候会算不出结果，算出来是一个nan
#自己进行除法可能出现Nan的情况，但是如果是通过mean函数求均值则不会出现这种情况；
import pandas as pd
import numpy as np

house_info = pd.read_csv('house_info.csv')
#
# house_info.sort_values('price',inplace=True)
# print(house_info['price'])
#
# price_mean = sum(house_info['price'])/len(house_info['price'])
# print(house_info['price'].mean())
# print(price_mean)


# 利用缺失值的填充情况 以及缺失值的一些常见处理方式：
# 可以直接去除缺失值再进行求均值；可以通过age_is_null 方法，也就是np.is_null()方法进行；
# 缺失值一般可以使用中位数，众数，或者是均值进行填充

#每一个船舱不同类型的均值，这是由于不同船舱可能价格相差太大，如果利用全部的价格求均值不是特别合理；所以，应该先分类再求均值；
#对应到房屋预测里面也是，对于出租类型和房屋类型的价格相差过大所以应该分开考虑；也可以对两种类型的房子分开考虑；

# 要想得到不同类别船舱的平均值：首先的要先
# 取出不同分类的行，即样本，然后在通过列来取得平均值；
# 如： Sale_rows = house_info[house_info['tradetype']=='Sale'])
# Sale_price_mean = Sale_rows['price'].mean

# 上面是传统的方法，那么pandas里面有没有好的方法呢：
#pivot_table方法，统计一个量和其他量一个关系的函数；感觉像是sql语句里面的where条件语句

# Sale_price = house_info.pivot_table(index='tradeTypeName',values='price',aggfunc=np.mean)
# print(Sale_price)
#这里的意思是以tradetypename 为基准，values统计的什么值，agggfun统计的值是和还是平均值，抑或是最小值等等；

# 那么如果想要统计一个量与多个两个关系，只需将values变成一个list。里面写上你想要统计的列就行了；

#filena 于dropna()一个是填充一个是丢失；

# 删除指定列的na值，采用dropna（axis=0,subset=[price,listdata])的方式

# 定位某一个样本某一列的值(也可以理解为某一行某一列的值）；如：
row_index_78_Sale = house_info.loc[78,'tradeTypeName']
print(row_index_78_Sale)

