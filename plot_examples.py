#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:55:06 2017

@author: xuerjun
"""

import matplotlib as mpl
#print(mpl.get_backend())

import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

fig = Figure()
canvas =  FigureCanvasAgg(fig)

ax = fig.add_subplot(111)
ax.plot(3,2,'.')
canvas.print_png('test.png')


plt.figure()
plt.plot(3,2,'o')
ax = plt.gca()
ax.axis([0,6,0,10])

plt.figure()
plt.plot(1.5,1.5,'o')
plt.plot(2.5,2.5,'o')
plt.plot(0.5,0.5,'o')

#scatter
x = np.array([1,2,3,4,5,6,7,8])
y = x
colors = ['green']*len(x)
colors[len(x)-1] = 'red'

plt.figure()
plt.scatter(x,y,s =100, c = colors)

#zip generator
zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
list(zip_generator)
zip_generator = zip([1,2,3,4,5],[6,7,8,9,10])
x,y = zip(*zip_generator)

plt.figure()
plt.scatter(x[:2],y[:2],s=100, c='red', label = 'tall students')
plt.scatter(x[2:],y[2:],s=100, c='blue', label = 'short students')
plt.xlabel('x label is here')
plt.ylabel('y label is here')
plt.title('title is here')
plt.legend()
plt.legend(loc = 4, frameon = False, title = 'theLegend')



#line chart
linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2
plt.figure()
plt.plot(linear_data, '-o',quadratic_data,'-o')

plt.plot([22,44,55],'--r')
plt.xlabel('Some data')
plt.ylabel('Some data y')
plt.title('A title')
plt.legend(['baselline', 'compettition','aa'],loc = 2)
#plt.legend(loc = 2, frameon = True)
plt.gca().fill_between(range(len(linear_data)),linear_data, quadratic_data,facecolor='blue',alpha=0.25)

plt.figure()
obs_dates= np.arange('2017-01-01','2017-01-09',dtype = 'datetime64[D]')
obs_dates = list(map(pd.to_datetime,obs_dates))
plt.plot(obs_dates,linear_data,'o',obs_dates,quadratic_data,'o')

x = plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(90)

plt.xlabel('date')
plt.title("quadratic ($x^2$) vs. linear ($x$) ")
plt.ylabel('units')

#bar chart

#what is gcf





# sub plot






















