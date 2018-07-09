#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: get_data_and_pre_processing_data.py
@time: 2018/7/9
"""
import pandas as pd

house_info = pd.read_csv('test_house_info.csv')

# print(house_info.loc[0]) #取出第一行的所有数，数前面是当前列的列名

#object 相当于string

# print(house_info.loc[3:6]) #取出第三行到第6行，注意行号是从0开始的；

#需求变了，要按列取数据了，
# print(house_info['province']) #pandas 读取数据的时候，如果不指定参数，他会把第一列指定为列名；通过列名来定位列

# 定位两个列
# 首先指定一个list来指出你需要拿出的列：['province','city']
# columns = ['province','city']
# print(house_info[columns]) #注意是两个中括号

# 查找那个单位是以单位结尾的；
# col_names = house_info.columns.tolist()
# print(col_names)
#
# gram_columns =[]
#
# for i in col_names:
#     if i.endswith('e'):
#         gram_columns.append(i)
# gram_df = house_info[gram_columns]
# print(gram_df.head(3))

# 读取文件 loc行定位，列定位；

#取出某一列数据进行操作；可以进行加减乘除等操作
# print(house_info['price'])
# div_1000 = house_info['price']/1000
#
# print(div_1000)


#还可以向dataframe中新加一列：就相当于字典操作一样，指定一个列明，后面再来一个列表就行l了
# ，但是这里不是单纯的列表而是DataFrame本来的结构；series.Series的类型；
# div_1000 = house_info['price']/1000
# print(type(div_1000))
# house_info['div_1000'] =div_1000
# print(house_info.shape)
# print(house_info)

# 加减乘除操作：如果维度相同则为对应元素相乘，如果不同，是一个，则为每一个与当前的相乘；
# print(house_info['price'].mean()) #还有其他操作，比如max.min之类的函数；

# 如果想要把数据归一化到0，1之间其实可以直接除以该列的最大值，就可以实现归一化0到1了；
# print(house_info['price']/house_info['price'].max()

# 对列进行排序操作
# house_info.sort_values('price',inplace=True)  # 参数只需要给出对应的列名就可以了；inplace是用来指定是否产生一个新的实例；
# #默认从小到大的排序，ascending=True，如果是false则是从大到小了；
# print(house_info['price'])

#pandas把NaN值认为是缺失值或者是没有的值，排序的时候一般把他放在后面；

# 做一些竞赛题，也是一种加分项


#泰坦尼克船员获救的事：分类任务，船票的编码基本没用；

# NaN怎么处理呢：
# age_is_null = pd.isnull(age) 判断是不是缺失值
#age_is_null_true = age[age_is_null]
#print(age_is_null_true)
#age_is_null_len = len(age_is_null_true)
#print(age_is_null_len)