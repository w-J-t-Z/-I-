from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate


path=r'data_NaI.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['MultipleChannel']

cells_range=ws1['D2':'D1025']

counting=np.zeros(1024)
temp=0
for i in cells_range:
    counting[temp]=i[0].value
    temp+=1

channelId=np.arange(1,1025,1)

cc=savgol_filter(counting,31,3)

fig=plt.figure(num=1,figsize=(24,7))
ax1=fig.add_subplot(111)
#ax1.scatter(channelId,counting,s=3,color="red",label='experiment result')
ax1.plot(channelId,cc,color="blue",lw=2,label='(I) Co + Cs long distance')
ax1.plot([141.1,141.1],[1922,2122],color="red",lw=3)
ax1.text(151.1,2022,"141.1",fontsize=20)

ax1.plot([424.7,424.7],[0,1200],"r--",lw=3)
ax1.text(434.7,1200,"424.7",fontsize=20)

ax1.plot([744.8,744.8],[0,717],"r--",lw=3)
ax1.text(754.8,617,"754.8",fontsize=20)

ax1.plot([843,843],[0,513],"r--",lw=3)
ax1.text(853,413,"843.0",fontsize=20)

ax1.set_xlabel("Channel ID",fontsize=25)
ax1.set_ylabel("counting result (per 300 s)",fontsize=25)


#D finished
#begin C
cells_range=ws1['C2':'C1025']

counting=np.zeros(1024)
temp=0
for i in cells_range:
    counting[temp]=i[0].value
    temp+=1

channelId=np.arange(1,1025,1)

cc=savgol_filter(counting,31,3)
ax1.plot(channelId*424.7/434.4,cc,color="green",lw=2,label='(II) Cs long distance')

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(100)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(20)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(200)
y1_minor_locator=MultipleLocator(40)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)
ax1.set_xlim(xmin = 0, xmax = 1024)
ax1.set_ylim(ymin = 0, ymax = 2300)

#begin A
ws1 = wb1['MultipleChannel']

cells_range2=ws1['A2':'A1025']

counting2=np.zeros(1024)
temp=0
for i in cells_range2:
    counting2[temp]=i[0].value
    temp+=1

channelId2=np.arange(1,1025,1)

cc2=savgol_filter(counting2,31,3)

ax1.plot(channelId2*843/852.6,cc2,color="purple",lw=2,label='(III) Co long distance')
ax1.plot([143.2,143.2],[1360,1560],color="red",lw=3)
ax1.text(153.2,1460,"143.2",fontsize=20)

ax1.plot([126.7,126.7],[591,791],color="red",lw=3)
ax1.text(136.7,691,"126.7",fontsize=20)

#ax1.plot([852.6,852.6],[319,519],color="black",lw=3)
#ax1.text(862.6,419,"852.6",fontsize=20)

#线性插值后计算A+C

tckA=interpolate.splrep(channelId2*843/852.6,cc2,k=1)
ttA=np.linspace(0,1025,1025)
ccA=interpolate.splev(ttA,tckA,der=0)

tckC=interpolate.splrep(channelId*424.7/434.4,cc,k=1)
ttC=np.linspace(0,1025,1025)
ccC=interpolate.splev(ttC,tckC,der=0)

ax1.plot(ttC,ccC+ccA,color="pink",lw=10,alpha=0.6,label='add up (II) & (III)')

#A+C finished
ax1.legend(loc="upper right",fontsize=20)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)

plt.show()