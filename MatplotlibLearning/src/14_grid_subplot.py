import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1:subplot2grid
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3, rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')

ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2),rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3),(2,1))

# method 2:gridspec
# plt.figure()
# gs = gridspec.GridSpec(3,3)
# ax1 = plt.subplot(gs[0,:])
# ax2 = plt.subplot(gs[1,:2])
# ax3 = plt.subplot(gs[1:,2])
# ax4 = plt.subplot(gs[-1,0])  # 创建一个位于网格布局的最后一行第一列的子图对象ax4
# ax5 = plt.subplot(gs[-1,-2])  # 创建一个位于网格布局的最后一行倒数第二列的子图对象ax5

# method 3:easy to define structure
# f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True,
#                                                sharey=True)  # 创建一个包含2行2列的子图布局，并将每个子图对象分别赋值给ax11、ax12、ax21和ax22变量
# ax11.scatter([1, 2], [1, 2])
#
# plt.tight_layout()  # 调整子图布局，使其适应窗口

plt.show()
