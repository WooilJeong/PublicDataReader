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