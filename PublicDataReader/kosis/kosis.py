"""
KOSIS Open API Python Module
"""

import requests
import pandas as pd


class Kosis:
    """Kosis 공유서비스 클래스"""

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
            return pd.DataFrame(res)
        except:
            print("Dataframe Failed!")
            return None
