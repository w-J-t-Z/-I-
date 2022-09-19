from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate

path=r'data_NaI.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['SingleChannel']

cells_range=ws1['A2':'B81']

threshold=np.zeros(80)
counting=np.zeros(80)

temp=0
for i in cells_range:
    threshold[temp]=i[0].value
    counting[temp]=i[1].value
    temp+=1

tck=interpolate.splrep((threshold+0.05)[::-1],(counting/30)[::-1],k=3)
tt=np.linspace(0.15,8.05,threshold.size*10)
cc=interpolate.splev(tt,tck,der=0)



fig=plt.figure(num=1,figsize=(8,4))
ax1=fig.add_subplot(111)
bar_width=0.1  # 条形宽度
ax1.bar(threshold,counting,label='single channel experiment result',width=bar_width,align='edge',color='#FFB6C1')
#ax1.set_title("initial wave shape")
#ax1.legend(loc="upper left",fontsize=20)
#ax1.legend()
#ax1.set_ylabel("single channel counting (per 30 s)",fontsize=25)
ax1.set_ylim(ymin = 0, ymax = 18000)
plt.xticks(fontsize=30)
plt.yticks(fontsize=20)

plt.xlim(5.8,8.2)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(.4)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(.08)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(5000)
y1_minor_locator=MultipleLocator(1000)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)


ax2=ax1.twinx()
ax2.plot(tt, cc, "b--",lw=3, label="fitting result")
ax2.plot([5,7.379],[255.5,255.5],"r--",lw=3)
ax2.plot([7.035,7.035],[0,511],"r--",lw=3)
ax2.text(7.135,511,"7.035",fontsize=20)
ax2.plot([6.683,6.683],[0,255.5],"r--",lw=3)
ax2.text(6.3,255.5,"6.683",fontsize=20)
ax2.plot([7.379,7.379],[0,255.5],"r--",lw=3)
ax2.text(7.479,255.5,"7.379",fontsize=20)
ax2.plot([5,7.035],[511,511],"r--",lw=3)

#ax2.set_ylabel("counting rate ($s^{-1}$)",fontsize=25)
#ax2.legend(loc="upper right",fontsize=20)
#ax2.legend()
ax2.set_ylim(ymin = 0, ymax = 600)

y2_major_locator=MultipleLocator(100)
y2_minor_locator=MultipleLocator(20)
#调用刻度设置
ax2.yaxis.set_minor_locator(y2_minor_locator)
ax2.yaxis.set_major_locator(y2_major_locator)

#plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()