#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: some_function_fo_numpy.py
@time: 2018/7/9
"""

import numpy as np

# b = np.arange(3)
# print(np.exp(b)) #也就是求e的多少次幂
# print(np.sqrt(b)) # 也就是求平方根

#对于一个多维度的矩阵可以通过a.ravel()把他转换成一维的向量；但是感觉没啥必要完全可以通过reshape也可以完成；同时flatten也有这样的效果；
# b = np.ones((2,3))
# print(b)
# print(b.ravel())
# print(b.flatten())

# 通过vstack可以把 多行进行拼接在一起；
# 如：
# c = np.ones((2,3))
# print(np.vstack((b,c))) #按照行进行拼接的，按照列进行拼接就是通过hstack进行凭借，样本的拼接
# print(np.hstack((b,c))) # 特征的拼接

#切分数据：
# split_a = np.ones((2,3))
#
# print(np.hsplit(split_a,3)) # 平均的分成几块
# #还可以再某个地方指定切分；按行的
# print(np.vsplit(split_a,(1,2))) # 也就是再第一行切一刀，再在第二行切一刀；


# 赋值的操作容易出现的错误：
# a = np.arange(12)
# b = a
# print(b is a)
# b.shape = 3,4
# a.shape=4,3
# print(a.shape,b.shape)
# print(id(a))
# print(id(b))
# # 以上操作，a和b其实是完全相同的，只不过命名不一样，内存地址是完全相同的；


# 创建一个值相同的，但是内存地址不同的数据变量；
# a = np.arange(12)
# c = a.view() # 利用浅复制的方式，让c不完全等于a,只是只有数据相同，内村地址不同；
# print(c is a )
# c.shape=3,4
# print(a.shape)
# c[0,3] =1234
# print(a)
# print(id(c))
# print(id(a))
# # 以上是表示浅拷贝，不会造成


# 还有通过a.copy()来进行赋值；
# a = np.arange(12)
# d = a.copy()
# print(d is a)

# 以上解决的是，对于变量赋值的时候如果要想两个变量的值初始值相等，但是后续的操作两个变量没有关系，则用copy反之则用=号


np.argmax(axis=0) #返回列中最大值的下标0：按列进行找，1：按行进行找

np.tile(a,(2,3))#将a矩阵的行变成原来的两倍，列变成原来的3倍；

# np.sort(axis=1) 按行排序，0：按列排序；

