import xlrd
import pymysql
import numpy as np
from datetime import date


# 讀取 Excel
df_accident = xlrd.open_workbook("/Users/kayzhang/Downloads/第6屆ETC創意競賽資料/108年公警局所轄事故資料/108年國道(A1A2A3)事故資料.xlsx")

# 獲取 Excel 檔案的第一個模組
sheet = df_accident.sheet_by_index(0)

# 獲取每一格的資料
data_list = []
for nrows in range(sheet.nrows):
    row_list = []
    for ncols in range(sheet.ncols):
        data_value = sheet.cell(nrows, ncols).value # 獲取資料值
        data_type = sheet.cell(nrows, ncols).ctype # 獲取資料型別
        if data_type == 2:
            data_value = str(int(data_value))
        if data_type == 3:
            data_t = xlrd.xldate_as_tuple(data_value, df_accident.datemode)
            data_value = date(*data_t[:3]).strftime('%y/%m/%d')
        row_list.append(data_value)
    data_list.append(row_list)
for i in range(len(data_list)):
    data_list[i][1] = ('%s:%s:%s' % (data_list[i][1][0:2], data_list[i][1][2:4], data_list[i][1][4:6]))
    data_list[i][7] = data_list[i][7].replace("", '0')  # 將公尺欄位的空值處補0
data_list = np.delete(data_list, 0, axis=0)
data_list = tuple([tuple(row) for row in data_list])
print(data_list)


# 資料庫連線
conn = pymysql.connect(host='XXXXX', # MySQL主機服務器名稱，使用 SHOW VARIABLES WHERE Variable_name = 'hostname' 查詢
                       user='root',
                       password='xxxxx',
                       db='ETC_Contest', # 要連接的數據庫
                       charset='utf8')
# 連接光標
cursor = conn.cursor()

# 開始使用 SQL 語句，先建表
sql_createTb = """CREATE TABLE df_accident (發生日期 varchar(20), 發生時間 varchar(20), 事故類別名稱 varchar(20), \
                縣市名稱 varchar(20), 市區鄉鎮名稱 varchar(20), 公路名稱 varchar(50), 公里 int, 公尺 int, \
                向車道 varchar(5), 24小時內死亡人數 varchar(20), 2至30日內死亡人數 varchar(20), 受傷人數 varchar(20), \
                天候代碼 varchar(5), 光線代碼 varchar(5), 道路類別代碼 varchar(5), 速限 varchar(5), \
                道路型態子類別代碼 varchar(5), 事故位置子類別代碼 varchar(5), 路面鋪裝代碼 varchar(5), 路面狀態代碼 varchar(5), \
                路面缺陷代碼 varchar(5), 障礙物代碼 varchar(5), 視距代碼 varchar(5), 號誌種類代碼 varchar(5), \
                號誌動作代碼 varchar(5), 分向設施子類別代碼 varchar(5), 快車道或一般車道間代碼 varchar(5), \
                快慢車道間代碼 varchar(5), 路面邊線代碼 varchar(5), 事故類型及型態子類別代碼 varchar(5), \
                肇因研判子類別代碼 varchar(5), 當事者區分代碼 varchar(10))
                """
cursor.execute(sql_createTb)

# 打包傳入資料庫中
val = ''
for i in range(0, sheet.ncols):
    val = val + '%s,'

result =cursor.executemany("INSERT INTO df_accident (發生日期, 發生時間, 事故類別名稱, 縣市名稱, 市區鄉鎮名稱, \
                            公路名稱, 公里, 公尺, 向車道, 24小時內死亡人數, \
                            2至30日內死亡人數, 受傷人數, 天候代碼, 光線代碼, 道路類別代碼, \
                            速限, 道路型態子類別代碼, 事故位置子類別代碼, 路面鋪裝代碼, 路面狀態代碼, \
                            路面缺陷代碼, 障礙物代碼, 視距代碼, 號誌種類代碼, 號誌動作代碼, \
                            分向設施子類別代碼, 快車道或一般車道間代碼, 快慢車道間代碼, 路面邊線代碼, 事故類型及型態子類別代碼, \
                            肇因研判子類別代碼, 當事者區分代碼) \
                            VALUES ("+val[:-1]+")", data_list)
# 提交資料至 MySQL 資料庫
conn.commit()

# 關閉光標
cursor.close()
# 關閉資料庫連線
conn.close()