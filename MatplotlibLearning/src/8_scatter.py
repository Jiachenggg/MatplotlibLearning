import numpy as np
import matplotlib.pyplot as plt

n = 1024
# 生成了一个包含 n 个元素的服从正态分布（均值为 0，标准差为 1）的随机数数组，存储在变量 X 和 Y 中。
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)  # for color value

# plt.scatter(X, Y, s=75, c=T, alpha=0.5)
plt.scatter(np.arange(5),np.arange(5))

# plt.xlim((-1.5,-1.5))
# plt.ylim((-1.5,-1.5))
# 隐藏 x, y轴的刻度标签
plt.xticks(())
plt.yticks(())

plt.show()
