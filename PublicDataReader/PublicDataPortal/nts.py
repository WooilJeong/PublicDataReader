import requests
import pandas as pd

requests.packages.urllib3.disable_warnings()


class Nts:
    """
    NTS Open API 클래스
    """

    def __init__(self, service_key=None):
        self.service_key = service_key
        self.url_dict = {
            "진위확인": "https://api.odcloud.kr/api/nts-businessman/v1/validate",
            "상태조회": "https://api.odcloud.kr/api/nts-businessman/v1/status",
        }

    def validate(self, businesses):
        """
        사업자등록정보 진위확인 API

        Parameters
        ----------
        businesses : list, DataFrame
            사업자등록정보 리스트 (1회 호출 시 최대 100개까지 조회 가능)

        Returns
        -------
        DataFrame
            진위확인 결과
        """
        url = self.url_dict["진위확인"]
        params = {
            "serviceKey": requests.utils.unquote(self.service_key),
        }
        if type(businesses) == pd.DataFrame:
            businesses = businesses.to_dict("records")
        json_data = {
            "businesses": businesses,
        }
        try:
            response = requests.post(
                url, params=params, json=json_data, verify=False)
            df = pd.json_normalize(response.json()['data'])
        except Exception as e:
            print("Error")
            print(e)
            return
        return df

    def status(self, b_no):
        """
        사업자등록정보 상태조회 API

        Parameters
        ----------
        b_no : list
            사업자등록번호 (1회 호출 시 최대 100개까지 조회 가능)

        Returns
        -------
        DataFrame
            상태조회 결과
        """
        url = self.url_dict["상태조회"]
        params = {
            "serviceKey": requests.utils.unquote(self.service_key),
        }
        data = {
            "b_no": b_no,
        }
        try:
            response = requests.post(
                url, params=params, json=data, verify=False)
            df = pd.DataFrame(response.json()['data'])
        except Exception as e:
            print("Error")
            print(e)
            return
        return df
