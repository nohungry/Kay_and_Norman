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

    def cctvStaticData(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/CCTV.xml", verify=False):
        """
        提供CCTV之空間位置描述及其他相關欄位
        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        cctvCrawler = requests.get(url, headers=self.headers, verify=verify)
        cctvContent = cctvCrawler.content
        cctvContentBytes = BytesIO(cctvContent)
        cctvTree = ET.parse(cctvContentBytes)

        cctvIDList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:CCTVID", namespaces=namespaces)

        subAuthorityCodeList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:SubAuthorityCode", namespaces=namespaces)

        linkIDList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:LinkID", namespaces=namespaces)

        videoStreamURLList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:VideoStreamURL", namespaces=namespaces)

        locationType = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:LocationType", namespaces=namespaces)

        positionLon = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:PositionLon", namespaces=namespaces)

        positionLat = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:PositionLat", namespaces=namespaces)

        roadIDList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadID", namespaces=namespaces)

        roadNameList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadName", namespaces=namespaces)

        roadClassList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadClass", namespaces=namespaces)

        roadDirectionList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadDirection", namespaces=namespaces)

        startList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadSection/xmlns:Start", namespaces=namespaces)

        endList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadSection/xmlns:End", namespaces=namespaces)

        locationMileList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:LocationMile", namespaces=namespaces)

    def sectionShapeGraph(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/SectionShape.xml", verify=False):
        """
        機關發布路段線型圖資資訊(v2.0)
        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        sectionCrawler = requests.get(url, headers=self.headers, verify=verify)
        sectionContent = sectionCrawler.content
        sectionContentBytes = BytesIO(sectionContent)
        sectionTree = ET.parse(sectionContentBytes)

        sectionIDList = sectionTree.findall(
            "xmlns:SectionShapes/xmlns:SectionShape/xmlns:SectionID", namespaces=namespaces)

        geometryList = sectionTree.findall(
            "xmlns:SectionShapes/xmlns:SectionShape/xmlns:SectionID", namespaces=namespaces)

    def sectionLink(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/SectionLink.xml", verify=False):
        """
        提供機關發布路段與基礎路段組合對應資訊(v2.0)
        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        sectionCrawler = requests.get(url, headers=self.headers, verify=verify)
        sectionContent = sectionCrawler.content
        sectionContentBytes = BytesIO(sectionContent)
        sectionTree = ET.parse(sectionContentBytes)

        sectionIDList = sectionTree.findall("xmlns:SectionLinks/xmlns:SectionLink/xmlns:SectionID", namespaces=namespaces)

        startLinkIDList = sectionTree.findall("xmlns:SectionLinks/xmlns:SectionLink/xmlns:StartLinkID", namespaces=namespaces)

        endLinkIDList = sectionTree.findall("xmlns:SectionLinks/xmlns:SectionLink/xmlns:EndLinkID", namespaces=namespaces)

    def section(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/Section.xml", verify=False):
        """
        提供該路段之機關發布路段基本資訊(v2.0)
        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        sectionCrawler = requests.get(url, headers=self.headers, verify=verify)
        sectionContent = sectionCrawler.content
        sectionContentBytes = BytesIO(sectionContent)
        sectionTree = ET.parse(sectionContentBytes)

        sectionIDList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:SectionID", namespaces=namespaces)
        
        sectionNameList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:SectionName", namespaces=namespaces)

        roadIDList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:RoadID", namespaces=namespaces)

        roadNameList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:RoadName", namespaces=namespaces)

        roadClassList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:RoadClass", namespaces=namespaces)

        roadDirectionList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:RoadDirection", namespaces=namespaces)

        startList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:RoadSection/xmlns:Start", namespaces=namespaces)

        endList = sectionTree.finall("xmlns:Sections/xmlns:Section/xmlns:RoadSection/xmlns:End", namespaces=namespaces)
        
        sectionLengthList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:SectionLength", namespaces=namespaces)
        
        startKMList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:SectionMile/xmlns:StartKM", namespaces=namespaces)

        endKMList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:SectionMile/xmlns:EndKM", namespaces=namespaces)

        speedLimitList = sectionTree.findall("xmlns:Sections/xmlns:Section/xmlns:SpeedLimit", namespaces=namespaces)

    


# Testing code
if __name__ == "__main__":
    vdTest = EtcData()
    vdTest.vdStaticData()
