import matplotlib.pyplot as plt
import numpy as np
from palettable.colorbrewer.qualitative import Pastel1_7


def draw_donut(labels, values):
    """ Draws a donut chart """
    plt.rcdefaults()

    # draw a pie using data, the color palette comes from "palettable" module
    plt.pie(values, labels=labels, colors=Pastel1_7.hex_colors)

    # draw a white inner circle, which draws a hole in the center of the pie chart,
    # which makes it look like a donut
    p = plt.gcf()
    inner_circle = plt.Circle((0, 0), 0.7, color='white')
    p.gca().add_artist(inner_circle)

    p.gca().set_aspect('equal')
    plt.show()


def draw_bar_chart(title, y_label, x_labels, data):
    plt.rcdefaults()

    x_axis = x_labels
    y_axis = data

    y_pos = np.arange(len(y_axis))

    plt.bar(y_pos, y_axis, align="center")

    plt.xticks(y_pos, x_axis)
    plt.ylabel(y_label)

    plt.title(title)

    plt.show()
