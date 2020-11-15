from lxml import etree
import lxml.html
import re
import requests
import pymysql

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}


# res = requests.get("http://www.tami.org.tw/category/contact_2.php?ms=A5570&on=1", headers=headers)
# originHTML = etree.HTML(res.text)  # 原始HTML文件
# companyName = originHTML.xpath("//span[contains(@class, 'company-top')]/text()")[0].split()
# companyPhone = originHTML.xpath("//tr[2]//td[contains(@class, 'list_td')][2]/text()")[0].split()
# companyFax = originHTML.xpath("//tr[2]//td[contains(@class, 'list_td')][4]/text()")[0].split()
# companyAddress = originHTML.xpath("//tr[3]//td[contains(@class, 'list_td')][2]/text()")[0].split()
# factoryPhone = originHTML.xpath("//tr[4]//td[contains(@class, 'list_td')][2]/text()")[0].split()
# factoryFax = originHTML.xpath("//tr[4]//td[contains(@class, 'list_td')][4]//font/text()")[0].split()
# factoryAddress = originHTML.xpath("//tr[5]//td[contains(@class, 'list_td')][2]/text()")[0].split()
# website = originHTML.xpath("//tr[6]//td[contains(@class, 'list_td')][2]//a/@href")[0].split()
# capital = originHTML.xpath("//tr[6]//td[contains(@class, 'list_td')][4]/text()")[0].split()
# email = originHTML.xpath("//tr[7]//td[contains(@class, 'list_td')][2]//a/text()")[0].split()
# employeeNumber = originHTML.xpath("//tr[7]//td[contains(@class, 'list_td')][4]/text()")[0].split()
# products = originHTML.xpath("//tr[8]//td[contains(@class, 'list_td')][2]/text()")[0].split()


# print(companyName, companyPhone, companyFax, companyAddress, factoryPhone, factoryFax, factoryAddress, website, capital, email, employeeNumber, products)

testDict = {'切削工具機':{'車床':{'達岡工業股份有限公司':['達岡工業股份有限公司', '886-4-2359-9589', '886-4-2350-4985', '台中市西屯區工業區一路98巷7弄78號', '886-4-2359-9589', '886-4-2350-4985', '台中市西屯區工業區一路98巷7弄78號', 'http://www.cnctakang.com.tw/', '1,188萬元', 'takangts@ms78.hinet.net', '1', '車床,普通車床,高速精密車床,六角車床,自動車床,其他車床,CNC車床,斜床式CNC車床,CNC立式車床,CNC雙端同時加工車床,CNC車床，４軸式(7軸式),CNC車銑複合機,高速高精密雙主軸雙刀塔車削中心機,CNC切角車床,CNC五軸切削中心機,CNC自動車床,教導式電腦車床,櫛式電腦車床,雙主軸CNC車床,CNC'], '世寶機器五金股份有限公司':['世寶機器五金股份有限公司', '886-7-771-3121', '886-7-771-3121', '高雄市苓雅區中正1路120號14樓之4', '886-4-2359-9589', '886-4-2350-4985', '高雄市苓雅區中正1路120號14樓之4', 'http://www.cnctakang.com.tw/', '1,188萬元', 'takangts@ms78.hinet.net', '1', 'CNC車床,斜床式CNC車床,CNC車銑複合機,高速高精密雙主軸雙刀塔車削中心機,CNC自動車床,雙主軸CNC車床,綜合加工機,CNC 立式綜合加工機,CNC 臥式加工中心機,龍門型立式綜合加工機,高速龍門加工機,加工中心機(橫樑移動式或動柱式),五面加工機,五面加工機，門型,立臥五面加工中心機,石墨高速切削中心機, 車床,普通車床,高速精密車床,六角車床,自動車床,其他車床,CNC車床,斜床式CNC車床,CNC立式車床,CNC雙端同時加工車床,CNC車床，４軸式(7軸式),CNC車銑複合機,高速高精密雙主軸雙刀塔車削中心機,CNC切角車床,CNC五軸切削中心機,CNC自動車床,教導式電腦車床,櫛式電腦車床,雙主軸CNC車床,CNC']}}}

# for key, value in testDict.items():
#     print(key)
#     print(value)
#     print('-----')
#     for keyTwo, valueTwo in value.items():
#         print(keyTwo)
#         print(valueTwo)
#     print('-----next-----')

# print(testDict['testOne']['one'])



conn = pymysql.connect(host='localhost',
                            user='root',
                            password='kay121128',
                            port=3306,                       
                            db='tami',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    
try:
    with conn.cursor() as cursor:
        sql_createTb =  """
                        CREATE TABLE tamiRowData(
                            公司名稱 varchar(50), 公司電話 varchar(30), 公司傳真 varchar(30), 公司地址 varchar(80),
                            工廠電話 varchar(30), 工廠傳真 varchar(30), 工廠地址 varchar(80), 公司網址 varchar(50),
                            資本額 varchar(30), 電子郵件 varchar(50), 員工人數 varchar(10), 主要產品 varchar(500)
                        );
                        """
        cursor.execute(sql_createTb)
        
        # 打包傳入資料庫中
        sql_insertData = """
                        INSERT INTO tamiRowData (公司名稱, 公司電話, 公司傳真, 公司地址, 工廠電話, 工廠傳真, 工廠地址, 公司網址,
                            資本額, 電子郵件, 員工人數, 主要產品) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """
        dataNumber = 0
        for keyOne, valueOne in testDict.items():
            for keyTwo, valueTwo in valueOne.items():
                for keyThree, valueThree in valueTwo.items():
                    dataNumber += 1
        val = [list(range(12)) for _ in range(dataNumber)]
        count = 0
        for keyOne, valueOne in testDict.items():
            for keyTwo, valueTwo in valueOne.items():
                for keyThree, valueThree in valueTwo.items():
                    val[count].clear()
                    for value in valueThree:
                        val[count].append(value)
                    val[count] = list(val[count])
                    count += 1
        print(val[0])
        cursor.executemany(sql_insertData, val)
        conn.commit()
        
        sql = 'SELECT * FROM tamiRowData'
        cursor.execute(sql)
        # 取出第一筆結果
        result = cursor.fetchall()
        print(result)
finally:
    # 即便程式錯誤也會執行到這行關閉資料庫連線
    conn.close()

# dataNumber = 0
# for keyOne, valueOne in testDict.items():
#     for keyTwo, valueTwo in valueOne.items():
#         for keyThree, valueThree in valueTwo.items():
#             dataNumber += 1


# val = [list(range(3)) for _ in range(dataNumber)]
# count = 0
# for keyOne, valueOne in testDict.items():
#     for keyTwo, valueTwo in valueOne.items():
#         print(valueTwo)
#         for keyThree, valueThree in valueTwo.items():
#             val[count].clear()
#             # print(valueThree)
#             print('-----')
#             for value in valueThree:
#                 val[count].append(value)
#             val[count] = tuple(val[count])
#             count += 1

# print(val)
# print(count)