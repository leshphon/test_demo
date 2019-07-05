import numpy as np
import matplotlib.pyplot as plt

'''-----------sine wave---------'''
# x = np.linspace(0, 4 * np.pi, 100)
# y1, y2 = np.sin(x), np.cos(x)
 
# plt.plot(x, y1)
# plt.plot(x, y2)
 
# plt.title('line chart')
# plt.xlabel('x')
# plt.ylabel('y')
 
# plt.show()

# x = np.linspace(0, 2*np.pi)
# y = np.sin(x)
# fig, (ax1, ax2) = plt.subplots(2)
# ax1.plot(x, y)
# ax2.plot(x, y)
# ax2.set_xlim([-1, 6])
# ax2.set_ylim([-1, 3])
# plt.show()

''' ---------------------------------------------------'''
# plt.plot([1,2,3,4], [1,4,9,16], 'ro')#x=[1,2,3,4],y=[1,4,9,16],'ro'表示红色的圆点

# #axis接收的list参数表示：[xmin, xmax, ymin, ymax] 

# plt.axis([0, 6, 0, 20])#设置x、y轴的长度，x轴为[0,6],y轴为[0,20]

# plt.show()

''' ------------------------散点图---------------------------'''

x = np.linspace(0, 2*np.pi)
y = x * (np.sin(x))
plt.scatter(x, y, color='red', marker='+')
plt.show()