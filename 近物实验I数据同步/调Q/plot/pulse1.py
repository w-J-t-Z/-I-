#from itertools import count
from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate
from scipy.optimize import curve_fit

path=r'Q.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['LD']

cells_range=ws1['A2':'B41']

current1=np.zeros(40)
power1=np.zeros(40)

temp=0
for i in cells_range:
    current1[temp]=i[0].value
    power1[temp]=i[1].value
    temp+=1


ws2=wb1['pulse']
cells_range=ws2['A2':'D8']

current2=np.zeros(7)
powerAV=np.zeros(7)
#powerYAG=np.zeros(7)

temp=0
for i in cells_range:
    current2[temp]=i[0].value
    powerAV[temp]=i[1].value
    #powerYAG[temp]=i[2].value
    temp+=1

tt1=np.linspace(1,2.2,1024)
tck1=interpolate.splrep(current1,power1,k=3)
cc1=interpolate.splev(tt1,tck1,der=0)
cc12=interpolate.splev(current2,tck1,der=0)

tckAV=interpolate.splrep(current2,powerAV,k=3)
ccAV=interpolate.splev(tt1,tckAV,der=0)



fig=plt.figure(num=1,figsize=(24,7))
ax1=fig.add_subplot(111)
#ax1.plot(tt1,cc1*1000,lw=3,label="interpolate line")

ax1.plot(cc1*1000,ccAV,color="blue",lw=3,label="interpolate line $\overline{P}$")
ax1.errorbar(cc12*1000,powerAV,yerr=1,fmt="o",color="red",ms=10,ecolor="red",capsize=10,elinewidth=4,capthick=3,label="experiment points $\overline{P}$")



#ax1.plot([0.43,0.43],[0,250],lw=3,color="black")
#ax1.text(0.4,50,"I$_{th}$=0.43 A")

ax1.legend(loc="upper left",fontsize=15)
#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(250)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(50)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(25)
y1_minor_locator=MultipleLocator(5)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)

ax1.set_xlim(xmin = 200, xmax = 1500)
ax1.set_ylim(ymin = 0, ymax = 100)

ax1.set_ylabel("pulse laser average power $\overline{P}$(mW)",fontsize=25)
ax1.set_xlabel("LD power P$_{LD}$(mW)",fontsize=25)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


#begin B
ax2=ax1.twinx()

ax2.plot(cc1*1000,ccAV/cc1/1000,"g--",lw=3,label="efficiency interpolate line $\eta$")
#很不稳定, 估计功率的测量误差为1mW
ax2.errorbar(cc12*1000,powerAV/cc12/1000,yerr=(0.001/cc12+1/powerAV)*powerAV/cc12/1000,fmt="^",color="orange",ms=10,ecolor="orange",capsize=10,elinewidth=4,capthick=3,label=" efficiency experiment points $\eta$")

ax2.set_ylim(ymin = 0, ymax = 0.1)

y2_major_locator=MultipleLocator(0.02)
y2_minor_locator=MultipleLocator(0.004)
#调用刻度设置
ax2.yaxis.set_minor_locator(y2_minor_locator)
ax2.yaxis.set_major_locator(y2_major_locator)
ax2.set_ylabel("conversion efficiency $\eta$",fontsize=25)
ax2.legend(loc="upper right",fontsize=15)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()
