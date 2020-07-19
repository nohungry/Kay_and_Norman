import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df_accident = pd.read_excel("/Users/kayzhang/Downloads/第6屆ETC創意競賽資料/108年公警局所轄事故資料/108年國道(A1A2A3)事故資料.xlsx")
# df_accident.info()

# sns.countplot(df_accident[' 事故類型及型態子類別代碼'])
# plt.show()

sns.countplot(df_accident[' 發生-路線-公路名稱(國道/省道/縣道/鄉道)'], hue=df_accident[' 事故類型及型態子類別代碼'])
plt.show()