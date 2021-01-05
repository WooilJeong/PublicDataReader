'''
서울 열린데이터 광장 Open API

1. TransInfo 클래스: 서울시 교통 관련 정보 조회

'''

import pandas as pd
import numpy as np
import datetime
import requests
from bs4 import BeautifulSoup

class TransInfo:
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
        """
        지하철 승하차 정보 조회
        입력: 시작 인덱스, 끝 인덱스, 조회 일자
        조건: 1회 1000건 제한        
        """

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
        
        # 전체 자료 건 수
        n_data = xmlsoup.findAll("list_total_count")[0].text
        print(f">>> 전체 자료 건 수: {n_data}")
        
        return df

    def CardBusTimeNew(self, start_index, end_index, use_mon):
        """
        버스 승하차 정보 조회
        입력: 시작 인덱스, 끝 인덱스, 조회 년월
        조건: 1회 1000건 제한        
        """

        url = f"{self.urlBase}{self.serviceKey}/xml/CardBusTimeNew/{start_index}/{end_index}/{use_mon}"

        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("row")
            
            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ["USE_MON", "BUS_ROUTE_NO", "BUS_ROUTE_NM", "STND_BSST_ID", "BSST_ARS_NO", "BUS_STA_NM", "MIDNIGHT_RIDE_NUM", "MIDNIGHT_ALIGHT_NUM", "ONE_RIDE_NUM", "ONE_ALIGHT_NUM", "TWO_RIDE_NUM", "TWO_ALIGHT_NUM", "THREE_RIDE_NUM", "THREE_ALIGHT_NUM", "FOUR_RIDE_NUM", "FOUR_ALIGHT_NUM", "FIVE_RIDE_NUM", "FIVE_ALIGHT_NUM", "SIX_RIDE_NUM", "SIX_ALIGHT_NUM", "SEVEN_RIDE_NUM", "SEVEN_ALIGHT_NUM", "EIGHT_RIDE_NUM", "EIGHT_ALIGHT_NUM", "NINE_RIDE_NUM", "NINE_ALIGHT_NUM", "TEN_RIDE_NUM", "TEN_ALIGHT_NUM", "ELEVEN_RIDE_NUM", "ELEVEN_ALIGHT_NUM", "TWELVE_RIDE_NUM", "TWELVE_ALIGHT_NUM", "THIRTEEN_RIDE_NUM", "THIRTEEN_ALIGHT_NUM", "FOURTEEN_RIDE_NUM", "FOURTEEN_ALIGHT_NUM", "FIFTEEN_RIDE_NUM", "FIFTEEN_ALIGHT_NUM", "SIXTEEN_RIDE_NUM", "SIXTEEN_ALIGHT_NUM", "SEVENTEEN_RIDE_NUM", "SEVENTEEN_ALIGHT_NUM", "EIGHTEEN_RIDE_NUM", "EIGHTEEN_ALIGHT_NUM", "NINETEEN_RIDE_NUM", "NINETEEN_ALIGHT_NUM", "TWENTY_RIDE_NUM", "TWENTY_ALIGHT_NUM", "TWENTY_ONE_RIDE_NUM", "TWENTY_ONE_ALIGHT_NUM", "TWENTY_TWO_RIDE_NUM", "TWENTY_TWO_ALIGHT_NUM", "TWENTY_THREE_RIDE_NUM", "TWENTY_THREE_ALIGHT_NUM", "WORK_DT"]

            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[USE_MON, BUS_ROUTE_NO, BUS_ROUTE_NM, STND_BSST_ID, BSST_ARS_NO, BUS_STA_NM, MIDNIGHT_RIDE_NUM, MIDNIGHT_ALIGHT_NUM, ONE_RIDE_NUM, ONE_ALIGHT_NUM, TWO_RIDE_NUM, TWO_ALIGHT_NUM, THREE_RIDE_NUM, THREE_ALIGHT_NUM, FOUR_RIDE_NUM, FOUR_ALIGHT_NUM, FIVE_RIDE_NUM, FIVE_ALIGHT_NUM, SIX_RIDE_NUM, SIX_ALIGHT_NUM, SEVEN_RIDE_NUM, SEVEN_ALIGHT_NUM, EIGHT_RIDE_NUM, EIGHT_ALIGHT_NUM, NINE_RIDE_NUM, NINE_ALIGHT_NUM, TEN_RIDE_NUM, TEN_ALIGHT_NUM, ELEVEN_RIDE_NUM, ELEVEN_ALIGHT_NUM, TWELVE_RIDE_NUM, TWELVE_ALIGHT_NUM, THIRTEEN_RIDE_NUM, THIRTEEN_ALIGHT_NUM, FOURTEEN_RIDE_NUM, FOURTEEN_ALIGHT_NUM, FIFTEEN_RIDE_NUM, FIFTEEN_ALIGHT_NUM, SIXTEEN_RIDE_NUM, SIXTEEN_ALIGHT_NUM, SEVENTEEN_RIDE_NUM, SEVENTEEN_ALIGHT_NUM, EIGHTEEN_RIDE_NUM, EIGHTEEN_ALIGHT_NUM, NINETEEN_RIDE_NUM, NINETEEN_ALIGHT_NUM, TWENTY_RIDE_NUM, TWENTY_ALIGHT_NUM, TWENTY_ONE_RIDE_NUM, TWENTY_ONE_ALIGHT_NUM, TWENTY_TWO_RIDE_NUM, TWENTY_TWO_ALIGHT_NUM, TWENTY_THREE_RIDE_NUM, TWENTY_THREE_ALIGHT_NUM, WORK_DT]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            # Set Index
            df.index = range(len(df))
            
            # 숫자 형 변환
            cols = df.columns.drop(['USE_MON','BUS_ROUTE_NO','BUS_ROUTE_NM','STND_BSST_ID','BSST_ARS_NO','BUS_STA_NM','WORK_DT'])
            df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
         
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
        
        # 전체 자료 건 수
        n_data = xmlsoup.findAll("list_total_count")[0].text
        print(f">>> 전체 자료 건 수: {n_data}")

        return df