# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:21:02 2019

@author: Keya
"""
x1=[1,4,5,6]
y1=[2.4,4.5,5.9,6.9]

x2=[11,41,25,36]
y2=[24,45,59,69]

lines = plt.plot(x1, y1, x2, y2)
# use keyword args
plt.setp(lines[0], color='r', linewidth=2.0)
#plt.setp(lines[1], color='b', linewidth=2.0)
# or MATLAB style string value pairs
#plt.setp(lines, 'color', 'r', 'linewidth', 2.0)