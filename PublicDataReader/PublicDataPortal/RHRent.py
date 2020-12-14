'''
@ Author : Wooil Jeong
@ E-mail : wooil@kakao.com
@ Github : https://github.com/WooilJeong/PublicDataReader
@ Blog : https://wooiljeong.github.io
'''


import pandas as pd
import numpy as np
import datetime
import requests
from bs4 import BeautifulSoup
from PublicDataReader.PublicDataPortal.__init__ import *

class RHRentReader(Common):
    
    def __init__(self, serviceKey):
        super().__init__(serviceKey)
        # ServiceKey 유효성 검사
        api_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?serviceKey=" + self.serviceKey
        super().test(api_url)
        
    
    def CodeFinder(self, name):
        '''
        국토교통부 실거래가 정보 오픈API는 법정동코드 10자리 중 앞 5자리인 구를 나타내는 지역코드를 사용합니다.
        API에 사용할 구 별 코드를 조회하는 메소드이며, 문자열 지역 명을 입력받고, 조회 결과를 Pandas DataFrame형식으로 출력합니다.
        '''

        result = self.code[self.code['법정동명'].str.contains(name)][['법정동명','법정구코드']]
        result.index = range(len(result))
        
        return result

    def DataReader(self, LAWD_CD, DEAL_YMD):
        '''
        지역코드와 계약월을 입력받고, 관련 자료를 Pandas DataFrame 형식으로 출력합니다.
        '''

        # URL
        url_1="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent?LAWD_CD="+LAWD_CD
        url_2="&DEAL_YMD=" + DEAL_YMD
        url_3="&serviceKey=" + self.serviceKey
        url = url_1+url_2+url_3

        try:
            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ['법정동','지역코드','연립다세대','지번','년','월','일','전용면적','건축년도','층','보증금액','월세금액']
            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[법정동,지역코드,연립다세대,지번,년,월,일,전용면적,건축년도,층,보증금액,월세금액]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set Columns
            colNames = ['지역코드','법정동','거래일','연립다세대','지번','전용면적','건축년도','층','보증금액','월세금액']

            # Feature Engineering
            try:
                if len(df['년']!=0) & len(df['월']!=0) & len(df['일']!=0):

                    df['거래일'] = df['년'] + '-' + df['월'] + '-' + df['일']
                    df['거래일'] = pd.to_datetime(df['거래일'])
                    df['보증금액'] = pd.to_numeric(df['보증금액'].str.replace(',',''))
                    df['월세금액'] = pd.to_numeric(df['월세금액'].str.replace(',',''))

            except:
                df = pd.DataFrame(columns=colNames)
                print("조회할 자료가 없습니다.")


            # Arange Columns
            df = df[colNames]
            df = df.sort_values(['법정동','거래일'])
            df['법정동'] = df['법정동'].str.strip()
            df.index = range(len(df))

            return df

        except:

            # Get raw data
            result = requests.get(url, verify=False)

            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

            # Filtering
            te = xmlsoup.findAll("header")

            # 정상 요청시 에러 발생 -> Python 코드 에러
            if te[0].find('resultCode').text == "00":
                print(">>> Python Logic Error. e-mail : wooil@kakao.com")

            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find['resultMsg']))


    def DataCollector(self, LAWD_CD, start_date, end_date):
        '''
        특정 기간 동안의 데이터 수집 메소드
        '''

        end_date = datetime.datetime.strptime(end_date, "%Y-%m")
        end_date = end_date + datetime.timedelta(days=31)
        end_date = datetime.datetime.strftime(end_date, "%Y-%m")

        ts = pd.date_range(start=start_date, end=end_date, freq='m')
        date_list = list(ts.strftime('%Y%m'))
        
        df = pd.DataFrame()
        df_sum = pd.DataFrame()
        for m in date_list:
            
            print('>>> LAWD_CD :', LAWD_CD, 'DEAL_YMD :', m)
            
            DEAL_YMD = m
            
            df = self.DataReader(LAWD_CD, DEAL_YMD)
            df_sum = pd.concat([df_sum, df])
            
        df_sum.index = range(len(df_sum))

        return df_sum