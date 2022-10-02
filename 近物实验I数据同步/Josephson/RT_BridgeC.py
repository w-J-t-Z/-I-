from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate


path=r'data\RT bridge scan.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['RT bridge scan']

cells_range=ws1['A2':'B83']

V1=np.zeros(82)
V2=np.zeros(82)
temp=0
for i in cells_range:
    V1[temp]=i[0].value
    V2[temp]=i[1].value
    temp+=1

fig=plt.figure(num=1,figsize=(20,10))
ax1=fig.add_subplot(111)
ax1.plot(V1,V2,color="blue",lw=3,label='$V_J-V_T$ relation')
ax1.plot([19.8,19.8],[0,3],color="red",lw=3)
ax1.plot([24.1,24.1],[0,3],color="red",lw=3)
ax1.plot([101.8,101.8],[37.6-1.5,37.6+1.5],color="red",lw=3)
ax1.text(10,1,"19.8",fontsize=30)
ax1.text(25,1,"24.1",fontsize=30)
ax1.text(102,36,"101.8",fontsize=30)

ax1.set_xlabel("$V_T$ /mV",fontsize=25)
ax1.set_ylabel("$V_J$ /mV",fontsize=25)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(20)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(4)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(5)
y1_minor_locator=MultipleLocator(1)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)
ax1.set_xlim(xmin = 0, xmax = 120)
ax1.set_ylim(ymin = 0, ymax = 40)

ax1.legend(loc="upper center",fontsize=20)

plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

bwith=3
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)

plt.show()