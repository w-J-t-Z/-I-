from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate

#开始拟合
n=[-4,-3,-2,-1,0,1,2,3]
Vn=[-72.9 , -54.0 , -36.9 , -18.0 , 0.0 , 18.0 , 36.3 , 54.6]


fig=plt.figure(num=1,figsize=(16,8))
ax1=fig.add_subplot(111)
ax1.plot([0,0],[-80,80],color="black",lw=3)
ax1.plot([-5,5],[0,0],color="black",lw=3)
ax1.plot([-4,3],[-72.725,54.5],color="blue",lw=3,label="fitted calibration")
#ax2.plot(EXp,Xp,color="black",lw=3,label="fitted calibration")
ax1.errorbar(n,Vn,yerr=0.4,fmt="o",color="red",ms=10,ecolor="red",capsize=10,elinewidth=4,capthick=3,label="estimated platform position")
ax1.text(1.5,0.75,"$V_n$($\mu$V)=18.175n-0.025,\n r=0.9999754",fontsize=20)
#ax2.scatter(EXp,Xp,s=40,color="red",label="estimated peak position")
ax1.legend(loc="upper left",fontsize=20)
#ax2.legend()


ax1.set_xlabel("platform number n", fontsize=25)
ax1.set_ylabel("platform voltage $V_n$ /$\mu$V",fontsize=25)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(1)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(1)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(10)
y1_minor_locator=MultipleLocator(2)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)
ax1.set_xlim(xmin = -5, xmax = 5)
ax1.set_ylim(ymin = -80, ymax = 80)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()