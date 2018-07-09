#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: numpy_test.py
@time: 2018/7/9
"""

import numpy as np

'''
house_info = np.genfromtxt('test_house_info.csv',delimiter=',',dtype='str')

print(type(house_info))
print(house_info)
'''

# 在使用一个函数的时候要去查文档；不断去积累，也就是说可以用到help函数去查看官方的文档；

# 矩阵操作：核心结构就是array，也就是ndarray

#在array定义中，如果传入一个一维的数组，即list只有一个list内部没有嵌套list这是后通常称之为向量（vector）
# 如果传入的是一个list 0f list 的结构则是matricx矩阵的结构，是一个ndarray的结构；

#还有一个shape属性特别重要；
vector = np.array([1,2,3,4,5])
metrix = np.array([[2,3,4],[1,3,4]])
# 一维和多维的形状有很大区别；在神经网络中就是因为这个错线了很多的坑；
print(vector.shape)
print(metrix.shape)
# 在ndarray中只能是相同类型的数
# 读取文件用pandas比numpy好用且简单许多；
#numpy读取的数是矩阵；

print(vector[1])
print(metrix[1][2])
print(metrix[1,2])

list_a = list([[2,3,4],[1,3,4]])

#print(list_a[1,2]) #报错：TypeError: list indices must be integers or slices, not tuple

#numpy也接受切片操作；与python的一样；

print(metrix[:,1]) #用：占位，表示所有，或者：前后也有数，表示几到几；

