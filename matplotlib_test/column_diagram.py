#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: column_diagram.py
@time: 2018/7/10
"""

# 把他当作是工具，注意里面参数的含义就行了；
# 值相同的频率记录出来，
# 也同时可以分区间来显示该区间段值的频率；

#比如价格，分区间统计出个数；得到bins,在统计
#注意盒图和饼状图的区别；
import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = os.path.dirname(os.getcwd())
file_name = '\house_info.csv'
house_info_path = file_path + file_name

house_info = pd.read_csv(house_info_path)
# print(house_info)
columns = ['price','expectedDealPrice']
print(house_info[columns][:5])

#等于不同值的数确定一个范围得到不同值区间的值个数；
# 对于sale类型和Lease类型的数的范围；

fig,ax = plt.subplots()
ax.hist(house_info['price'],range=(1,2),bins=20) #指定区间；
#setylim确认区间
plt.show()






