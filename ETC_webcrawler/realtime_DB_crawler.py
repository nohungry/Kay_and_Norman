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

        dataList = []

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

        assert len(authorityCodeList) == len(vDIDList), "業管機關簡碼 != VD設備代碼"

        for index in range(len(authorityCodeList)):
            dataDict = {

            }
            dataList.append(dataDict)

        return dataList

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
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:ETagPairID", namespaces=namespaces)  # etag配對路徑代碼

        startETagGantryIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:StartETagGantryID", namespaces=namespaces)  # etag配對起始點偵測站代碼

        endETagGantryIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:EndETagGantryID", namespaces=namespaces)  # eTag配對結束點偵測站代碼

        descriptionList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:Description", namespaces=namespaces)  # 配對路徑文字描述

        distanceList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:Distance", namespaces=namespaces)  # 配對路徑距離, GIS提供的配對路徑距離(KM), 可到小數點3位

        startLinkIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:StartLinkID", namespaces=namespaces)  # 起點基礎路段代碼, 請參閱[基礎路段代碼表]，https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        endLinkIDList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:EndLinkID", namespaces=namespaces)  # 迄點基礎路段代碼, 請參閱[基礎路段代碼表]，https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        geometryList = etagTree.findall(
            "xmlns:ETagPairs/xmlns:ETagPair/xmlns:Geometry", namespaces=namespaces)  # 配對路徑線型圖資資料, 格式為WKT

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
            "xmlns:ETags/xmlns:ETag/xmlns:ETagGantryID", namespaces=namespaces)  # eTag偵測站代碼

        linkIDList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:LinkID", namespaces=namespaces)  # 基礎路段代碼, 請參閱[基礎路段代碼表]，https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        locationTypeList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:LocationType", namespaces=namespaces)  # 設置地點位置類型 = ['1: 路側', '2: 道路中央分隔島', '3: 快慢分隔島', '4: 車道上門架', '5: 車道鋪面', '6: 其他']

        positionLonList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:PositionLon", namespaces=namespaces)  # 設備架設位置 X 坐標

        positionLatList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:PositionLat", namespaces=namespaces)  # 設備架設位置 Y 坐標

        roadIDList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadID", namespaces=namespaces)  # 道路代碼, 請參閱[路名碼基本資料]，https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        roadNameList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadName", namespaces=namespaces)  # 道路名稱

        # 道路分類 = ['0: 國道', '1: 快速道路', '2: 市區快速道路', '3: 省道', '4: 縣道', '5: 鄉道', '6: 市區一般道路', '7: 匝道']
        roadClassList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadClass", namespaces=namespaces)

        roadDirectionList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadDirection", namespaces=namespaces)  # 基礎路段所屬道路方向, 請參閱[道路方向資料表]，https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        roadSectionStart = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadSection/xmlns:Start", namespaces=namespaces)  # 路段起點描述

        roadSectionEnd = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:RoadSection/xmlns:End", namespaces=namespaces)  # 路段迄點描述

        locationMileList = etagTree.findall(
            "xmlns:ETags/xmlns:ETag/xmlns:LocationMile", namespaces=namespaces)  # 所在方向里程數

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
            "xmlns:CMSs/xmlns:CMS/xmlns:CMSID", namespaces=namespaces)  # CMS設備代碼

        subAuthorityCodeList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:SubAuthorityCode", namespaces=namespaces)  # 業管子機關簡碼

        linkIDList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:LinkID", namespaces=namespaces)  # 基礎路段代碼, 請參閱[基礎路段代碼表], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        locationTypeList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:LocationType", namespaces=namespaces)  # 設置地點位置類型 = ['1: 路側', '2: 道路中央分隔島', '3: 快慢分隔島', '4: 車道上門架', '5: 車道鋪面', '6: 其他']

        positionLonList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:PositionLon", namespaces=namespaces)  # 設備架設位置 X 坐標

        positionLatList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:PositionLat", amespaces=namespaces)  # 設備架設位置 Y 坐標

        roadIDList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadID", amespaces=namespaces)  # 道路代碼, 請參閱[路名碼基本資料], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        roadNameList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadName", amespaces=namespaces)  # 道路名稱

        roadClassList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadClass", amespaces=namespaces)  # 道路分類 = ['0: 國道', '1: 快速道路', '2: 市區快速道路', '3: 省道', '4: 縣道', '5: 鄉道', '6: 市區一般道路', '7: 匝道']

        roaddirectionList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadDirection", amespaces=namespaces)  # 基礎路段所屬道路方向, 請參閱[道路方向資料表], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        startList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadSection/xmlns:Start", amespaces=namespaces)  # 路段起點描述

        endList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:RoadSection/xmlns:End", amespaces=namespaces)  # 路段迄點描述

        locationMileList = cmsTree.findall(
            "xmlns:CMSs/xmlns:CMS/xmlns:LocationMile", amespaces=namespaces)  # 所在方向里程數

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
            "xmlns:CCTVs/xmlns:CCTV/xmlns:CCTVID", namespaces=namespaces)  # CCTV設備代碼

        subAuthorityCodeList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:SubAuthorityCode", namespaces=namespaces)  # 業管子機關簡碼

        linkIDList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:LinkID", namespaces=namespaces)  # 基礎路段代碼, 請參閱[基礎路段代碼表], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        videoStreamURLList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:VideoStreamURL", namespaces=namespaces)  # 動態影像串流網址

        locationType = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:LocationType", namespaces=namespaces)  # 設置地點位置類型 = ['1: 路側', '2: 道路中央分隔島', '3: 快慢分隔島', '4: 車道上門架', '5: 車道鋪面', '6: 其他']

        positionLon = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:PositionLon", namespaces=namespaces)  # 設備架設位置 X 坐標

        positionLat = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:PositionLat", namespaces=namespaces)  # 設備架設位置 Y 坐標

        roadIDList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadID", namespaces=namespaces)  # 道路代碼, 請參閱[路名碼基本資料], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        roadNameList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadName", namespaces=namespaces)  # 道路名稱

        roadClassList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadClass", namespaces=namespaces)  # 道路分類 = ['0: 國道', '1: 快速道路', '2: 市區快速道路', '3: 省道', '4: 縣道', '5: 鄉道', '6: 市區一般道路', '7: 匝道']

        roadDirectionList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadDirection", namespaces=namespaces)  # 基礎路段所屬道路方向, 請參閱[道路方向資料表], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        startList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadSection/xmlns:Start", namespaces=namespaces)  # 路段起點描述

        endList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:RoadSection/xmlns:End", namespaces=namespaces)  # 路段迄點描述

        locationMileList = cctvTree.findall(
            "xmlns:CCTVs/xmlns:CCTV/xmlns:LocationMile", namespaces=namespaces)  # 所在方向里程數

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
            "xmlns:SectionShapes/xmlns:SectionShape/xmlns:SectionID", namespaces=namespaces)  # 機關發布路段代碼

        geometryList = sectionTree.findall(
            "xmlns:SectionShapes/xmlns:SectionShape/xmlns:SectionID", namespaces=namespaces)  # 機關發布路段線型圖資資料, 格式為WKT

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

        sectionIDList = sectionTree.findall(
            "xmlns:SectionLinks/xmlns:SectionLink/xmlns:SectionID", namespaces=namespaces)  # 機關發布路段代碼

        startLinkIDList = sectionTree.findall(
            "xmlns:SectionLinks/xmlns:SectionLink/xmlns:StartLinkID", namespaces=namespaces)  # 起點基礎路段代碼,請參閱[基礎路段代碼表], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        endLinkIDList = sectionTree.findall(
            "xmlns:SectionLinks/xmlns:SectionLink/xmlns:EndLinkID", namespaces=namespaces)  # 迄點基礎路段代碼,請參閱[基礎路段代碼表], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

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

        sectionIDList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:SectionID", namespaces=namespaces)  # 機關發布路段代碼

        sectionNameList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:SectionName", namespaces=namespaces)  # 機關發布路段中文名稱描述

        roadIDList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:RoadID", namespaces=namespaces)  # 道路代碼,請參閱[路名碼基本資料], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        roadNameList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:RoadName", namespaces=namespaces)  # 道路路名

        roadClassList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:RoadClass", namespaces=namespaces)  # 道路分類 = ['0: 國道', '1: 快速道路', '2: 市區快速道路', '3: 省道', '4: 縣道', '5: 鄉道', '6: 市區一般道路', '7: 匝道']

        roadDirectionList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:RoadDirection", namespaces=namespaces)  # 基礎路段所屬道路方向, 請參閱[道路方向資料表], https://traffic-api-documentation.gitbook.io/traffic/xiang-dai-zhao-biao

        startList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:RoadSection/xmlns:Start", namespaces=namespaces)  # 路段起點描述

        endList = sectionTree.finall(
            "xmlns:Sections/xmlns:Section/xmlns:RoadSection/xmlns:End", namespaces=namespaces)  # 路段迄點描述

        sectionLengthList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:SectionLength", namespaces=namespaces)  # 機關發布路段長度, GIS的提供路段長度(KM), 可到小數點3位, 單位:KM

        startKMList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:SectionMile/xmlns:StartKM", namespaces=namespaces)  # 起點里程數, 里程表示方式：整數公里數+整數公里數下 3 位，如 36K+525

        endKMList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:SectionMile/xmlns:EndKM", namespaces=namespaces)  # 迄點里程數, 里程表示方式：整數公里數+整數公里數下 3 位，如 36K+525

        speedLimitList = sectionTree.findall(
            "xmlns:Sections/xmlns:Section/xmlns:SpeedLimit", namespaces=namespaces)  # 速限

    def congestionLevelList(self, url="https://tisvcloud.freeway.gov.tw/history/motc20/CongestionLevel.xml", verify=False):
        """
        提供機關路況壅塞水準定義基本資訊(v2.0)
        """
        url = str(url)
        verify = verify
        namespaces = {
            "xmlns": "http://traffic.transportdata.tw/standard/traffic/schema/"}
        congestionCrawler = requests.get(
            url, headers=self.headers, verify=verify)
        congestionContent = congestionCrawler.content
        congestionContentBytes = BytesIO(congestionContent)
        congestionTree = ET.parse(congestionContentBytes)

        congestionLevelIDList = congestionTree.findall(
            "xmlns:CongestionLevels/xmlns:CongestionLevel/xmlns:CongestionLevelID", namespaces=namespaces)  # 壅塞水準組別代碼

        congestionLevelNameList = congestionTree.findall(
            "xmlns:CongestionLevels/xmlns:CongestionLevel/xmlns:CongestionLevelName", namespaces=namespaces)  # 壅塞水準組別名稱

        measureIndexList = congestionTree.findall(
            "xmlns:CongestionLevels/xmlns:CongestionLevel/xmlns:MeasureIndex", namespaces=namespaces)  # 壅塞衡量基準 = ['Speed: 速率', 'Occupancy: 佔有率', 'TravelTime: 旅行時間', 'Combined: 綜合指標']

        levelList = congestionTree.findall(
            "xmlns:CongestionLevels/xmlns:CongestionLevel/xmlns:Levels/xmlns:Level/xmlns:Level", namespaces=namespaces)  # 壅塞級別 = ['0: 未知/資料不足', '1: 順暢', '2: 車多', '3: 車多', '4: 壅塞', '5: 壅塞']

        levelNameList = congestionTree.findall(
            "xmlns:CongestionLevels/xmlns:CongestionLevel/xmlns:Levels/xmlns:Level/xmlns:LevelName", namespaces=namespaces)  # 壅塞級別文字描述

        topValueList = congestionTree.findall(
            "xmlns:CongestionLevels/xmlns:CongestionLevel/xmlns:Levels/xmlns:Level/xmlns:TopValue", namespaces=namespaces)  # 門檻值上限

        lowValueList = congestionTree.findall(
            "xmlns:CongestionLevels/xmlns:CongestionLevel/xmlns:Levels/xmlns:Level/xmlns:LowValue", namespaces=namespaces)  # 門檻值下限


# Testing code
if __name__ == "__main__":
    vdTest = EtcData()
    vdTest.vdStaticData()
