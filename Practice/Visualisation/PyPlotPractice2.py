# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:22:11 2019

@author: Keya
"""

data = {'a': np.arange(50),
        'c': np.random.randint(0, 10, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 100 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
print(data['a'])
print(data['b'])
plt.scatter('a', 'b', c='c', s='d', data=data)

plt.show()