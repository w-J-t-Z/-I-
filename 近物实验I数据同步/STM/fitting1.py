from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from sklearn import linear_model

def polyfit(x, y):
    x=x.reshape(-1,1)
    y=y.reshape(-1,1)
    linear = linear_model.LinearRegression()
    linear.fit(x, y)
    y_hat = linear.predict(x)
    y_mean = np.mean(y)
    SSR = 0
    SST = 0
    for i in range(len(y)):
        SSR += (y_hat[i] - y_mean) ** 2
        SST += (y[i] - y_mean) ** 2
    return linear.coef_[0],linear.intercept_,np.sqrt(SSR / SST)*np.sign(linear.coef_[0])

path=r'minimapoint.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['Sheet1']

pointmap=np.zeros((6,3,2),dtype="float32")

cells_range=ws1['A1':'F6']

temp=0
q=0
for i in cells_range:
    for j in range(6):
        pointmap[j,temp,q]=i[j].value
    if q==0:
        q=1
    else:
        q=0
        temp=temp+1

pointmap[5,2,:]=pointmap[5,1,:]

s1fitting=np.zeros((15,2))
s1fitting[0:6,:]=pointmap[:,0,:]
corx1=-pointmap[0,1,0]+s1fitting[5,0]
cory1=-pointmap[0,1,1]+s1fitting[5,1]
s1fitting[6:11,0]=pointmap[1:6,1,0]+corx1
s1fitting[6:11,1]=pointmap[1:6,1,1]+cory1
corx1=-pointmap[0,2,0]+s1fitting[10,0]
cory1=-pointmap[0,2,1]+s1fitting[10,1]
s1fitting[11:15,0]=pointmap[1:5,2,0]+corx1
s1fitting[11:15,1]=pointmap[1:5,2,1]+cory1

s1fitting[:,0]=-s1fitting[:,0]

#fitting
a1x,a0x,rx=polyfit(np.arange(15),s1fitting[:,0])
a1x,a0x,rx=a1x[0],a0x[0],rx[0]
print(a1x,a0x,rx)

a1y,a0y,ry=polyfit(np.arange(15),s1fitting[:,1])
a1y,a0y,ry=a1y[0],a0y[0],ry[0]
print(a1y,a0y,ry)



fig=plt.figure(num=1,figsize=(12,5))
ax1=fig.add_subplot(111)


ax1.scatter(range(15),s1fitting[:,0],s=100,color='b',label="y experiment")
ax1.scatter(range(15),s1fitting[:,1],s=100,color='orange',label="x experiment")
ax1.plot([0,14],[a0x,a1x*14+a0x],lw=3,color='green',label="y fitting")
ax1.plot([0,14],[a0y,a1y*14+a0y],lw=3,color='purple',label='x fitting')
ax1.text(4,-20,"$y_n$=%.2f n%.2f, r=%.6f"%(a1x,a0x,rx),fontsize=20)
ax1.text(6,200,"$x_n$=%.2f n+%.2f, r=%.6f"%(a1y,a0y,ry),fontsize=20)

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(1)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(1)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(50)
y1_minor_locator=MultipleLocator(10)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)

ax1.set_xlim(xmin = 0, xmax = 15)
ax1.set_ylim(ymin = -100, ymax = 650)

ax1.set_ylabel("$x_n$ or $y_n$ (pixel)",fontsize=25)
ax1.set_xlabel("n",fontsize=25)
ax1.legend(loc="upper left",fontsize=20)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.show()








