import os
import json
import pandas as pd

_path = os.path.dirname(__file__)
_project_root_path = os.path.dirname(_path)
_json_file_path = f"""{_project_root_path}/raw/code_bdong.json"""


def code_bdong():
    """
    법정동코드 테이블 반환
    """
    with open(f"""{_json_file_path}""", "r") as f:
        data = f.read()
        return pd.DataFrame(json.loads(data))


def get_vworld_data_api_info_by_dataframe():
    """
    vworld 코드 테이블 반환
    """
    with open(f"""{_project_root_path}/raw/code_vworld.json""", "r") as f:
        data = f.read()
        return pd.DataFrame(json.loads(data).items(), columns=["서비스명","서비스ID"])


def get_vworld_data_api_info_by_dict():
    """
    vworld 코드 테이블 반환
    """
    with open(f"""{_project_root_path}/raw/code_vworld.json""", "r") as f:
        data = f.read()
        return json.loads(data)