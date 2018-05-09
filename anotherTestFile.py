"""
the purpose of the this file is to fully test the date_time_opreations


"""
import matplotlib.pyplot as plt
import numpy as np
linear_data = np.array([1,2,3,4,5,6,7,8])
quadratic_data = linear_data**2
plt.figure()
plt.plot(linear_data, '-o', quadratic_data, '-o')


"""
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

"""

