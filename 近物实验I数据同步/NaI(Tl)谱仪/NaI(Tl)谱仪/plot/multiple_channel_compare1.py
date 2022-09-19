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
ax1.plot(channelId,cc,color="blue",lw=2,label='Co + Cs long distance')
ax1.plot([141.1,141.1],[1922,2122],color="red",lw=3)
ax1.text(151.1,2022,"141.1",fontsize=20)

ax1.plot([424.7,424.7],[0,1600],"r--",lw=3)
ax1.text(434.7,1600,"424.7",fontsize=20)

ax1.plot([744.8,744.8],[517,717],color="black",lw=3)
ax1.text(754.8,617,"754.8",fontsize=20)

ax1.plot([843,843],[313,513],color="black",lw=3)
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
ax1.plot(channelId*424.7/434.4,cc,color="green",lw=2,label='Cs long distance')

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

ax1.legend(loc="upper center",fontsize=20)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)

#begin B
ax2=ax1.twinx()

cells_range=ws1['B2':'B1025']

counting=np.zeros(1024)
temp=0
for i in cells_range:
    counting[temp]=i[0].value
    temp+=1

channelId=np.arange(1,1025,1)

cc=savgol_filter(counting,31,3)
ax2.plot(channelId*424.7/452.9,cc,color="orange",lw=2,label='Cs short distance')

ax2.plot([123.2,123.2],[3620,5320],color="red",lw=3)
ax2.text(60,4620,"123.2",fontsize=20)

ax2.plot([126.7,126.7],[3620,5320],color="red",lw=3)
ax2.text(136.7,4620,"126.7",fontsize=20)

ax2.set_ylim(ymin = 0, ymax = 15000)

y2_major_locator=MultipleLocator(2000)
y2_minor_locator=MultipleLocator(400)
#调用刻度设置
ax2.yaxis.set_minor_locator(y2_minor_locator)
ax2.yaxis.set_major_locator(y2_major_locator)
ax2.set_ylabel("counting result (per 300 s)",fontsize=25)
ax2.legend(loc="upper right",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()