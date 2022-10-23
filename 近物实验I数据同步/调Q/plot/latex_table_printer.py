from openpyxl import *
from openpyxl.styles import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from scipy.signal import savgol_filter
from scipy import interpolate

path=r'Q.xlsx'
wb1 = load_workbook(path)
ws1 = wb1['doulbe']

cells_range=ws1['A2':'B19']

threshold=np.zeros(18)
counting=np.zeros(18)
#uu=np.zeros(7)
#vv=np.zeros(7)

temp=0
for i in cells_range:
    threshold[temp]=i[0].value
    counting[temp]=i[1].value
    #uu[temp]=i[2].value
    #vv[temp]=i[3].value
    temp+=1

for i in np.arange(9):
    print("%.2f & %.2f & %.2f & %.2f  \\\\ "%(threshold[i], counting[i], threshold[i+9], counting[i+9]))