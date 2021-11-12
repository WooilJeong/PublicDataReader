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
import logging
import requests
from bs4 import BeautifulSoup



class StoreInfo:
    """
    소상공인 상가업소 정보 조회 클래스
    """

    def __init__(self, serviceKey, debug=False):
        """
        공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.
        - serviceKey: 서비스 인증키 문자열
        - debug: True이면 모든 로깅 메시지 출력, False이면 에러 로깅 메시지만 출력
        """
        # 로거 설정
        self.logger = logging.getLogger("root")
        # 로깅 레벨 설정
        if debug == True:
            self.logger.setLevel(logging.INFO)
        else:
            self.logger.setLevel(logging.ERROR)
        # 출력 포매팅 설정 - 시간, 로거이름, 로깅레벨, 메세지
        formatter = logging.Formatter("[%(levelname)s] %(message)s")
        if len(self.logger.handlers) == 0:
            # 스트림 핸들러 설정 - 콘솔에 출력
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

        # Open API 서비스 키 초기화
        self.serviceKey = serviceKey

        # ServiceKey 등록
        self.urlBase = f"http://apis.data.go.kr/B553077/api/open/sdsc/"
        self.endpoint = f"http://apis.data.go.kr/B553077/api/open/sdsc/"

        # 오퍼레이션별 URL 및 컬럼 매핑 딕셔너리
        self.metaDict = {
            
            "지정상권": {
                "url": f"{self.endpoint}storeZoneOne?serviceKey={self.serviceKey}",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },
            
            "반경상권": {
                "url": f"{self.endpoint}storeZoneInRadius?serviceKey={self.serviceKey}",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },

            "사각형상권": {
                "url": f"{self.endpoint}storeZoneInRectangle?serviceKey={self.serviceKey}",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },

            "행정구역상권": {
                "url": f"{self.endpoint}storeZoneInAdmi?serviceKey={self.serviceKey}",
                "columns": ['trarNo', 'mainTrarNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'trarArea', 'coordNum', 'coords', 'stdrDt'],
            },

            "단일상가": {
                "url": f"{self.endpoint}storeOne?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "건물상가": {
                "url": f"{self.endpoint}storeListInBuilding?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "지번상가": {
                "url": f"{self.endpoint}storeListInPnu?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "행정동상가": {
                "url": f"{self.endpoint}storeListInDong?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "상권상가": {
                "url": f"{self.endpoint}storeListInArea?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "반경상가": {
                "url": f"{self.endpoint}storeListInRadius?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "사각형상가": {
                "url": f"{self.endpoint}storeListInRectangle?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "다각형상가": {
                "url": f"{self.endpoint}storeListInPolygon?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "업종별상가": {
                "url": f"{self.endpoint}storeListInUpjong?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "수정일자상가": {
                "url": f"{self.endpoint}storeListByDate?serviceKey={self.serviceKey}",
                "columns": ['bizesId', 'bizesNm', 'brchNm', 'indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'ksicCd', 'ksicNm', 'ctprvnCd', 'ctprvnNm', 'signguCd', 'signguNm', 'adongCd', 'adongNm', 'ldongCd', 'ldongNm', 'lnoCd', 'plotSctCd', 'plotSctNm', 'lnoMnno', 'lnoSlno', 'lnoAdr', 'rdnmCd', 'rdnm', 'bldMnno', 'bldSlno', 'bldMngNo', 'bldNm', 'rdnmAdr', 'oldZipcd', 'newZipcd', 'dongNo', 'flrNo', 'hoNo', 'lon', 'lat'],
            },

            "업종대분류": {
                "url": f"{self.endpoint}largeUpjongList?serviceKey={self.serviceKey}",
                "columns": ["indsLclsCd", "indsLclsNm", "stdrDt"],
            },

            "업종중분류": {
                "url": f"{self.endpoint}middleUpjongList?serviceKey={self.serviceKey}",
                "columns": ["indsLclsCd", "indsLclsNm", "indsMclsCd", "indsMclsNm", "stdrDt"],
            },

            "업종소분류": {
                "url": f"{self.endpoint}smallUpjongList?serviceKey={self.serviceKey}",
                "columns": ['indsLclsCd', 'indsLclsNm', 'indsMclsCd', 'indsMclsNm', 'indsSclsCd', 'indsSclsNm', 'stdrDt'],
            },
            
        }


    def read_data(self, category, **kwargs):

        # 엔드포인트, 파라미터 및 컬럼 목록 매핑
        try:
            endpoint = self.metaDict[category]['url']
            columns = self.metaDict[category]['columns']
        except:
            self.logger.error(f"{category} 참조 오류")
            return

        try:
            params = ""
            for key, value in kwargs.items():
                params += f"&{key}={value}"
        except:
            self.logger.error(f"{category} 파라미터 파싱 오류")
            return

        try:
            # URL
            url=f"""{endpoint}{params}&numOfRows=99999"""

            # Open API 호출
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            header = xmlsoup.find("header")
            result_code = header.find("resultCode").text
            result_msg = header.find("resultMsg").text
            items = xmlsoup.findAll("item")

        except:
            self.logger.error(f"Open API 호출 오류")
            return

        if result_code == "00":
            """
            결과 정상
            """
            # 데이터프레임 생성
            try:
                df = pd.DataFrame()
                for item in items:
                    row = {}
                    for col in columns:
                        try:
                            tag = item.find(col)
                            row[col] = tag.text.strip()
                        except:
                            row[col] = ""
                    df_ = pd.DataFrame([row])
                    df = df.append(df_)

                if len(df) != 0:
                    df = df[columns]
    #                 df = self.ChangeCols(df, category)
                    df.index = range(len(df))

                else:
                    self.logger.info(f"조회 결과 없음")
                    df = pd.DataFrame(columns=columns)
    #                 df = self.ChangeCols(df, category)
                    return df

            except:
                self.logger.error(f"조회 로직 오류")
                return

        else:
            """
            결과 에러
            """
            self.logger.error(f"({result_code}) {result_msg}")
            return

        return df