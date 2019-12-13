import pandas as pd
import numpy as np
import datetime
import requests
from bs4 import BeautifulSoup

class Station:
    '''
    측정소정보 조회 서비스 클래스
    '''
    
    def __init__(self, serviceKey):
        '''
        서비스키 초기화
        '''
        self.serviceKey = serviceKey
    
    def GetNearby(self, tmX, tmY, ver):
        '''
        01 오퍼레이션
        근접측정소 목록 조회(getNearbyMsrstnList)
        '''
        # URL
        url_1="http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList?tmX="+tmX
        url_2=url_1+"&tmY="+tmY
        url_3=url_2+"&ver="+ver
        url=url_3+"&ServiceKey="+self.serviceKey
                
        # Get raw data
        result = requests.get(url, verify=False)

        # Parsing
        xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

        # Filtering
        te = xmlsoup.findAll("item")

        # Creating Pandas Data Frame
        df = pd.DataFrame()    
        variables = ['stationName', 'addr', 'tm']

        for t in te: 
            for variable in variables:       
                try :
                    globals()[variable] = t.find(variable).text
                except :
                    globals()[variable] = np.nan
            data = pd.DataFrame(
                                [[stationName, addr, tm]], 
                                columns = variables
                                )
            df = pd.concat([df, data])

        # Arange Columns
        df.index = range(len(df))

        return df
    
    def GetList(self, addr, stationName, pageNo, numOfRows):
        '''
        02 오퍼레이션
        측정소 목록 조회(getMsrstnList)
        '''
         # URL
        url_1="http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getMsrstnList?addr="+addr
        url_2=url_1+"&stationName="+stationName
        url_3=url_2+"&pageNo="+pageNo
        url_4=url_3+"&numOfRows="+numOfRows
        url=url_4+"&ServiceKey="+self.serviceKey
                        
        # Get raw data
        result = requests.get(url, verify=False)

        # Parsing
        xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

        # Filtering
        te = xmlsoup.findAll("item")

        # Creating Pandas Data Frame
        df = pd.DataFrame()    
        variables = ['stationName', 'addr', 'year', 'oper', 'photo', 'vrml', 'map', 'mangName', 'item', 'dmX', 'dmY']

        for t in te: 
            for variable in variables:       
                try :
                    globals()[variable] = t.find(variable).text
                except :
                    globals()[variable] = np.nan
            data = pd.DataFrame(
                                [[stationName, addr, year, oper, photo, vrml, map, mangName, item, dmX, dmY]], 
                                columns = variables
                                )
            df = pd.concat([df, data])

        # Arange Columns
        df.index = range(len(df))

        return df   
    
    def GetTM(self,umdName,pageNo,numOfRows):
        '''
        03 오퍼레이션
        TM 기준좌표 조회(getTMStdrCrdnt)
        '''
        
         # URL
        url_1="http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getTMStdrCrdnt?umdName="+umdName
        url_2=url_1+"&pageNo="+pageNo
        url_3=url_2+"&numOfRows="+numOfRows
        url=url_3+"&ServiceKey="+self.serviceKey
                        
        # Get raw data
        result = requests.get(url, verify=False)

        # Parsing
        xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

        # Filtering
        te = xmlsoup.findAll("item")

        # Creating Pandas Data Frame
        df = pd.DataFrame()    
        variables = ['sidoName', 'sggName', 'umdName', 'tmX', 'tmY']

        for t in te: 
            for variable in variables:       
                try :
                    globals()[variable] = t.find(variable).text
                except :
                    globals()[variable] = np.nan
            data = pd.DataFrame(
                                [[sidoName, sggName, umdName, tmX, tmY]], 
                                columns = variables
                                )
            df = pd.concat([df, data])

        # Arange Columns
        df.index = range(len(df))

        return df



class AirDataRT:
    
    def __init__(self, serviceKey):
        '''
        서비스키 초기화
        '''
        self.serviceKey = serviceKey
  
    def DataReader(self, stationName, dataTerm, pageNo, numOfRows, ver):

        # URL
        url_1="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName="+stationName
        url_2=url_1+"&dataTerm="+dataTerm
        url_3=url_2+"&pageNo="+pageNo
        url_4=url_3+"&numOfRows="+numOfRows
        url_5=url_4+"&ServiceKey="+self.serviceKey
        url=url_5+"&ver="+ver
                
        # Get raw data
        result = requests.get(url, verify=False)

        # Parsing
        xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

        # Filtering
        te = xmlsoup.findAll("item")

        # Creating Pandas Data Frame
        df = pd.DataFrame()    
        variables = ['dataTime','mangName','so2Value','coValue','o3Value',
                     'no2Value','pm10Value','pm10Value24','pm25Value',
                     'pm25Value24','khaiValue','khaiGrade','so2Grade',
                     'coGrade','o3Grade','no2Grade','pm10Grade','pm25Grade',
                     'pm10Grade1h','pm25Grade1h']

        for t in te: 
            for variable in variables:       
                try :
                    globals()[variable] = t.find(variable).text
                except :
                    globals()[variable] = np.nan
            data = pd.DataFrame(
                                [[dataTime,mangName,so2Value,coValue,o3Value,
                                 no2Value,pm10Value,pm10Value24,pm25Value,
                                 pm25Value24,khaiValue,khaiGrade,so2Grade,
                                 coGrade,o3Grade,no2Grade,pm10Grade,pm25Grade,
                                 pm10Grade1h,pm25Grade1h]], 
                                columns = variables
                                )
            df = pd.concat([df, data])

        # Arange Columns
        df.index = range(len(df))

        return df



class AirData:
    
    def __init__(self, serviceKey):
        '''
        서비스키 초기화
        '''
        self.serviceKey = serviceKey
  
    def StnDataReader(self, stationName, searchCondition, pageNo, numOfRows):
        '''
        01 오퍼레이션
        측정소별 최종확정 농도 조회(getMsrstnAcctoLastDcsnDnsty)
        측정소명을 입력하여 일별, 월별, 연별 확정농도 수치 조회
        '''

        # URL
        url_1="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnStatsSvc/getMsrstnAcctoLastDcsnDnsty?stationName="+stationName
        url_2=url_1+"&searchCondition="+searchCondition
        url_3=url_2+"&pageNo="+pageNo
        url_4=url_3+"&numOfRows="+numOfRows
        url=url_4+"&ServiceKey="+self.serviceKey
     
        # Get raw data
        result = requests.get(url, verify=False)

        # Parsing
        xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

        # Filtering
        te = xmlsoup.findAll("item")

        # Creating Pandas Data Frame
        df = pd.DataFrame()    
        variables = ['dataTime', 'so2Avg', 'coAvg', 'o3Avg', 'no2Avg', 'pm10Avg']

        for t in te: 
            for variable in variables:       
                try :
                    globals()[variable] = t.find(variable).text
                except :
                    globals()[variable] = np.nan
            data = pd.DataFrame(
                                [[dataTime, so2Avg, coAvg, o3Avg, no2Avg, pm10Avg]], 
                                columns = variables
                                )
            df = pd.concat([df, data])

        # Arange Columns
        df.index = range(len(df))

        return df
    
    
    def PeriodDataReader(self,searchDataTime,statArticleCondition,pageNo,numOfRows):
        '''
        02 오퍼레이션
        기간별 오염통계 정보 조회(getDatePollutnStatInfo)
        '''
        
        # URL
        url_1="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnStatsSvc/getDatePollutnStatInfo?searchDataTime="+searchDataTime
        url_2=url_1+"&statArticleCondition="+statArticleCondition
        url_3=url_2+"&pageNo="+pageNo
        url_4=url_3+"&numOfRows="+numOfRows
        url=url_4+"&ServiceKey="+self.serviceKey
        
        # Get raw data
        result = requests.get(url, verify=False)

        # Parsing
        xmlsoup = BeautifulSoup(result.text, 'lxml-xml')

        # Filtering
        te = xmlsoup.findAll("item")

        # Creating Pandas Data Frame
        df = pd.DataFrame()    
        variables = ['sidoName', 'dataTime', 'so2Avg', 'coAvg', 'o3Avg', 'no2Avg', 
                    'pm10Avg', 'so2Max', 'coMax', 'o3Max', 'no2Max', 'pm10Max', 'so2Min',
                    'coMin', 'o3Min', 'no2Min', 'pm10Min']

        for t in te: 
            for variable in variables:       
                try :
                    globals()[variable] = t.find(variable).text
                except :
                    globals()[variable] = np.nan
            data = pd.DataFrame(
                                [[sidoName, dataTime, so2Avg, coAvg, o3Avg, no2Avg, 
                                 pm10Avg, so2Max, coMax, o3Max, no2Max, pm10Max, so2Min,
                                 coMin, o3Min, no2Min, pm10Min]], 
                                columns = variables
                                )
            df = pd.concat([df, data])

        # Arange Columns
        df.index = range(len(df))

        return df