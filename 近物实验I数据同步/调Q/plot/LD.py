#from itertools import count
from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate
from scipy.optimize import curve_fit

def Fun(x,a,b):
    return a*x+b

path=r'Q.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['LD']

cells_range=ws1['A2':'B41']

threshold=np.zeros(40)
counting=np.zeros(40)

temp=0
for i in cells_range:
    threshold[temp]=i[0].value
    counting[temp]=i[1].value
    temp+=1


tck1=interpolate.splrep(threshold,counting,k=3)
tt1=np.linspace(0.0,2.2,threshold.size*10)
cc1=interpolate.splev(tt1,tck1,der=0)

tt2=np.linspace(0.42,2.2,threshold.size*10)
para,pcov=curve_fit(Fun,threshold[15:40],counting[15:40])
y_fitted = Fun(tt2,para[0],para[1])

fig=plt.figure(num=1,figsize=(24,7))
ax1=fig.add_subplot(111)
#ax1.plot(tt1,cc1*1000,lw=3,label="interpolate line")

ax1.plot(tt2,y_fitted*1000,lw=3,color="green",label="fitting line")

ax1.errorbar(threshold,counting*1000,yerr=counting,fmt="o",color="red",ms=10,ecolor="red",capsize=10,elinewidth=4,capthick=3,label="experiment points")
ax1.text(1.6,651,"P$_{LD}$(mW)=%.2f I(A) %.2f\n r=%.5f"%(para[0]*1000,para[1]*1000,0.99989),fontsize=20)

ax1.plot([0.43,0.43],[0,250],lw=3,color="black")
ax1.text(0.4,300,"I$_{th}$=0.43 A",fontsize=20)

ax1.legend(loc="upper left",fontsize=20)
#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(0.5)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(0.1)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(250)
y1_minor_locator=MultipleLocator(50)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)

ax1.set_xlim(xmin = 0, xmax = 2.5)
ax1.set_ylim(ymin = 0, ymax = 1500)

ax1.set_xlabel("excitation current I(A)",fontsize=25)
ax1.set_ylabel("LD power P$_{LD}$(mW)",fontsize=25)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()
