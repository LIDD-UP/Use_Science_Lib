#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: the_struct_of_Series.py
@time: 2018/7/9
"""

import pandas as pd

house_info = pd.read_csv('house_info.csv')

#其中的某一列或者是某一列就是series

# 对各个网站对电影的评分操作是什么

#  拿出其中一列是series
price = house_info['price']

# print(type(price))
# print(price.values)
# print(type(price.values))
#这说明pandas实在numpy的基础上来的，因为，Series的values值是numpy类型的；

from pandas import Series

series_custom = Series(price.values,index=house_info['province'].values)# 可以给每一个得分值指定一个索引；
# print(series_custom)
# print(series_custom['Ontario'])
#重新定义下标：
# reindex 是重新定义下标,下面是思路，由于不是具体的值，是字符，无法排序，所以但是一下还是思路；
# original_index = series_custom.index.tolist()
# print(original_index)
# sorted_index = sorted(original_index)
# sorted_by_inde = series_custom.reindex(sorted_index)
# print(sorted_by_inde)

# sort_index() 按键值排序，按值进行排序

# series 还可以相加

# dataframe可以当作所索引的；
# 字符也可以索引，并且也可以做切片，
# 这时候可以通过字符和数值进行取值
# Series操作让我有点懵，那个索引有点悬，多练习；才行；