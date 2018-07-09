#-*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: init_metrix.py
@time: 2018/7/9
"""

import numpy as np


a = np.zeros([3,2]) #注意里面参数接收一个元祖或者是一个list（列表），不能直接给几逗号几直接给；
print(a) # 零矩阵，默认创建的都是float的举证；

b = np.ones((2,3,4),dtype=np.int32) # 不能直接写int32，而是np.int32
print(b) # 1矩阵

c = np.arange(10,40,5) # 创建一个连续的数；
#传进来的数必须是相同类型的；

e= np.random.random((2,3)) #随机的模块；构造一个权重矩阵，初始化有高斯和均匀；注意random模块也是接受的是一个元祖或者是一个列表（-1，1）之间
print(e)

f = np.linspace(0,2*3.14,100) # 在一个区间内（0，2*3.14）中平均找100个点；
print(f)

# numpy的加减乘除
# 对于两个维度是一样的numpy矩阵，则是对应元素位置相减
#如：
substract_m = np.zeros((2,3))
substract_m2 = np.ones((2,3))

print(substract_m-substract_m2)

# 那么就让他减一个数值也是可以的
sub_value = substract_m2-2  #相当于每一个元素都做了同样的操作；
print(sub_value)

# 乘法操作也是一样的：也是所有的元素都进行一样的操作；
# 对于判断也是所有的元素进行操作；

# random.random相当于到了random模块下再使用该模块下的函数；

# 对于矩阵a*b的操作就是一个求内积的过程，也就是对应元素相乘；
# 矩阵的操作就是，a.dot(b) 矩阵乘法行乘以列；也可以np.dot(a,b)两种都是可以的





