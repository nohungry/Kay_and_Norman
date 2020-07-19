import xlrd
import pandas as pd
import re
import datetime

pd.reset_option("max_columns")

df_TrafficControl = pd.read_excel("/Users/kayzhang/Downloads/第6屆ETC創意競賽資料/108年高公局所轄各分局事故簡訊資料/108年_南區交控中心.xlsx")
df_TrafficControl['通報級數'] = df_TrafficControl['簡訊內容'].str.split(',').str.get(0).str[:6]
df_TrafficControl['簡訊日期'] = df_TrafficControl['簡訊內容'].str.split(',').str.get(0).str[6:]
df_TrafficControl['簡訊時間'] = df_TrafficControl['簡訊內容'].str.split(',').str.get(1).str[:5]

roadName = []
for road in df_TrafficControl['簡訊內容']:
    roadName.append(re.findall(r'國\d+', road))
roadName = ([i for road in roadName for i in road])
df_TrafficControl['公路名稱'] = pd.Series(roadName)

direction = []
for direct in range(len(df_TrafficControl['簡訊內容'])):
    if re.findall(r'[東西南北][上下向 ]', df_TrafficControl['簡訊內容'][direct]):
        direction.append(re.findall(r'[東西南北][上下向 ]', df_TrafficControl['簡訊內容'][direct]))
    else:
        direction.append([''])
direction = ([i for direct in direction for i in direct])
df_TrafficControl['向車道'] = pd.Series(direction)

solveTime = []
for time in range(len(df_TrafficControl['簡訊內容'])):
    solveTime.append(re.findall(r'\w\w:\w\w', df_TrafficControl['簡訊內容'][time])[-1])
df_TrafficControl['事故排除時間'] = pd.Series(solveTime)


# df_TrafficControl['Col3'] = df_TrafficControl['簡訊內容'].str.split(',').str.get(2)
df_TrafficControl = df_TrafficControl.drop(['簡訊內容'], axis=1)
# print(df_TrafficControl.head(30))
print(df_TrafficControl.info())

