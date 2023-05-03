import os
import json
import pandas as pd

_path = os.path.dirname(__file__)
_project_root_path = os.path.dirname(_path)
_code_bdong_json_path = f"""{_project_root_path}/raw/code_bdong.json"""
_code_hdong_json_path = f"""{_project_root_path}/raw/code_hdong.json"""
_code_hdong_bdong_json_path = f"""{_project_root_path}/raw/code_hdong_bdong.json"""
_code_vworld_json_path = f"""{_project_root_path}/raw/code_vworld.json"""


CODE_INFORMATION = F"""\
출처: 행정기관(행정동) 및 관할구역(법정동) 변경내역(2023. 5. 1. 시행)
URL: https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000052&nttId=100215
"""


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
    print(CODE_INFORMATION)
    return pd.DataFrame(read_json_file(_code_bdong_json_path)).fillna("")


def code_hdong():
    """
    행정기관코드(행정동) 데이터 반환
    """
    print(CODE_INFORMATION)
    return pd.DataFrame(read_json_file(_code_hdong_json_path)).fillna("")


def code_hdong_bdong():
    """
    행정기관코드 + 관할 법정동코드 데이터 반환
    """
    print(CODE_INFORMATION)
    return pd.DataFrame(read_json_file(_code_hdong_bdong_json_path)).fillna("")


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
