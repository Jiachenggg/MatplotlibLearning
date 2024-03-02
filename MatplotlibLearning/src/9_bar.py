import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):  # 将两个数组 X 和 Y1 中对应位置的值进行配对，形成一个元素为 (x, y1) 的元组
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')  # ha:horizontal alignment  va:vertical alignment

for x, y in zip(X, Y2):
    plt.text(x, -y - 0.05, '-%.2f' % y, ha='center', va='top')

plt.xticks(())
plt.yticks(())

plt.show()
