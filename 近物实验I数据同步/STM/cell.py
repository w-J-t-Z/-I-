from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from sklearn import linear_model

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

#figure

fig=plt.figure(num=1,figsize=(12,5))
ax1=fig.add_subplot(111)

#add arrows
for i in range(5):
    ax1.arrow(pointmap[i,0,1],-pointmap[i,0,0],(pointmap[i+1,0,1]-pointmap[i,0,1]),-(pointmap[i+1,0,0]-pointmap[i,0,0]),color='r',width=1,head_width=5,length_includes_head=True)

for i in range(5):
    ax1.arrow(pointmap[i,1,1],-pointmap[i,1,0],(pointmap[i+1,1,1]-pointmap[i,1,1]),-(pointmap[i+1,1,0]-pointmap[i,1,0]),color='r',width=1,head_width=5,length_includes_head=True)

for i in range(4):
    ax1.arrow(pointmap[i,2,1],-pointmap[i,2,0],(pointmap[i+1,2,1]-pointmap[i,2,1]),-(pointmap[i+1,2,0]-pointmap[i,2,0]),color='r',width=1,head_width=5,length_includes_head=True)

for i in range(6):
    ax1.arrow(pointmap[i,1,1],-pointmap[i,1,0],(pointmap[i,0,1]-pointmap[i,1,1]),-(pointmap[i,0,0]-pointmap[i,1,0]),color='green',width=1,head_width=5,length_includes_head=True)

for i in range(5):
    ax1.arrow(pointmap[i,2,1],-pointmap[i,2,0],(pointmap[i+1,1,1]-pointmap[i,2,1]),-(pointmap[i+1,1,0]-pointmap[i,2,0]),color='green',width=1,head_width=5,length_includes_head=True)

for i in range(1,6):
    ax1.arrow(pointmap[i,1,1],-pointmap[i,1,0],(pointmap[i-1,0,1]-pointmap[i,1,1]),-(pointmap[i-1,0,0]-pointmap[i,1,0]),color='purple',width=1,head_width=5,length_includes_head=True,fill=False)

for i in range(5):
    ax1.arrow(pointmap[i,2,1],-pointmap[i,2,0],(pointmap[i,1,1]-pointmap[i,2,1]),-(pointmap[i,1,0]-pointmap[i,2,0]),color='purple',width=1,head_width=5,length_includes_head=True,fill=False)



ax1.scatter(pointmap[:,:,1],-pointmap[:,:,0],s=200,marker="o",color="black")
#为了跟扫描图一致，这里y加一个负号方便看

#把x轴的主刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(50)
#把x轴的副刻度间隔设置为.2，并存在变量里
x_minor_locator=MultipleLocator(10)
#调用刻度设置
ax1.xaxis.set_minor_locator(x_minor_locator)
ax1.xaxis.set_major_locator(x_major_locator)

y1_major_locator=MultipleLocator(50)
y1_minor_locator=MultipleLocator(10)
#调用刻度设置
ax1.yaxis.set_minor_locator(y1_minor_locator)
ax1.yaxis.set_major_locator(y1_major_locator)

ax1.set_xlim(xmin = 0, xmax = 246)
ax1.set_ylim(ymin = -106, ymax = 0)

ax1.set_ylabel("y (pixel)",fontsize=25)
ax1.set_xlabel("x (pixel)",fontsize=25)

bwith=2
ax1.spines['bottom'].set_linewidth(bwith)
ax1.spines['left'].set_linewidth(bwith)
ax1.spines['top'].set_linewidth(bwith)
ax1.spines['right'].set_linewidth(bwith)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.show()



