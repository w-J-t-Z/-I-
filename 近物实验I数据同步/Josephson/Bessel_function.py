from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate
from scipy.special import jv

z=np.linspace(0,10,4096)

fig=plt.figure(num=1,figsize=(20,8))
ax1=fig.add_subplot(111)
ax1.plot(z,abs(jv(0,z)),"black",lw=3,label="$|\mathbf{J}_0(z)|$")
ax1.plot(z,abs(jv(1,z)),"b-",lw=3,label="$|\mathbf{J}_1(z)|$")
ax1.plot(z,abs(jv(2,z)),"g-",lw=3,label="$|\mathbf{J}_2(z)|$")
ax1.plot(z,abs(jv(3,z)),"purple",lw=3,label="$|\mathbf{J}_3(z)|$")
ax1.plot(z,abs(jv(4,z)),"orange",lw=3,label="$|\mathbf{J}_4(z)|$")
ax1.plot([1,1],[0,1],'r--',lw=3)
ax1.plot([1.6,1.6],[0,1],'r--',lw=3)
ax1.plot([2,2],[0,1],'r--',lw=3)

ax1.set_xlabel("z",fontsize=25)
ax1.set_ylabel("$|\mathbf{J}_n(z)|$",fontsize=25)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(1)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(0.2)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(0.1)
y1_minor_locator=MultipleLocator(0.02)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)
ax1.set_xlim(xmin = 0, xmax = 10)
ax1.set_ylim(ymin = 0, ymax = 1)

ax1.legend(loc="upper right",fontsize=20)

plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

bwith=3
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)

plt.show()