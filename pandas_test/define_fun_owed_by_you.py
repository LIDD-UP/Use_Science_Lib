#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: define_fun_owed_by_you.py
@time: 2018/7/9
"""
'''
自定义 numpy函数模块；
'''

# 把排完序的数下标改成新的不要原来的；
# 通过，reset_index（drop=True)完成，drop=true就是把以前的下标舍弃了；

import pandas as pd
import numpy as np

house_info = pd.read_csv('house_info.csv')
# new_house_info = house_info.sort_values('price')
# print(new_house_info)
#
# new_house_info1 = new_house_info.reset_index(drop=True)
#
# print(new_house_info1)
#


#有一个需求，pandas得不到，可以通过apply来定义自定义函数
# apply就是自己定义了函数之后通过apply一下之后，就可以通过pandas对像进行操作了，

# 算出每一列的空值：
# def not_null_count(column):
#     column_null = pd.isnull(column)
#     null = column[column_null]
#     return len(null)
#
# column_null_count = house_info.apply(not_null_count)
# print(column_null_count )
#

# 通过apply可以定义很多操作

# 把连续值离散化比如年龄大于某个数是社么，或者小于某个数是是什么；

