# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:11:01 2019

@author: Keya
"""

import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

print(t) 

# red dashes, blue squares and green triangles
plt.plot(t, t**3, 'r--')
plt.show()