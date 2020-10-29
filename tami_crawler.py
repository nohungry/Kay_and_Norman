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
    print(linkList)
    print('-----------')


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
            companyName = originHTML.xpath("//a[@class='company-word3']")  # 產品分類

            companyNameLinkList = []  # 產品分類URL列表
            for indexThree in range(len(companyName)):
                companyNameLink = companyName[indexThree].get("onclick")
                companyNameLinkpart = re.findall(r"\w?\d+", companyNameLink)[0]
                companyNameLink = "http://www.tami.org.tw/category/contact_2.php?ms=" + companyNameLinkpart + "&on=1"
                companyNameLinkList.append(companyNameLink)
                linkList[indexOne][indexTwo][indexThree] = companyNameLink

                
    print(linkList[0][0][0])
    print('-----------')
