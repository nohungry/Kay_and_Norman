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
            "xmlns:AuthorityCode", namespaces=namespaces)   # 業管機關簡碼

        vdVDIDList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:VDID", namespaces=namespaces)  # VD設備代碼

        vdSubAuthorityCodeList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:SubAuthorityCode", namespaces=namespaces)  # 業管子機關簡碼

        vdBiDirectionalList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:BiDirectional", namespaces=namespaces)    # 是否為雙向偵測 = ['0: 偵測單向', '1: 偵測雙向']

        vdLinkIDList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:LinkID", namespaces=namespaces)  # 基礎路段代碼, 請參閱[基礎路段代碼表]

        vdBearingList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:Bearing", namespaces=namespaces)  # 基礎路段方位 = ['N: 北', 'E: 東', 'W: 西', 'S: 南', 'NE: 東北', 'SE: 東南', 'NW: 西北', 'SW: 西南']

        vdRoadDirectionList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:RoadDirection", namespaces=namespaces)   # 基礎路段所屬道路方向, 請參閱[道路方向資料表]

        vdLaneNumList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:LaneNum", namespaces=namespaces)  # 設備於該方向基礎路段所能偵側車道數

        vdActualLaneNumList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:ActualLaneNum", namespaces=namespaces)   # 該方向基礎路段的實際車道數

        vdTypeList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:VDType", namespaces=namespaces)   # VD 類別 = ['1: 線圈式', '2: 微波式', '3: 影像式', '4: 紅外線', '5: 超音波', '6: 其它']

        vdLocationTypeList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:LocationType", namespaces=namespaces)  # 設置地點位置類型 = ['1: 路側', '2: 道路中央分隔島', '3: 快慢分隔島', '4: 車道上門架', '5: 車道鋪面', '6: 其他']

        vdDetectionTypeList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionType", namespaces=namespaces)    # 車流偵側類型 = ['1: 高快速公路/市快主線', '2: 高快速公路/市快匝道', '3: 其它道路路段中', '4: 其它道路路口(靠近路口或停止線)']

        vdPositionLonList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:PositionLon", namespaces=namespaces)  # 設備架設位置 X 坐標

        vdPositionLatList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:PositionLat", namespaces=namespaces)  # 設備架設位置 Y 坐標

        vdRoadIDList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadID", namespaces=namespaces)   # 道路代碼, 請參閱[路名碼基本資料]

        vdRoadNameList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadName", namespaces=namespaces)  # 道路名稱

        vdRoadClassList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadClass", namespaces=namespaces)    # 道路分類 = ['0: 國道', '1: 快速道路', '2: 市區快速道路', '3: 省道', '4: 縣道', '5: 鄉道', '6: 市區一般道路', '7: 匝道']

        vdStartList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadSection/xmlns:Start", namespaces=namespaces)  # 路段起點描述

        vdEndList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadSection/xmlns:End", namespaces=namespaces)    # 路段迄點描述

        vdLocationMileList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:LocationMile", namespaces=namespaces)  # 所在方向里程數


# Testing code
if __name__ == "__main__":
    vdTest = EtcData()
    vdTest.vdStaticData()
