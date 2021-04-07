"""
소상공인 진흥공단 Open API
semas(Small Enterprise And Market Service)

1. StoreInfo 클래스: 소상공인 상가업소 정보 조회
    1. storeZoneOne: 지정 상권조회
    2. storeZoneInRadius: 반경내 상권조회
    3. storeZoneInRectangle: 사각형내 상권조회
    4. storeZoneInAdmi: 행정구역 단위 상권조회
    5. storeOne: 단일 상가업소 조회
    6. storeListInBuilding: 건물단위 상가업소 조회
    7. storeListInPnu: 지번단위 상가업소 조회
    8. storeListInDong: 행정동 단위 상가업소 조회
    9. storeListInArea: 상권내 상가업소 조회
    10. storeListInRadius: 반경내 상가업소 조회
    11. storeListInRectangle: 사각형내 상가업소 조회
    12. storeListInPolygon: 다각형내 상가업소 조회
    13. storeListInUpjong: 업종별 상가업소 조회
    14. storeListByDate: 수정일자기준 상가업소 조회
    15. reqStoreModify: 상가업소정보 변경요청
    16. (보류) storeStatsUpjongInAdmi: 행정구역내 업종별 상가업소 통계
    17. (보류) storeStatsUpjongInBuilding: 건물내 업종별 상가업소 통계
    18. (보류) storeStatsUpjongInRadius: 반경내 업종별 상가업소 통계
    19. (보류) storeStatsUpjongInRectangle: 사각형내 업종별 상가업소 통계
    20. (보류) storeStatsUpjongInPolygon: 다각형내 업종별 상가업소 통계
    21. largeUpjongList: 상권정보 업종 대분류 조회
    22. middleUpjongList: 상권정보 업종 중분류 조회
    23. smallUpjongList: 상권정보 업종 소분류 조회
"""

import pandas as pd
import numpy as np
import datetime
import requests
from bs4 import BeautifulSoup


class StoreInfo:
    def __init__(self, serviceKey):
        """
        공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.
        """
        # Open API 서비스 키 초기화
        self.serviceKey = serviceKey

        # ServiceKey 등록
        self.urlBase = f"http://apis.data.go.kr/B553077/api/open/sdsc/"

        print(">> Open API Services initialized!")

    def storeZoneOne(self, key):
        """
        1. 지정 상권조회
        입력: 상권번호
        """
        url = f"{self.urlBase}storeZoneOne?ServiceKey={self.serviceKey}&key={key}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "trarNo",
                "mainTrarNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "trarArea",
                "coordNum",
                "coords",
                "stdrDt",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            trarNo,
                            mainTrarNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            trarArea,
                            coordNum,
                            coords,
                            stdrDt,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeZoneInRadius(self, radius, cx, cy):
        """
        2. 반경내 상권조회
        입력: 반경(m), 중심점 경도(WGS84 좌표계), 중심점 위도(WGS84 좌표계)
        """
        url = f"{self.urlBase}storeZoneInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "trarNo",
                "mainTrarNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "trarArea",
                "coordNum",
                "coords",
                "stdrDt",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            trarNo,
                            mainTrarNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            trarArea,
                            coordNum,
                            coords,
                            stdrDt,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeZoneInRectangle(self, minx, miny, maxx, maxy):
        """
        3. 사각형내 상권조회
        입력: 서쪽 경도, 남쪽 위도, 동쪽 경도, 북쪽 위도 (WGS84 좌표계)
        """
        url = f"{self.urlBase}storeZoneInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "trarNo",
                "mainTrarNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "trarArea",
                "coordNum",
                "coords",
                "stdrDt",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            trarNo,
                            mainTrarNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            trarArea,
                            coordNum,
                            coords,
                            stdrDt,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeZoneInAdmi(self, divId, key):
        """
        4. 행정구역 단위 상권조회
        입력: 구분ID, 행정구역코드
        구분ID - 시도(ctprvnCd), 시군구(signguCd), 행정동(adongCd)
        행정구역코드 - 시도(시도코드값), 시군구(시군구코드값), 행정동(행정동코드값)
        """
        url = f"{self.urlBase}storeZoneInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "trarNo",
                "mainTrarNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "trarArea",
                "coordNum",
                "coords",
                "stdrDt",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            trarNo,
                            mainTrarNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            trarArea,
                            coordNum,
                            coords,
                            stdrDt,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeOne(self, key):
        """
        5. 단일 상가업소 조회
        입력: 상가업소번호
        """
        url = f"{self.urlBase}storeOne?ServiceKey={self.serviceKey}&key={key}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListInBuilding(
        self, key, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None, numOfRows=1000, pageNo=1
    ):
        """
        6. 건물단위 상가업소 조회
        입력: 건물관리번호, 상권업종대분류코드, 상권업종중분류코드, 상권업종소분류코드, 페이지당 건수(최대 1000), 페이지 번호
        """

        # 대/중/소 모두 None인 경우
        if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&key={key}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 대/소만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중/소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중/소 모두 값이 존재하는 경우
        else:
            url = f"{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListInPnu(
        self, key, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None, numOfRows=1000, pageNo=1
    ):
        """
        7. 지번단위 상가업소 조회
        입력: PNU코드, 상권업종대분류코드, 상권업종중분류코드, 상권업종소분류코드, 페이지 번호
        """

        # 대/중/소 모두 None인 경우
        if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&key={key}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 대/소만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중/소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중/소 모두 값이 존재하는 경우
        else:
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListInDong(
        self,
        divId,
        key,
        indsLclsCd_=None,
        indsMclsCd_=None,
        indsSclsCd_=None,
        numOfRows=1000,
        pageNo=1,
    ):
        """
        8. 행정동 단위 상가업소 조회
        입력: 구분ID(시도:ctprvnCd, 시군구:signguCd, 행정동:adongCd), 행정구역코드, 상권업종대분류코드, 상권업종중분류코드, 상권업종소분류코드, 페이지 번호
        """

        # 대/중/소 모두 None인 경우
        if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInDong?ServiceKey={self.serviceKey}&divId={divId}&key={key}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInDong?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 대/소만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInDong?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중/소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInDong?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsLclsCd={indsLclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInDong?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInDong?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInDong?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중/소 모두 값이 존재하는 경우
        else:
            url = f"{self.urlBase}storeListInPnu?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListInArea(
        self, key, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None, numOfRows=1000, pageNo=1
    ):
        """
        9. 상권내 상가업소 조회
        입력: 상권번호, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
        """
        # 대/중/소 모두 None인 경우
        if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&key={key}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 대/소만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중/소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중/소 모두 값이 존재하는 경우
        else:
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListInRadius(
        self,
        radius,
        cx,
        cy,
        indsLclsCd_=None,
        indsMclsCd_=None,
        indsSclsCd_=None,
        numOfRows=1000,
        pageNo=1,
    ):
        """
        10. 반경내 상가업소 조회
        입력: 반경, 중심점 경도, 중심점 위도, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
        """
        # 대/중/소 모두 None인 경우
        if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 대/소만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중/소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsLclsCd={indsLclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중/소 모두 값이 존재하는 경우
        else:
            url = f"{self.urlBase}storeListInArea?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListInRectangle(
        self,
        minx,
        miny,
        maxx,
        maxy,
        indsLclsCd_=None,
        indsMclsCd_=None,
        indsSclsCd_=None,
        numOfRows=1000,
        pageNo=1,
    ):
        """
        11. 사각형내 상가업소 조회
        입력: 서쪽 경도, 남쪽 위도, 동쪽 경도, 북쪽 위도, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
        """
        # 대/중/소 모두 None인 경우
        if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 대/소만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중/소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&indsLclsCd={indsLclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중/소 모두 값이 존재하는 경우
        else:
            url = f"{self.urlBase}storeListInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListInPolygon(
        self, key, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None, numOfRows=1000, pageNo=1
    ):
        """
        12. 다각형내 상가업소 조회
        입력: 다각형 좌표값, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
        """
        # 대/중/소 모두 None인 경우
        if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInPolygon?ServiceKey={self.serviceKey}&key={key}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInPolygon?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 대/소만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInPolygon?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중/소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInPolygon?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInPolygon?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListInPolygon?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListInPolygon?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중/소 모두 값이 존재하는 경우
        else:
            url = f"{self.urlBase}storeListInPolygon?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListInUpjong(self, divId, key, numOfRows=1000, pageNo=1):
        """
        13. 업종별 상가업소 조회
        입력: 구분ID(대분류:indsLclsCd, 중분류:indsMclsCd, 소분류:indsSclsCd), 업종코드값, 페이지 번호
        """
        url = f"{self.urlBase}storeListInUpjong?ServiceKey={self.serviceKey}&divId={divId}&key={key}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def storeListByDate(
        self, key, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None, numOfRows=1000, pageNo=1
    ):
        """
        14. 수정일자기준 상가업소 조회
        입력: 일자(YYYYMMDD), 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
        """
        # 대/중/소 모두 None인 경우
        if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListByDate?ServiceKey={self.serviceKey}&key={key}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListByDate?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 대/소만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListByDate?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중/소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListByDate?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대만 None인 경우
        elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListByDate?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 중만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
            url = f"{self.urlBase}storeListByDate?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"
        # 소만 None인 경우
        elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
            url = f"{self.urlBase}storeListByDate?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        # 대/중/소 모두 값이 존재하는 경우
        else:
            url = f"{self.urlBase}storeListByDate?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}&numOfRows={numOfRows}&pageNo={pageNo}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "bizesId",
                "bizesNm",
                "brchNm",
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "ksicCd",
                "ksicNm",
                "ctprvnCd",
                "ctprvnNm",
                "signguCd",
                "signguNm",
                "adongCd",
                "adongNm",
                "ldongCd",
                "ldongNm",
                "lnoCd",
                "plotSctCd",
                "plotSctNm",
                "lnoMnno",
                "lnoSlno",
                "lnoAdr",
                "rdnmCd",
                "rdnm",
                "bldMnno",
                "bldSlno",
                "bldMngNo",
                "bldNm",
                "rdnmAdr",
                "oldZipcd",
                "newZipcd",
                "dongNo",
                "flrNo",
                "hoNo",
                "lon",
                "lat",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            bizesId,
                            bizesNm,
                            brchNm,
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            ksicCd,
                            ksicNm,
                            ctprvnCd,
                            ctprvnNm,
                            signguCd,
                            signguNm,
                            adongCd,
                            adongNm,
                            ldongCd,
                            ldongNm,
                            lnoCd,
                            plotSctCd,
                            plotSctNm,
                            lnoMnno,
                            lnoSlno,
                            lnoAdr,
                            rdnmCd,
                            rdnm,
                            bldMnno,
                            bldSlno,
                            bldMngNo,
                            bldNm,
                            rdnmAdr,
                            oldZipcd,
                            newZipcd,
                            dongNo,
                            flrNo,
                            hoNo,
                            lon,
                            lat,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def reqStoreModify(
        self,
        bizresId,
        bizresNm,
        brchNm,
        indsSclsCd,
        adongCd,
        lnoAdr,
        rdnmAdr,
        bldNm,
        dongNo,
        flrNo,
        hoNo,
        opbizDt,
        clbizDt,
        etcChgReqCnts,
    ):
        """
        15. 상가업소정보 변경요청
        입력: 상가업소번호, 상호명, 지점명, 상권업종소분류코드, 행정동코드, 지번주소, 도로명주소, 건물명, 동정보, 층정보, 호정보, 개업일자, 폐업일자, 기타입력사항
        """
        url = f"{self.urlBase}reqStoreModify?ServiceKey={self.serviceKey}&bizresId={bizresId}&bizresNm={bizresNm}&brchNm={brchNm}&indsSclsCd={indsSclsCd}&adongCd={adongCd}&lnoAdr={lnoAdr}&rdnmAdr={rdnmAdr}&bldNm={bldNm}&dongNo={dongNo}&flrNo={flrNo}&hoNo={hoNo}&opbizDt={opbizDt}&clbizDt={clbizDt}&etcChgReqCnts={etcChgReqCnts}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["bizresId", "result", "message"]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame([[bizresId, result, message]], columns=variables)
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    #     def storeStatsUpjongInAdmi(self, divId, key, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None):
    #         '''
    #         16. 행정구역내 업종별 상가업소 통계
    #         입력: 구분ID(시도:ctprvnCd, 시군구:signguCd, 행정동:adongCd), 행정구역코드, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드
    #         '''
    #         # 대/중/소 모두 None인 경우
    #         if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}'

    #         # 대/중만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsSclsCd={indsSclsCd_}'
    #         # 대/소만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsMclsCd={indsMclsCd_}'
    #         # 중/소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsLclsCd={indsLclsCd_}'

    #         # 대만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsSclsCd={indsSclsCd_}'
    #         # 중만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsSclsCd={indsSclsCd_}'
    #         # 소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsMclsCd={indsMclsCd_}'

    #         # 대/중/소 모두 값이 존재하는 경우
    #         else:
    #             url = f'{self.urlBase}storeStatsUpjongInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}'

    #

    #         try:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("item")

    #             # Creating Pandas Data Frame
    #             df = pd.DataFrame()
    #             variables = ['bizesId','bizesNm','brchNm','indsLclsCd','indsLclsNm',
    #                          'indsMclsCd','indsMclsNm','indsSclsCd','indsSclsNm','ksicCd',
    #                          'ksicNm','ctprvnCd','ctprvnNm','signguCd','signguNm',
    #                          'adongCd','adongNm','ldongCd','ldongNm','lnoCd',
    #                          'plotSctCd','plotSctNm','lnoMnno','lnoSlno','lnoAdr',
    #                          'rdnmCd','rdnm','bldMnno','bldSlno','bldMngNo',
    #                          'bldNm','rdnmAdr','oldZipcd','newZipcd','dongNo',
    #                          'flrNo','hoNo','lon','lat']

    #             for t in te:
    #                 for variable in variables:
    #                     try :
    #                         globals()[variable] = t.find(variable).text
    #                     except :
    #                         globals()[variable] = np.nan
    #                 data = pd.DataFrame(
    #                                     [[bizesId,bizesNm,brchNm,indsLclsCd,indsLclsNm,
    #                                      indsMclsCd,indsMclsNm,indsSclsCd,indsSclsNm,ksicCd,
    #                                      ksicNm,ctprvnCd,ctprvnNm,signguCd,signguNm,
    #                                      adongCd,adongNm,ldongCd,ldongNm,lnoCd,
    #                                      plotSctCd,plotSctNm,lnoMnno,lnoSlno,lnoAdr,
    #                                      rdnmCd,rdnm,bldMnno,bldSlno,bldMngNo,
    #                                      bldNm,rdnmAdr,oldZipcd,newZipcd,dongNo,
    #                                      flrNo,hoNo,lon,lat]],
    #                                     columns = variables
    #                                     )
    #                 df = pd.concat([df, data])

    #             # Set col names
    #             df.columns = variables
    #             # Set Index
    #             df.index = range(len(df))

    #         except:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("header")
    #             # 정상 요청시 에러 발생 -> Python 코드 에러
    #             if te[0].find('resultCode').text == "00":
    #                 print(">>> Python Logic Error. e-mail : wooil@kakao.com")
    #             elif te[0].find('resultCode').text == "03":
    #                 print(">>> NODATA_ERROR")
    #             # Open API 서비스 제공처 오류
    #             else:
    #                 print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
    #             pass

    #         return df

    #     def storeStatsUpjongInBuilding(self, key, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None):
    #         '''
    #         17. 건물내 업종별 상가업소 통계
    #         입력: 건물관리번호, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드
    #         '''
    #         # 대/중/소 모두 None인 경우
    #         if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&key={key}'

    #         # 대/중만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}'
    #         # 대/소만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}'
    #         # 중/소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}'

    #         # 대만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}'
    #         # 중만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}'
    #         # 소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}'

    #         # 대/중/소 모두 값이 존재하는 경우
    #         else:
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}'

    #

    #         try:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("item")

    #             # Creating Pandas Data Frame
    #             df = pd.DataFrame()
    #             variables = ['bizesId','bizesNm','brchNm','indsLclsCd','indsLclsNm',
    #                          'indsMclsCd','indsMclsNm','indsSclsCd','indsSclsNm','ksicCd',
    #                          'ksicNm','ctprvnCd','ctprvnNm','signguCd','signguNm',
    #                          'adongCd','adongNm','ldongCd','ldongNm','lnoCd',
    #                          'plotSctCd','plotSctNm','lnoMnno','lnoSlno','lnoAdr',
    #                          'rdnmCd','rdnm','bldMnno','bldSlno','bldMngNo',
    #                          'bldNm','rdnmAdr','oldZipcd','newZipcd','dongNo',
    #                          'flrNo','hoNo','lon','lat']

    #             for t in te:
    #                 for variable in variables:
    #                     try :
    #                         globals()[variable] = t.find(variable).text
    #                     except :
    #                         globals()[variable] = np.nan
    #                 data = pd.DataFrame(
    #                                     [[bizesId,bizesNm,brchNm,indsLclsCd,indsLclsNm,
    #                                      indsMclsCd,indsMclsNm,indsSclsCd,indsSclsNm,ksicCd,
    #                                      ksicNm,ctprvnCd,ctprvnNm,signguCd,signguNm,
    #                                      adongCd,adongNm,ldongCd,ldongNm,lnoCd,
    #                                      plotSctCd,plotSctNm,lnoMnno,lnoSlno,lnoAdr,
    #                                      rdnmCd,rdnm,bldMnno,bldSlno,bldMngNo,
    #                                      bldNm,rdnmAdr,oldZipcd,newZipcd,dongNo,
    #                                      flrNo,hoNo,lon,lat]],
    #                                     columns = variables
    #                                     )
    #                 df = pd.concat([df, data])

    #             # Set col names
    #             df.columns = variables
    #             # Set Index
    #             df.index = range(len(df))

    #         except:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("header")
    #             # 정상 요청시 에러 발생 -> Python 코드 에러
    #             if te[0].find('resultCode').text == "00":
    #                 print(">>> Python Logic Error. e-mail : wooil@kakao.com")
    #             elif te[0].find('resultCode').text == "03":
    #                 print(">>> NODATA_ERROR")
    #             # Open API 서비스 제공처 오류
    #             else:
    #                 print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
    #             pass

    #         return df

    #     def storeStatsUpjongInRadius(self, radius, cx, cy, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None):
    #         '''
    #         18. 반경내 업종별 상가업소 통계
    #         입력: 반경, 중심점 경도, 중심점 위도, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드
    #         '''
    #         # 대/중/소 모두 None인 경우
    #         if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}'

    #         # 대/중만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}'
    #         # 대/소만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsMclsCd={indsMclsCd_}'
    #         # 중/소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsLclsCd={indsLclsCd_}'

    #         # 대만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}'
    #         # 중만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}'
    #         # 소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsMclsCd={indsMclsCd_}'

    #         # 대/중/소 모두 값이 존재하는 경우
    #         else:
    #             url = f'{self.urlBase}storeStatsUpjongInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}'

    #

    #         try:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("item")

    #             # Creating Pandas Data Frame
    #             df = pd.DataFrame()
    #             variables = ['bizesId','bizesNm','brchNm','indsLclsCd','indsLclsNm',
    #                          'indsMclsCd','indsMclsNm','indsSclsCd','indsSclsNm','ksicCd',
    #                          'ksicNm','ctprvnCd','ctprvnNm','signguCd','signguNm',
    #                          'adongCd','adongNm','ldongCd','ldongNm','lnoCd',
    #                          'plotSctCd','plotSctNm','lnoMnno','lnoSlno','lnoAdr',
    #                          'rdnmCd','rdnm','bldMnno','bldSlno','bldMngNo',
    #                          'bldNm','rdnmAdr','oldZipcd','newZipcd','dongNo',
    #                          'flrNo','hoNo','lon','lat']

    #             for t in te:
    #                 for variable in variables:
    #                     try :
    #                         globals()[variable] = t.find(variable).text
    #                     except :
    #                         globals()[variable] = np.nan
    #                 data = pd.DataFrame(
    #                                     [[bizesId,bizesNm,brchNm,indsLclsCd,indsLclsNm,
    #                                      indsMclsCd,indsMclsNm,indsSclsCd,indsSclsNm,ksicCd,
    #                                      ksicNm,ctprvnCd,ctprvnNm,signguCd,signguNm,
    #                                      adongCd,adongNm,ldongCd,ldongNm,lnoCd,
    #                                      plotSctCd,plotSctNm,lnoMnno,lnoSlno,lnoAdr,
    #                                      rdnmCd,rdnm,bldMnno,bldSlno,bldMngNo,
    #                                      bldNm,rdnmAdr,oldZipcd,newZipcd,dongNo,
    #                                      flrNo,hoNo,lon,lat]],
    #                                     columns = variables
    #                                     )
    #                 df = pd.concat([df, data])

    #             # Set col names
    #             df.columns = variables
    #             # Set Index
    #             df.index = range(len(df))

    #         except:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("header")
    #             # 정상 요청시 에러 발생 -> Python 코드 에러
    #             if te[0].find('resultCode').text == "00":
    #                 print(">>> Python Logic Error. e-mail : wooil@kakao.com")
    #             elif te[0].find('resultCode').text == "03":
    #                 print(">>> NODATA_ERROR")
    #             # Open API 서비스 제공처 오류
    #             else:
    #                 print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
    #             pass

    #         return df

    #     def storeStatsUpjongInRectangle(self, minx, miny, maxx, maxy, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None):
    #         '''
    #         19. 사각형내 업종별 상가업소 통계
    #         입력: 서쪽 경도, 남쪽 위도, 동쪽 경도, 북쪽 위도, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드
    #         '''
    #         # 대/중/소 모두 None인 경우
    #         if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInRectangle?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}'

    #         # 대/중만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInRectangle?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}'
    #         # 대/소만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInRectangle?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsMclsCd={indsMclsCd_}'
    #         # 중/소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInRectangle?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsLclsCd={indsLclsCd_}'

    #         # 대만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInRectangle?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}'
    #         # 중만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInRectangle?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsSclsCd={indsSclsCd_}'
    #         # 소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInRectangle?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsMclsCd={indsMclsCd_}'

    #         # 대/중/소 모두 값이 존재하는 경우
    #         else:
    #             url = f'{self.urlBase}storeStatsUpjongInBuilding?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}'

    #

    #         try:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("item")

    #             # Creating Pandas Data Frame
    #             df = pd.DataFrame()
    #             variables = ['bizesId','bizesNm','brchNm','indsLclsCd','indsLclsNm',
    #                          'indsMclsCd','indsMclsNm','indsSclsCd','indsSclsNm','ksicCd',
    #                          'ksicNm','ctprvnCd','ctprvnNm','signguCd','signguNm',
    #                          'adongCd','adongNm','ldongCd','ldongNm','lnoCd',
    #                          'plotSctCd','plotSctNm','lnoMnno','lnoSlno','lnoAdr',
    #                          'rdnmCd','rdnm','bldMnno','bldSlno','bldMngNo',
    #                          'bldNm','rdnmAdr','oldZipcd','newZipcd','dongNo',
    #                          'flrNo','hoNo','lon','lat']

    #             for t in te:
    #                 for variable in variables:
    #                     try :
    #                         globals()[variable] = t.find(variable).text
    #                     except :
    #                         globals()[variable] = np.nan
    #                 data = pd.DataFrame(
    #                                     [[bizesId,bizesNm,brchNm,indsLclsCd,indsLclsNm,
    #                                      indsMclsCd,indsMclsNm,indsSclsCd,indsSclsNm,ksicCd,
    #                                      ksicNm,ctprvnCd,ctprvnNm,signguCd,signguNm,
    #                                      adongCd,adongNm,ldongCd,ldongNm,lnoCd,
    #                                      plotSctCd,plotSctNm,lnoMnno,lnoSlno,lnoAdr,
    #                                      rdnmCd,rdnm,bldMnno,bldSlno,bldMngNo,
    #                                      bldNm,rdnmAdr,oldZipcd,newZipcd,dongNo,
    #                                      flrNo,hoNo,lon,lat]],
    #                                     columns = variables
    #                                     )
    #                 df = pd.concat([df, data])

    #             # Set col names
    #             df.columns = variables
    #             # Set Index
    #             df.index = range(len(df))

    #         except:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("header")
    #             # 정상 요청시 에러 발생 -> Python 코드 에러
    #             if te[0].find('resultCode').text == "00":
    #                 print(">>> Python Logic Error. e-mail : wooil@kakao.com")
    #             elif te[0].find('resultCode').text == "03":
    #                 print(">>> NODATA_ERROR")
    #             # Open API 서비스 제공처 오류
    #             else:
    #                 print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
    #             pass

    #         return df

    #     def storeStatsUpjongInPolygon(self, key, indsLclsCd_=None, indsMclsCd_=None, indsSclsCd_=None):
    #         '''
    #         20. 다각형내 업종별 상가업소 통계
    #         입력: 다각형 좌표값, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드
    #         '''
    #         # 대/중/소 모두 None인 경우
    #         if (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInPolygon?ServiceKey={self.serviceKey}&key={key}'

    #         # 대/중만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInPolygon?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}'
    #         # 대/소만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInPolygon?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}'
    #         # 중/소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInPolygon?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}'

    #         # 대만 None인 경우
    #         elif (indsLclsCd_ == None) & (indsMclsCd_ != None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInPolygon?ServiceKey={self.serviceKey}&key={key}&indsSclsCd={indsSclsCd_}'
    #         # 중만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ == None) & (indsSclsCd_ != None):
    #             url = f'{self.urlBase}storeStatsUpjongInPolygon?ServiceKey={self.serviceKey}key={key}&indsSclsCd={indsSclsCd_}'
    #         # 소만 None인 경우
    #         elif (indsLclsCd_ != None) & (indsMclsCd_ != None) & (indsSclsCd_ == None):
    #             url = f'{self.urlBase}storeStatsUpjongInPolygon?ServiceKey={self.serviceKey}&key={key}&indsMclsCd={indsMclsCd_}'

    #         # 대/중/소 모두 값이 존재하는 경우
    #         else:
    #             url = f'{self.urlBase}storeStatsUpjongInPolygon?ServiceKey={self.serviceKey}&key={key}&indsLclsCd={indsLclsCd_}&indsMclsCd={indsMclsCd_}&indsSclsCd={indsSclsCd_}'

    #

    #         try:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("item")

    #             # Creating Pandas Data Frame
    #             df = pd.DataFrame()
    #             variables = ['bizesId','bizesNm','brchNm','indsLclsCd','indsLclsNm',
    #                          'indsMclsCd','indsMclsNm','indsSclsCd','indsSclsNm','ksicCd',
    #                          'ksicNm','ctprvnCd','ctprvnNm','signguCd','signguNm',
    #                          'adongCd','adongNm','ldongCd','ldongNm','lnoCd',
    #                          'plotSctCd','plotSctNm','lnoMnno','lnoSlno','lnoAdr',
    #                          'rdnmCd','rdnm','bldMnno','bldSlno','bldMngNo',
    #                          'bldNm','rdnmAdr','oldZipcd','newZipcd','dongNo',
    #                          'flrNo','hoNo','lon','lat']

    #             for t in te:
    #                 for variable in variables:
    #                     try :
    #                         globals()[variable] = t.find(variable).text
    #                     except :
    #                         globals()[variable] = np.nan
    #                 data = pd.DataFrame(
    #                                     [[bizesId,bizesNm,brchNm,indsLclsCd,indsLclsNm,
    #                                      indsMclsCd,indsMclsNm,indsSclsCd,indsSclsNm,ksicCd,
    #                                      ksicNm,ctprvnCd,ctprvnNm,signguCd,signguNm,
    #                                      adongCd,adongNm,ldongCd,ldongNm,lnoCd,
    #                                      plotSctCd,plotSctNm,lnoMnno,lnoSlno,lnoAdr,
    #                                      rdnmCd,rdnm,bldMnno,bldSlno,bldMngNo,
    #                                      bldNm,rdnmAdr,oldZipcd,newZipcd,dongNo,
    #                                      flrNo,hoNo,lon,lat]],
    #                                     columns = variables
    #                                     )
    #                 df = pd.concat([df, data])

    #             # Set col names
    #             df.columns = variables
    #             # Set Index
    #             df.index = range(len(df))

    #         except:
    #             # Get raw data
    #             result = requests.get(url, verify=False)
    #             # Parsing
    #             xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
    #             # Filtering
    #             te = xmlsoup.findAll("header")
    #             # 정상 요청시 에러 발생 -> Python 코드 에러
    #             if te[0].find('resultCode').text == "00":
    #                 print(">>> Python Logic Error. e-mail : wooil@kakao.com")
    #             elif te[0].find('resultCode').text == "03":
    #                 print(">>> NODATA_ERROR")
    #             # Open API 서비스 제공처 오류
    #             else:
    #                 print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
    #             pass

    #         return df

    def largeUpjongList(self):
        """
        21. 상권정보 업종 대분류 조회
        """
        url = f"{self.urlBase}largeUpjongList?ServiceKey={self.serviceKey}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["indsLclsCd", "indsLclsNm", "stdrDt"]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame([[indsLclsCd, indsLclsNm, stdrDt]], columns=variables)
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def middleUpjongList(self, indsLclsCd_):
        """
        22. 상권정보 업종 중분류 조회
        입력: 상권업종 업종 대분류코드
        """
        url = (
            f"{self.urlBase}middleUpjongList?ServiceKey={self.serviceKey}&indsLclsCd={indsLclsCd_}"
        )

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = ["indsLclsCd", "indsLclsNm", "indsMclsCd", "indsMclsNm", "stdrDt"]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [[indsLclsCd, indsLclsNm, indsMclsCd, indsMclsNm, stdrDt]], columns=variables
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df

    def smallUpjongList(self, indsLclsCd_=None, indsMclsCd_=None):
        """
        23. 상권정보 업종 소분류 조회
        입력: 상권정보 업종 대분류코드, 상권정보 업종 중분류코드
        """

        if (indsLclsCd_ != None) & (indsMclsCd_ == None):
            url = f"{self.urlBase}smallUpjongList?ServiceKey={self.serviceKey}&indsLclsCd={indsLclsCd_}"

        elif (indsLclsCd_ == None) & (indsMclsCd_ != None):
            url = f"{self.urlBase}smallUpjongList?ServiceKey={self.serviceKey}&indsMclsCd={indsMclsCd_}"

        elif (indsLclsCd_ != None) & (indsMclsCd_ != None):
            url = f"{self.urlBase}smallUpjongList?ServiceKey={self.serviceKey}&indsMclsCd={indsMclsCd_}"

        else:
            print(">> Parameters None")
            return 0

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()
            variables = [
                "indsLclsCd",
                "indsLclsNm",
                "indsMclsCd",
                "indsMclsNm",
                "indsSclsCd",
                "indsSclsNm",
                "stdrDt",
            ]

            for t in te:
                for variable in variables:
                    try:
                        globals()[variable] = t.find(variable).text
                    except:
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                    [
                        [
                            indsLclsCd,
                            indsLclsNm,
                            indsMclsCd,
                            indsMclsNm,
                            indsSclsCd,
                            indsSclsNm,
                            stdrDt,
                        ]
                    ],
                    columns=variables,
                )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            # Filtering
            te = xmlsoup.findAll("header")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find("resultCode").text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")
            elif te[0].find("resultCode").text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find["resultMsg"]))
            pass

        return df
