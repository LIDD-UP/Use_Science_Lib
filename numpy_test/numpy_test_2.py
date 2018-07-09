#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: numpy_test_2.py
@time: 2018/7/9
"""

import numpy as np

# vector = np.array([2,4,6,6,])


# print(vector==10)
# [False False False False]
#从上面可以看出；numpy是把所有的数都拿出来进行比较；也就是分别进行比较的；


metric = np.array([[1,10,4,5],[1,4,5,10,]])
equal_to_ten = (metric==10)

print(equal_to_ten)
print(metric[equal_to_ten])
#这里相当于是把返回的值生成一个array的数组，然后再传入原来的数组中，把满足条件的值再取出来；

# & 和 |

# numpy中的类型转换：把string类型转换成float类型，也就是astype这个方法，实现类型之间的转换；

# 可以通过一些函数如vector.min,等来求的函数中的一些值
# 还有求和函数如：metrix.sum(axis =1)是按行来进行求和，或者是axis=0,是按列来进行求和； 指定维度或者是方向来求；

# 对于线性回归，误差是独立并且具有相同分布通常认为服从均值为0，方差是0^2 的高斯分布；

# 线性回归找极大似然函数

#也可以通过np.arange(15)来顶以一个排列或者是索引；

a = np.arange(13)
print(a)
#通过reshape函数可以改变矩阵的维度，
print(a.size) #打印出矩阵之中有多少个元素；
#数据经过很多步矩阵变换的时候出现，为了避免出现错误，其实可以将每一步的shape打印出来来计算；





