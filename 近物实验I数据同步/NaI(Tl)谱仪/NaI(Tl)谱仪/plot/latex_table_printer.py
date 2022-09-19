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

for i in np.arange(40):
    print("%.2f & %d & %.2f & %d \\\\ "%(threshold[i], counting[i], threshold[i+40], counting[i+40]))