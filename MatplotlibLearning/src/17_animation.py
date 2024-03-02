import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 10))  # 通过修改 line 对象的 y 值来实现正弦曲线的移动效果
    return line,


def init():
    line.set_ydata(np.sin(x))
    return line,


# 调用 animation.FuncAnimation 创建了一个动画对象 ani，并指定了动画的参数：fig 为图表对象，func 为动画函数，frames 为总帧数，init_func 为初始化函数，interval 为每帧之间的间隔时间，blit=True 表示只重新绘制发生变化的部分
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20,
                              blit=True)  # blit=True means only re-draw the parts that have changed

plt.show()
