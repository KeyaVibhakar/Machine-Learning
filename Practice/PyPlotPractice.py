# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:34:35 2019

@author: Keya
"""

import matplotlib.pyplot as plt
import numpy as np
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g^')
plt.axis([0, 6, 0, 20])
plt.ylabel('some numbers')
plt.show()
t = np.arange(0., 5., 0.2)
print(t)
print(type(t))

