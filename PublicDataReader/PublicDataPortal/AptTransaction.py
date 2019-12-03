import pandas as pd
import requests
from bs4 import BeautifulSoup

class AptTransactionReader:
    
    def __init__(self, serviceKey):
        '''
        공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.
        '''
        self.serviceKey = serviceKey
        
    
    def CodeFinder(self, name):
        '''
        국토교통부 실거래가 정보 오픈API는 법정동코드 10자리 중 앞 5자리인 구를 나타내는 지역코드를 사용합니다.
        API에 사용할 구 별 코드를 조회하는 메소드이며, 문자열 지역 명을 입력받고, 조회 결과를 Pandas DataFrame형식으로 출력합니다.
        '''
        path_code = "https://raw.githubusercontent.com/WooilJeong/PublicDataReader/f14e4de3410cc0f798a83ee5934070d651cbd67b/docs/%EB%B2%95%EC%A0%95%EB%8F%99%EC%BD%94%EB%93%9C%20%EC%A0%84%EC%B2%B4%EC%9E%90%EB%A3%8C.txt"
        code = pd.read_csv(path_code, encoding='cp949', sep='\t')
        code = code.loc[code['폐지여부']=='존재']
        code['법정구코드'] = list(map(lambda a: str(a)[:5], list(code['법정동코드'])))
        result = code[code['법정동명'].str.contains(name)][['법정동명','법정구코드']]
        result.index = range(len(result))
        
        return result

    def DataReader(self, LAWD_CD, DEAL_YMD):
        '''
        지역코드와 계약월을 입력받고, 아파트 실거래 정보를 Pandas DataFrame 형식으로 출력합니다.
        '''

        # URL
        url_1="http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?LAWD_CD="+LAWD_CD
        url_2="&DEAL_YMD=" + DEAL_YMD
        url_3="&serviceKey=" + self.serviceKey
        url = url_1+url_2+url_3

        # Get raw data
        result = requests.get(url, verify=False)

        # Parsing
        xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

        # Filtering
        te = xmlsoup.findAll("item")

        # Creating Pandas Data Frame
        df = pd.DataFrame()    
        variables = ['법정동','지역코드','아파트','지번','년','월','일','건축년도','전용면적','층','거래금액']

        for t in te: 
            for variable in variables:       
                try :
                    globals()[variable] = t.find(variable).text
                except :
                    globals()[variable] = np.nan
            data = pd.DataFrame(
                                [[법정동,지역코드,아파트,지번,년,월,일,건축년도,전용면적,층,거래금액]], 
                                columns = variables
                                )
            df = pd.concat([df, data])

        # Feature Engineering
        df['거래일'] = df['년'] + '-' + df['월'] + '-' + df['일']
        df['거래일'] = pd.to_datetime(df['거래일'])
        df['거래금액'] = pd.to_numeric(df['거래금액'].str.replace(',',''))

        # Arange Columns
        df = df[['지역코드','법정동','거래일','아파트','지번','전용면적','층','건축년도','거래금액']]
        df = df.sort_values(['법정동','거래일'])
        df['법정동'] = df['법정동'].str.strip()
        df.index = range(len(df))

        return df