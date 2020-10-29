from lxml import etree
import lxml.html
import re
import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
res = requests.get(
    "http://www.tami.org.tw/category/product-new1.php", headers=headers)
content = res.content.decode()
originHTML = etree.HTML(content)  # 原始HTML文件

categoryOne = originHTML.xpath("//a[@class='product-link']")  # 產品分類


categoryOneLinkList = []  # 產品分類URL列表
for index in range(len(categoryOne)):
    categoryOneLink = categoryOne[index].get("href")
    print(categoryOneLink)
    categoryOneLink = "http://www.tami.org.tw/category/" + categoryOneLink
    categoryOneLinkList.append(categoryOneLink)

print(categoryOneLinkList)
