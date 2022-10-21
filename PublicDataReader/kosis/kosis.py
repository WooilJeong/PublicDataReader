"""
KOSIS Open API Python Module
"""

import requests
import pandas as pd


class Kosis:
    """KOSIS 공유서비스 클래스

    KOSIS 공유서비스에서 발급받은 사용자 인증키를 입력받아 초기화합니다.

    Parameters
    ----------
    apiKey : str
        KOSIS 공유서비스에서 발급받은 사용자 인증키
    serviceName : str
        KOSIS 공유서비스 서비스명

    Examples
    --------
    >>> import PublicDataReader as pdr
    >>> # KOSIS 공유서비스 OPEN API 인스턴스 생성
    >>> apiKey = "YOUR_API_KEY"
    >>> serviceName = "KOSIS통합검색" # (예시) KOSIS통합검색, 통계설명, 통계표설명, 통계목록, 통계자료
    >>> kosis = pdr.Kosis(apiKey, serviceName)
    """

    def __init__(self, apiKey, serviceName):
        self.apiKey = apiKey
        url_dict = {
            "KOSIS통합검색": "https://kosis.kr/openapi/statisticsSearch.do?method=getList",
            "통계설명": "https://kosis.kr/openapi/statisticsExplData.do?method=getList",
            "통계표설명": "https://kosis.kr/openapi/statisticsData.do?method=getMeta",
            "통계목록": "https://kosis.kr/openapi/statisticsList.do?method=getList",
            "통계자료": "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList",
        }
        self.url = url_dict.get(serviceName)

    def get_data(self, **kwargs):
        """API 호출

        KOSIS 공유서비스 API를 호출하여 데이터를 반환합니다.

        Parameters
        ----------
        **kwargs : dict
            API 호출에 필요한 파라미터

        Returns
        -------
        DataFrame
            API 호출 결과를 DataFrame 형태로 반환합니다.

        Examples
        --------
        >>> import PublicDataReader as pdr
        >>> # KOSIS 공유서비스 OPEN API 인스턴스 생성
        >>> apiKey = "YOUR_API_KEY"
        >>> serviceName = "KOSIS통합검색"
        >>> kosis = pdr.Kosis(apiKey, serviceName)
        >>> # 파라미터 설정
        >>> orgId = "101"
        >>> tblId = "DT_1B040A3"
        >>> metaItm = "ALL"
        >>> # 데이터 조회
        >>> df = kosis.get_data(orgId=orgId, tblId=tblId, metaItm=metaItm)
        """
        try:
            kwargs["apiKey"] = self.apiKey
            kwargs["format"] = "json"
            kwargs["jsonVD"] = "Y"
            kwargs["jsonMVD"] = "Y"
            if kwargs.get("detailServiceName"):
                type_dict = {
                    "통계표명칭": "TBL",
                    "기관명칭": "ORG",
                    "수록정보": "PRD",
                    "분류항목": "ITM",
                    "주석": "CMMT",
                    "단위": "UNIT",
                    "출처": "SOURCE",
                    "가중치": "WGT",
                    "자료갱신일": "NCD",
                }
                kwargs['type'] = type_dict.get(kwargs.get("detailServiceName"))
                kwargs.pop("detailServiceName")
        except:
            print("Incorrect Value!")
            return None

        try:
            res = requests.get(self.url, params=kwargs).json()
        except:
            print("Request Failed!")
            return None

        try:
            if type(res) == dict:
                if res.get("errMsg"):
                    print(res.get("errMsg"))
                    return None
            else:
                return pd.DataFrame(res)
        except:
            print("Data Frame Failed!")
            return None
