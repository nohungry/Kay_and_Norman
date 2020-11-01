from lxml import etree
import lxml.html
import re
import requests


# 產品分類 -> 再分類成細項
# def detailItemList(productItem: list, headers: dict):
#     listNum = len(productItem)
#     for index in range(listNum):
#         res = requests.get(productItem[index], headers=headers)
#         originHTML = etree.HTML(res.text)
#         detailItem = originHTML.xpath("//a[@class='product-link']")
#         detailItemLinkList = []
#         for index in range(len(detailItem)):
#             itemLink = detailItem[index].attrib["href"]
#             itemLink = "http://www.tami.org.tw/category/" + itemLink
#             detailItemLinkList.append(itemLink)

# # 產品分類：第一層分類
# def categoryOne(data):
#     listNum = len(data)
#     for index in range(listNum):
#         res = requests.get(data[index], headers=headers)
#         categoryOne = originHTML.xpath("//a[@class='product-link']")  # 產品分類
#         categoryOneLinkList = []  # 產品分類URL列表
#         for index in range(len(categoryOne)):
#             categoryOneLink = productItem[index].attrib["href"]
#             categoryOne = "http://www.tami.org.tw/category/" + categoryOne
#             categoryOneLinkList.append(categoryOne)


# # 產品分類：第二層分類
# def categoryTwo(data):
#     listNum = len(data)
#     for index in range(listNum):
#         res = requests.get(data[index], headers=headers)
#         categoryTwo = originHTML.xpath("//a[@class='product-link']")
#         categoryTwoLinkList = []
#         for index in range(len(categoryTwo)):
#             categoryTwoLink = categoryTwo[index].attrib["href"]
#             categoryTwoLink = "http://www.tami.org.tw/category/" + categoryTwoLink
#             categoryTwoLinkList.append(categoryTwoLink)


# # 產品分類：第三層公司
# def company(data):
#     listNum = len(data)
#     for index in range(listNum):
#         res = requests.get(data[index], headers=headers)
#         company = originHTML.xpath("//a[@class='company-word3']")
#         companyLinkList = []
#         for index in range(len(company)):
#             companyLink = company[index].attrib["onclick"]
#             companyLink = "http://www.tami.org.tw/category/contact_2.php?ms=" + companyLink + "&on=1"
#             companyLinkList.append(companyLink)


def companyDetailInfo(data):
    for keyOne, valueOne in data.items():
        for keyTwo, valueTwo in valueOne.items():
            for keyThree, valueThree in valueTwo.items():
                res = requests.get(valueThree, headers=headers)
                originHTML = etree.HTML(res.text)  # 原始HTML文件
                companyName = originHTML.xpath("//span[contains(@class, 'company-top')]/text()")[0].split()
                companyPhone = originHTML.xpath("//tr[2]//td[contains(@class, 'list_td')][2]/text()")[0].split()
                companyFax = originHTML.xpath("//tr[2]//td[contains(@class, 'list_td')][4]/text()")[0].split()
                companyAddress = originHTML.xpath("//tr[3]//td[contains(@class, 'list_td')][2]/text()")[0].split()
                factoryPhone = originHTML.xpath("//tr[4]//td[contains(@class, 'list_td')][2]/text()")[0].split()
                factoryFax = originHTML.xpath("//tr[4]//td[contains(@class, 'list_td')][4]//font/text()")[0].split()
                factoryAddress = originHTML.xpath("//tr[5]//td[contains(@class, 'list_td')][2]/text()")[0].split()
                website = originHTML.xpath("//tr[6]//td[contains(@class, 'list_td')][2]//a/@href")[0].split()
                capital = originHTML.xpath("//tr[6]//td[contains(@class, 'list_td')][4]/text()")[0].split()
                email = originHTML.xpath("//tr[7]//td[contains(@class, 'list_td')][2]//a/text()")[0].split()
                employeeNumber = originHTML.xpath("//tr[7]//td[contains(@class, 'list_td')][4]/text()")[0].split()
                products = originHTML.xpath("//tr[8]//td[contains(@class, 'list_td')][2]/text()")[0].split()
                try:
                    print(companyName, companyPhone, companyFax, companyAddress, factoryPhone, factoryFax, factoryAddress, website, capital, email, employeeNumber, products)
                except:
                    print('No data.')


if __name__ == "__main__":
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    res = requests.get(
        "http://www.tami.org.tw/category/product-new1.php", headers=headers)
    content = res.content.decode()
    originHTML = etree.HTML(content)  # 原始HTML文件
    categoryOne = originHTML.xpath("//a[@class='product-link']")  # 產品分類

    linkList = {}

    categoryOneLinkList = []  # 產品分類URL列表
    for index in range(len(categoryOne)):
        categoryOneLink = categoryOne[index].get("href")
        categoryOneLink = "http://www.tami.org.tw/category/" + categoryOneLink
        categoryOneLinkList.append(categoryOneLink)
        linkList[index] = categoryOneLink


    # 產品分類第二層
    for indexOne in range(len(categoryOneLinkList)):
        resTwo = requests.get(categoryOneLinkList[indexOne], headers=headers)
        contentTwo = resTwo.content.decode()
        originHTMLTwo = etree.HTML(contentTwo)  # 原始HTML文件
        categoryTwo = originHTMLTwo.xpath("//a[@class='product-link']")  # 產品分類
        
        linkList[indexOne] = {}
    
        categoryTwoLinkList = []  # 產品分類URL列表
        for indexTwo in range(len(categoryTwo)):
            categoryTwoLink = categoryTwo[indexTwo].get("href")
            categoryTwoLink = "http://www.tami.org.tw/category/" + categoryTwoLink
            categoryTwoLinkList.append(categoryTwoLink)
            linkList[indexOne][indexTwo] = categoryTwoLink

            linkList[indexOne][indexTwo] = {}

        for indexTwo in range(len(categoryTwoLinkList)):
            resThree = requests.get(categoryTwoLinkList[indexTwo], headers=headers)
            contentThree = resThree.content.decode()
            originHTML = etree.HTML(contentThree)  # 原始HTML文件
            companysName = originHTML.xpath("//a[@class='company-word3']")  # 產品分類

            companysNameLinkList = []  # 產品分類URL列表
            for indexThree in range(len(companysName)):
                companysNameLink = companysName[indexThree].get("onclick")
                companysNameLinkpart = re.findall(r"\w?\d+", companysNameLink)[0]
                companysNameLink = "http://www.tami.org.tw/category/contact_2.php?ms=" + companysNameLinkpart + "&on=1"
                companysNameLinkList.append(companysNameLink)
                linkList[indexOne][indexTwo][indexThree] = companysNameLink


    print('------start------')
    companyDetailInfo(linkList)
    print('------end------')