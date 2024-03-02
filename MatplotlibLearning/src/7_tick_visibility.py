import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y = 0.1 * x

plt.figure()
# zorder参数用于控制绘图元素的层级顺序。层级越高（数值越大），对应的绘图元素就会被绘制在更靠前的位置。
# 通过设置 zorder=1，可以调整标注文本和箭头的绘制顺序，使其显示在更上层的图层。
plt.plot(x, y, linewidth=10, zorder=1)

plt.ylim(-2, 2)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():  # 遍历 x 轴和 y 轴上的刻度标签
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.7, zorder=2))

plt.show()
