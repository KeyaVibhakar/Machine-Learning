# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:13:17 2019

@author: Keya
"""

import matplotlib.pyplot as plt
x=[1,4,5,6]
y=[2.4,4.5,5.9,6.9]

x2=[1.1,4.6,2.5,3.6]
y2=[2.4,1.3,3.2,6.3]

fig = plt.figure(1,figsize=(12,6))
#We use tuple unpacking with line, to get the first element of that list:
plt.subplot(131)
sp1,=plt.plot(x,y,linewidth=4.0,linestyle ='steps')
#sp1.set_antialiased(False)
plt.plot(x,y,linewidth=4.0,c='r',linestyle='--')

plt.subplot(133)
sp2,= plt.plot(x,y,linewidth=4.0)
sp2.set_antialiased(True)

plt.subplot(132)
plt.bar(x,y)
plt.show()
plt.close('all')
