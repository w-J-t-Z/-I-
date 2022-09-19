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

cells_range=ws1['B2':'B1025']

counting=np.zeros(1024)
temp=0
for i in cells_range:
    counting[temp]=i[0].value
    temp+=1

channelId=np.arange(1,1025,1)

cc=savgol_filter(counting,31,3)

fig=plt.figure(num=1,figsize=(10,7))
ax1=fig.add_subplot(111)
#ax1.scatter(channelId,counting,s=3,color="red",label='experiment result')
ax1.plot(channelId,cc,color="orange",lw=2,label='savgol filtered result')
#ax1.plot([130.8,130.8],[3560,5560],color="black",lw=3)
#ax1.text(140.8,4560,"130.8",fontsize=20)

ax1.plot([452.9,452.9],[0,10530],"r--",lw=3)
ax1.text(457.9,10530,"452.9",fontsize=25)

ax1.plot([360,452.9],[10530,10530],"r--",lw=3)
ax1.plot([360,473.1],[5265,5265],"r--",lw=3)
ax1.plot([430.4,430.4],[0,5265],"r--",lw=3)
ax1.text(410,5265,"430.4",fontsize=25)
ax1.plot([473.1,473.1],[0,5265],"r--",lw=3)
ax1.text(478.1,5265,"473.1",fontsize=25)

#ax1.plot([852.6,852.6],[319,519],color="black",lw=3)
#ax1.text(862.6,419,"852.6",fontsize=20)

#ax1.set_xlabel("Channel ID",fontsize=25)
#ax1.set_ylabel("counting result (per 300 s)",fontsize=25)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(20)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(4)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(2000)
y1_minor_locator=MultipleLocator(400)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)
ax1.set_xlim(xmin = 400, xmax = 520)
ax1.set_ylim(ymin = 0, ymax = 12000)

#ax1.legend(loc="upper center",fontsize=20)

plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)

plt.show()