import pymysql


# 資料庫連線
conn = pymysql.connect(host='KaydeMacBook-Pro.local', # MySQL主機服務器名稱
                       user='root',
                       password='kay121128',
                       db='ETC_Contest', # 要連接的數據庫
                       charset='utf8')
# 連接光標
cursor = conn.cursor()

# 開始使用SQL語法查詢
sqlOne = ("SELECT 事故類型及型態子類別代碼, COUNT(事故類型及型態子類別代碼) \
        FROM df_accident \
        GROUP BY 事故類型及型態子類別代碼 \
        ORDER BY COUNT(事故類型及型態子類別代碼) DESC")
cursor.execute(sqlOne)
rowOne = cursor.fetchall()
print(rowOne)

print('-----我是分隔線-----')

# sqlTwo = ("SELECT 公路名稱, MAX(事故類型及型態子類別代碼), MAX(肇因研判子類別代碼)\
#         FROM df_accident \
#         GROUP BY 公路名稱, 事故類型及型態子類別代碼 \
#         ORDER BY 公路名稱")
# cursor.execute(sqlTwo)
# rowTwo = cursor.fetchall()
# print(rowTwo)

print('-----我是分隔線-----')

sqlThree = ("SELECT * FROM df_accident \
            WHERE 發生日期='19/01/03' AND 公路名稱='國道3號' \
            ORDER BY 發生時間")
cursor.execute(sqlThree)
sqlThree = cursor.fetchall()
print(sqlThree)

# # 關閉光標
# cursor.close()
# # 關閉資料庫連線
# conn.close()