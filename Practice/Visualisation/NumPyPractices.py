# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 15:28:01 2019

@author: Keya
"""

import numpy as np
import pandas as pd


s = pd.Series(['b', 'b', 'c', 'd', 'e', 'f'], [1, 3, 5, np.nan, 6, 8])

print(s[8])

print(s.value_counts())

for k, v in s.items():
    print(k, '=' , v)


d = {"lions" : 10, "tiger" : 20, "bear" : 5}
print(d)
print(d.items())
xs, freqs = zip(*sorted(d.items()))
ps = np.asarray(xs)
print(type(ps))
print(ps)
print(type(xs))
print(xs)

print(freqs)
s1 = np.cumsum(freqs, dtype=np.float)
print(s1)
print(type(s1))

s1 /= s1[-1]
print(s1)