# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from arr_operate import OperateNum

operateNum = OperateNum() # create a instance of the class OperateNum
print(operateNum.isTwoNumPrime(6, 9)) # test code
ft1 = 1.5 * 1000 # unit is Hz
ft2 = 2.1 * 1000
fs = 8 * 1000
T1 = 1 / ft1
T2 = 1 / ft2
Ts = 1 / fs
# print(T1, T2)
N = 1
while(1):
    if((N * ft1) % fs == 0 and (N * ft2) % fs == 0 ):
        M1 = N / fs * ft1
        M2 = N / fs * ft2
        # if (N % M1 != 0 and N % M2 != 0):
        # if (operateNum.isTwoNumPrime(N, M1) == 1 and operateNum.isTwoNumPrime(N, M2) == 1):
        print("N = %d" % N)
        print('M1 = %d' % M1 )
        print('M2 = %d' % M2 )
        break
    # if (N == 1000000):
    #     break
    N += 1


# np.random.seed(1)
# x = np.arange(5)
# y = np.random.randn(5)

# fig, axes = plt.subplots(ncols=2, figsize=plt.figaspect(1./2))

# vert_bars = axes[0].bar(x, y, color='lightblue', align='center')
# horiz_bars = axes[1].barh(x, y, color='lightblue', align='center')
# #在水平或者垂直方向上画线
# axes[0].axhline(0, color='gray', linewidth=1)
# axes[1].axvline(0, color='gray', linewidth=1)
# plt.show()
