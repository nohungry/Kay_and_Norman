import requests
import xml.etree.ElementTree as ET
from io import BytesIO


class EtcData:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

    def vdStaticData(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/VD.xml", verify=False):
        """
        提供VD之空間位置描述及其他相關欄位
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
        authorityCodeList = vdTree.findall(
            "xmlns:AuthorityCode", namespaces=namespaces)   # 業管機關簡碼

        vDIDList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:VDID", namespaces=namespaces)  # VD設備代碼

        subAuthorityCodeList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:SubAuthorityCode", namespaces=namespaces)  # 業管子機關簡碼

        biDirectionalList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:BiDirectional", namespaces=namespaces)    # 是否為雙向偵測 = ['0: 偵測單向', '1: 偵測雙向']

        linkIDList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:LinkID", namespaces=namespaces)  # 基礎路段代碼, 請參閱[基礎路段代碼表]

        bearingList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:Bearing", namespaces=namespaces)  # 基礎路段方位 = ['N: 北', 'E: 東', 'W: 西', 'S: 南', 'NE: 東北', 'SE: 東南', 'NW: 西北', 'SW: 西南']

        roadDirectionList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:RoadDirection", namespaces=namespaces)   # 基礎路段所屬道路方向, 請參閱[道路方向資料表]

        laneNumList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:LaneNum", namespaces=namespaces)  # 設備於該方向基礎路段所能偵側車道數

        actualLaneNumList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionLinks/xmlns:DetectionLink/xmlns:ActualLaneNum", namespaces=namespaces)   # 該方向基礎路段的實際車道數

        typeList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:VDType", namespaces=namespaces)   # VD 類別 = ['1: 線圈式', '2: 微波式', '3: 影像式', '4: 紅外線', '5: 超音波', '6: 其它']

        locationTypeList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:LocationType", namespaces=namespaces)  # 設置地點位置類型 = ['1: 路側', '2: 道路中央分隔島', '3: 快慢分隔島', '4: 車道上門架', '5: 車道鋪面', '6: 其他']

        detectionTypeList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:DetectionType", namespaces=namespaces)    # 車流偵側類型 = ['1: 高快速公路/市快主線', '2: 高快速公路/市快匝道', '3: 其它道路路段中', '4: 其它道路路口(靠近路口或停止線)']

        positionLonList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:PositionLon", namespaces=namespaces)  # 設備架設位置 X 坐標

        positionLatList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:PositionLat", namespaces=namespaces)  # 設備架設位置 Y 坐標

        roadIDList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadID", namespaces=namespaces)   # 道路代碼, 請參閱[路名碼基本資料]

        roadNameList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadName", namespaces=namespaces)  # 道路名稱

        roadClassList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadClass", namespaces=namespaces)    # 道路分類 = ['0: 國道', '1: 快速道路', '2: 市區快速道路', '3: 省道', '4: 縣道', '5: 鄉道', '6: 市區一般道路', '7: 匝道']

        startList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadSection/xmlns:Start", namespaces=namespaces)  # 路段起點描述

        endList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:RoadSection/xmlns:End", namespaces=namespaces)    # 路段迄點描述

        locationMileList = vdTree.findall(
            "xmlns:VDs/xmlns:VD/xmlns:LocationMile", namespaces=namespaces)  # 所在方向里程數

    def eTagPairStaticData(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/ETagPair.xml", verify=False):
        """
        提供eTag之配對路徑靜態資料
        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        etagPairCrawler = requests.get(
            url, headers=self.headers, verify=verify)
        etagPairContent = etagPairCrawler.content
        etagPairContentBytes = BytesIO(etagPairContent)
        etagTree = ET.parse(etagPairContentBytes)

        # 下面資料皆回傳"list"
        etagPairIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:ETagPairID", namespaces=namespaces)

        startETagGantryIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:StartETagGantryID", namespaces=namespaces)

        endETagGantryIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:EndETagGantryID", namespaces=namespaces)

        descriptionList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:Description", namespaces=namespaces)

        distanceList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:Distance", namespaces=namespaces)

        startLinkIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:StartLinkID", namespaces=namespaces)

        endLinkIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:EndLinkID", namespaces=namespaces)

        geometryList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:Geometry", namespaces=namespaces)

        geometryList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:Geometry", namespaces=namespaces)

    def eTagPlaceStaticData(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/ETag.xml", verify=False):
        """
        提供eTag之空間位置描述資訊
        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        etagPlaceCrawler = requests.get(
            url, headers=self.headers, verify=verify)
        etagPlaceContent = etagPlaceCrawler.content
        etagPlaceContentBytes = BytesIO(etagPlaceContent)
        etagTree = ET.parse(etagPlaceContentBytes)

        eTagGantryIDList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:ETagGantryID", namespaces=namespaces)

        linkIDList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:LinkID", namespaces=namespaces)

        locationTypeList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:LocationType", namespaces=namespaces)

        positionLonList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:PositionLon", namespaces=namespaces)

        positionLatList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:PositionLat", namespaces=namespaces)

        roadIDList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadID", namespaces=namespaces)

        roadNameList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadName", namespaces=namespaces)

        roadDirectionList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadDirection", namespaces=namespaces)

        roadSectionStart = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadSection/xmlns:Start", namespaces=namespaces)

        roadSectionEnd = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadSection/xmlns:End", namespaces=namespaces)

        locationMileList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:LocationMile", namespaces=namespaces)

    def cmsStaticData(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/CMS.xml", verify=False):
        """
        提供CMS之空間位置描述及其他相關欄位
        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        cmsCrawler = requests.get(url, headers=self.headers, verify=verify)
        cmsContent = cmsCrawler.content
        cmsContentBytes = BytesIO(cmsContent)
        cmsTree = ET.parse(cmsContentBytes)

        cmsIDList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:CMSID", namespaces=namespaces)

        subAuthorityCodeList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:SubAuthorityCode", namespaces=namespaces)

        linkIDList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:LinkID", namespaces=namespaces)

        locationTypeList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:LocationType", namespaces=namespaces)

        positionLonList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:PositionLon", namespaces=namespaces)

        positionLatList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:PositionLat", amespaces=namespaces)

        roadIDList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadID", amespaces=namespaces)

        roadNameList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadName", amespaces=namespaces)

        roadClassList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadClass", amespaces=namespaces)

        roaddirectionList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadDirection", amespaces=namespaces)

        startList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadSection/xmlns:Start", amespaces=namespaces)

        endList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadSection/xmlns:End", amespaces=namespaces)

        locationMileList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:LocationMile", amespaces=namespaces)


# Testing code
if __name__ == "__main__":
    vdTest = EtcData()
    vdTest.vdStaticData()
