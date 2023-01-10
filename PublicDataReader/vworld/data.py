"""
Vworld 데이터 API Python Module
"""
import requests
from ..utils.code import get_vworld_data_api_info_by_dict


class VworldData:
    """Vworld 데이터 API 클래스

    Vworld에서 발급받은 API 서비스 인증키를 입력받아 초기화합니다.

    Parameters
    ----------
    apiKey : str
        Vworld Open API 서비스 인증키
    """

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.url = "http://api.vworld.kr/req/data"

    def get_data(self, **kwargs):
        """API 호출

        Parameters
        ----------
        **kwargs : dict
            API 호출에 필요한 파라미터를 입력합니다.
            API 호출에 필요한 파라미터는 Vworld Open API 문서를 참고하세요.
            https://www.vworld.kr/dev/v4dv_2ddataguide2_s001.do

        Returns
        -------
        dict
            API 호출 결과를 반환합니다.
        """
        try:
            kwargs["key"] = self.apiKey
            kwargs["service"] = "data"
            kwargs["request"] = "GetFeature"
            kwargs["page"] = 1
            kwargs["size"] = 1000
            if kwargs.get("serviceName"):
                kwargs["data"] = get_vworld_data_api_info_by_dict()[
                    kwargs["serviceName"]]
        except:
            print("Incorrect Value!")
            return None
        featureCollection = {"type": "FeatureCollection", "features": []}
        try:
            while True:
                res = requests.get(self.url, params=kwargs,
                                   verify=False).json()
                kwargs["page"] = int(kwargs["page"]) + 1
                featureCollection["features"].extend(
                    res["response"]["result"]["featureCollection"]["features"])
                if res['response']['page']['current'] == res['response']['page']['total']:
                    break
        except:
            print("Error!")
            pass
        return featureCollection
