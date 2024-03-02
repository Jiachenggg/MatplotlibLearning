import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
# ax = Axes3D(fig)  # 弃用
ax = Axes3D(fig, auto_add_to_figure=False)  # 创建一个三维坐标轴对象
fig.add_axes(ax)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)

R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)  # height value

"""
    使用plot_surface函数绘制三维曲面图：
    rstride=1和cstride=1表示网格线的步长，这里设置为1。
    cmap=plt.get_cmap('rainbow')表示使用彩虹色映射来表示曲面图的高度。
"""
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
"""
    使用contour函数在Z轴方向上绘制等高线：
    zdir='z'表示在Z轴方向上绘制等高线。
    offset=-2表示等高线的起始高度。
    cmap='rainbow'表示使用彩虹色映射来表示等高线的高度。
"""
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)

plt.show()
