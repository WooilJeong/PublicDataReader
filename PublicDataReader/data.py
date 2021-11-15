import pandas as pd
import glob
import os

# 국토교통부(molit) Open API 통합
from PublicDataReader.PublicDataPortal.molit import Transaction, Building

# 소상공인 진흥공단(semas) Open API 통합
from PublicDataReader.PublicDataPortal.semas import StoreInfo

# 서울시 지하철호선별 역별 승하차 인원 정보 Open API
from PublicDataReader.Seoul.transportation import Transportation


# 코드 테이블
# def code_list():
#     data_path_str = os.path.join(os.path.dirname(__file__), 'data/*.csv')
#     data_path_list = glob.glob(data_path_str)
#     df = pd.read_csv(data_path_list[0], encoding='cp949')
#     return df

code_list_path = "https://raw.githubusercontent.com/WooilJeong/PublicDataReader/develop/PublicDataReader/data/bdong_code.csv"
def code_list():
    df = pd.read_csv(code_list_path, encoding="cp949")
    return df