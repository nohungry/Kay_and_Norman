import xlrd
import pandas as pd
import re
from datetime import datetime


pd.reset_option("max_columns")

df_TrafficControl = pd.read_excel("/Users/kayzhang/Downloads/第6屆ETC創意競賽資料/108年高公局所轄各分局事故簡訊資料/108年_南區交控中心.xlsx")

dataLength = len(df_TrafficControl['簡訊內容'])


# 級數
content = []
for i in range(dataLength):
    content.append(re.findall(r'.*通報\d級', df_TrafficControl['簡訊內容'][i]))
content = ([j for con in content for j in con])
df_TrafficControl['通報級數'] = pd.Series(content)


# 時間
smsDate = []
startTime = []
endTime = []
for i in range(dataLength):
    smsDate.append(re.findall(r'\d\d/\d\d', df_TrafficControl['簡訊內容'][i]))
    startTime.append(re.findall(r'\d\d:\d\d', df_TrafficControl['簡訊內容'][i])[0])
    endTime.append(re.findall(r'\d\d:\d\d', df_TrafficControl['簡訊內容'][i])[-1])
smsDate = ([j for sms in smsDate for j in sms])
df_TrafficControl['簡訊日期'] = pd.Series(smsDate)
df_TrafficControl['簡訊時間'] = pd.Series(startTime)
df_TrafficControl['事故排除時間'] = pd.Series(endTime)

df_TrafficControl['簡訊時間_cul'] = pd.Series(startTime)
df_TrafficControl['事故排除時間_cul'] = pd.Series(endTime)
df_TrafficControl['處理耗時'] = pd.Series(endTime) # 先隨便給個符合dataFrame的格式

for i in range(dataLength):
    df_TrafficControl['簡訊時間_cul'][i] = datetime.strptime(df_TrafficControl['簡訊時間'][i], "%H:%M")
    df_TrafficControl['事故排除時間_cul'][i] = datetime.strptime(df_TrafficControl['事故排除時間'][i], "%H:%M")
    df_TrafficControl['處理耗時'][i] = (df_TrafficControl['事故排除時間_cul'][i] - df_TrafficControl['簡訊時間_cul'][i])

df_TrafficControl = df_TrafficControl.drop(['簡訊時間_cul'], axis=1)
df_TrafficControl = df_TrafficControl.drop(['事故排除時間_cul'], axis=1)


roadName = []
for road in df_TrafficControl['簡訊內容']:
    roadName.append(re.findall(r'國\d+', road))
roadName = ([i for road in roadName for i in road])
df_TrafficControl['公路名稱'] = pd.Series(roadName)


direction = []
for direct in range(dataLength):
    if re.findall(r'[東西南北][上下向 ]', df_TrafficControl['簡訊內容'][direct]):
        direction.append(re.findall(r'[東西南北][上下向 ]', df_TrafficControl['簡訊內容'][direct]))
    else:
        direction.append([''])
direction = ([i for direct in direction for i in direct])
df_TrafficControl['向車道'] = pd.Series(direction)


hurt = []
for i in range(dataLength):
    if re.findall(r'[無\d+]人受傷', df_TrafficControl['簡訊內容'][i]):
        hurt.append(re.findall(r'[無\d+]人受傷', df_TrafficControl['簡訊內容'][i]))
    else:
        hurt.append(['0'])
hurt = ([i for j in hurt for i in j])
df_TrafficControl['受傷人數'] = pd.Series(hurt)
for i in range(dataLength):
    if df_TrafficControl['受傷人數'][i] == '無人受傷':
        df_TrafficControl['受傷人數'][i] = 0
    elif df_TrafficControl['受傷人數'][i] == '0':
        df_TrafficControl['受傷人數'][i] = 0
    else:
        df_TrafficControl['受傷人數'][i] = re.findall(r'\d+', df_TrafficControl['受傷人數'][i])[0]

dead = []
for i in range(dataLength):
    if re.findall(r'[無\d+]人死亡', df_TrafficControl['簡訊內容'][i]):
        dead.append(re.findall(r'[無\d+]人死亡', df_TrafficControl['簡訊內容'][i]))
    else:
        dead.append(['0'])
dead = ([i for j in dead for i in j])
df_TrafficControl['死亡人數'] = pd.Series(dead)
for i in range(dataLength):
    if df_TrafficControl['死亡人數'][i] == '無人死亡':
        df_TrafficControl['死亡人數'][i] = 0
    elif df_TrafficControl['死亡人數'][i] == '0':
        df_TrafficControl['死亡人數'][i] = 0
    else:
        df_TrafficControl['死亡人數'][i] = re.findall(r'\d+', df_TrafficControl['死亡人數'][i])[0]

kilometers = []
for i in range(dataLength):
    if re.findall(r'回堵約\d+K', df_TrafficControl['簡訊內容'][i], re.IGNORECASE):
        kilometers.append(re.findall(r'\d+K', df_TrafficControl['簡訊內容'][i], re.IGNORECASE)[-1])
        kilometers_notK = []
        for j in kilometers:
            kilometers_notK.append(j.upper().strip('K'))
    else:
        kilometers.append('0')
df_TrafficControl['回堵公里數(K)'] = pd.Series(kilometers_notK)


df_TrafficControl = df_TrafficControl.drop(['簡訊內容'], axis=1)
print(df_TrafficControl.head(60))