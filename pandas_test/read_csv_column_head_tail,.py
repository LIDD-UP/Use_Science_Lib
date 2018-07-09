#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: read_csv_column_head_tail,.py
@time: 2018/7/9
"""

import pandas as pd
# 用于数据处理；
# pandas 底层很多都是基于numpy的

house_info = pd.read_csv('test_house_info.csv')
#代码和文件都在同一个文件夹下；
print(house_info)

# pandas 也是有一个核心结构：pandas/core。frame.DtaFrame

print(house_info.dtypes)
# 字符型的类型定义为了object,其实就是string 类型的结构；

head_data = house_info.head()# 取出前五行数据，也可以使用参数来指定显示几行；
print(head_data)

print(house_info.tail()) #打印后几行，也就是可以从前往后去，然后从后往前取；
print(house_info.columns) #取出所有的列名；
print(house_info.shape) # 显示当前数据的规模；



