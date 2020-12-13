'''
@ Author : Wooil Jeong
@ E-mail : wooil@kakao.com
@ Github : https://github.com/WooilJeong/PublicDataReader
@ Blog : https://wooiljeong.github.io
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

class Common():
    def __init__(self, serviceKey):
        '''
        공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.
        '''
        # Open API 서비스 키 초기화
        self.serviceKey = serviceKey
        
    def test(self, api_url):
        # Get raw data
        result = requests.get(api_url, verify=False)

        # Parsing
        xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

        # Filtering
        te = xmlsoup.findAll("header")
            
        if te[0].find('resultCode').text == "00":
            print(">>> 서비스가 정상 작동합니다.")
        
        else:
            print(">>> 서비스키 미등록 오류입니다.")
            

        # 지역 코드 초기화
        # 법정동 코드 출처 : https://code.go.kr
        path_code = "https://raw.githubusercontent.com/WooilJeong/PublicDataReader/f14e4de3410cc0f798a83ee5934070d651cbd67b/docs/%EB%B2%95%EC%A0%95%EB%8F%99%EC%BD%94%EB%93%9C%20%EC%A0%84%EC%B2%B4%EC%9E%90%EB%A3%8C.txt"
        code = pd.read_csv(path_code, encoding='cp949', sep='\t')
        code = code.loc[code['폐지여부']=='존재']
        code['법정구코드'] = list(map(lambda a: str(a)[:5], list(code['법정동코드'])))
        self.code = code