"""
국토교통부 Open API
molit(Ministry of Land, Infrastructure and Transport)

1. Transaction 클래스: 부동산 실거래가 조회
    01.아파트매매 실거래 상세 자료 조회
    02.아파트 전월세 자료 조회
    03.아파트 분양권전매 신고 자료 조회
    04.오피스텔 매매 신고 조회
    05.오피스텔 전월세 신고 조회
    06.연립다세대 매매 실거래자료 조회
    07.연립다세대 전월세 실거래자료 조회
    08.단독/다가구 매매 실거래 조회
    09.단독/다가구 전월세 자료 조회
    10.토지 매매 신고 조회
    11.상업업무용 부동산 매매 신고 자료 조회

2. Building 클래스: 건축물대장정보 서비스
    01.건축물대장 기본개요 조회
    02.건축물대장 총괄표제부 조회
    03.건축물대장 표제부 조회
    04.건축물대장 층별개요 조회
    05.건축물대장 부속지번 조회
    06.건축물대장 전유공용면적 조회
    07.건축물대장 오수정화시설 조회
    08.건축물대장 주택가격 조회
    09.건축물대장 전유부 조회
    10.건축물대장 지역지구구역 조회
"""

import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta
import datetime
import logging
import requests
from bs4 import BeautifulSoup


class Transaction:
    """
    부동산 실거래가 조회 클래스
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
        # ServiceKey 유효성 검사
        self.urlAptTrade = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey="
            + self.serviceKey
        )
        self.urlAptTradeDetail = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey="
            + self.serviceKey
        )
        self.urlAptRent = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?serviceKey="
            + self.serviceKey
        )
        self.urlAptOwnership = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSilvTrade?serviceKey="
            + self.serviceKey
        )
        self.urlOffiTrade = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade?serviceKey="
            + self.serviceKey
        )
        self.urlOffiRent = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiRent?serviceKey="
            + self.serviceKey
        )
        self.urlRHTrade = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade?serviceKey="
            + self.serviceKey
        )
        self.urlRHRent = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?serviceKey="
            + self.serviceKey
        )
        self.urlDHTrade = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHTrade?serviceKey="
            + self.serviceKey
        )
        self.urlDHRent = (
            "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent?serviceKey="
            + self.serviceKey
        )
        self.urlLandTrade = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcLandTrade?serviceKey="
            + self.serviceKey
        )
        self.urlBizTrade = (
            "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade?serviceKey="
            + self.serviceKey
        )

        # Open API URL Dict
        urlDict = {
            "아파트매매 실거래자료 조회": self.urlAptTrade,
            "아파트매매 실거래 상세 자료 조회": self.urlAptTradeDetail,
            "아파트 전월세 자료 조회": self.urlAptRent,
            "아파트 분양권전매 신고 자료 조회": self.urlAptOwnership,
            "오피스텔 매매 신고 조회": self.urlOffiTrade,
            "오피스텔 전월세 신고 조회": self.urlOffiRent,
            "연립다세대 매매 실거래자료 조회": self.urlRHTrade,
            "연립다세대 전월세 실거래자료 조회": self.urlRHRent,
            "단독/다가구 매매 실거래 조회": self.urlDHTrade,
            "단독/다가구 전월세 자료 조회": self.urlDHRent,
            "토지 매매 신고 조회": self.urlLandTrade,
            "상업업무용 부동산 매매 신고 자료 조회": self.urlBizTrade,
        }

        # 서비스 정상 작동 여부 확인
        for serviceName, url in urlDict.items():
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            header = xmlsoup.findAll("header")[0]
            result_code = header.find('resultCode').text
            result_message = header.find('resultMsg').text
            if result_code == "00":
                self.logger.info(f"{serviceName} - ({result_code}) {result_message}")
            else:
                self.logger.error(f"{serviceName} - ({result_code}) {result_message}")

        # URL 및 컬럼 리스트 매핑
        self.metaDict = {
            "아파트": {
                "매매": {
                    "url": self.urlAptTradeDetail,
                    "columns": ['지역코드', '도로명', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일', '거래금액', '도로명건물본번호코드', '도로명건물부번호코드', '도로명시군구코드', '도로명일련번호코드', '도로명지상지하코드', '도로명코드', '법정동본번코드', '법정동부번코드', '법정동시군구코드', '법정동읍면동코드', '법정동지번코드', '일련번호', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": self.urlAptRent,
                    "columns": ['지역코드', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일', '보증금액', '월세금액']
                }
            },
            
            "오피스텔": {
                "매매": {
                    "url": self.urlOffiTrade,
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '건축년도', '층', '전용면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": self.urlOffiRent,
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '건축년도', '층', '전용면적', '년', '월', '일', '보증금', '월세']
                }
            },
            
            "단독다가구": {
                "매매": {
                    "url": self.urlDHTrade,
                    "columns":['지역코드', '법정동', '주택유형', '건축년도', '대지면적', '연면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": self.urlDHRent,
                    "columns": ['지역코드', '법정동', '건축년도', '계약면적', '년', '월', '일', '보증금액', '월세금액']
                }
            },
            
            "연립다세대": {
                "매매": {
                    "url": self.urlRHTrade,
                    "columns": ['지역코드', '법정동', '지번', '연립다세대', '건축년도', '층', '대지권면적', '전용면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": self.urlRHRent,
                    "columns": ['지역코드', '법정동', '지번', '연립다세대', '건축년도', '층', '전용면적', '년', '월', '일', '보증금액', '월세금액']
                }
            },
            
            "상업업무용": {
                "매매": {
                    "url": self.urlBizTrade,
                    "columns": ['지역코드', '시군구', '법정동', '유형', '용도지역', '건물주용도', '건축년도', '대지면적', '건물면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },

            "토지": {
                "매매": {
                    "url": self.urlLandTrade,
                    "columns":['지역코드', '시군구', '법정동', '용도지역', '지목', '거래면적', '거래금액', '년', '월', '일', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },
            
            "분양입주권": {
                "매매": {
                    "url": self.urlAptOwnership,
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '층', '전용면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },
        }


    def collect_data(self, prod, trans, sigunguCode, startYearMonth, endYearMonth):
        """
        prod: 상품유형 (ex.아파트, 오피스텔, 단독다가구, 연립다세대, 토지, 상업업무용)
        trans: 매매, 전월세
        sigunguCode: 시군구코드(5자리)
        startYearMonth: 조회시작 계약년월("YYYYmm")
        endYearMonth: 조회종료 계약년월("YYYYmm")
        """
        start_date = datetime.datetime.strptime(str(startYearMonth), "%Y%m")
        start_date = datetime.datetime.strftime(start_date, "%Y-%m")
        end_date = datetime.datetime.strptime(str(endYearMonth), "%Y%m")
        end_date = end_date + datetime.timedelta(days=31)
        end_date = datetime.datetime.strftime(end_date, "%Y-%m")
        ts = pd.date_range(start=start_date, end=end_date, freq="m")
        date_list = list(ts.strftime("%Y%m"))
        df = pd.DataFrame()
        for yearMonth in date_list:
            try:
                self.logger.info(f"{prod} {trans} {yearMonth} 조회 시작")
                df_ = self.read_data(prod, trans, sigunguCode, yearMonth)
                df = df.append(df_)
            except:
                self.logger.eeror(f"{prod} {trans} {yearMonth} 조회 오류")
                return
        df.index = range(len(df))
        return df


    def read_data(self, prod, trans, sigunguCode, yearMonth):
        """
        prod: 상품유형 (ex.아파트, 오피스텔, 단독다가구, 연립다세대, 토지, 상업업무용)
        trans: 매매, 전월세
        sigunguCode: 시군구코드(5자리)
        yearMonth: 계약년월("YYYYmm")
        """
        # 엔드포인트 및 컬럼 목록 매핑
        try:
            endpoint = self.metaDict[prod][trans]['url']
            columns = self.metaDict[prod][trans]['columns']
        except:
            self.logger.error(f"{prod} {trans} 참조 오류")
            return
        
        try:
            # URL
            url=f"""{endpoint}&LAWD_CD={str(sigunguCode)}&DEAL_YMD={str(yearMonth)}&numOfRows=99999"""
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
                    df.index = range(len(df))
                else:
                    self.logger.info(f"조회 결과 없음")
                    return pd.DataFrame(columns=columns)

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


class Building:
    """
    건축물대장정보 서비스
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

        # ServiceKey 유효성 검사
        self.baseUrl = "http://apis.data.go.kr/1613000/BldRgstService_v2/"

        self.url_getBrBasisOulnInfo = (
            self.baseUrl + "getBrBasisOulnInfo" + f"?serviceKey={self.serviceKey}"
        )
        self.url_getBrRecapTitleInfo = (
            self.baseUrl + "getBrRecapTitleInfo" + f"?serviceKey={self.serviceKey}"
        )
        self.url_getBrTitleInfo = self.baseUrl + "getBrTitleInfo" + f"?serviceKey={self.serviceKey}"
        self.url_getBrFlrOulnInfo = (
            self.baseUrl + "getBrFlrOulnInfo" + f"?serviceKey={self.serviceKey}"
        )
        self.url_getBrAtchJibunInfo = (
            self.baseUrl + "getBrAtchJibunInfo" + f"?serviceKey={self.serviceKey}"
        )

        self.url_getBrExposPubuseAreaInfo = (
            self.baseUrl + "getBrExposPubuseAreaInfo" + f"?serviceKey={self.serviceKey}"
        )
        self.url_getBrWclfInfo = self.baseUrl + "getBrWclfInfo" + f"?serviceKey={self.serviceKey}"
        self.url_getBrHsprcInfo = self.baseUrl + "getBrHsprcInfo" + f"?serviceKey={self.serviceKey}"
        self.url_getBrExposInfo = self.baseUrl + "getBrExposInfo" + f"?serviceKey={self.serviceKey}"
        self.url_getBrJijiguInfo = (
            self.baseUrl + "getBrJijiguInfo" + f"?serviceKey={self.serviceKey}"
        )

        # Open API URL Dict
        urlDict = {
            "건축물대장 기본개요 조회": self.url_getBrBasisOulnInfo,
            "건축물대장 총괄표제부 조회": self.url_getBrRecapTitleInfo,
            "건축물대장 표제부 조회": self.url_getBrTitleInfo,
            "건축물대장 층별개요 조회": self.url_getBrFlrOulnInfo,
            "건축물대장 부속지번 조회": self.url_getBrAtchJibunInfo,
            "건축물대장 전유공용면적 조회": self.url_getBrExposPubuseAreaInfo,
            "건축물대장 오수정화시설 조회": self.url_getBrWclfInfo,
            "건축물대장 주택가격 조회": self.url_getBrHsprcInfo,
            "건축물대장 전유부 조회": self.url_getBrExposInfo,
            "건축물대장 지역지구구역 조회": self.url_getBrJijiguInfo,
        }

        # 서비스 정상 작동 여부 확인
        for serviceName, url in urlDict.items():
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            header = xmlsoup.findAll("header")[0]
            result_code = header.find('resultCode').text
            result_message = header.find('resultMsg').text
            if result_code == "00":
                self.logger.info(f"{serviceName} - ({result_code}) {result_message}")
            else:
                self.logger.error(f"{serviceName} - ({result_code}) {result_message}")
        
        self.metaDict = {
            
            "기본개요": {
                "url": self.url_getBrBasisOulnInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'guyukCd', 'guyukCdNm', 'ji', 'jiguCd', 'jiguCdNm', 'jiyukCd', 'jiyukCdNm', 'lot', 'mgmBldrgstPk', 'mgmUpBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },
            
            "총괄표제부": {
                "url": self.url_getBrRecapTitleInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['archArea', 'atchBldArea', 'atchBldCnt', 'bcRat', 'bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'engrEpi', 'engrGrade', 'engrRat', 'etcPurps', 'fmlyCnt', 'gnBldCert', 'gnBldGrade', 'hhldCnt', 'hoCnt', 'indrAutoArea', 'indrAutoUtcnt', 'indrMechArea', 'indrMechUtcnt', 'itgBldCert', 'itgBldGrade', 'ji', 'lot', 'mainBldCnt', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newOldRegstrGbCd', 'newOldRegstrGbCdNm', 'newPlatPlc', 'oudrAutoArea', 'oudrAutoUtcnt', 'oudrMechArea', 'oudrMechUtcnt', 'platArea', 'platGbCd', 'platPlc', 'pmsDay', 'pmsnoGbCd', 'pmsnoGbCdNm', 'pmsnoKikCd', 'pmsnoKikCdNm', 'pmsnoYear', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'stcnsDay', 'totArea', 'totPkngCnt', 'useAprDay', 'vlRat', 'vlRatEstmTotArea']
            },

            "표제부": {
                "url": self.url_getBrTitleInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['archArea', 'atchBldArea', 'atchBldCnt', 'bcRat', 'bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'dongNm', 'emgenUseElvtCnt', 'engrEpi', 'engrGrade', 'engrRat', 'etcPurps', 'etcRoof', 'etcStrct', 'fmlyCnt', 'gnBldCert', 'gnBldGrade', 'grndFlrCnt', 'heit', 'hhldCnt', 'hoCnt', 'indrAutoArea', 'indrAutoUtcnt', 'indrMechArea', 'indrMechUtcnt', 'itgBldCert', 'itgBldGrade', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'oudrAutoArea', 'oudrAutoUtcnt', 'oudrMechArea', 'oudrMechUtcnt', 'platArea', 'platGbCd', 'platPlc', 'pmsDay', 'pmsnoGbCd', 'pmsnoGbCdNm', 'pmsnoKikCd', 'pmsnoKikCdNm', 'pmsnoYear', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rideUseElvtCnt', 'rnum', 'roofCd', 'roofCdNm', 'rserthqkAblty', 'rserthqkDsgnApplyYn', 'sigunguCd', 'splotNm', 'stcnsDay', 'strctCd', 'strctCdNm', 'totArea', 'totDongTotArea', 'ugrndFlrCnt', 'useAprDay', 'vlRat', 'vlRatEstmTotArea']
            },

            "층별개요": {
                "url": self.url_getBrFlrOulnInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['area', 'areaExctYn', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'etcPurps', 'etcStrct', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'flrNoNm', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'rnum', 'sigunguCd', 'splotNm', 'strctCd', 'strctCdNm']
            },

            "부속지번": {
                "url": self.url_getBrAtchJibunInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['atchBjdongCd', 'atchBlock', 'atchBun', 'atchEtcJibunNm', 'atchJi', 'atchLot', 'atchPlatGbCd', 'atchRegstrGbCd', 'atchRegstrGbCdNm', 'atchSigunguCd', 'atchSplotNm', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },

            "전유공용면적": {
                "url": self.url_getBrExposPubuseAreaInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate', 'dongNm', 'hoNm'],
                "columns": ['area', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'etcPurps', 'etcStrct', 'exposPubuseGbCd', 'exposPubuseGbCdNm', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'flrNoNm', 'hoNm', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'strctCd', 'strctCdNm']
            },

            "오수정화시설": {
                "url": self.url_getBrWclfInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'capaLube', 'capaPsper', 'crtnDay', 'etcMode', 'ji', 'lot', 'mgmBldrgstPk', 'modeCd', 'modeCdNm', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'unitGbCd', 'unitGbCdNm']
            },

            "주택가격": {
                "url": self.url_getBrHsprcInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'hsprc', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },

            "전유부": {
                "url": self.url_getBrExposInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'hoNm', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },

            "지역지구구역": {
                "url": self.url_getBrJijiguInfo,
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'block', 'bun', 'crtnDay', 'etcJijigu', 'ji', 'jijiguCd', 'jijiguCdNm', 'jijiguGbCd', 'jijiguGbCdNm', 'lot', 'mgmBldrgstPk', 'newPlatPlc', 'platGbCd', 'platPlc', 'reprYn', 'rnum', 'sigunguCd', 'splotNm']
            },

        }

    def read_data(self, category, **kwargs):
        
        # 엔드포인트, 파라미터 및 컬럼 목록 매핑
        try:
            endpoint = self.metaDict[category]['url']
            parameters = self.metaDict[category]['parameters']
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
                    df = self.ChangeCols(df, category)
                    df.index = range(len(df))

                else:
                    self.logger.info(f"조회 결과 없음")
                    df = pd.DataFrame(columns=columns)
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


    def ChangeCols(self, df, category):
        """
        영문 컬럼명을 국문 컬럼명으로 변경
        """

        if category == "기본개요":
            self.colDict = {
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "bylotCnt": "외필지수",
                "crtnDay": "생성일자",
                "guyukCd": "구역코드",
                "guyukCdNm": "구역코드명",
                "ji": "지",
                "jiguCd": "지구코드",
                "jiguCdNm": "지구코드명",
                "jiyukCd": "지역코드",
                "jiyukCdNm": "지역코드명",
                "lot": "로트",
                "mgmBldrgstPk": "관리건축물대장PK",
                "mgmUpBldrgstPk": "관리상위건축물대장PK",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newPlatPlc": "도로명대지위치",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "regstrGbCd": "대장구분코드",
                "regstrGbCdNm": "대장구분코드명",
                "regstrKindCd": "대장종류코드",
                "regstrKindCdNm": "대장종류코드명",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
            }

        elif category == "총괄표제부":
            self.colDict = {
                "archArea": "건축면적",
                "atchBldArea": "부속건축물면적",
                "atchBldCnt": "부속건축물수",
                "bcRat": "건폐율",
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "bylotCnt": "외필지수",
                "crtnDay": "생성일자",
                "engrEpi": "EPI점수",
                "engrGrade": "에너지효율등급",
                "engrRat": "에너지절감율",
                "etcPurps": "기타용도",
                "fmlyCnt": "가구수",
                "gnBldCert": "친환경건축물인증점수",
                "gnBldGrade": "친환경건축물등급",
                "hhldCnt": "세대수",
                "hoCnt": "호수",
                "indrAutoArea": "옥내자주식면적",
                "indrAutoUtcnt": "옥내자주식대수",
                "indrMechArea": "옥내기계식면적",
                "indrMechUtcnt": "옥내기계식대수",
                "itgBldCert": "지능형건축물인증점수",
                "itgBldGrade": "지능형건축물등급",
                "ji": "지",
                "lot": "로트",
                "mainBldCnt": "주건축물수",
                "mainPurpsCd": "주용도코드",
                "mainPurpsCdNm": "주용도코드명",
                "mgmBldrgstPk": "관리건축물대장PK",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newOldRegstrGbCd": "신구대장구분코드",
                "newOldRegstrGbCdNm": "신구대장구분코드명",
                "newPlatPlc": "도로명대지위치",
                "oudrAutoArea": "옥외자주식면적",
                "oudrAutoUtcnt": "옥외자주식대수",
                "oudrMechArea": "옥외기계식면적",
                "oudrMechUtcnt": "옥외기계식대수",
                "platArea": "대지면적",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "pmsDay": "허가일",
                "pmsnoGbCd": "허가번호구분코드",
                "pmsnoGbCdNm": "허가번호구분코드명",
                "pmsnoKikCd": "허가번호기관코드",
                "pmsnoKikCdNm": "허가번호기관코드명",
                "pmsnoYear": "허가번호년",
                "regstrGbCd": "대장구분코드",
                "regstrGbCdNm": "대장구분코드명",
                "regstrKindCd": "대장종류코드",
                "regstrKindCdNm": "대장종류코드명",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
                "stcnsDay": "착공일",
                "totArea": "연면적",
                "totPkngCnt": "총주차수",
                "useAprDay": "사용승인일",
                "vlRat": "용적률",
                "vlRatEstmTotArea": "용적률산정연면적",
            }

        elif category == "표제부":
            self.colDict = {
                "archArea": "건축면적",
                "atchBldArea": "부속건축물면적",
                "atchBldCnt": "부속건축물수",
                "bcRat": "건폐율",
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "bylotCnt": "외필지수",
                "crtnDay": "생성일자",
                "dongNm": "동명칭",
                "emgenUseElvtCnt": "비상용승강기수",
                "engrEpi": "EPI점수",
                "engrGrade": "에너지효율등급",
                "engrRat": "에너지절감율",
                "etcPurps": "기타용도",
                "etcRoof": "기타지붕",
                "etcStrct": "기타구조",
                "fmlyCnt": "가구수",
                "gnBldCert": "친환경건축물인증점수",
                "gnBldGrade": "친환경건축물등급",
                "grndFlrCnt": "지상층수",
                "heit": "높이",
                "hhldCnt": "세대수",
                "hoCnt": "호수",
                "indrAutoArea": "옥내자주식면적",
                "indrAutoUtcnt": "옥내자주식대수",
                "indrMechArea": "옥내기계식면적",
                "indrMechUtcnt": "옥내기계식대수",
                "itgBldCert": "지능형건축물인증점수",
                "itgBldGrade": "지능형건축물등급",
                "ji": "지",
                "lot": "로트",
                "mainAtchGbCd": "주부속구분코드",
                "mainAtchGbCdNm": "주부속구분코드명",
                "mainPurpsCd": "주용도코드",
                "mainPurpsCdNm": "주용도코드명",
                "mgmBldrgstPk": "관리건축물대장PK",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newPlatPlc": "도로명대지위치",
                "oudrAutoArea": "옥외자주식면적",
                "oudrAutoUtcnt": "옥외자주식대수",
                "oudrMechArea": "옥외기계식면적",
                "oudrMechUtcnt": "옥외기계식대수",
                "platArea": "대지면적",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "pmsDay": "허가일",
                "pmsnoGbCd": "허가번호구분코드",
                "pmsnoGbCdNm": "허가번호구분코드명",
                "pmsnoKikCd": "허가번호기관코드",
                "pmsnoKikCdNm": "허가번호기관코드명",
                "pmsnoYear": "허가번호년",
                "regstrGbCd": "대장구분코드",
                "regstrGbCdNm": "대장구분코드명",
                "regstrKindCd": "대장종류코드",
                "regstrKindCdNm": "대장종류코드명",
                "rideUseElvtCnt": "승용승강기수",
                "rnum": "순번",
                "roofCd": "지붕코드",
                "roofCdNm": "지붕코드명",
                "rserthqkAblty": "내진 능력",
                "rserthqkDsgnApplyYn": "내진 설계 적용 여부",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
                "stcnsDay": "착공일",
                "strctCd": "구조코드",
                "strctCdNm": "구조코드명",
                "totArea": "연면적",
                "totDongTotArea": "총동연면적",
                "ugrndFlrCnt": "지하층수",
                "useAprDay": "사용승인일",
                "vlRat": "용적률",
                "vlRatEstmTotArea": "용적률산정연면적",
            }

        elif category == "층별개요":
            self.colDict = {
                "area": "면적",
                "areaExctYn": "면적제외여부",
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "crtnDay": "생성일자",
                "dongNm": "동명칭",
                "etcPurps": "기타용도",
                "etcStrct": "기타구조",
                "flrGbCd": "층구분코드",
                "flrGbCdNm": "층구분코드명",
                "flrNo": "층번호",
                "flrNoNm": "층번호명",
                "ji": "지",
                "lot": "로트",
                "mainAtchGbCd": "주부속구분코드",
                "mainAtchGbCdNm": "주부속구분코드명",
                "mainPurpsCd": "주용도코드",
                "mainPurpsCdNm": "주용도코드명",
                "mgmBldrgstPk": "관리건축물대장PK",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newPlatPlc": "도로명대지위치",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
                "strctCd": "구조코드",
                "strctCdNm": "구조코드명",
            }

        elif category == "부속지번":
            self.colDict = {
                "atchBjdongCd": "부속법정동코드",
                "atchBlock": "부속블록",
                "atchBun": "부속번",
                "atchEtcJibunNm": "부속기타지번명",
                "atchJi": "부속지",
                "atchLot": "부속로트",
                "atchPlatGbCd": "부속대지구분코드",
                "atchRegstrGbCd": "부속대장구분코드",
                "atchRegstrGbCdNm": "부속대장구분코드명",
                "atchSigunguCd": "부속시군구코드",
                "atchSplotNm": "부속특수지명",
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "crtnDay": "생성일자",
                "ji": "지",
                "lot": "로트",
                "mgmBldrgstPk": "관리건축물대장PK",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newPlatPlc": "도로명대지위치",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "regstrGbCd": "대장구분코드",
                "regstrGbCdNm": "대장구분코드명",
                "regstrKindCd": "대장종류코드",
                "regstrKindCdNm": "대장종류코드명",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
            }

        elif category == "전유공용면적":
            self.colDict = {
                "area": "면적",
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "crtnDay": "생성일자",
                "dongNm": "동명칭",
                "etcPurps": "기타용도",
                "etcStrct": "기타구조",
                "exposPubuseGbCd": "전유공용구분코드",
                "exposPubuseGbCdNm": "전유공용구분코드명",
                "flrGbCd": "층구분코드",
                "flrGbCdNm": "층구분코드명",
                "flrNo": "층번호",
                "flrNoNm": "층번호명",
                "hoNm": "호명칭",
                "ji": "지",
                "lot": "로트",
                "mainAtchGbCd": "주부속구분코드",
                "mainAtchGbCdNm": "주부속구분코드명",
                "mainPurpsCd": "주용도코드",
                "mainPurpsCdNm": "주용도코드명",
                "mgmBldrgstPk": "관리건축물대장PK",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newPlatPlc": "도로명대지위치",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "regstrGbCd": "대장구분코드",
                "regstrGbCdNm": "대장구분코드명",
                "regstrKindCd": "대장종류코드",
                "regstrKindCdNm": "대장종류코드명",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
                "strctCd": "구조코드",
                "strctCdNm": "구조코드명",
            }

        elif category == "오수정화시설":
            self.colDict = {
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "capaLube": "용량(루베)",
                "capaPsper": "용량(인용)",
                "crtnDay": "생성일자",
                "etcMode": "기타형식",
                "ji": "지",
                "lot": "로트",
                "mgmBldrgstPk": "관리건축물대장PK",
                "modeCd": "형식코드",
                "modeCdNm": "형식코드명",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newPlatPlc": "도로명대지위치",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "regstrGbCd": "대장구분코드",
                "regstrGbCdNm": "대장구분코드명",
                "regstrKindCd": "대장종류코드",
                "regstrKindCdNm": "대장종류코드명",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
                "unitGbCd": "단위구분코드",
                "unitGbCdNm": "단위구분코드명",
            }

        elif category == "주택가격":
            self.colDict = {
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "bylotCnt": "외필지수",
                "crtnDay": "생성일자",
                "hsprc": "주택가격",
                "ji": "지",
                "lot": "로트",
                "mgmBldrgstPk": "관리건축물대장PK",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newPlatPlc": "도로명대지위치",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "regstrGbCd": "대장구분코드",
                "regstrGbCdNm": "대장구분코드명",
                "regstrKindCd": "대장종류코드",
                "regstrKindCdNm": "대장종류코드명",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
            }

        elif category == "전유부":
            self.colDict = {
                "bjdongCd": "법정동코드",
                "bldNm": "건물명",
                "block": "블록",
                "bun": "번",
                "crtnDay": "생성일자",
                "dongNm": "동명칭",
                "flrGbCd": "층구분코드",
                "flrGbCdNm": "층구분코드명",
                "flrNo": "층번호",
                "hoNm": "호명칭",
                "ji": "지",
                "lot": "로트",
                "mgmBldrgstPk": "관리건축물대장PK",
                "naBjdongCd": "새주소법정동코드",
                "naMainBun": "새주소본번",
                "naRoadCd": "새주소도로코드",
                "naSubBun": "새주소부번",
                "naUgrndCd": "새주소지상지하코드",
                "newPlatPlc": "도로명대지위치",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "regstrGbCd": "대장구분코드",
                "regstrGbCdNm": "대장구분코드명",
                "regstrKindCd": "대장종류코드",
                "regstrKindCdNm": "대장종류코드명",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
            }

        elif category == "지역지구구역":
            self.colDict = {
                "bjdongCd": "법정동코드",
                "block": "블록",
                "bun": "번",
                "crtnDay": "생성일자",
                "etcJijigu": "기타지역지구구역",
                "ji": "지",
                "jijiguCd": "지역지구구역코드",
                "jijiguCdNm": "지역지구구역코드명",
                "jijiguGbCd": "지역지구구역구분코드",
                "jijiguGbCdNm": "지역지구구역구분코드명",
                "lot": "로트",
                "mgmBldrgstPk": "관리건축물대장PK",
                "newPlatPlc": "도로명대지위치",
                "platGbCd": "대지구분코드",
                "platPlc": "대지위치",
                "reprYn": "대표여부",
                "rnum": "순번",
                "sigunguCd": "시군구코드",
                "splotNm": "특수지명",
            }

        df = df.rename(columns=self.colDict)

        return df



