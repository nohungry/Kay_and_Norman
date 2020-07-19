import requests
import xml.etree.ElementTree as ET
from io import BytesIO


class EtcData:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

    def vdStaticData(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/VD.xml", verify=False):
        """

        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        vdCrawler = requests.get(url, headers=self.headers, verify=verify)
        vdContent = vdCrawler.content
        vdContentBytes = BytesIO(vdContent)
        vdTree = ET.parse(vdContentBytes)

        # 下面資料皆回傳"list"
        vdAuthorityCodeList = vdTree.findall(
            "xmlns:AuthorityCode", namespaces=namespaces)  # 業管機關簡碼

        for index in vdAuthorityCodeList:
            print(type(index.text))
            print(index.text)
        pass


if __name__ == "__main__":
    test = EtcData()
    test.vdStaticData()
