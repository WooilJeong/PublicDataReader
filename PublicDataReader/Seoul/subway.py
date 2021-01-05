'''
서울 열린데이터 광장 Open API

1. subwayInfo 클래스: 서울시 지하철호선별 역별 승하차 인원 정보 조회

'''

import pandas as pd
import numpy as np
import datetime
import requests
from bs4 import BeautifulSoup

class SubwayInfo:
    def __init__(self, serviceKey):
        '''
        서울 열린데이터 광장에서 발급받은 Service Key를 입력받아 초기화합니다.
        '''
        # Open API 서비스 키 초기화
        self.serviceKey = serviceKey

        # ServiceKey 등록
        self.urlBase = f'http://openapi.seoul.go.kr:8088/'
        
        print('>> Open API Services initialized!')

    def CardSubwayStatsNew(self, start_index, end_index, use_dt):

        url = f"{self.urlBase}{self.serviceKey}/xml/CardSubwayStatsNew/{start_index}/{end_index}/{use_dt}"
        
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("row")

            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ['USE_DT', 'LINE_NUM', 'SUB_STA_NM', 'RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM', 'WORK_DT']

            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[USE_DT, LINE_NUM, SUB_STA_NM, RIDE_PASGR_NUM, ALIGHT_PASGR_NUM, WORK_DT]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))

            # Datetime 변환
            df['USE_DT'] = pd.to_datetime(df['USE_DT'], format='%Y%m%d')
            df['WORK_DT'] = pd.to_datetime(df['WORK_DT'], format='%Y%m%d')

            # 숫자형 변환
            df['RIDE_PASGR_NUM'] = pd.to_numeric(df['RIDE_PASGR_NUM'])
            df['ALIGHT_PASGR_NUM'] = pd.to_numeric(df['ALIGHT_PASGR_NUM'])
            
        except:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("RESULT")
            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find('CODE').text == "INFO-000":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(f">>> {te[0].find('CODE').text} {te[0].find('MESSAGE').text}")
            pass
        
        return df
