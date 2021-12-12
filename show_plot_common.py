import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data_common.csv')
    x = data['x_hour']
    y1 = data['temperature']
    y2 = data['humidity']
    y3 = data['dust']

    plt.cla()

    plt.plot(x, y1, label='Temperature')
    plt.plot(x, y2, label='Humidity')
    plt.plot(x, y3, label='Dust')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
