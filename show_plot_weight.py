from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data_weight.csv')
    x = data['x_hour']
    y1 = data['weight_ratio_flour']
    y2 = data['weight_ratio_sugar']
    y3 = data['weight_ratio_eggs']

    plt.cla()

    plt.plot(x, y1, label='Flour')
    plt.plot(x, y2, label='Sugar')
    plt.plot(x, y3, label='Eggs')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
