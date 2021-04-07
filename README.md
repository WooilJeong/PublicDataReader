# PublicDataReader

![PNG](./img_logo.png)


## Open Source Project

- **Project Owner: 정우일(Wooil Jeong)**
- **e-mail: wooil@kakao.com**
- **사용 설명서**: 
  - [PublicDataReader - 부동산 데이터 수집하기](https://wooiljeong.github.io/python/public_data_reader_01/)
  - [PublicDataReader - 상가업소 데이터 수집하기](https://wooiljeong.github.io/python/public_data_reader_02/)
- **코랩 실습 코드**: 
  - [Colab - 국토교통부 실거래가 정보 조회](https://colab.research.google.com/drive/1pFtMFr_te9T_maHjee8Sd8Yq9rTrE-4F)
  - [Colab - 소상공인진흥공단 상가업소 정보 조회](https://colab.research.google.com/drive/14AAR6dRiTubZ8rnc883GitaB5q9pnIox?usp=sharing)


## 소개

- **최신 버전**  
![](https://img.shields.io/badge/PublicDataReader-2021.4.7-blue.svg)  

    - 20121.4.7 Version (2021-04):
      - 국토교통부 건축물대장정보 서비스 추가
    - 2021.1.9 Version (2021-01): 
      - 소상공인 상가업소 정보 조회 기능 추가
      - 서울시 지하철호선별 역별 승하차 인원 정보 조회 기능 추가   
      - 서울시 버스노선별 정류장별 시간대별 승하차 인원 정보 조회 기능 추가
    - 0.1.2 Version (2020-12): 
      - 국토교통부 실거래가 정보 조회 기능 전면 수정


- **요구 사항**  
![](https://img.shields.io/badge/Python-3.7.4-yellow.svg) ![](https://img.shields.io/badge/Pandas-0.25.3-red.svg)

**PublicDataReader**는 [공공데이터포털](https://data.go.kr), [서울 열린데이터 광장](https://data.seoul.go.kr/) 등 에서 제공하는 OpenAPI 서비스를 Python으로 쉽게 이용할 수 있도록 도와주는 **데이터 수집 라이브러리**입니다. 

**2021년 04월** 현재 아래 Open API 서비스를 이용하여 데이터를 Pandas DataFrame 형태로 조회할 수 있습니다. 추후 수요가 높은 Open API 서비스에 대한 인터페이스도 지속적으로 업데이트할 예정입니다.

- [국토교통부 실거래가 정보](https://www.data.go.kr/dataset/3050988/openapi.do)
- [국토교통부 건축물대장정보 서비스](https://www.data.go.kr/data/15044713/openapi.do)
- [소상공인 상가업소 정보](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15012005)
- [서울시 지하철호선별 역별 승하차 인원 정보](https://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do)
- [서울시 버스노선별 정류장별 시간대별 승하차 인원 정보](https://data.seoul.go.kr/dataList/OA-12913/S/1/datasetView.do)


## 공공 데이터 포털 서비스 목록

### 1) 국토교통부 실거래가 정보 조회 서비스

| **메서드**     | **서비스 명**                         |
| -------------- | ------------------------------------- |
| CondeFinder    | 지역코드 조회                         |
| DataCollector  | 서비스/기간 별 데이터 조회            |
| AptTrade       | 아파트매매 실거래자료 조회            |
| AptTradeDetail | 아파트매매 실거래 상세 자료 조회      |
| AptRent        | 아파트 전월세 자료 조회               |
| AptOwnership   | 아파트 분양권전매 신고 자료 조회      |
| OffiTrade      | 오피스텔 매매 신고 조회               |
| OffiRent       | 오피스텔 전월세 신고 조회             |
| RHTrade        | 연립다세대 매매 실거래자료 조회       |
| RHRent         | 연립다세대 전월세 실거래자료 조회     |
| DHTrade        | 단독/다가구 매매 실거래 조회          |
| DHRent         | 단독/다가구 전월세 자료 조회          |
| LandTrade      | 토지 매매 신고 조회                   |
| BizTrade       | 상업업무용 부동산 매매 신고 자료 조회 |


### 2) 국토교통부 건축물대장정보 서비스

| **메서드**               | **서비스 명**                |
| ------------------------ | ---------------------------- |
| getBrBasisOulnInfo       | 건축물대장 기본개요 조회     |
| getBrRecapTitleInfo      | 건축물대장 총괄표제부 조회   |
| getBrTitleInfo           | 건축물대장 표제부 조회       |
| getBrFlrOulnInfo         | 건축물대장 층별개요 조회     |
| getBrAtchJibunInfo       | 건축물대장 부속지번 조회     |
| getBrExposPubuseAreaInfo | 건축물대장 전유공용면적 조회 |
| getBrWclfInfo            | 건축물대장 오수정화시설 조회 |
| getBrHsprcInfo           | 건축물대장 주택가격 조회     |
| getBrExposInfo           | 건축물대장 전유부 조회       |
| getBrJijiguInfo          | 건축물대장 지역지구구역 조회 |


### 3) 소상공인 상가업소 정보 조회 서비스

| **메서드**           | **서비스 명**              |
| -------------------- | -------------------------- |
| storeZoneOne         | 지정 상권조회              |
| storeZoneInRadius    | 반경내 상권조회            |
| storeZoneInRectangle | 사각형내 상권조회          |
| storeZoneInAdmi      | 행정구역 단위 상권조회     |
| storeOne             | 단일 상가업소 조회         |
| storeListInBuilding  | 건물단위 상가업소 조회     |
| storeListInPnu       | 지번단위 상가업소 조회     |
| storeListInDong      | 행정동 단위 상가업소 조회  |
| storeListInArea      | 상권내 상가업소 조회       |
| storeListInRadius    | 반경내 상가업소 조회       |
| storeListInRectangle | 사각형내 상가업소 조회     |
| storeListInPolygon   | 다각형내 상가업소 조회     |
| storeListInUpjong    | 업종별 상가업소 조회       |
| storeListByDate      | 수정일자기준 상가업소 조회 |
| reqStoreModify       | 상가업소정보 변경요청      |
| largeUpjongList      | 상권정보 업종 대분류 조회  |
| middleUpjongList     | 상권정보 업종 중분류 조회  |
| smallUpjongList      | 상권정보 업종 소분류 조회  |


## 서울 열린데이터 광장 서비스 목록

### 1) 서울시 교통 관련 정보 조회 서비스

| **메서드**         | **서비스 명**                                        |
| ------------------ | ---------------------------------------------------- |
| CardSubwayStatsNew | 서울시 지하철호선별 역별 승하차 인원 정보            |
| CardBusTimeNew     | 서울시 버스노선별 정류장별 시간대별 승하차 인원 정보 |


## 설치 방법

```bash
pip install PublicDataReader
```

## 사용 방법
### (예시1) 국토교통부 실거래가 정보 조회 서비스

```python
# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
print(pdr.__version__)

# 2. 공공 데이터 포털 Open API 서비스 인증키 입력하기
serviceKey = "공공 데이터 포털에서 발급받은 서비스 키"

# 3. 국토교통부(molit) 실거래가 정보 조회 Open API 인스턴스 생성하기
molit = pdr.Transaction(serviceKey)

# 4. 지역코드 검색하기
codeResult = molit.CodeFinder("분당구")                            # 지역코드 : 41135
codeResult.head()


# 5. 지역, 월 별 데이터 프레임 만들기
# Function(지역코드(5자리), 계약월(YYYYMM))
# (예시) '2020년 12월', '분당구'에 해당하는 자료를 Pandas DataFrame으로 반환

df_AptTrade = molit.AptTrade(41135, 202012)             # 아파트매매 실거래자료 조회
df_AptTradeDetail = molit.AptTradeDetail(41135, 202012) # 아파트매매 실거래 상세 자료 조회
df_AptRent = molit.AptRent(41135, 202012)               # 아파트 전월세 자료 조회
df_AptOwnership = molit.AptOwnership(41135, 202012)     # 아파트 분양권전매 신고 자료 조회

df_OffiTrade = molit.OffiTrade(41135, 202012)           # 오피스텔 매매 신고 조회
df_OffiRent = molit.OffiRent(41135, 202012)             # 오피스텔 전월세 신고 조회
df_RHTrade = molit.RHTrade(41135, 202012)               # 연립다세대 매매 실거래자료 조회
df_RHRent = molit.RHRent(41135, 202012)                 # 연립다세대 전월세 실거래자료 조회

df_DHTrade = molit.DHTrade(41135, 202012)               # 단독/다가구 매매 실거래 조회
df_DHRent = molit.DHRent(41135, 202012)                 # 단독/다가구 전월세 자료 조회
df_LandTrade = molit.LandTrade(41135, 202012)           # 토지 매매 신고 조회
df_BizTrade = molit.BizTrade(41135, 202012)             # 상업업무용 부동산 매매 신고 자료 조회


# 6. 지역, 기간 별 데이터 프레임 만들기
# Function(API서비스 메서드, 지역코드(5자리), 시작월(YYYYMM), 종료월(YYYYMM))
df_AptTradeSum = molit.DataCollector(molit.AptTrade, 41135, 202001, 202012)
df_AptTradeDetailSum = molit.DataCollector(molit.AptTradeDetail, 41135, 202001, 202012)
df_AptRentSum = molit.DataCollector(molit.AptRent, 41135, 202001, 202012)
df_AptOwnershipSum = molit.DataCollector(molit.AptOwnership, 41135, 202001, 202012)

df_OffiTradeSum = molit.DataCollector(molit.OffiTrade, 41135, 202001, 202012)
df_OffiRentSum = molit.DataCollector(molit.OffiRent, 41135, 202001, 202012)
df_RHTradeSum = molit.DataCollector(molit.RHTrade, 41135, 202001, 202012)
df_RHRentSum = molit.DataCollector(molit.RHRent, 41135, 202001, 202012)

df_DHTradeSum = molit.DataCollector(molit.DHTrade, 41135, 202001, 202012)
df_DHRentSum = molit.DataCollector(molit.DHRent, 41135, 202001, 202012)
df_LandTradeSum = molit.DataCollector(molit.LandTrade, 41135, 202001, 202012)
df_BizTradeSum = molit.DataCollector(molit.BizTrade, 41135, 202001, 202012)

```

### (예시2) 소상공인 상가업소 정보 조회 서비스

```python
# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
print(pdr.__version__)

# 2. 공공 데이터 포털 Open API 서비스 인증키 입력하기
serviceKey = "공공 데이터 포털에서 발급받은 서비스 키"

# 3. 소상공인 상가업소 정보 조회 Open API 인스턴스 생성하기
semas = pdr.Transaction(serviceKey)

# 4. 데이터프레임으로 자료 조회하기

## 4-1 지정 상권조회
## 입력: 상권번호
key = 1
df = semas.storeZoneOne(key=key)

## 4-2 반경내 상권조회
## 입력: 반경(m), 중심점 경도(WGS84 좌표계), 중심점 위도(WGS84 좌표계)
radius = 500
cx = 127.03641615737838
cy = 37.50059843782878
df = semas.storeZoneInRadius(radius=radius, cx=cx, cy=cy)

## 4-3 사각형내 상권조회
## 입력: 서쪽 경도, 남쪽 위도, 동쪽 경도, 북쪽 위도 (WGS84 좌표계)
minx = 127.0327683531071
miny = 37.495967935149146
maxx = 127.04268179746694
maxy = 37.502402894207286
df = semas.storeZoneInRectangle(minx=minx, miny=miny, maxx=maxx, maxy=maxy)

## 4-4 행정구역 단위 상권조회
## 입력: 구분ID, 행정구역코드
## 구분ID - 시도(ctprvnCd), 시군구(signguCd), 행정동(adongCd)
## 행정구역코드 - 시도(시도코드값), 시군구(시군구코드값), 행정동(행정동코드값)
divId = 'adongCd'
key = '1168058000'
df = semas.storeZoneInAdmi(divId=divId, key=key)

## 4-5 단일 상가업소 조회
## 입력: 상가업소번호
key = '19911027'
df = semas.storeOne(key=key)

## 4-6. 건물단위 상가업소 조회
## 입력: 건물관리번호, 상권업종대분류코드, 상권업종중분류코드, 상권업종소분류코드, 페이지당 건수(최대 1000), 페이지 번호
key = '1168011000104940000004966'
pageNo = '1'
df = semas.storeListInBuilding(key=key, pageNo=1)

## 4-7. 지번단위 상가업소 조회
## 입력: PNU코드, 상권업종대분류코드, 상권업종중분류코드, 상권업종소분류코드, 페이지 번호
key = '1168010600209380024'
pageNo = '1'
indsLclsCd = 'Q'
indsMclsCd = 'Q12'
indsSclsCd = 'Q12A01' 
df = semas.storeListInPnu(key=key, indsLclsCd_=indsLclsCd, pageNo=1)

## 4-8. 행정동 단위 상가업소 조회
## 입력: 구분ID(시도:ctprvnCd, 시군구:signguCd, 행정동:adongCd), 행정구역코드, 상권업종대분류코드, 상권업종중분류코드, 상권업종소분류코드, 페이지 번호
divId = 'adongCd'
key = '1168064000'
indsLclsCd = 'Q'
pageNo = 1

df = semas.storeListInDong(divId = divId, key = key, indsLclsCd_=indsLclsCd, pageNo = pageNo)

## 4-9 상권내 상가업소 조회
## 입력: 상권번호, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
key = '1819'
pageNo = '1'
indsLclsCd = 'Q'

df = semas.storeListInArea(key=key, pageNo=pageNo, indsLclsCd_=indsLclsCd)

## 4-10. 반경내 상가업소 조회
## 입력: 반경, 중심점 경도, 중심점 위도, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
radius = '500'
cx = 127.03641615737838
cy = 37.50059843782878
indsLclsCd = 'Q'
pageNo = '1'

df = semas.storeListInRadius(radius=radius, cx=cx, cy=cy, indsLclsCd_=indsLclsCd, pageNo=pageNo)

## 4-11. 사각형내 상가업소 조회
## 입력: 서쪽 경도, 남쪽 위도, 동쪽 경도, 북쪽 위도, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
minx = 127.0327683531071
miny = 37.495967935149146
maxx = 127.04268179746694
maxy = 37.502402894207286
indsLclsCd = 'Q'
pageNo = 1

df = semas.storeListInRectangle(minx=minx, miny=miny, maxx=maxx, maxy=maxy, indsLclsCd_=indsLclsCd, pageNo=1)

## 4-12. 다각형내 상가업소 조회
## 입력: 다각형 좌표값, 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호
key = 'POLYGON((127.02355609555755 37.504264372557095, 127.02496157306963 37.50590702991155, 127.0270858825753 37.50486867039889, 127.02628121988377 37.503489842823114))'
pageNo = 1
indsLclsCd = 'Q'
df = semas.storeListInPolygon(key, indsLclsCd_=indsLclsCd, pageNo=pageNo)

## 4-13. 업종별 상가업소 조회
## 입력: 구분ID(대분류:indsLclsCd, 중분류:indsMclsCd, 소분류:indsSclsCd), 업종코드값, 페이지 번호
divId = 'indsLclsCd'
key = 'Q'
pageNo = 1

df = semas.storeListInUpjong(divId=divId, key=key, pageNo=pageNo)

## 4-14. 수정일자기준 상가업소 조회
## 입력: 일자(YYYYMMDD), 상권업종 대분류코드, 상권업종 중분류코드, 상권업종 소분류코드, 페이지 번호소분류코드, 페이지 번호
key = '20200101'
indsLclsCd = 'Q'
pageNo = '1'

df = semas.storeListByDate(key=key, pageNo=pageNo)

## 4-21. 상권정보 업종 대분류 조회
df = semas.largeUpjongList()

## 4-22. 상권정보 업종 중분류 조회
## 입력: 상권업종 업종 대분류코드
indsLclsCd = 'Q'

df = semas.middleUpjongList(indsLclsCd_=indsLclsCd)

## 4-23. 상권정보 업종 소분류 조회
## 입력: 상권정보 업종 대분류코드, 상권정보 업종 중분류코드
indsLclsCd = 'Q'
indsMclsCd = 'Q01'

df = semas.smallUpjongList(indsLclsCd_=indsLclsCd)
```