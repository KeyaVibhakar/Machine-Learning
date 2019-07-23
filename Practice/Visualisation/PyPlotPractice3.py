# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:53:55 2019

@author: Keya
"""

import matplotlib.pyplot as plt

names = ['a', 'b', 'c']
values = [1, 10, 100]

plt.figure(1, figsize=(6, 6))

plt.subplot(241,label='one')
plt.bar(names, values)
plt.subplot(142)
plt.scatter(names, values)
plt.subplot(143)
plt.plot(names, values)
plt.grid(True)
plt.suptitle('Categorical Plotting')
print('figure 1 = ',plt.gcf())




plt.figure(2, figsize=(4, 4))

plt.subplot(221)
plt.bar(names, values)
plt.subplot(222)
plt.scatter(names, values)

plt.suptitle('Categorical Plotting')
print('figure 2 = ',plt.gcf())

fig=plt.figure(1)
plt.subplot(144)
plt.scatter(names, values)
plt.grid(True)
plt.show()
plt.close('all')

