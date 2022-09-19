from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter

path=r'data_NaI.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['SingleChannel']

cells_range=ws1['A2':'B81']

threshold=np.zeros(80)
counting=np.zeros(80)
"""
temp=0
for i in cells_range:
    threshold[temp]=i[0].value
    counting[temp]=i[1].value
    temp+=1
"""

counting=np.random.rand(80)
threshold=np.linspace(0.1,8.0,80)

fig=plt.figure(num=1,figsize=(8,8))
ax1=fig.add_subplot(111)
bar_width=0.1  # 条形宽度
ax1.bar(threshold,counting,label='单道统计结果',ec='#A0522D',width=bar_width,align='edge',color='#FFB6C1')
#ax1.set_title("initial wave shape")
#ax1.legend()

plt.show()