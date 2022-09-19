import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

fig=plt.figure(num=1,figsize=(24,7))
ax1=fig.add_subplot(111)
ax1.plot([0,0.17,0.23,0.29,0.928,0.978,1.028,1.409,1.489,1.569,1.77,1.87,2,2.13],[5,5,10,5,5,7,5,5,10,5,5,0,20,0],lw=3)

ax1.text(0.21,10,"0.21",fontsize=20)
ax1.text(0.928,7,"0.978",fontsize=20)
ax1.text(1.409,10,"1.489",fontsize=20)
ax1.text(1.77,6,"1.77",fontsize=20)
ax1.text(1.95,20,"2.00",fontsize=20)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(0.5)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(0.1)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(5)
y1_minor_locator=MultipleLocator(1)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)

ax1.set_xlim(xmin = 0, xmax = 2.2)
ax1.set_ylim(ymin = 0, ymax = 25)

ax1.set_xlabel("signal energy (MeV)",fontsize=25)
ax1.set_ylabel("counting rate (relative value)",fontsize=25)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.show()
