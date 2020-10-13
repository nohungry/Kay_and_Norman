from lxml import etree
import lxml.html
import re
import requests


# 產品分類 -> 再分類成細項
def detailItemList(productItem: list, headers: dict):
    listNum = len(productItem)
    for index in range(listNum):
        res = requests.get(productItem[index], headers=headers)
        originHTML = etree.HTML(res.text)
        detailItem = originHTML.xpath("//a[@class='product-link']")
        detailItemLinkList = []
        for index in range(len(detailItem)):
            itemLink = detailItem[index].attrib["href"]
            itemLink = "http://www.tami.org.tw/category/" + itemLink
            detailItemLinkList.append(itemLink)

# 應該要分兩個功能做


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    res = requests.get(
        "http://www.tami.org.tw/category/product-new1.php", headers=headers)

    originHTML = etree.HTML(res.text)  # 原始HTML文件
    productItem = originHTML.xpath("//a[@class='product-link']")  # 產品分類
    productItemLinkList = []  # 產品分類URL列表
    for index in range(len(productItem)):
        itemLink = productItem[index].attrib["href"]
        itemLink = "http://www.tami.org.tw/category/" + itemLink
        productItemLinkList.append(itemLink)

    # 產品分類內層
    for index in range(len(productItemLinkList)):
        res = requests.get(productItemLinkList[index], headers=headers)
