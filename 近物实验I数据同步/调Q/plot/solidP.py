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


ws2=wb1['solidP']
cells_range=ws2['A2':'C19']

current2=np.zeros(18)
powerYVO4=np.zeros(18)
powerYAG=np.zeros(18)

temp=0
for i in cells_range:
    current2[temp]=i[0].value
    powerYVO4[temp]=i[1].value
    powerYAG[temp]=i[2].value
    temp+=1

tt1=np.linspace(0.5,2.2,1024)
tck1=interpolate.splrep(current1,power1,k=3)
cc1=interpolate.splev(tt1,tck1,der=0)
cc12=interpolate.splev(current2,tck1,der=0)

tckYVO4=interpolate.splrep(current2,powerYVO4,k=3)
ccYVO4=interpolate.splev(tt1,tckYVO4,der=0)

tckYAG=interpolate.splrep(current2,powerYAG,k=3)
ccYAG=interpolate.splev(tt1,tckYAG,der=0)




fig=plt.figure(num=1,figsize=(24,7))
ax1=fig.add_subplot(111)
#ax1.plot(tt1,cc1*1000,lw=3,label="interpolate line")

ax1.plot(cc1*1000,ccYVO4*1000,color="blue",lw=3,label="interpolate line YVO$_4$")
ax1.errorbar(cc12*1000,powerYVO4*1000,yerr=powerYVO4,fmt="o",color="red",ms=10,ecolor="red",capsize=10,elinewidth=4,capthick=3,label="experiment points YVO$_4$")

ax1.plot(cc1*1000,ccYAG*1000,color="green",lw=3,label="interpolate line YAG")
ax1.errorbar(cc12*1000,powerYAG*1000,yerr=powerYAG,fmt="s",color="orange",ms=10,ecolor="orange",capsize=10,elinewidth=4,capthick=3,label="experiment points YAG")


#ax1.plot([0.43,0.43],[0,250],lw=3,color="black")
#ax1.text(0.4,50,"I$_{th}$=0.43 A")

ax1.legend(loc="upper left",fontsize=10)
#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(250)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(50)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(50)
y1_minor_locator=MultipleLocator(10)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)

ax1.set_xlim(xmin = 0, xmax = 1500)
ax1.set_ylim(ymin = 0, ymax = 600)

ax1.set_ylabel("solid laser power P$_{Nd}$(mW)",fontsize=25)
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

ax2.plot(cc1*1000,ccYVO4/cc1,"C7--",lw=3,label="efficiency interpolate line YVO$_4$")
ax2.errorbar(cc12*1000,powerYVO4/cc12,yerr=(0.001/powerYVO4+0.001/cc12)*powerYVO4/cc12,fmt="^",color="C6",ms=10,ecolor="C6",capsize=10,elinewidth=4,capthick=3,label=" efficiency experiment points YVO$_4$")

ax2.plot(cc1*1000,ccYAG/cc1,"C5--",lw=3,label="efficiency interpolate line YAG")
ax2.errorbar(cc12*1000,powerYAG/cc12,yerr=(0.001/powerYAG+0.001/cc12)*powerYAG/cc12,fmt="v",color="C8",ms=10,ecolor="C8",capsize=10,elinewidth=4,capthick=3,label="efficiency experiment points YAG")

ax2.text(550,0.40,"$\eta_{YAG,max}$=0.366",fontsize=20)
ax2.text(700,0.37,"$\eta_{YVO4,max}$=0.362",fontsize=20)

ax2.set_ylim(ymin = 0, ymax = 0.6)


y2_major_locator=MultipleLocator(0.1)
y2_minor_locator=MultipleLocator(0.02)
#调用刻度设置
ax2.yaxis.set_minor_locator(y2_minor_locator)
ax2.yaxis.set_major_locator(y2_major_locator)
ax2.set_ylabel("conversion efficiency $\eta$",fontsize=25)
ax2.legend(loc="upper right",fontsize=10)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()
