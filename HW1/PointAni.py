import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.1)
line, = ax.plot(x, np.sin(x))


def animate(i):
    # update the data.
    # 如果你打印一下i,就能明白为什么要设置为2
    if len(ax.lines) == 2:
        ax.lines.pop(1)
    ax.plot(x[i], np.sin(x)[i], 'o', color='red')
    return line, ax


ani = animation.FuncAnimation(
    fig, animate, frames=x.size, interval=100, blit=False, save_count=50)
plt.show()
