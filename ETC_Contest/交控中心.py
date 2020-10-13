import xlrd
import pandas as pd
import re
from datetime import datetime


class ControlCenter():
    def __init__(self, title, path, sheet):
        self.title = title
        self.df_TrafficControl = pd.read_excel(path, sheet_name=sheet)
        self.dataLength = len(self.df_TrafficControl['簡訊內容'])

    def data(self):
        content = []
        for i in range(self.dataLength):
            content.append(re.findall(r'.*通報.*\d級', self.df_TrafficControl['簡訊內容'][i]))
        content = ([j for con in content for j in con])
        self.df_TrafficControl['通報級數'] = pd.Series(content)

        smsDate = []
        startTime = []
        endTime = []
        for i in range(self.dataLength):
            smsDate.append(re.findall(r'\d\d/\d{1,2}', self.df_TrafficControl['簡訊內容'][i]))
            startTime.append(re.findall(r'\d\d:\d\d', self.df_TrafficControl['簡訊內容'][i])[0])
            endTime.append(re.findall(r'\d\d:\d\d', self.df_TrafficControl['簡訊內容'][i])[-1])
            endTime[i] = endTime[i].replace("24:00", "00:00")
        smsDate = ([j for sms in smsDate for j in sms])
        self.df_TrafficControl['簡訊日期'] = pd.Series(smsDate)
        self.df_TrafficControl['簡訊時間'] = pd.Series(startTime)
        self.df_TrafficControl['事故排除時間'] = pd.Series(endTime)

        self.df_TrafficControl['簡訊時間_cul'] = pd.Series(startTime)
        self.df_TrafficControl['事故排除時間_cul'] = pd.Series(endTime)
        self.df_TrafficControl['處理耗時'] = pd.Series(endTime)  # 先隨便給個符合dataFrame的格式

        for i in range(self.dataLength):
            self.df_TrafficControl['簡訊時間_cul'][i] = datetime.strptime(self.df_TrafficControl['簡訊時間'][i], "%H:%M")
            self.df_TrafficControl['事故排除時間_cul'][i] = datetime.strptime(self.df_TrafficControl['事故排除時間'][i], "%H:%M")
            self.df_TrafficControl['處理耗時'][i] = (self.df_TrafficControl['事故排除時間_cul'][i] - self.df_TrafficControl['簡訊時間_cul'][i])

        self.df_TrafficControl = self.df_TrafficControl.drop(['簡訊時間_cul'], axis=1)
        self.df_TrafficControl = self.df_TrafficControl.drop(['事故排除時間_cul'], axis=1)

        roadName = []
        for road in self.df_TrafficControl['簡訊內容']:
            roadName.append(re.findall(r'國\d+', road))
        roadName = ([i for road in roadName for i in road])
        self.df_TrafficControl['公路名稱'] = pd.Series(roadName)

        direction = []
        for direct in range(self.dataLength):
            if re.findall(r'[東西南北][上下向 ]', self.df_TrafficControl['簡訊內容'][direct]):
                direction.append(re.findall(r'[東西南北][上下向 ]', self.df_TrafficControl['簡訊內容'][direct]))
            else:
                direction.append([''])
        direction = ([i for direct in direction for i in direct])
        self.df_TrafficControl['向車道'] = pd.Series(direction)

        hurt = []
        for i in range(self.dataLength):
            if re.findall(r'\d+[人傷].*送醫|\d+[人傷][受輕]傷', self.df_TrafficControl['簡訊內容'][i]):
                hurt.append(re.findall(r'\d+[人傷].*送醫|\d+[人傷][受輕]傷', self.df_TrafficControl['簡訊內容'][i])[0])
                hurt[i] = re.findall(r'\d+', hurt[i])[0]
            else:
                hurt.append('0')
        self.df_TrafficControl['受傷人數'] = pd.Series(hurt)

        dead = []
        for i in range(self.dataLength):
            if re.findall(r'\d+人死亡', self.df_TrafficControl['簡訊內容'][i]):
                dead.append(re.findall(r'\d+人死亡', self.df_TrafficControl['簡訊內容'][i])[0])
                dead[i] = re.findall(r'\d+', dead[i])[0]
            else:
                dead.append('0')
        self.df_TrafficControl['死亡人數'] = pd.Series(dead)

        kilometers = []
        for i in range(self.dataLength):
            if re.findall(r'回堵[約]?\d+公里|回堵[約]?\d+K', self.df_TrafficControl['簡訊內容'][i], re.IGNORECASE):
                kilometers.append(re.findall(r'回堵[約]?\d+公里|回堵[約]?\d+K', self.df_TrafficControl['簡訊內容'][i], re.IGNORECASE)[-1])
                kilometers[i] = re.findall(r'\d', kilometers[i])[0]
            else:
                kilometers.append('0')
        self.df_TrafficControl['回堵公里數(K)'] = pd.Series(kilometers)


        self.df_TrafficControl = self.df_TrafficControl.drop(['簡訊內容'], axis=1)
        return self.df_TrafficControl.head(60)


if __name__ == '__main__':
    # North = ControlCenter('North', "/Users/kayzhang/Downloads/第6屆ETC創意競賽資料/108年高公局所轄各分局事故簡訊資料/108年_北區交控中心.xlsx", 0)
    # South = ControlCenter('South', "/Users/kayzhang/Downloads/第6屆ETC創意競賽資料/108年高公局所轄各分局事故簡訊資料/108年_南區交控中心.xlsx", 0)
    Pinglin = []
    for i in range(11):
        Pinglin.append(ControlCenter('Pinglin', "/Users/kayzhang/Downloads/第6屆ETC創意競賽資料/108年高公局所轄各分局事故簡訊資料/108年_坪林行控中心.xlsx", i))
        Pinglin[i] = Pinglin[i].data()
    # print(North.data())
    # print(B.data())
    # print(B.data().iloc[350:370, :])
    res = pd.concat(Pinglin, axis=0, ignore_index=True)
    # res = pd.concat([North.data(), South.data()], axis=0, ignore_index=True)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    print(res)
    for a in res:
        # 跳過我們沒興趣的顧客
        if re.findall(r'-1 day.*', a['處理耗時']):
            continue
        # 利用 custkey 取德該顧客的購買紀錄
        c_orders = orders[c['custkey']]

        # 將所有排序後的記錄回傳
        for o in c_orders_sorted:
            values = [c['name'], str(o['totalprice']), str(o['orderdate'])]
            print(" | ".join(values))
        # 已經找到該顧客，提早結束迴圈以減少處理時間
        break