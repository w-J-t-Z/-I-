from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate


path=r'data\IV junction microwave scan(13).xlsx'
wb1 = load_workbook(path)
ws1 = wb1['IV junction microwave scan(13)']

cells_range=ws1['A2':'B92']

V1=np.zeros(91)
V2=np.zeros(91)
temp=0
for i in cells_range:
    V1[temp]=i[0].value
    V2[temp]=i[1].value
    temp+=1

fig=plt.figure(num=1,figsize=(15,10))
ax1=fig.add_subplot(111)

ax1.plot([-3,3],[0,0],color="black",lw=3)
ax1.plot([0,0],[-200,200],color="black",lw=3)
ax1.plot(V1/50,V2,color="blue",lw=3,label='$V_J-I_J$ relation')
#ax1.plot([-0.95,-0.95],[-20,20],color="red",lw=3)
#ax1.plot([1.2,1.2],[-20,20],color="red",lw=3)
#ax1.text(1.0,50,"1.20",fontsize=30)
#ax1.text(-1.3,50,"-0.95",fontsize=30)
#ax1.text(104,24,"103.8",fontsize=30)

ax1.set_xlabel("$I_J$ /mA",fontsize=25)
ax1.set_ylabel("$V_J$ /$\mu$V",fontsize=25)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(0.5)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(0.1)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(50)
y1_minor_locator=MultipleLocator(10)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)
ax1.set_xlim(xmin = -2, xmax = 2)
ax1.set_ylim(ymin = -120, ymax = 100)

ax1.legend(loc="upper left",fontsize=25)

plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

bwith=3
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)

plt.show()