import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, axes_lst = plt.subplots(3, 3)  # a figure with a 2x2 grid of Axes

for axis_subplot in axes_lst:
    print(axis_subplot)

