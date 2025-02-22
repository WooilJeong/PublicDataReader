import requests
import pandas as pd

requests.packages.urllib3.disable_warnings()


class Ecos:
    """
    Ecos API 클래스
    """

    def __init__(self, service_key=None):
        self.service_key = service_key
        self.base_url = "http://ecos.bok.or.kr/api"

    def get_statistic_table_list(self, 통계표코드=None, translate=True):
        """
        서비스 통계 목록 API

        Parameters
        ----------
        통계표코드 : str, optional
            통계표코드, by default None

        Output
        ----------
        상위통계표코드(P_STAT_CODE) : str(8)
        통계표코드(STAT_CODE) : str(8)
        통계명(STAT_NAME) : str(200)
        주기(CYCLE) : str(2)
        검색가능여부(SRCH_YN) : str(1)
        출처(ORG_NAME) : str(50)
        """
        if 통계표코드 is None:
            통계표코드 = ""
        params = {
            "서비스명": "StatisticTableList",
            "인증키": self.service_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "99999",
            "통계표코드": 통계표코드,
        }
        query_params = '/'.join(params.values())
        url = f"{self.base_url}/{query_params}"
        res = requests.get(url, verify=False)
        res_json = res.json()
        if res_json.get("RESULT"):
            if res_json.get("RESULT").get("MESSAGE"):
                print(res_json.get("RESULT").get("MESSAGE"))
                return None
        df = pd.DataFrame(res_json['StatisticTableList']['row'])
        if translate:
            df = self.translate(df)
        return df

    def get_statistic_word(self, 용어, translate=True):
        """
        통계용어사전 API

        Parameters
        ----------
        용어 : str
            통계용어 (예시 : 소비자동향지수)

        Output
        ----------
        용어(WORD) : str(100)
        용어설명(CONTENT) : str(4000)
        """
        params = {
            "서비스명": "StatisticWord",
            "인증키": self.service_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "99999",
            "용어": 용어,
        }
        query_params = '/'.join(params.values())
        url = f"{self.base_url}/{query_params}"
        res = requests.get(url, verify=False)
        res_json = res.json()
        if res_json.get("RESULT"):
            if res_json.get("RESULT").get("MESSAGE"):
                print(res_json.get("RESULT").get("MESSAGE"))
                return None
        df = pd.DataFrame(res_json['StatisticWord']['row'])
        if translate:
            df = self.translate(df)
        return df

    def get_statistic_item_list(self, 통계표코드, translate=True):
        """
        통계 세부항목 목록 API

        Parameters
        ----------
        통계표코드 : str
            통계표코드

        Output
        ----------
        통계표코드(STAT_CODE) : str(8)
        통계명(STAT_NAME) : str(200)
        항목그룹코드(GRP_CODE) : str(20)
        항목그룹명(GRP_NAME) : str(60)
        통계항목코드(ITEM_CODE) : str(20)
        통계항목명(ITEM_NAME) : str(200)
        상위통계항목코드(P_ITEM_CODE) : str(8)
        상위통계항목명(P_ITEM_NAME) : str(200)
        주기(CYCLE) : str(2)
        수록시작일자(START_TIME) : str(8)
        수록종료일자(END_TIME) : str(8)
        자료수(DATA_CNT) : str(22)
        단위(UNIT_NAME) : str(200)
        가중치(WEIGHT) : str(22)
        """
        params = {
            "서비스명": "StatisticItemList",
            "인증키": self.service_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "99999",
            "통계표코드": 통계표코드,
        }
        query_params = '/'.join(params.values())
        url = f"{self.base_url}/{query_params}"
        res = requests.get(url, verify=False)
        res_json = res.json()
        if res_json.get("RESULT"):
            if res_json.get("RESULT").get("MESSAGE"):
                print(res_json.get("RESULT").get("MESSAGE"))
                return None
        df = pd.DataFrame(res_json['StatisticItemList']['row'])
        if translate:
            df = self.translate(df)
        return df

    def get_statistic_search(self, 통계표코드, 주기, 검색시작일자, 검색종료일자, 통계항목코드1=None, 통계항목코드2=None, 통계항목코드3=None, 통계항목코드4=None, translate=True):
        """
        통계 조회 조건 설정 API

        Parameters
        ----------
        통계표코드 : str
            통계표코드
        주기 : str
            주기 (년:A, 반년:S, 분기:Q, 월:M, 반월:SM, 일: D)
        검색시작일자 : str
            검색시작일자(주기에 맞는 형식으로 입력: 2015, 2015Q1, 201501, 20150101 등)
        검색종료일자 : str
            검색종료일자(주기에 맞는 형식으로 입력: 2021, 2021Q1, 202101, 20210101 등)
        통계항목코드1 : str, optional
            통계항목코드1, by default None
        통계항목코드2 : str, optional
            통계항목코드2, by default None
        통계항목코드3 : str, optional
            통계항목코드3, by default None
        통계항목코드4 : str, optional
            통계항목코드4, by default None

        Output
        ----------
        통계표코드(STAT_CODE) : str(8)
        통계명(STAT_NAME) : str(200)
        통계항목코드1(ITEM_CODE1) : str(20)
        통계항목명1(ITEM_NAME1) : str(200)
        통계항목코드2(ITEM_CODE2) : str(20)
        통계항목명2(ITEM_NAME2) : str(200)
        통계항목코드3(ITEM_CODE3) : str(20)
        통계항목명3(ITEM_NAME3) : str(200)
        통계항목코드4(ITEM_CODE4) : str(20)
        통계항목명4(ITEM_NAME4) : str(200)
        단위(UNIT_NAME) : str(200)
        가중치(WGT) : str(22)
        시점(TIME) : str(8)
        값(DATA_VALUE) : str(23)
        """
        if 통계항목코드1 is None:
            통계항목코드1 = ""
        if 통계항목코드2 is None:
            통계항목코드2 = ""
        if 통계항목코드3 is None:
            통계항목코드3 = ""
        if 통계항목코드4 is None:
            통계항목코드4 = ""

        params = {
            "서비스명": "StatisticSearch",
            "인증키": self.service_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "99999",
            "통계표코드": 통계표코드,
            "주기": 주기,
            "검색시작일자": 검색시작일자,
            "검색종료일자": 검색종료일자,
            "통계항목코드1": 통계항목코드1,
            "통계항목코드2": 통계항목코드2,
            "통계항목코드3": 통계항목코드3,
            "통계항목코드4": 통계항목코드4,
        }
        query_params = '/'.join(params.values())
        url = f"{self.base_url}/{query_params}"
        res = requests.get(url, verify=False)
        res_json = res.json()
        if res_json.get("RESULT"):
            if res_json.get("RESULT").get("MESSAGE"):
                print(res_json.get("RESULT").get("MESSAGE"))
                return None
        df = pd.DataFrame(res_json['StatisticSearch']['row'])
        if translate:
            df = self.translate(df)
        return df

    def get_key_statistic_list(self, translate=True):
        """
        100대 통계지표

        Output
        ----------
        통계그룹명(CLASS_NAME) : str(400)
        통계명(KEYSTAT_NAME) : str(200)
        값(DATA_VALUE) : str(23)
        시점(CYCLE) : str(13)
        단위(UNIT_NAME) : str(200)
        """
        params = {
            "서비스명": "KeyStatisticList",
            "인증키": self.service_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "100",
        }
        query_params = '/'.join(params.values())
        url = f"{self.base_url}/{query_params}"
        res = requests.get(url, verify=False)
        res_json = res.json()
        if res_json.get("RESULT"):
            if res_json.get("RESULT").get("MESSAGE"):
                print(res_json.get("RESULT").get("MESSAGE"))
                return None
        df = pd.DataFrame(res_json['KeyStatisticList']['row'])
        if translate:
            df = self.translate(df)
        return df

    def get_statistic_meta(self, 데이터명, translate=True):
        """
        통계메타DB API

        Parameters
        ----------
        데이터명 : str
            데이터명 (예시 : 경제심리지수)

        Output
        ----------
        레벨(LVL) : str(2)
        상위통계항목코드(P_CONT_CODE) : str(8)
        통계항목코드(CONT_CODE) : str(8)
        통계항목명(CONT_NAME) : str(200)
        메타데이터(META_DATA) : str(200)
        """
        params = {
            "서비스명": "StatisticMeta",
            "인증키": self.service_key,
            "요청유형": "json",
            "언어구분": "kr",
            "요청시작건수": "1",
            "요청종료건수": "99999",
            "데이터명": 데이터명,
        }
        query_params = '/'.join(params.values())
        url = f"{self.base_url}/{query_params}"
        res = requests.get(url, verify=False)
        res_json = res.json()
        if res_json.get("RESULT"):
            if res_json.get("RESULT").get("MESSAGE"):
                print(res_json.get("RESULT").get("MESSAGE"))
                return None
        df = pd.DataFrame(res_json['StatisticMeta']['row'])
        if translate:
            df = self.translate(df)
        return df

    def translate(self, df):
        """
        한글로 된 컬럼명을 영어로 변환
        """
        translate_dict = {
            'P_STAT_CODE': '상위통계표코드',
            'STAT_CODE': '통계표코드',
            'STAT_NAME': '통계명',
            'CYCLE': '시점',
            'SRCH_YN': '검색가능여부',
            'ORG_NAME': '출처',
            'WORD': '용어',
            'CONTENT': '용어설명',
            'GRP_CODE': '항목그룹코드',
            'GRP_NAME': '항목그룹명',
            'ITEM_CODE': '통계항목코드',
            'ITEM_NAME': '통계항목명',
            'P_ITEM_CODE': '상위통계항목코드',
            'P_ITEM_NAME': '상위통계항목명',
            'START_TIME': '수록시작일자',
            'END_TIME': '수록종료일자',
            'DATA_CNT': '자료수',
            'UNIT_NAME': '단위',
            'WEIGHT': '가중치',
            'ITEM_CODE1': '통계항목코드1',
            'ITEM_NAME1': '통계항목명1',
            'ITEM_CODE2': '통계항목코드2',
            'ITEM_NAME2': '통계항목명2',
            'ITEM_CODE3': '통계항목코드3',
            'ITEM_NAME3': '통계항목명3',
            'ITEM_CODE4': '통계항목코드4',
            'ITEM_NAME4': '통계항목명4',
            'TIME': '시점',
            'DATA_VALUE': '값',
            'CLASS_NAME': '통계그룹명',
            'KEYSTAT_NAME': '통계명',
            'LVL': '레벨',
            'P_CONT_CODE': '상위통계항목코드',
            'CONT_CODE': '통계항목코드',
            'CONT_NAME': '통계항목명',
            'META_DATA': '메타데이터'
        }
        df = df.rename(columns=translate_dict)
        return df
