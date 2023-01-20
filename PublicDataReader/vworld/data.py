"""
Vworld 데이터 API Python Module
"""
import requests
from ..utils.code import get_vworld_data_api_info_by_dict

requests.packages.urllib3.disable_warnings()


class VworldData:
    """Vworld 데이터 API 클래스

    Vworld에서 발급받은 API 서비스 인증키를 입력받아 초기화합니다.

    Parameters
    ----------
    service_key : str
        Vworld Open API 서비스 인증키
    """

    def __init__(self, service_key=None):
        self.service_key = service_key
        self.url = "http://api.vworld.kr/req/data"

    def get_data(self, service_name, **kwargs):
        """
        API 호출

        Parameters
        ----------
        service_name : str
            API 호출에 필요한 서비스 이름을 입력합니다.

        **kwargs : dict
            API 호출에 필요한 파라미터를 입력합니다.
            API 호출에 필요한 파라미터는 Vworld Open API 문서를 참고하세요.
            https://www.vworld.kr/dev/v4dv_2ddataguide2_s001.do

        Returns
        -------
        dict
            API 호출 결과를 반환합니다.
        """
        params = {
            "key": requests.utils.unquote(self.service_key),
            "service": "data",
            "request": "GetFeature",
            "page": 1,
            "size": 1000,
            "data": get_vworld_data_api_info_by_dict()[service_name]
        }
        params.update(kwargs)
        featureCollection = {"type": "FeatureCollection", "features": []}
        while True:
            try:
                res = requests.get(self.url, params=params, verify=False)
                res_json = res.json()
            except Exception as e:
                print("API 요청이 실패했습니다.")
                print(e)
                return None
            params["page"] = int(params["page"]) + 1
            featureCollection["features"].extend(
                res_json["response"]["result"]["featureCollection"]["features"])
            if res_json['response']['page']['current'] == res_json['response']['page']['total']:
                break
        return featureCollection
