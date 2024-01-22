import os
import json
import requests
import pandas as pd

_path = os.path.dirname(__file__)
_project_root_path = os.path.dirname(_path)
_code_vworld_json_path = f"""{_project_root_path}/raw/code_vworld.json"""

_code_bdong_json_url = "https://raw.githubusercontent.com/WooilJeong/code/main/code/code_dong/code_bdong.json"
_code_hdong_json_url = "https://raw.githubusercontent.com/WooilJeong/code/main/code/code_dong/code_hdong.json"
_code_hdong_bdong_json_url = "https://raw.githubusercontent.com/WooilJeong/code/main/code/code_dong/code_hdong_bdong.json"

def get_code_dong_by_url(url):
    """
    URL로 동 코드 JSON 읽기
    """
    res = requests.get(url)
    return json.loads(res.content)


def read_json_file(file_path):
    """
    json 파일 읽기
    """
    with open(file_path, "r") as f:
        data = f.read()
        return json.loads(data)


def code_bdong():
    """
    법정동코드(실제주소) 데이터 반환
    """
    res = get_code_dong_by_url(_code_bdong_json_url)
    name = res['name']
    data = res['data']
    print(f"출처: {name}")
    return pd.DataFrame(data).fillna("")

def code_hdong():
    """
    행정기관코드(행정동) 데이터 반환
    """
    res = get_code_dong_by_url(_code_hdong_json_url)
    name = res['name']
    data = res['data']
    print(f"출처: {name}")
    return pd.DataFrame(data).fillna("")

def code_hdong_bdong():
    """
    행정기관코드 + 관할 법정동코드 데이터 반환
    """
    res = get_code_dong_by_url(_code_hdong_bdong_json_url)
    name = res['name']
    data = res['data']
    print(f"출처: {name}")
    return pd.DataFrame(data).fillna("")

def get_vworld_data_api_info_by_dataframe():
    """
    vworld 코드 데이터 반환
    """
    return pd.DataFrame(read_json_file(_code_vworld_json_path).items(), columns=["서비스명", "서비스ID"])


def get_vworld_data_api_info_by_dict():
    """
    vworld 코드 테이블 반환
    """
    return read_json_file(_code_vworld_json_path)
