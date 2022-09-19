from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate

path=r'data_NaI.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['calibration']

cells_range=ws1['A2':'H8']

threshold1=np.zeros(7)
counting1=np.zeros(7)
threshold2=np.zeros(7)
counting2=np.zeros(7)
threshold3=np.zeros(7)
counting3=np.zeros(7)
threshold4=np.zeros(7)
counting4=np.zeros(7)

temp=0
for i in cells_range:
    threshold1[temp]=i[0].value
    counting1[temp]=i[1].value
    threshold2[temp]=i[2].value
    counting2[temp]=i[3].value
    threshold3[temp]=i[4].value
    counting3[temp]=i[5].value
    threshold4[temp]=i[6].value
    counting4[temp]=i[7].value
    temp+=1

tck1=interpolate.splrep((threshold1+0.05)[::-1],(counting1)[::-1],k=3)
tt1=np.linspace(3.25,3.85,threshold1.size*10)
cc1=interpolate.splev(tt1,tck1,der=0)
tck2=interpolate.splrep((threshold2+0.05)[::-1],(counting2)[::-1],k=3)
tt2=np.linspace(0.85,1.45,threshold2.size*10)
cc2=interpolate.splev(tt2,tck2,der=0)
tck3=interpolate.splrep((threshold3+0.05)[::-1],(counting3)[::-1],k=3)
tt3=np.linspace(6.75,7.35,threshold3.size*10)
cc3=interpolate.splev(tt3,tck3,der=0)
tck4=interpolate.splrep((threshold4+0.05)[::-1],(counting4)[::-1],k=3)
tt4=np.linspace(5.95,6.55,threshold4.size*10)
cc4=interpolate.splev(tt4,tck4,der=0)


fig=plt.figure(num=1,figsize=(16,8))
ax1=fig.add_subplot(111)
bar_width=0.1  # 条形宽度
ax1.bar(threshold1,counting1,label='single channel Cs',width=bar_width,align='edge',color='#FFB6C1')
ax1.plot(tt1, cc1, "b--",lw=3, label="fitting result")
ax1.bar(threshold2,counting2,width=bar_width,align='edge',color='#FFB6C1')
ax1.plot(tt2, cc2, "b--",lw=3)
ax1.bar(threshold3,counting3,label='single channel Co',width=bar_width,align='edge',color='gold')
ax1.plot(tt3, cc3, "b--",lw=3)
ax1.bar(threshold4,counting4,width=bar_width,align='edge',color='gold')
ax1.plot(tt4, cc4, "b--",lw=3)
#ax1.set_title("initial wave shape")




ax1.legend(loc="upper left",fontsize=20)
#ax1.legend()
ax1.set_xlabel("threshold voltage (V)", fontsize=25)
ax1.set_ylabel("single channel counting (per 30 s)",fontsize=25)
ax1.set_ylim(ymin = 0, ymax = 30000)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.xlim(0,8.3)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(1)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(.2)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(5000)
y1_minor_locator=MultipleLocator(1000)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)


#开始拟合
Xp=[0.184,0.662,1.17,1.33]
EXp=[1.13,3.51,6.42,7.20]

ax2=ax1.twinx()

ax2.set_ylabel("peak energy X$_p$ (MeV)",fontsize=25)

ax2.plot([0.0805,8],[0,1.4775],color="black",lw=3,label="fitted calibration")
#ax2.plot(EXp,Xp,color="black",lw=3,label="fitted calibration")
ax2.errorbar(EXp,Xp,xerr=0.1,fmt="o",color="red",ms=10,ecolor="red",capsize=10,elinewidth=4,capthick=3,label="estimated peak position")
ax2.text(0.2,0.75,"X$_p$(V)=5.36E(X$_p$)(MeV)+0.0805,\n r=0.999546",fontsize=20)
#ax2.scatter(EXp,Xp,s=40,color="red",label="estimated peak position")
ax2.legend(loc="upper right",fontsize=20)
#ax2.legend()
ax2.set_ylim(ymin = 0, ymax = 2.0)

y2_major_locator=MultipleLocator(0.25)
y2_minor_locator=MultipleLocator(0.05)
#调用刻度设置
ax2.yaxis.set_minor_locator(y2_minor_locator)
ax2.yaxis.set_major_locator(y2_major_locator)

#plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()