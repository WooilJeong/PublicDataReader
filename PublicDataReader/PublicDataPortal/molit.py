"""
국토교통부 Open API
molit(Ministry of Land, Infrastructure and Transport)

- TransactionPrice 클래스: 부동산 실거래가
- BuildingLedger 클래스: 건축물대장
- HousingLicense 클래스: 주택인허가
"""

import pandas as pd
import time
import datetime
import logging
import requests
import xmltodict
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()


class TransactionPrice:
    """
    국토교통부 부동산 실거래가 조회 클래스

    parameters
    ----------
    service_key : str
        국토교통부 Open API 서비스키
    """

    def __init__(self, service_key=None):
        self.service_key = service_key
        self.meta_dict = {
            "아파트": {
                "매매": {
                    "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev",
                    "columns": ['지역코드', '도로명', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일', '거래금액', '도로명건물본번호코드', '도로명건물부번호코드', '도로명시군구코드', '도로명일련번호코드', '도로명지상지하코드', '도로명코드', '법정동본번코드', '법정동부번코드', '법정동시군구코드', '법정동읍면동코드', '법정동지번코드', '일련번호', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent",
                    "columns": ['지역코드', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일', '보증금액', '월세금액', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                },
            },
            "오피스텔": {
                "매매": {
                    "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '건축년도', '층', '전용면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiRent",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '건축년도', '층', '전용면적', '년', '월', '일', '보증금', '월세', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                },
            },
            "단독다가구": {
                "매매": {
                    "url": "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHTrade",
                    "columns": ['지역코드', '법정동', '지번', '주택유형', '건축년도', '대지면적', '연면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent",
                    "columns": ['지역코드', '법정동', '건축년도', '계약면적', '년', '월', '일', '보증금액', '월세금액', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                },
            },
            "연립다세대": {
                "매매": {
                    "url": "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade",
                    "columns": ['지역코드', '법정동', '지번', '연립다세대', '건축년도', '층', '대지권면적', '전용면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent",
                    "columns": ['지역코드', '법정동', '지번', '연립다세대', '건축년도', '층', '전용면적', '년', '월', '일', '보증금액', '월세금액', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                },
            },
            "상업업무용": {
                "매매": {
                    "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '유형', '용도지역', '건물주용도', '건축년도', '층', '대지면적', '건물면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },
            "토지": {
                "매매": {
                    "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcLandTrade",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '용도지역', '지목', '거래면적', '거래금액', '구분', '년', '월', '일', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },
            "분양입주권": {
                "매매": {
                    "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSilvTrade",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '층', '전용면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },
            "공장창고등": {
                "매매": {
                    "url": "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcInduTrade",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '유형', '용도지역', '건물주용도', '건축년도', '층', '대지면적', '건물면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },
        }
        self.integer_columns = ['년', '월', '일', '층', '건축년도',
                                '거래금액', '보증금액', '보증금', '월세금액', '월세', '종전계약보증금', '종전계약월세']
        self.float_columns = ['전용면적', '대지권면적',
                              '대지면적', '연면적', '계약면적', '건물면적', '거래면적']

    def get_data(self,
                 property_type,
                 trade_type,
                 sigungu_code,
                 year_month=None,
                 start_year_month=None,
                 end_year_month=None,
                 verbose=False,
                 **kwargs):
        """
        부동산 실거래가 조회

        Parameters
        ----------
        property_type : str
            부동산 이름 (ex. 아파트, 오피스텔, 단독다가구, 연립다세대, 토지, 분양입주권, 공장창고등)
        trade_type : str
            거래 유형 (ex. 매매, 전월세)
        sigungu_code : str
            시군구코드 (ex. 11110)
        year_month : str, optional
            조회할 연월 (ex. 201901), by default None
        start_year_month : str, optional
            조회할 시작 연월 (ex. 201901), by default None
        end_year_month : str, optional
            조회할 종료 연월 (ex. 201901), by default None
        verbose : bool, optional
            진행 상황 출력 여부, by default False
        **kwargs : dict
            API 요청에 필요한 추가 인자
        """

        try:
            # 부동산 이름과 거래 유형으로 API URL 선택 (ex. 아파트, 매매)
            url = self.meta_dict.get(property_type).get(trade_type).get("url")
            # 부동산 이름과 거래 유형으로 API 컬럼 선택 (ex. 아파트, 매매)
            columns = self.meta_dict.get(property_type).get(
                trade_type).get("columns")
        except AttributeError:
            raise AttributeError("부동산 이름과 거래 유형을 확인해주세요.")

        # 서비스키, 행수, 시군구코드 설정
        params = {
            "serviceKey": requests.utils.unquote(self.service_key),
            "numOfRows": "99999",
            "LAWD_CD": sigungu_code,
        }

        # 선택 파라미터 추가 설정
        params.update(kwargs)

        # 기간으로 조회
        if start_year_month and end_year_month:
            start_date = datetime.datetime.strptime(
                str(start_year_month), "%Y%m")
            start_date = datetime.datetime.strftime(start_date, "%Y-%m")
            end_date = datetime.datetime.strptime(str(end_year_month), "%Y%m")
            end_date += datetime.timedelta(days=31)
            end_date = datetime.datetime.strftime(end_date, "%Y-%m")
            ts = pd.date_range(start=start_date, end=end_date, freq="m")
            date_list = list(ts.strftime("%Y%m"))

            df = pd.DataFrame(columns=columns)
            for year_month in date_list:
                if verbose:
                    print(year_month)
                params['DEAL_YMD'] = year_month
                res = requests.get(url, params=params, verify=False)
                res_json = xmltodict.parse(res.text)
                if res_json['response']['header']['resultCode'] != '00':
                    error_message = res_json['response']['header']['resultMsg']
                    raise Exception(error_message)
                items = res_json['response']['body']['items']
                if not items:
                    continue
                data = items['item']
                if isinstance(data, list):
                    sub = pd.DataFrame(data)
                elif isinstance(data, dict):
                    sub = pd.DataFrame([data])
                df = pd.concat([df, sub], axis=0, ignore_index=True)

        # 기간으로 조회하지 않고 단일 연월로 조회
        else:
            if verbose:
                print(year_month)
            df = pd.DataFrame(columns=columns)
            params['DEAL_YMD'] = year_month
            res = requests.get(url, params=params, verify=False)
            res_json = xmltodict.parse(res.text)
            if res_json['response']['header']['resultCode'] != '00':
                error_message = res_json['response']['header']['resultMsg']
                raise Exception(error_message)
            items = res_json['response']['body']['items']
            if not items:
                return pd.DataFrame(columns=columns)
            data = items['item']
            if isinstance(data, list):
                sub = pd.DataFrame(data)
            elif isinstance(data, dict):
                sub = pd.DataFrame([data])
            df = pd.concat([df, sub], axis=0, ignore_index=True)

        # 컬럼 타입 변환
        try:
            for col in self.integer_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col].apply(
                        lambda x: x.strip().replace(",", "") if x is not None and not pd.isnull(x) else x)).astype("Int64")
            for col in self.float_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col])
        except Exception as e:
            raise Exception(e)

        return df


class BuildingLedger:
    """
    국토교통부 건축물대장 정보 조회 클래스

    parameters
    ----------
    service_key : str
        국토교통부 API 서비스키
    """

    def __init__(self, service_key=None):
        self.service_key = service_key
        self.meta_dict = {
            "기본개요": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrBasisOulnInfo",
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'guyukCd', 'guyukCdNm', 'ji', 'jiguCd', 'jiguCdNm', 'jiyukCd', 'jiyukCdNm', 'lot', 'mgmBldrgstPk', 'mgmUpBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },
            "총괄표제부": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrRecapTitleInfo",
                "columns": ['archArea', 'atchBldArea', 'atchBldCnt', 'bcRat', 'bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'engrEpi', 'engrGrade', 'engrRat', 'etcPurps', 'fmlyCnt', 'gnBldCert', 'gnBldGrade', 'hhldCnt', 'hoCnt', 'indrAutoArea', 'indrAutoUtcnt', 'indrMechArea', 'indrMechUtcnt', 'itgBldCert', 'itgBldGrade', 'ji', 'lot', 'mainBldCnt', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newOldRegstrGbCd', 'newOldRegstrGbCdNm', 'newPlatPlc', 'oudrAutoArea', 'oudrAutoUtcnt', 'oudrMechArea', 'oudrMechUtcnt', 'platArea', 'platGbCd', 'platPlc', 'pmsDay', 'pmsnoGbCd', 'pmsnoGbCdNm', 'pmsnoKikCd', 'pmsnoKikCdNm', 'pmsnoYear', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'stcnsDay', 'totArea', 'totPkngCnt', 'useAprDay', 'vlRat', 'vlRatEstmTotArea']
            },
            "표제부": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo",
                "columns": ['archArea', 'atchBldArea', 'atchBldCnt', 'bcRat', 'bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'dongNm', 'emgenUseElvtCnt', 'engrEpi', 'engrGrade', 'engrRat', 'etcPurps', 'etcRoof', 'etcStrct', 'fmlyCnt', 'gnBldCert', 'gnBldGrade', 'grndFlrCnt', 'heit', 'hhldCnt', 'hoCnt', 'indrAutoArea', 'indrAutoUtcnt', 'indrMechArea', 'indrMechUtcnt', 'itgBldCert', 'itgBldGrade', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'oudrAutoArea', 'oudrAutoUtcnt', 'oudrMechArea', 'oudrMechUtcnt', 'platArea', 'platGbCd', 'platPlc', 'pmsDay', 'pmsnoGbCd', 'pmsnoGbCdNm', 'pmsnoKikCd', 'pmsnoKikCdNm', 'pmsnoYear', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rideUseElvtCnt', 'rnum', 'roofCd', 'roofCdNm', 'rserthqkAblty', 'rserthqkDsgnApplyYn', 'sigunguCd', 'splotNm', 'stcnsDay', 'strctCd', 'strctCdNm', 'totArea', 'totDongTotArea', 'ugrndFlrCnt', 'useAprDay', 'vlRat', 'vlRatEstmTotArea']
            },
            "층별개요": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrFlrOulnInfo",
                "columns": ['area', 'areaExctYn', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'etcPurps', 'etcStrct', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'flrNoNm', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'rnum', 'sigunguCd', 'splotNm', 'strctCd', 'strctCdNm']
            },
            "부속지번": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrAtchJibunInfo",
                "columns": ['atchBjdongCd', 'atchBlock', 'atchBun', 'atchEtcJibunNm', 'atchJi', 'atchLot', 'atchPlatGbCd', 'atchRegstrGbCd', 'atchRegstrGbCdNm', 'atchSigunguCd', 'atchSplotNm', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },
            "전유공용면적": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo",
                "columns": ['area', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'etcPurps', 'etcStrct', 'exposPubuseGbCd', 'exposPubuseGbCdNm', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'flrNoNm', 'hoNm', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'strctCd', 'strctCdNm']
            },
            "오수정화시설": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrWclfInfo",
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'capaLube', 'capaPsper', 'crtnDay', 'etcMode', 'ji', 'lot', 'mgmBldrgstPk', 'modeCd', 'modeCdNm', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'unitGbCd', 'unitGbCdNm']
            },
            "주택가격": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrHsprcInfo",
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'hsprc', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },
            "전유부": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo",
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'hoNm', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },
            "지역지구구역": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrJijiguInfo",
                "columns": ['bjdongCd', 'block', 'bun', 'crtnDay', 'etcJijigu', 'ji', 'jijiguCd', 'jijiguCdNm', 'jijiguGbCd', 'jijiguGbCdNm', 'lot', 'mgmBldrgstPk', 'newPlatPlc', 'platGbCd', 'platPlc', 'reprYn', 'rnum', 'sigunguCd', 'splotNm']
            },
        }

    def get_data(self,
                 ledger_type,
                 sigungu_code,
                 bdong_code,
                 plat_code=None,
                 bun=None,
                 ji=None,
                 translate=True,
                 verbose=False,
                 wait_time=30,
                 **kwargs):
        """
        건축물대장 정보 조회

        Parameters
        ----------
        ledger_type : str
            건축물대장 유형 (ex. 기본개요, 총괄표제부, 표제부, 층별개요, 부속지번, 전유공용면적, 오수정화시설, 주택가격, 전유부, 지역지구구역)
        sigungu_code : str
            시군구 코드 (ex. 11110)
        bdong_code : str
            법정동 코드 (ex. 1111051500)
        plat_code : str
            대지구분 코드 (대지: 0, 산: 1, 블록: 2)
        bun : str
            번 (ex. 200)
        ji : str
            지 (ex. 5)
        translate : bool
            한글 컬럼명으로 변환 여부 (기본값: True)
        verbose : bool
            진행 상황 출력 여부 (기본값: False)
        wait_time : int
            API 요청 간의 대기 시간 (초) (기본값: 30초)
        **kwargs : dict
            API 요청에 필요한 추가 인자
        """
        try:
            # 건축물대장 유형으로 API URL 선택 (ex. 기본개요, 표제부, 총괄표제부 등)
            url = self.meta_dict.get(ledger_type).get("url")
            # 건축물대장 유형으로 API 컬럼 선택 (ex. 기본개요, 표제부, 총괄표제부 등)
            columns = self.meta_dict.get(ledger_type).get("columns")
        except AttributeError:
            raise AttributeError("건축물대장 유형을 확인해주세요.")
        # 서비스키, 행수, 시군구코드, 법정동코드 설정
        params = {
            "serviceKey": requests.utils.unquote(self.service_key),
            "numOfRows": 99999,
            "sigunguCd": sigungu_code,
            "bjdongCd": bdong_code,
        }
        # 본번, 부번 설정 시 Zero Fill 적용
        if bun:
            params.update({"bun": str(bun).zfill(4)})
        if ji:
            params.update({"ji": str(ji).zfill(4)})
        # 플랫코드 설정 시 platGbCd 파라미터 추가
        if plat_code:
            params.update({"platGbCd": plat_code})
        # 선택 파라미터 추가 설정
        params.update(kwargs)
        # 빈 데이터 프레임 생성
        df = pd.DataFrame(columns=columns)
        # API 요청
        res = requests.get(url, params=params, verify=False)
        # 요청 결과 JSON 변환
        res_json = xmltodict.parse(res.text)
        # 응답 키 존재 확인
        if not res_json.get("response"):
            if verbose:
                print(res_json)
            raise Exception("API 요청이 실패했습니다.")
        # 결과코드가 정상이 아닌 경우
        if res_json['response']['header']['resultCode'] != '00':
            error_message = res_json['response']['header']['resultMsg']
            raise Exception(error_message)
        # 요청 행 수
        _numOfRows = res_json['response']['body']['numOfRows']
        # 페이지 번호
        _pageNo = res_json['response']['body']['pageNo']
        # 총 데이터 크기
        _totalCount = res_json['response']['body']['totalCount']
        # 순회해야 하는 페이지 수
        _pageNoCount = int(_totalCount) // int(_numOfRows) + 1
        if verbose:
            print(
                f"""- 요청 행 수: {_numOfRows}\n- 현재 페이지 번호: {_pageNo}\n- 총 행 수: {_totalCount}\n- 총 페이지 수: {_pageNoCount}\n- API 요청 대기시간: {wait_time}초""")
        items = res_json['response']['body']['items']
        if not items:
            if translate:
                return self.translate_columns(pd.DataFrame(columns=columns))
            else:
                return pd.DataFrame(columns=columns)
        data = items['item']
        if isinstance(data, list):
            sub = pd.DataFrame(data)
        elif isinstance(data, dict):
            sub = pd.DataFrame([data])
        df = pd.concat([df, sub], axis=0, ignore_index=True)
        if _pageNoCount > 1:
            if verbose:
                print(f"페이지가 {_pageNoCount}개 있습니다.")
            # 페이지 순회
            for i in range(2, _pageNoCount + 1):
                # 다음 페이지 조회 전 대기
                time.sleep(wait_time)
                if verbose:
                    print(f"page {i} / {_pageNoCount} 요청")
                params['pageNo'] = i
                # API 요청
                res = requests.get(url, params=params, verify=False)
                # 요청 결과 JSON 변환
                res_json = xmltodict.parse(res.text)
                # 응답 키 존재 확인
                if not res_json.get("response"):
                    if verbose:
                        print(res_json)
                    raise Exception("API 요청이 실패했습니다.")
                # 결과코드가 정상이 아닌 경우
                if res_json['response']['header']['resultCode'] != '00':
                    error_message = res_json['response']['header']['resultMsg']
                    raise Exception(error_message)
                items = res_json['response']['body']['items']
                if not items:
                    if translate:
                        return self.translate_columns(pd.DataFrame(columns=columns))
                    else:
                        return pd.DataFrame(columns=columns)
                data = items['item']
                if isinstance(data, list):
                    sub = pd.DataFrame(data)
                elif isinstance(data, dict):
                    sub = pd.DataFrame([data])
                df = pd.concat([df, sub], axis=0, ignore_index=True)
        # 컬럼명 한글로 변경
        if translate:
            df = self.translate_columns(df)
        return df

    def translate_columns(self, df):
        """
        영문 컬럼명을 한글로 변경
        """
        rename_columns = {
            'bjdongCd': '법정동코드',
            'bldNm': '건물명',
            'block': '블록',
            'bun': '번',
            'bylotCnt': '외필지수',
            'crtnDay': '생성일자',
            'guyukCd': '구역코드',
            'guyukCdNm': '구역코드명',
            'ji': '지',
            'jiguCd': '지구코드',
            'jiguCdNm': '지구코드명',
            'jiyukCd': '지역코드',
            'jiyukCdNm': '지역코드명',
            'lot': '로트',
            'mgmBldrgstPk': '관리건축물대장PK',
            'mgmUpBldrgstPk': '관리상위건축물대장PK',
            'naBjdongCd': '새주소법정동코드',
            'naMainBun': '새주소본번',
            'naRoadCd': '새주소도로코드',
            'naSubBun': '새주소부번',
            'naUgrndCd': '새주소지상지하코드',
            'newPlatPlc': '도로명대지위치',
            'platGbCd': '대지구분코드',
            'platPlc': '대지위치',
            'regstrGbCd': '대장구분코드',
            'regstrGbCdNm': '대장구분코드명',
            'regstrKindCd': '대장종류코드',
            'regstrKindCdNm': '대장종류코드명',
            'rnum': '순번',
            'sigunguCd': '시군구코드',
            'splotNm': '특수지명',
            'archArea': '건축면적',
            'atchBldArea': '부속건축물면적',
            'atchBldCnt': '부속건축물수',
            'bcRat': '건폐율',
            'engrEpi': 'EPI점수',
            'engrGrade': '에너지효율등급',
            'engrRat': '에너지절감율',
            'etcPurps': '기타용도',
            'fmlyCnt': '가구수',
            'gnBldCert': '친환경건축물인증점수',
            'gnBldGrade': '친환경건축물등급',
            'hhldCnt': '세대수',
            'hoCnt': '호수',
            'indrAutoArea': '옥내자주식면적',
            'indrAutoUtcnt': '옥내자주식대수',
            'indrMechArea': '옥내기계식면적',
            'indrMechUtcnt': '옥내기계식대수',
            'itgBldCert': '지능형건축물인증점수',
            'itgBldGrade': '지능형건축물등급',
            'mainBldCnt': '주건축물수',
            'mainPurpsCd': '주용도코드',
            'mainPurpsCdNm': '주용도코드명',
            'newOldRegstrGbCd': '신구대장구분코드',
            'newOldRegstrGbCdNm': '신구대장구분코드명',
            'oudrAutoArea': '옥외자주식면적',
            'oudrAutoUtcnt': '옥외자주식대수',
            'oudrMechArea': '옥외기계식면적',
            'oudrMechUtcnt': '옥외기계식대수',
            'platArea': '대지면적',
            'pmsDay': '허가일',
            'pmsnoGbCd': '허가번호구분코드',
            'pmsnoGbCdNm': '허가번호구분코드명',
            'pmsnoKikCd': '허가번호기관코드',
            'pmsnoKikCdNm': '허가번호기관코드명',
            'pmsnoYear': '허가번호년',
            'stcnsDay': '착공일',
            'totArea': '연면적',
            'totPkngCnt': '총주차수',
            'useAprDay': '사용승인일',
            'vlRat': '용적률',
            'vlRatEstmTotArea': '용적률산정연면적',
            'dongNm': '동명칭',
            'emgenUseElvtCnt': '비상용승강기수',
            'etcRoof': '기타지붕',
            'etcStrct': '기타구조',
            'grndFlrCnt': '지상층수',
            'heit': '높이',
            'mainAtchGbCd': '주부속구분코드',
            'mainAtchGbCdNm': '주부속구분코드명',
            'rideUseElvtCnt': '승용승강기수',
            'roofCd': '지붕코드',
            'roofCdNm': '지붕코드명',
            'rserthqkAblty': '내진 능력',
            'rserthqkDsgnApplyYn': '내진 설계 적용 여부',
            'strctCd': '구조코드',
            'strctCdNm': '구조코드명',
            'totDongTotArea': '총동연면적',
            'ugrndFlrCnt': '지하층수',
            'area': '면적',
            'areaExctYn': '면적제외여부',
            'flrGbCd': '층구분코드',
            'flrGbCdNm': '층구분코드명',
            'flrNo': '층번호',
            'flrNoNm': '층번호명',
            'atchBjdongCd': '부속법정동코드',
            'atchBlock': '부속블록',
            'atchBun': '부속번',
            'atchEtcJibunNm': '부속기타지번명',
            'atchJi': '부속지',
            'atchLot': '부속로트',
            'atchPlatGbCd': '부속대지구분코드',
            'atchRegstrGbCd': '부속대장구분코드',
            'atchRegstrGbCdNm': '부속대장구분코드명',
            'atchSigunguCd': '부속시군구코드',
            'atchSplotNm': '부속특수지명',
            'exposPubuseGbCd': '전유공용구분코드',
            'exposPubuseGbCdNm': '전유공용구분코드명',
            'hoNm': '호명칭',
            'capaLube': '용량(루베)',
            'capaPsper': '용량(인용)',
            'etcMode': '기타형식',
            'modeCd': '형식코드',
            'modeCdNm': '형식코드명',
            'unitGbCd': '단위구분코드',
            'unitGbCdNm': '단위구분코드명',
            'hsprc': '주택가격',
            'etcJijigu': '기타지역지구구역',
            'jijiguCd': '지역지구구역코드',
            'jijiguCdNm': '지역지구구역코드명',
            'jijiguGbCd': '지역지구구역구분코드',
            'jijiguGbCdNm': '지역지구구역구분코드명',
            'reprYn': '대표여부',
        }
        return df.rename(columns=rename_columns)


class HousingLicense:
    """
    국토교통부 주택인허가 정보 조회 클래스

    parameters
    ----------
    service_key: str
        국토교통부 API 인증키
    """

    def __init__(self, service_key: str):
        self.service_key = service_key
        self.meta_dict = {
            "기본개요": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpBasisOulnInfo",
                "columns": ['bldNm', 'splotNm', 'block', 'lot', 'purpsCd', 'purpsCdNm', 'strctCd', 'strctCdNm', 'mainBldCnt', 'totArea', 'totHhldCnt', 'demolExtngGbCd', 'demolExtngGbCdNm', 'demolStrtDay', 'demolEndDay', 'demolExtngDay', 'apprvDay', 'stcnsSchedDay', 'stcnsDay', 'useInsptDay', 'useInsptSchedDay', 'crtnDay', 'rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHsrgstPk'],
            },
            "동별개요": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpDongOulnInfo",
                "columns": ['mainPurpsCdNm', 'hhldCntPeplRent', 'hhldCntPubRent_5', 'hhldCntPubRent_10', 'hhldCntPubRentEtc', 'hhldCntPubRentTot', 'hhldCntPubLotou', 'hhldCntEmplRent', 'hhldCntLaborWlfar', 'hhldCntCvlRent', 'hhldCntCvlLotou', 'strctCd', 'strctCdNm', 'roofCd', 'roofCdNm', 'archArea', 'totArea', 'ugrndArea', 'vlRatEstmTotArea', 'ugrndFlrCnt', 'grndFlrCnt', 'heit', 'rideUseElvtCnt', 'emgenUseElvtCnt', 'flrhFrom', 'ceilHeit', 'stairValidWidth', 'hwayWidth', 'ouwlThick', 'adjHhldWallThick', 'crtnDay', 'rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmDongOulnPk', 'mgmHsrgstPk', 'bldNm', 'splotNm', 'block', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'dongNm', 'mainPurpsCd'],
            },
            "층별개요": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpFlrOulnInfo",
                "columns": ['mgmFlrOulnPk', 'mgmDongOulnPk', 'bldNm', 'splotNm', 'block', 'lot', 'dongNm', 'flrNo', 'flrGbCd', 'flrGbCdNm', 'flrArea', 'purpsCd', 'purpsCdNm', 'crtnDay', 'rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji'],
            },
            "호별개요": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpHoOulnInfo",
                "columns": ['rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHoDetlPk', 'mgmDongOulnPk', 'bldNm', 'splotNm', 'block', 'lot', 'dongNm', 'flrNo', 'flrGbCd', 'flrGbCdNm', 'hoNo', 'hoNm', 'pngtypGbNm', 'changGbCd', 'changGbCdNm', 'crtnDay'],
            },
            "부대시설": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpSbsdFcInfo",
                "columns": ['platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHsrgstPk', 'bldNm', 'splotNm', 'block', 'lot', 'sbsdfcKindCd', 'sbsdfcKindCdNm', 'etcFcKind', 'instalCurst', 'cmplxinCurst', 'cmplxbyndCurst', 'changbefInstalCurst', 'changbefCmplxinCurst', 'changbefCmplxbyndCurst', 'befSbsdKindCd', 'befSbsdKindCdNm', 'befEtcFcKind', 'crtnDay', 'rnum'],
            },
            "오수정화시설": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpWclfInfo",
                "columns": ['wclfModeCd', 'wclfModeCdNm', 'etcWclf', 'capaPsper', 'capaLube', 'dongRelGb', 'dongRelGbNm', 'crtnDay', 'rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHsrgstPk', 'hjdongCd', 'splotNm', 'block', 'lot', 'reprYn'],
            },
            "주차장": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpPklotInfo",
                "columns": ['rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHsrgstPk', 'splotNm', 'block', 'lot', 'indrAutoUtcnt', 'indrAutoArea', 'oudrAutoUtcnt', 'oudrAutoArea', 'indrMechUtcnt', 'indrMechArea', 'oudrMechUtcnt', 'oudrMechArea', 'neigAutoUtcnt', 'neigAutoArea', 'neigMechUtcnt', 'neigMechArea', 'exmptUtcnt', 'crtnDay'],
            },
            "부설주차장": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpAtchPklotInfo",
                "columns": ['platGbCd', 'bun', 'ji', 'mgmHsrgstPk', 'hjdongCd', 'splotNm', 'block', 'lot', 'jimokCd', 'jimokCdNm', 'relJibunNm', 'crtnDay', 'rnum', 'platPlc', 'sigunguCd', 'bjdongCd'],
            },
            "전유공용면적": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpExposPubuseAreaInfo",
                "columns": ['rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmExposPubusePk', 'mgmTypeOulnPk', 'exposPubuseGbCd', 'exposPubuseGbCdNm', 'mainAtchGbCd', 'mainAtchGbCdNm', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'flrNoNm', 'strctCd', 'strctCdNm', 'etcStrct', 'purpsCd', 'purpsCdNm', 'etcPurps', 'area', 'crtnDay'],
            },
            "행위호전유공용면적": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpHoExposPubuseAreaInfo",
                "columns": ['rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmActHoExposPubusePk', 'mgmHoDetlPk', 'splotNm', 'block', 'lot', 'pngtypGbNm', 'exposPubuseGbCd', 'exposPubuseGbCdNm', 'mainAtchGbCd', 'mainAtchGbCdNm', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'strctCd', 'strctCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'etcPurps', 'area', 'crtnDay'],
            },
            "행위개요": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpActOulnInfo",
                "columns": ['splotNm', 'block', 'lot', 'actGb', 'actGbCd', 'actGbCdNm', 'cmplxNm', 'bldYn', 'fcKind', 'archArea', 'totArea', 'btmArea', 'mainPurpsCd', 'mainPurpsCdNm', 'etcPurps', 'constArea', 'ugrndFlrCnt', 'grndFlrCnt', 'totWkp', 'stcnsSchedDay', 'useInsptSchedDay', 'hhldCnt', 'cmplxFlrCntDongCnt', 'regstrGbCd', 'regstrGbCdNm', 'actBefPurpsCd', 'actBefPurpsCdNm', 'actBefArea', 'actAftPurpsCd', 'actAftPurpsCdNm', 'actAftArea', 'fcNm', 'actBefEtcPurps', 'actAftEtcPurps', 'crtnDay', 'rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHsrgstPk'],
            },
            "관리공동형별개요": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpMgmCoopTpOulnInfo",
                "columns": ['mgmSigunguCd', 'crtnDay', 'platGbCd', 'bun', 'ji', 'mgmCoophsrgstPk', 'splotNm', 'block', 'lot', 'typeGb', 'etcType', 'exuseArea', 'cmplxNm', 'bizBodyNm', 'bizApprvDay', 'useInsptDay', 'mainBldCnt', 'maxFlrCnt', 'hhldCnt', 'strctCd', 'strctCdNm', 'elvtRideUse', 'elvtEmgen', 'platArea', 'totArea', 'archArea', 'hwayModeCd', 'hwayModeCdNm', 'wtspCd', 'wtspCdNm', 'mgmMthdCd', 'mgmMthdCdNm', 'sfgvMgmStrtDay', 'heatMthdCd', 'heatMthdCdNm', 'useFuel', 'hsStyleGbCd', 'hsStyleGbCdNm', 'hsTypeGbCd', 'hsTypeGbCdNm', 'rnum', 'platPlc', 'sigunguCd', 'bjdongCd'],
            },
            "관리공동부대복리시설": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpMgmCoopSbsdWlfarFcInfo",
                "columns": ['rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmCoophsrgstPk', 'splotNm', 'block', 'lot', 'grndPklotUtcnt', 'ugrndPklotUtcnt', 'totPklotUtcnt', 'pkngCctvCnt', 'reprMtrmArea', 'mgmOffcArea', 'plgndCctvCnt', 'wttnkCapa', 'lndscArea', 'guardrmCnt', 'hsoldArea', 'lifeConvFcArea', 'nturFcArea', 'jmExcsFcCnt', 'kgtFlrCnt', 'kgtLotArea', 'kgtPurps', 'mediFcArea', 'plgndCnt', 'crtnDay'],
            },
            "지역지구구역": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpJijiguInfo",
                "columns": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHsrgstPk', 'splotNm', 'block', 'lot', 'jijiguGbCd', 'jijiguGbCdNm', 'jijiguCd', 'jijiguCdNm', 'reprYn', 'jijiguNm', 'dongRelGb', 'dongRelGbNm', 'crtnDay', 'rnum', 'platPlc'],
            },
            "복리분양시설": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpWlfarLotouFcInfo",
                "columns": ['changbefPurpsCd', 'changbefPurpsCdNm', 'changbefEtcPurps', 'changbefArea', 'changbefCnt', 'changbefEtcCurst', 'befWlfarFcKindCd', 'befWlfarFcKindCdNm', 'befEtcFc', 'crtnDay', 'rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHsrgstPk', 'bldNm', 'splotNm', 'block', 'lot', 'wlfarLotouFcKindCd', 'wlfarLotouFcKindCdNm', 'etcFc', 'purpsCd', 'purpsCdNm', 'etcPurps', 'area', 'openCnt'],
            },
            "대지위치": {
                "url": "http://apis.data.go.kr/1611000/HsPmsService/getHpPlatPlcInfo",
                "columns": ['rnum', 'platPlc', 'sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'mgmHsrgstPk', 'reprYn', 'hjdongCd', 'splotNm', 'block', 'lot', 'jimokCd', 'jimokCdNm', 'relJibunNm', 'platArea', 'minPlatWidth', 'maxPlatWidth', 'dongRelGb', 'dongRelGbNm', 'crtnDay'],
            },
        }

    def get_data(self,
                 service_type,
                 sigungu_code,
                 bdong_code,
                 plat_code=None,
                 bun=None,
                 ji=None,
                 translate=True,
                 verbose=False,
                 wait_time=30,
                 **kwargs):
        """
        주택인허가 정보 조회

        Parameters
        ----------
        service_type : str
            서비스 유형 (ex. 기본개요, 동별개요, 층별개요, 호별개요, 부대시설, 오수정화시설, 주차장, 부설주차장, 전유공용면적, 행위호전유공용면적, 행위개요, 관리공동형별개요, 관리공동부대복리시설, 지역지구구역, 복리분양시설, 대지위치)
        sigungu_code : str
            시군구 코드 (ex. 11110)
        bdong_code : str
            법정동 코드 (ex. 1111051500)
        plat_code : str
            대지구분 코드 (대지: 0, 산: 1, 블록: 2)
        bun : str
            번 (ex. 200)
        ji : str
            지 (ex. 5)
        translate : bool
            한글 컬럼명으로 변환 여부 (기본값: True)
        verbose : bool
            진행 상황 출력 여부 (기본값: False)
        wait_time : int
            API 요청 간의 대기 시간 (초) (기본값: 30초)
        **kwargs : dict
            API 요청에 필요한 추가 인자
        """
        try:
            # 주택인허가 유형으로 API URL 선택 (ex. 기본개요, 표제부, 총괄표제부 등)
            url = self.meta_dict.get(service_type).get("url")
            # 주택인허가 유형으로 API 컬럼 선택 (ex. 기본개요, 표제부, 총괄표제부 등)
            columns = self.meta_dict.get(service_type).get("columns")
        except AttributeError:
            raise AttributeError("주택인허가 서비스 유형을 확인해주세요.")
        # 서비스키, 행수, 시군구코드, 법정동코드 설정
        params = {
            "serviceKey": requests.utils.unquote(self.service_key),
            "numOfRows": 99999,
            "sigunguCd": sigungu_code,
            "bjdongCd": bdong_code,
        }
        # 본번, 부번 설정 시 Zero Fill 적용
        if bun:
            params.update({"bun": str(bun).zfill(4)})
        if ji:
            params.update({"ji": str(ji).zfill(4)})
        # 플랫코드 설정 시 platGbCd 파라미터 추가
        if plat_code:
            params.update({"platGbCd": plat_code})
        # 선택 파라미터 추가 설정
        params.update(kwargs)
        # 빈 데이터 프레임 생성
        df = pd.DataFrame(columns=columns)
        # API 요청
        res = requests.get(url, params=params, verify=False)
        # 요청 결과 JSON 변환
        res_json = xmltodict.parse(res.text)
        # 응답 키 존재 확인
        if not res_json.get("response"):
            if verbose:
                print(res_json)
            raise Exception("API 요청이 실패했습니다.")
        # 결과코드가 정상이 아닌 경우
        if res_json['response']['header']['resultCode'] != '00':
            error_message = res_json['response']['header']['resultMsg']
            raise Exception(error_message)
        # 요청 행 수
        _numOfRows = res_json['response']['body']['numOfRows']
        # 페이지 번호
        _pageNo = res_json['response']['body']['pageNo']
        # 총 데이터 크기
        _totalCount = res_json['response']['body']['totalCount']
        # 순회해야 하는 페이지 수
        _pageNoCount = int(_totalCount) // int(_numOfRows) + 1
        if verbose:
            print(
                f"""- 요청 행 수: {_numOfRows}\n- 현재 페이지 번호: {_pageNo}\n- 총 행 수: {_totalCount}\n- 총 페이지 수: {_pageNoCount}\n- API 요청 대기시간: {wait_time}초""")
        items = res_json['response']['body']['items']
        if not items:
            if translate:
                return self.translate_columns(pd.DataFrame(columns=columns))
            else:
                return pd.DataFrame(columns=columns)
        data = items['item']
        if isinstance(data, list):
            sub = pd.DataFrame(data)
        elif isinstance(data, dict):
            sub = pd.DataFrame([data])
        df = pd.concat([df, sub], axis=0, ignore_index=True)
        if _pageNoCount > 1:
            if verbose:
                print(f"페이지가 {_pageNoCount}개 있습니다.")
            # 페이지 순회
            for i in range(2, _pageNoCount + 1):
                # 다음 페이지 조회 전 대기
                time.sleep(wait_time)
                if verbose:
                    print(f"page {i} / {_pageNoCount} 요청")
                params['pageNo'] = i
                # API 요청
                res = requests.get(url, params=params, verify=False)
                # 요청 결과 JSON 변환
                res_json = xmltodict.parse(res.text)
                # 응답 키 존재 확인
                if not res_json.get("response"):
                    if verbose:
                        print(res_json)
                    raise Exception("API 요청이 실패했습니다.")
                # 결과코드가 정상이 아닌 경우
                if res_json['response']['header']['resultCode'] != '00':
                    error_message = res_json['response']['header']['resultMsg']
                    raise Exception(error_message)
                items = res_json['response']['body']['items']
                if not items:
                    if translate:
                        return self.translate_columns(pd.DataFrame(columns=columns))
                    else:
                        return pd.DataFrame(columns=columns)
                data = items['item']
                if isinstance(data, list):
                    sub = pd.DataFrame(data)
                elif isinstance(data, dict):
                    sub = pd.DataFrame([data])
                df = pd.concat([df, sub], axis=0, ignore_index=True)
        # 컬럼명 한글로 변경
        if translate:
            df = self.translate_columns(df)
        return df

    def translate_columns(self, df):
        """
        영문 컬럼명을 한글로 변경
        """
        rename_columns = {
            'bldNm': '건물명',
            'splotNm': '특수지명',
            'block': '블록',
            'lot': '로트',
            'purpsCd': '용도코드',
            'purpsCdNm': '용도코드명',
            'strctCd': '구조코드',
            'strctCdNm': '구조코드명',
            'mainBldCnt': '주건축물수',
            'totArea': '연면적(㎡)',
            'totHhldCnt': '총세대수(세대)',
            'demolExtngGbCd': '철거멸실구분코드',
            'demolExtngGbCdNm': '철거멸실구분코드명',
            'demolStrtDay': '철거시작일',
            'demolEndDay': '철거종료일',
            'demolExtngDay': '철거멸실일',
            'apprvDay': '건축허가일',
            'stcnsSchedDay': '착공예정일',
            'stcnsDay': '착공일',
            'useInsptDay': '사용검사일',
            'useInsptSchedDay': '사용검사예정일',
            'crtnDay': '생성일자',
            'rnum': '순번',
            'platPlc': '대지위치',
            'sigunguCd': '시군구코드',
            'bjdongCd': '법정동코드',
            'platGbCd': '대지구분코드',
            'bun': '번',
            'ji': '지',
            'mgmHsrgstPk': '관리주택대장PK',
            'mainPurpsCdNm': '주용도코드명',
            'hhldCntPeplRent': '세대수국민임대(세대)',
            'hhldCntPubRent_5': '세대수공공임대5(세대)',
            'hhldCntPubRent_10': '세대수공공임대10(세대)',
            'hhldCntPubRentEtc': '세대수공공임대기타(세대)',
            'hhldCntPubRentTot': '세대수공공임대계(세대)',
            'hhldCntPubLotou': '세대수공공분양(세대)',
            'hhldCntEmplRent': '세대수사원임대(세대)',
            'hhldCntLaborWlfar': '세대수근로복지(세대)',
            'hhldCntCvlRent': '세대수민간임대(세대)',
            'hhldCntCvlLotou': '세대수민간분양(세대)',
            'roofCd': '지붕코드',
            'roofCdNm': '지붕코드명',
            'archArea': '건축면적(㎡)',
            'ugrndArea': '지하면적(㎡)',
            'vlRatEstmTotArea': '용적률산정연면적(㎡)',
            'ugrndFlrCnt': '지하층수',
            'grndFlrCnt': '지상층수',
            'heit': '높이(m)',
            'rideUseElvtCnt': '승용승강기수',
            'emgenUseElvtCnt': '비상용승강기수',
            'flrhFrom': '층고FROM',
            'ceilHeit': '반자높이(m)',
            'stairValidWidth': '계단유효폭',
            'hwayWidth': '복도너비',
            'ouwlThick': '외벽두께',
            'adjHhldWallThick': '인접세대벽두께',
            'mgmDongOulnPk': '관리동별개요PK',
            'mainAtchGbCd': '주부속구분코드',
            'mainAtchGbCdNm': '주부속구분코드명',
            'dongNm': '동명칭',
            'mainPurpsCd': '주용도코드',
            'mgmFlrOulnPk': '관리층별개요PK',
            'flrNo': '층번호',
            'flrGbCd': '층구분코드',
            'flrGbCdNm': '층구분코드명',
            'flrArea': '층면적(㎡)',
            'mgmHoDetlPk': '관리호별명세PK',
            'hoNo': '호번호',
            'hoNm': '호명칭',
            'pngtypGbNm': '평형구분명',
            'changGbCd': '변경구분코드',
            'changGbCdNm': '변경구분코드명',
            'sbsdfcKindCd': '부대시설종류코드',
            'sbsdfcKindCdNm': '부대시설종류코드명',
            'etcFcKind': '기타시설종류',
            'instalCurst': '설치현황',
            'cmplxinCurst': '단지내현황',
            'cmplxbyndCurst': '단지외현황',
            'changbefInstalCurst': '변경전설치현황',
            'changbefCmplxinCurst': '변경전단지내현황',
            'changbefCmplxbyndCurst': '변경전단지외현황',
            'befSbsdKindCd': '전부대종류코드',
            'befSbsdKindCdNm': '전부대종류코드명',
            'befEtcFcKind': '전기타시설종류',
            'wclfModeCd': '오수정화시설형식코드',
            'wclfModeCdNm': '오수정화시설형식코드명',
            'etcWclf': '기타오수정화시설',
            'capaPsper': '용량(인용)',
            'capaLube': '용량(루베)',
            'dongRelGb': '동별관계구분',
            'dongRelGbNm': '동별관계구분명',
            'hjdongCd': '행정동코드',
            'reprYn': '대표여부',
            'indrAutoUtcnt': '옥내자주식대수(대)',
            'indrAutoArea': '옥내자주식면적(㎡)',
            'oudrAutoUtcnt': '옥외자주식대수(대)',
            'oudrAutoArea': '옥외자주식면적(㎡)',
            'indrMechUtcnt': '옥내기계식대수(대)',
            'indrMechArea': '옥내기계식면적(㎡)',
            'oudrMechUtcnt': '옥외기계식대수(대)',
            'oudrMechArea': '옥외기계식면적(㎡)',
            'neigAutoUtcnt': '인근자주식대수(대)',
            'neigAutoArea': '인근자주식면적(㎡)',
            'neigMechUtcnt': '인근기계식대수(대)',
            'neigMechArea': '인근기계식면적(㎡)',
            'exmptUtcnt': '면제대수(대)',
            'jimokCd': '지목코드',
            'jimokCdNm': '지목코드명',
            'relJibunNm': '관련지번명',
            'mgmExposPubusePk': '관리전유공용PK',
            'mgmTypeOulnPk': '관리형별개요PK',
            'exposPubuseGbCd': '전유공용구분코드',
            'exposPubuseGbCdNm': '전유공용구분코드명',
            'flrNoNm': '층번호명',
            'etcStrct': '기타구조',
            'etcPurps': '기타용도',
            'area': '면적(㎡)',
            'mgmActHoExposPubusePk': '관리행위호전유공용PK',
            'actGb': '행위구분',
            'actGbCd': '행위구분코드',
            'actGbCdNm': '행위구분코드명',
            'cmplxNm': '단지명',
            'bldYn': '건축물여부',
            'fcKind': '시설종류',
            'btmArea': '바닥면적(㎡)',
            'constArea': '공사면적(㎡)',
            'totWkp': '총사업비',
            'hhldCnt': '세대수(세대)',
            'cmplxFlrCntDongCnt': '단지층수동수',
            'regstrGbCd': '대장구분코드',
            'regstrGbCdNm': '대장구분코드명',
            'actBefPurpsCd': '행위전용도코드',
            'actBefPurpsCdNm': '행위전용도코드명',
            'actBefArea': '행위전면적(㎡)',
            'actAftPurpsCd': '행위후용도코드',
            'actAftPurpsCdNm': '행위후용도코드명',
            'actAftArea': '행위후면적(㎡)',
            'fcNm': '시설명',
            'actBefEtcPurps': '행위이전기타용도',
            'actAftEtcPurps': '행위이후기타용도',
            'mgmSigunguCd': '관리시군구코드',
            'mgmCoophsrgstPk': '관리공동주택대장PK',
            'typeGb': '형별구분',
            'etcType': '기타형별',
            'exuseArea': '전용면적(㎡)',
            'bizBodyNm': '사업주체명',
            'bizApprvDay': '사업승인일',
            'maxFlrCnt': '최고층수',
            'elvtRideUse': '승강기승용',
            'elvtEmgen': '승강기비상',
            'platArea': '대지면적(㎡)',
            'hwayModeCd': '복도형식코드',
            'hwayModeCdNm': '복도형식코드명',
            'wtspCd': '수도코드',
            'wtspCdNm': '수도코드명',
            'mgmMthdCd': '관리방식코드',
            'mgmMthdCdNm': '관리방식코드명',
            'sfgvMgmStrtDay': '자치관리개시일',
            'heatMthdCd': '난방방식코드',
            'heatMthdCdNm': '난방방식코드명',
            'useFuel': '사용연료',
            'hsStyleGbCd': '주택유형구분코드',
            'hsStyleGbCdNm': '주택유형구분코드명',
            'hsTypeGbCd': '주택형별구분코드',
            'hsTypeGbCdNm': '주택형별구분코드명',
            'grndPklotUtcnt': '지상주차장대수(대)',
            'ugrndPklotUtcnt': '지하주차장대수(대)',
            'totPklotUtcnt': '총주차장대수(대)',
            'pkngCctvCnt': '주차CCTV수',
            'reprMtrmArea': '대표회의실면적(㎡)',
            'mgmOffcArea': '관리소면적(㎡)',
            'plgndCctvCnt': '놀이터CCTV수',
            'wttnkCapa': '저수조용량',
            'lndscArea': '조경면적(㎡)',
            'guardrmCnt': '경비실개소',
            'hsoldArea': '노인정면적(㎡)',
            'lifeConvFcArea': '생활편익시설면적(㎡)',
            'nturFcArea': '보육시설면적(㎡)',
            'jmExcsFcCnt': '주민운동시설개소',
            'kgtFlrCnt': '유치원층수',
            'kgtLotArea': '유치원부지면적(㎡)',
            'kgtPurps': '유치원용도',
            'mediFcArea': '의료시설면적(㎡)',
            'plgndCnt': '놀이터개소',
            'jijiguGbCd': '지역지구구역구분코드',
            'jijiguGbCdNm': '지역지구구역구분코드명',
            'jijiguCd': '지역지구구역코드',
            'jijiguCdNm': '지역지구구역코드명',
            'jijiguNm': '지역지구구역명',
            'changbefPurpsCd': '변경전용도코드',
            'changbefPurpsCdNm': '변경전용도코드명',
            'changbefEtcPurps': '변경전기타용도',
            'changbefArea': '변경전면적(㎡)',
            'changbefCnt': '변경전개소',
            'changbefEtcCurst': '변경전기타현황',
            'befWlfarFcKindCd': '전복리시설종류코드',
            'befWlfarFcKindCdNm': '전복리시설종류코드명',
            'befEtcFc': '전기타시설',
            'wlfarLotouFcKindCd': '복리분양시설종류코드',
            'wlfarLotouFcKindCdNm': '복리분양시설종류코드명',
            'etcFc': '기타시설',
            'openCnt': '개소',
            'minPlatWidth': '최저대지폭',
            'maxPlatWidth': '최고대지폭'
        }
        return df.rename(columns=rename_columns)

class LandForestLedger:
    """
    국토교통부 토지임야 정보 조회 클래스

    parameters
    ----------
    service_key: str
        국토교통부 API 인증키
    """

    def __init__(self, service_key):

        self.service_key = service_key
        self.url = "http://apis.data.go.kr/1611000/nsdi/eios/LadfrlService/ladfrlList.xml"
        self.columns = ["pnu", "ldCodeNm", "ldCode", "mnnmSlno", "regstrSeCode", "regstrSeCodeNm", "lndcgrCode", "lndcgrCodeNm", "lndpclAr", "posesnSeCode", "posesnSeCodeNm", "cnrsPsnCo", "ladFrtlSc", "ladFrtlScNm", "lastUpdtDt",]

    def get_data(self, 
                 pnu_code, 
                 translate=True,
                 verbose=False,
                 wait_time=30,
                 **kwargs):
        """
        토지임야 정보 조회

        parameters
        ----------
        pnu_code: str
            각 필지를 서로 구별하기 위하여 필지마다 붙이는 고유한 번호
        kwargs: dict
            API 요청에 필요한 추가 인자
        """
        # 서비스키, 행수, PNU코드 설정
        params = {
            "serviceKey": requests.utils.unquote(self.service_key),
            "numOfRows": 100,
            "pnu": pnu_code,
        }
        # 선택 파라미터 추가 설정
        params.update(kwargs)
        # 빈 데이터 프레임 생성
        df = pd.DataFrame(columns=self.columns)
        # API 요청
        res = requests.get(self.url, params=params, verify=False)
        # 요청 결과 JSON 변환
        res_json = xmltodict.parse(res.text)

        # 요청 행 수
        _numOfRows = res_json['fields']['numOfRows']
        # 페이지 번호
        _pageNo = res_json['fields']['pageNo']
        # 총 데이터 크기
        _totalCount = res_json['fields']['totalCount']
        # 순회해야 하는 페이지 수
        _pageNoCount = int(_totalCount) // int(_numOfRows) + 1
        if verbose:
            print(
                f"""- 요청 행 수: {_numOfRows}\n- 현재 페이지 번호: {_pageNo}\n- 총 행 수: {_totalCount}\n- 총 페이지 수: {_pageNoCount}\n- API 요청 대기시간: {wait_time}초""")
        data = res_json['fields']['ladfrlVOList']
        if not data:
            if translate:
                return self.translate_columns(pd.DataFrame(columns=columns))
            else:
                return pd.DataFrame(columns=columns)
        if isinstance(data, list):
            sub = pd.DataFrame(data)
        elif isinstance(data, dict):
            sub = pd.DataFrame([data])
        df = pd.concat([df, sub], axis=0, ignore_index=True)
        if _pageNoCount > 1:
            if verbose:
                print(f"페이지가 {_pageNoCount}개 있습니다.")
            # 페이지 순회
            for i in range(2, _pageNoCount + 1):
                # 다음 페이지 조회 전 대기
                time.sleep(wait_time)
                if verbose:
                    print(f"page {i} / {_pageNoCount} 요청")
                params['pageNo'] = i
                # API 요청
                res = requests.get(url, params=params, verify=False)
                # 요청 결과 JSON 변환
                res_json = xmltodict.parse(res.text)
                data = res_json['fields']['ladfrlVOList']
                if not data:
                    if translate:
                        return self.translate_columns(pd.DataFrame(columns=columns))
                    else:
                        return pd.DataFrame(columns=columns)
                if isinstance(data, list):
                    sub = pd.DataFrame(data)
                elif isinstance(data, dict):
                    sub = pd.DataFrame([data])
                df = pd.concat([df, sub], axis=0, ignore_index=True)
        # 컬럼명 한글로 변경
        if translate:
            df = self.translate_columns(df)
        return df

    def translate_columns(self, df):
        """
        영문 컬럼명을 한글로 변경
        """
        rename_columns = {
            'pnu': '고유번호',
            'ldCodeNm': '법정동명',
            'ldCode': '법정동코드',
            'mnnmSlno': '지번',
            'regstrSeCode': '대장구분코드',
            'regstrSeCodeNm': '대장구분명',
            'lndcgrCode': '지목코드',
            'lndcgrCodeNm': '지목명',
            'lndpclAr': '면적(㎡)',
            'posesnSeCode': '소유구분코드',
            'posesnSeCodeNm': '소유구분명',
            'cnrsPsnCo': '소유(공유)인수(명)',
            'ladFrtlSc': '축척구분코드',
            'ladFrtlScNm': '축척구분명',
            'lastUpdtDt': '데이터기준일자',
        }
        return df.rename(columns=rename_columns)


# (Deprecated Class)


class Transaction:
    """
    (Deprecated) 부동산 실거래가 조회 클래스

    공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.

    parameters
    ----------
        serviceKey: 서비스 인증키 문자열
        debug: True이면 모든 로깅 메시지 출력, False이면 에러 로깅 메시지만 출력
    """

    def __init__(self, serviceKey=None, debug=False):
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

        # 메타정보 매핑
        self.metaDict = {
            "아파트": {
                "매매": {
                    "url": f"http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '도로명', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일', '거래금액', '도로명건물본번호코드', '도로명건물부번호코드', '도로명시군구코드', '도로명일련번호코드', '도로명지상지하코드', '도로명코드', '법정동본번코드', '법정동부번코드', '법정동시군구코드', '법정동읍면동코드', '법정동지번코드', '일련번호', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": f"http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일', '보증금액', '월세금액', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                }
            },

            "오피스텔": {
                "매매": {
                    "url": f"http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiTrade?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '건축년도', '층', '전용면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": f"http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiRent?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '건축년도', '층', '전용면적', '년', '월', '일', '보증금', '월세', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                }
            },

            "단독다가구": {
                "매매": {
                    "url": f"http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHTrade?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '법정동', '지번', '주택유형', '건축년도', '대지면적', '연면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": f"http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '법정동', '지번', '건축년도', '계약면적', '년', '월', '일', '보증금액', '월세금액', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                }
            },

            "연립다세대": {
                "매매": {
                    "url": f"http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHTrade?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '법정동', '지번', '연립다세대', '건축년도', '층', '대지권면적', '전용면적', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
                "전월세": {
                    "url": f"http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '법정동', '지번', '연립다세대', '건축년도', '층', '전용면적', '년', '월', '일', '보증금액', '월세금액', '계약구분', '계약기간', '갱신요구권사용', '종전계약보증금', '종전계약월세']
                }
            },

            "상업업무용": {
                "매매": {
                    "url": f"http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '유형', '용도지역', '건물주용도', '건축년도', '층', '대지면적', '건물면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },

            "토지": {
                "매매": {
                    "url": f"http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcLandTrade?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '용도지역', '지목', '거래면적', '거래금액', '구분', '년', '월', '일', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },

            "분양입주권": {
                "매매": {
                    "url": f"http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSilvTrade?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '단지', '층', '전용면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                },
            },

            "공장창고등": {
                "매매": {
                    "url": f"http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcInduTrade?serviceKey={self.serviceKey}",
                    "columns": ['지역코드', '시군구', '법정동', '지번', '유형', '용도지역', '건물주용도', '건축년도', '층', '대지면적', '건물면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']
                }
            }
        }

        self.integerCols = ['년', '월', '일', '층', '건축년도',
                            '거래금액', '보증금액', '보증금', '월세금액', '월세', '종전계약보증금', '종전계약월세']
        self.floatCols = ['전용면적', '대지권면적',
                          '대지면적', '연면적', '계약면적', '건물면적', '거래면적']

        # 서비스 정상 작동 여부 확인
        for prod in self.metaDict.keys():
            for trans in self.metaDict[prod].keys():
                # Endpoint
                url = self.metaDict[prod][trans]['url']
                result = requests.get(url, verify=False)
                xmlsoup = BeautifulSoup(result.text, "lxml-xml")
                header = xmlsoup.find('header')
                result_code = header.find('resultCode').text
                result_msg = header.find('resultMsg').text
                if result_code == "00":
                    self.logger.info(
                        f"{prod} {trans} 조회 서비스 정상 - ({result_code}) {result_msg}")
                else:
                    self.logger.error(
                        f"{prod} {trans} 조회 서비스 오류 - ({result_code}) {result_msg}")

    def collect_data(self, prod, trans, sigunguCode, startYearMonth, endYearMonth):
        """
        기간별 조회

        parameters
        ----------
            prod: 상품유형 (ex.아파트, 오피스텔, 단독다가구, 연립다세대, 토지, 상업업무용, 공장창고등)
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
                _info_message = f"{prod} {trans} {yearMonth} 조회 시작"
                self.logger.info(_info_message)
                df_ = self.read_data(prod, trans, sigunguCode, yearMonth)
                df = pd.concat([df, df_], axis=0).reset_index(drop=True)
            except:
                _error_message = f"{prod} {trans} {yearMonth} 조회 오류"
                self.logger.error(_error_message)
                return _error_message
        return df

    def read_data(self, prod, trans, sigunguCode, yearMonth):
        """
        월별 조회

        parameters
        ----------
            prod: 상품유형 (ex.아파트, 오피스텔, 단독다가구, 연립다세대, 토지, 상업업무용, 공장창고등)
            trans: 매매, 전월세
            sigunguCode: 시군구코드(5자리)
            yearMonth: 계약년월("YYYYmm")
        """
        # 엔드포인트 및 컬럼 목록 매핑
        try:
            endpoint = self.metaDict[prod][trans]['url']
            columns = self.metaDict[prod][trans]['columns']
        except:
            _error_message = f"{prod} {trans} 참조 오류"
            self.logger.error(_error_message)
            return _error_message

        try:
            # URL
            url = f"""{endpoint}&LAWD_CD={str(sigunguCode)}&DEAL_YMD={str(yearMonth)}&numOfRows=99999"""
            # Open API 호출
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            header = xmlsoup.find("header")
            result_code = header.find("resultCode").text
            result_msg = header.find("resultMsg").text
            items = xmlsoup.findAll("item")

        except:
            _error_message = f"HTTP 요청 혹은 파싱 오류"
            self.logger.error(_error_message)
            return _error_message

        if result_code == "00":
            """
            결과 정상
            """
            # 데이터프레임 생성
            try:
                df = pd.DataFrame(columns=columns)
                for item in items:
                    row = {}
                    for col in columns:
                        try:
                            tag = item.find(col)
                            row[col] = tag.text.strip()
                        except:
                            row[col] = ""
                    df_ = pd.DataFrame([row])[columns]
                    df = pd.concat([df, df_], axis=0).reset_index(drop=True)

                for col in self.integerCols:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col].apply(
                            lambda x: x.strip().replace(",", ""))).astype("Int64")
                for col in self.floatCols:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col])

                return df

            except:
                _error_message = f"전처리 오류"
                self.logger.error(_error_message)
                return _error_message

        else:
            """
            결과 에러
            """
            _error_message = f"({result_code}) {result_msg} OPEN API 오류 - 코드: {result_code}"
            self.logger.error(_error_message)
            return _error_message


class Building:
    """
    (Deprecated) 건축물대장정보 서비스

    공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.

    parameters
    ----------
        serviceKey: 서비스 인증키 문자열
        debug: True이면 모든 로깅 메시지 출력, False이면 에러 로깅 메시지만 출력
    """

    def __init__(self, serviceKey=None, debug=False):
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

        # 메타정보 매핑
        self.metaDict = {

            "기본개요": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrBasisOulnInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'guyukCd', 'guyukCdNm', 'ji', 'jiguCd', 'jiguCdNm', 'jiyukCd', 'jiyukCdNm', 'lot', 'mgmBldrgstPk', 'mgmUpBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },

            "총괄표제부": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrRecapTitleInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['archArea', 'atchBldArea', 'atchBldCnt', 'bcRat', 'bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'engrEpi', 'engrGrade', 'engrRat', 'etcPurps', 'fmlyCnt', 'gnBldCert', 'gnBldGrade', 'hhldCnt', 'hoCnt', 'indrAutoArea', 'indrAutoUtcnt', 'indrMechArea', 'indrMechUtcnt', 'itgBldCert', 'itgBldGrade', 'ji', 'lot', 'mainBldCnt', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newOldRegstrGbCd', 'newOldRegstrGbCdNm', 'newPlatPlc', 'oudrAutoArea', 'oudrAutoUtcnt', 'oudrMechArea', 'oudrMechUtcnt', 'platArea', 'platGbCd', 'platPlc', 'pmsDay', 'pmsnoGbCd', 'pmsnoGbCdNm', 'pmsnoKikCd', 'pmsnoKikCdNm', 'pmsnoYear', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'stcnsDay', 'totArea', 'totPkngCnt', 'useAprDay', 'vlRat', 'vlRatEstmTotArea']
            },

            "표제부": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrTitleInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['archArea', 'atchBldArea', 'atchBldCnt', 'bcRat', 'bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'dongNm', 'emgenUseElvtCnt', 'engrEpi', 'engrGrade', 'engrRat', 'etcPurps', 'etcRoof', 'etcStrct', 'fmlyCnt', 'gnBldCert', 'gnBldGrade', 'grndFlrCnt', 'heit', 'hhldCnt', 'hoCnt', 'indrAutoArea', 'indrAutoUtcnt', 'indrMechArea', 'indrMechUtcnt', 'itgBldCert', 'itgBldGrade', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'oudrAutoArea', 'oudrAutoUtcnt', 'oudrMechArea', 'oudrMechUtcnt', 'platArea', 'platGbCd', 'platPlc', 'pmsDay', 'pmsnoGbCd', 'pmsnoGbCdNm', 'pmsnoKikCd', 'pmsnoKikCdNm', 'pmsnoYear', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rideUseElvtCnt', 'rnum', 'roofCd', 'roofCdNm', 'rserthqkAblty', 'rserthqkDsgnApplyYn', 'sigunguCd', 'splotNm', 'stcnsDay', 'strctCd', 'strctCdNm', 'totArea', 'totDongTotArea', 'ugrndFlrCnt', 'useAprDay', 'vlRat', 'vlRatEstmTotArea']
            },

            "층별개요": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrFlrOulnInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['area', 'areaExctYn', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'etcPurps', 'etcStrct', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'flrNoNm', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'rnum', 'sigunguCd', 'splotNm', 'strctCd', 'strctCdNm']
            },

            "부속지번": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrAtchJibunInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['atchBjdongCd', 'atchBlock', 'atchBun', 'atchEtcJibunNm', 'atchJi', 'atchLot', 'atchPlatGbCd', 'atchRegstrGbCd', 'atchRegstrGbCdNm', 'atchSigunguCd', 'atchSplotNm', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },

            "전유공용면적": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposPubuseAreaInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate', 'dongNm', 'hoNm'],
                "columns": ['area', 'bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'etcPurps', 'etcStrct', 'exposPubuseGbCd', 'exposPubuseGbCdNm', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'flrNoNm', 'hoNm', 'ji', 'lot', 'mainAtchGbCd', 'mainAtchGbCdNm', 'mainPurpsCd', 'mainPurpsCdNm', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'strctCd', 'strctCdNm']
            },

            "오수정화시설": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrWclfInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'capaLube', 'capaPsper', 'crtnDay', 'etcMode', 'ji', 'lot', 'mgmBldrgstPk', 'modeCd', 'modeCdNm', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm', 'unitGbCd', 'unitGbCdNm']
            },

            "주택가격": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrHsprcInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'bylotCnt', 'crtnDay', 'hsprc', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },

            "전유부": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrExposInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'bldNm', 'block', 'bun', 'crtnDay', 'dongNm', 'flrGbCd', 'flrGbCdNm', 'flrNo', 'hoNm', 'ji', 'lot', 'mgmBldrgstPk', 'naBjdongCd', 'naMainBun', 'naRoadCd', 'naSubBun', 'naUgrndCd', 'newPlatPlc', 'platGbCd', 'platPlc', 'regstrGbCd', 'regstrGbCdNm', 'regstrKindCd', 'regstrKindCdNm', 'rnum', 'sigunguCd', 'splotNm']
            },

            "지역지구구역": {
                "url": f"http://apis.data.go.kr/1613000/BldRgstService_v2/getBrJijiguInfo?serviceKey={self.serviceKey}",
                "parameters": ['sigunguCd', 'bjdongCd', 'platGbCd', 'bun', 'ji', 'startDate', 'endDate'],
                "columns": ['bjdongCd', 'block', 'bun', 'crtnDay', 'etcJijigu', 'ji', 'jijiguCd', 'jijiguCdNm', 'jijiguGbCd', 'jijiguGbCdNm', 'lot', 'mgmBldrgstPk', 'newPlatPlc', 'platGbCd', 'platPlc', 'reprYn', 'rnum', 'sigunguCd', 'splotNm']
            },

        }

        for category in self.metaDict.keys():
            # Endpoint
            url = self.metaDict[category]['url']
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            header = xmlsoup.find('header')
            result_code = header.find('resultCode').text
            result_msg = header.find('resultMsg').text
            if result_code == "00":
                self.logger.info(
                    f"{category} 조회 서비스 정상 - ({result_code}) {result_msg}")
            else:
                self.logger.err(
                    f"{category} 조회 서비스 오류 - ({result_code}) {result_msg}")

    def read_data(self, category, **kwargs):
        """
        데이터 조회

        parameters
        ----------
            category: 오퍼레이션 종류 (ex. 기본개요, 총괄표제부, 표제부, 층별개요, 부속지번, 전유공용면적, 오수정화시설, 주택가격, 전유부, 지역지구구역)
        """

        # 엔드포인트, 파라미터 및 컬럼 목록 매핑
        try:
            endpoint = self.metaDict[category]['url']
            parameters = self.metaDict[category]['parameters']
            columns = self.metaDict[category]['columns']
        except:
            _error_message = f"{category} 참조 오류"
            self.logger.error(_error_message)
            return _error_message

        try:
            params = ""
            for key, value in kwargs.items():
                params += f"&{key}={value}"
        except:
            _error_message = f"{category} 파라미터 파싱 오류"
            self.logger.error(_error_message)
            return _error_message

        try:
            # URL
            url = f"""{endpoint}{params}&numOfRows=99999"""

            # Open API 호출
            result = requests.get(url, verify=False)
            xmlsoup = BeautifulSoup(result.text, "lxml-xml")
            header = xmlsoup.find("header")
            result_code = header.find("resultCode").text
            result_msg = header.find("resultMsg").text
            items = xmlsoup.findAll("item")

        except:
            _error_message = f"HTTP 요청 혹은 파싱 오류"
            self.logger.error(_error_message)
            return _error_message

        if result_code == "00":
            """
            결과 정상
            """
            # 데이터프레임 생성
            try:
                df = pd.DataFrame(columns=columns)
                for item in items:
                    row = {}
                    for col in columns:
                        try:
                            tag = item.find(col)
                            row[col] = tag.text.strip()
                        except:
                            row[col] = ""
                    df_ = pd.DataFrame([row])[columns]
                    df = pd.concat([df, df_], axis=0).reset_index(drop=True)
                df = self.ChangeCols(df, category)
                return df

            except:
                _error_message = f"전처리 오류"
                self.logger.error(_error_message)
                return _error_message

        else:
            """
            결과 에러
            """
            _error_message = f"({result_code}) {result_msg}"
            self.logger.error(_error_message)
            return _error_message

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
