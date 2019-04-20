# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:43:59 2019

@author: Keya
"""
import thinkplot
import thinkstats2

from pandas import Series
from collections import Counter

histogram = {}

t = Series([10, 12, 13, 10, 15, 12, 19, 19, 12, 19, 15, 19])
t1 = Series([10.2, 12.5, 13, 10, 15, 12.8, 13, 13, 19, 12.3, 19, 15, 12.3])
for x in t:
    histogram[x] = histogram.get(x, 0) + 1

print(histogram.items())

hist = thinkstats2.Hist(t1)
thinkplot.Hist(hist)
thinkplot.Show(xlabel='value' , ylabel='frequency')


counter = Counter(t1)

print(counter)