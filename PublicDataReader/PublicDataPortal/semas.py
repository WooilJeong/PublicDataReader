'''
소상공인 진흥공단 Open API
semas(Small Enterprise And Market Service)

1. StoreInfo 클래스: 소상공인 상가업소 정보 조회
    0. baroApi: 바로API
    1. storeZoneOne: 지정 상권조회
    2. storeZoneInRadius: 반경내 상권조회
    3. storeZoneInRectangle: 사각형내 상권조회
    4. storeZoneInAdmi: 행정구역 단위 상권조회
    5. storeOne: 단일 상가업소 조회
    6. storeListInBuilding: 건물단위 상가업소 조회
    7. storeListInPnu: 지번단위 상가업소 조회
    8. storeListInDong: 행정동 단위 상가업소 조회
    9. storeListInArea: 상권내 상가업소 조회
    10. storeListInRadius: 반경내 상가업소 조회
    11. storeListInRectangle: 사각형내 상가업소 조회
    12. storeListInPolygon: 다각형내 상가업소 조회
    13. storeListInUpjong: 업종별 상가업소 조회
    14. storeListByDate: 수정일자기준 상가업소 조회
    15. reqStoreModify: 상가업소정보 변경요청
    16. largeUpjongList: 행정구역내 업종별 상가업소 통계
    17. middleUpjongList: 건물내 업종별 상가업소 통계
    18. smallUpjongList: 반경내 업종별 상가업소 통계
    19. storeStatsUpjongInAdmi: 사각형내 업종별 상가업소 통계
    20. storeStatsUpjongInBuilding: 다각형내 업종별 상가업소 통계
    21. storeStatsUpjongInRadius: 상권정보 업종 대분류 조회
    22. storeStatsUpjongInRectangle: 상권정보 업종 중분류 조회
    23. storeStatsUpjongInPolygon: 상권정보 업종 소분류 조회
'''

import pandas as pd
import numpy as np
import datetime
import requests
from bs4 import BeautifulSoup

class StoreInfo:
    def __init__(self, serviceKey):
        '''
        공공 데이터 포털에서 발급받은 Service Key를 입력받아 초기화합니다.
        '''
        # Open API 서비스 키 초기화
        self.serviceKey = serviceKey

        # ServiceKey 등록
        self.urlBase = f'http://apis.data.go.kr/B553077/api/open/sdsc/'
        
        print('>> Open API Services initialized!')
        
    def storeZoneOne(self, key):
        '''
        1. 지정 상권조회
        입력: 상권번호
        '''
        url = f'{self.urlBase}storeZoneOne?ServiceKey={self.serviceKey}&key={key}'
        
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ['trarNo','mainTrarNm','ctprvnCd','ctprvnNm','signguCd','signguNm','trarArea','coordNum','coords','stdrDt']

            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[trarNo,mainTrarNm,ctprvnCd,ctprvnNm,signguCd,signguNm,trarArea,coordNum,coords,stdrDt]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            
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
            elif te[0].find('resultCode').text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
            pass
        
        return df
        
    def storeZoneInRadius(self, radius, cx, cy):
        '''
        2. 반경내 상권조회
        입력: 반경(m), 중심점 경도(WGS84 좌표계), 중심점 위도(WGS84 좌표계)
        '''
        url = f'{self.urlBase}storeZoneInRadius?ServiceKey={self.serviceKey}&radius={radius}&cx={cx}&cy={cy}'
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ['trarNo','mainTrarNm','ctprvnCd','ctprvnNm','signguCd','signguNm','trarArea','coordNum','coords','stdrDt']

            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[trarNo,mainTrarNm,ctprvnCd,ctprvnNm,signguCd,signguNm,trarArea,coordNum,coords,stdrDt]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            
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
            elif te[0].find('resultCode').text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
            pass
        
        return df
    

    def storeZoneInRectangle(self, minx, miny, maxx, maxy):
        '''
        3. 사각형내 상권조회
        입력: 서쪽 경도, 남쪽 위도, 동쪽 경도, 북쪽 위도 (WGS84 좌표계)
        '''
        url = f'{self.urlBase}storeZoneInRectangle?ServiceKey={self.serviceKey}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}'
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ['trarNo','mainTrarNm','ctprvnCd','ctprvnNm','signguCd','signguNm','trarArea','coordNum','coords','stdrDt']

            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[trarNo,mainTrarNm,ctprvnCd,ctprvnNm,signguCd,signguNm,trarArea,coordNum,coords,stdrDt]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            
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
            elif te[0].find('resultCode').text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
            pass
        
        return df        
        
    def storeZoneInAdmi(self, divId, key):
        '''
        4. 행정구역 단위 상권조회
        입력: 구분ID, 행정구역코드
        구분ID - 시도(ctprvnCd), 시군구(signguCd), 행정동(adongCd)
        행정구역코드 - 시도(시도코드값), 시군구(시군구코드값), 행정동(행정동코드값)
        '''
        url = f'{self.urlBase}storeZoneInAdmi?ServiceKey={self.serviceKey}&divId={divId}&key={key}'
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ['trarNo','mainTrarNm','ctprvnCd','ctprvnNm','signguCd','signguNm','trarArea','coordNum','coords','stdrDt']

            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[trarNo,mainTrarNm,ctprvnCd,ctprvnNm,signguCd,signguNm,trarArea,coordNum,coords,stdrDt]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            
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
            elif te[0].find('resultCode').text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
            pass
        
        return df
    

    def storeOne(self, key):
        '''
        5. 단일 상가업소 조회
        입력: 상가업소번호
        '''
        url = f'{self.urlBase}storeOne?ServiceKey={self.serviceKey}&key={key}'
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ['bizesId','bizesNm','brchNm','indsLclsCd','indsLclsNm',
                         'indsMclsCd','indsMclsNm','indsSclsCd','indsSclsNm','ksicCd',
                         'ksicNm','ctprvnCd','ctprvnNm','signguCd','signguNm',
                         'adongCd','adongNm','ldongCd','ldongNm','lnoCd',
                         'plotSctCd','plotSctNm','lnoMnno','lnoSlno','lnoAdr',
                         'rdnmCd','rdnm','bldMnno','bldSlno','bldMngNo',
                         'bldNm','rdnmAdr','oldZipcd','newZipcd','dongNo',
                         'flrNo','hoNo','lon','lat']

            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[bizesId,bizesNm,brchNm,indsLclsCd,indsLclsNm,
                                     indsMclsCd,indsMclsNm,indsSclsCd,indsSclsNm,ksicCd,
                                     ksicNm,ctprvnCd,ctprvnNm,signguCd,signguNm,
                                     adongCd,adongNm,ldongCd,ldongNm,lnoCd,
                                     plotSctCd,plotSctNm,lnoMnno,lnoSlno,lnoAdr,
                                     rdnmCd,rdnm,bldMnno,bldSlno,bldMngNo,
                                     bldNm,rdnmAdr,oldZipcd,newZipcd,dongNo,
                                     flrNo,hoNo,lon,lat]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            
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
            elif te[0].find('resultCode').text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
            pass
        
        return df        
        
    def storeListInBuilding(self,indsLclsCd, indsMclsCd=None, indsSclsCd=None, numOfRows=1000):
        '''
        6. 건물단위 상가업소 조회
        입력: 건물관리번호, 상권업종대분류코드, 상권업종중분류코드, 상권업종소분류코드, 페이지당 건수(최대 1000)
        '''
        url = f'{self.urlBase}storeListInBuilding?ServiceKey={self.serviceKey}&indsLclsCd={indsLclsCd}&indsMclsCd={indsMclsCd}&indsSclsCd={indsSclsCd}&numOfRows={numOfRows}'
        try:
            # Get raw data
            result = requests.get(url, verify=False)
            # Parsing
            xmlsoup = BeautifulSoup(result.text, 'lxml-xml')
            # Filtering
            te = xmlsoup.findAll("item")

            # Creating Pandas Data Frame
            df = pd.DataFrame()    
            variables = ['bizesId','bizesNm','brchNm','indsLclsCd','indsLclsNm',
                         'indsMclsCd','indsMclsNm','indsSclsCd','indsSclsNm','ksicCd',
                         'ksicNm','ctprvnCd','ctprvnNm','signguCd','signguNm',
                         'adongCd','adongNm','ldongCd','ldongNm','lnoCd',
                         'plotSctCd','plotSctNm','lnoMnno','lnoSlno','lnoAdr',
                         'rdnmCd','rdnm','bldMnno','bldSlno','bldMngNo',
                         'bldNm','rdnmAdr','oldZipcd','newZipcd','dongNo',
                         'flrNo','hoNo','lon','lat']

            for t in te: 
                for variable in variables:       
                    try :
                        globals()[variable] = t.find(variable).text
                    except :
                        globals()[variable] = np.nan
                data = pd.DataFrame(
                                    [[bizesId,bizesNm,brchNm,indsLclsCd,indsLclsNm,
                                     indsMclsCd,indsMclsNm,indsSclsCd,indsSclsNm,ksicCd,
                                     ksicNm,ctprvnCd,ctprvnNm,signguCd,signguNm,
                                     adongCd,adongNm,ldongCd,ldongNm,lnoCd,
                                     plotSctCd,plotSctNm,lnoMnno,lnoSlno,lnoAdr,
                                     rdnmCd,rdnm,bldMnno,bldSlno,bldMngNo,
                                     bldNm,rdnmAdr,oldZipcd,newZipcd,dongNo,
                                     flrNo,hoNo,lon,lat]], 
                                    columns = variables
                                    )
                df = pd.concat([df, data])

            # Set col names
            df.columns = variables
            
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
            elif te[0].find('resultCode').text == "03":
                print(">>> NODATA_ERROR")
            # Open API 서비스 제공처 오류
            else:
                print(">>> Open API Error: {}".format(te[0].find['resultMsg']))
            pass
        
        return df        
        
        
#     def storeListInPnu(self):
#         '''
#         7. 지번단위 상가업소 조회
#         '''
        
        
#     def storeListInDong(self):
#         '''
#         8. 행정동 단위 상가어소 조회
#         '''
        
        
#     def storeListInArea(self):
#         '''
#         9. 상권내 상가업소 조회
#         '''
        
        
#     def storeListInRadius(self):
#         '''
#         10. 반경내 상가업소 조회
#         '''
        
        
#     def storeListInRectangle(self):
#         '''
#         11. 사각형내 상가업소 조회
#         '''
        
        
#     def storeListInPolygon(self):
#         '''
#         12. 다각형내 상가업소 조회
#         '''
        
        
#     def storeListInUpjong(self):
#         '''
#         13. 업종별 상가업소 조회
#         '''
        
        
#     def storeListByDate(self):
#         '''
#         14. 수정일자기준 상가업소 조회
#         '''
        
        
#     def reqStoreModify(self):
#         '''
#         15. 상가업소정보 변경요청
#         '''
        
        
#     def largeUpjongList(self):
#         '''
#         16. 행정구역내 업종별 상가업소 통계
#         '''
        
        
#     def middleUpjongList(self):
#         '''
#         17. 건물내 업종별 상가업소 통계
#         '''
        
        
#     def smallUpjongList(self):
#         '''
#         18. 반경내 업종별 상가업소 통계
#         '''
        
        
#     def storeStatsUpjongInAdmi(self):
#         '''
#         19. 사각형내 업종별 상가업소 통계
#         '''
        
        
#     def storeStatsUpjongInBuilding(self):
#         '''
#         20. 다각형내 업종별 상가업소 통계
#         '''
        
        
#     def storeStatsUpjongInRadius(self):
#         '''
#         21. 상권정보 업종 대분류 조회
#         '''
        
        
#     def storeStatsUpjongInRectangle(self):
#         '''
#         22. 상권정보 업종 중분류 조회
#         '''
        
        
#     def storeStatsUpjongInPolygon(self):
#         '''
#         23. 상권정보 업종 소분류 조회
#         '''
        
        
