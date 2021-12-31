# PublicDataReader

![](https://img.shields.io/badge/pandas-1.3.4-red.svg)
![](https://img.shields.io/badge/requests-2.26.0-blue.svg)
![](https://img.shields.io/badge/beautifulsoup4-4.10.0-yellow.svg)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FWooilJeong%2FPublicDataReader&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23FFFFFF&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Linkedin Badge](https://img.shields.io/badge/-WooilJeong-blue?style=plastic&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wooil/)](https://www.linkedin.com/in/wooil/) 

![PNG](./img_logo.png)

**PublicDataReader**는 [공공데이터포털](https://data.go.kr), [서울 열린데이터 광장](https://data.seoul.go.kr/) 등 기관에서 제공하고 있는 데이터 관련 OpenAPI 서비스를 Python으로 쉽게 이용할 수 있도록 도와주는 **데이터 조회 라이브러리**입니다. 

- **Project Owner: 정우일**  
- **E-mail: wooil@kakao.com**  
- **라이브러리 사용 설명서**  
  - [PublicDataReader - 부동산 실거래가 조회하기](https://wooiljeong.github.io/python/public_data_reader_01/)
  - [PublicDataReader - 건축물대장 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_03/)
  - [PublicDataReader - 상가업소 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_02/)
- **[카카오톡 오픈채팅방 링크](https://open.kakao.com/o/gFYXtP2c)**  
  - PublicDataReader 사용 관련 Q&A를 위한 오픈채팅방입니다.


**2021년 11월** 현재 아래 OpenAPI 서비스 각각에 대해 데이터를 Pandas DataFrame 형태로 조회할 수 있습니다. 본 라이브러리를 정상적으로 이용하기 위해서는 아래 서비스에 대한 OpenAPI 활용신청을 반드시 완료해야합니다.

- [국토교통부 실거래가 정보](https://www.data.go.kr/dataset/3050988/openapi.do)
- [국토교통부 건축물대장정보 서비스](https://www.data.go.kr/data/15044713/openapi.do)
- [소상공인 상가업소 정보](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15012005)
- [서울시 지하철호선별 역별 승하차 인원 정보](http://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do)
- [서울시 버스노선별 정류장별 승하차 인원 정보](http://data.seoul.go.kr/dataList/OA-12912/S/1/datasetView.do)


## 공공 데이터 포털 서비스 목록

### 1) 국토교통부 실거래가 정보 조회 서비스

| **서비스명**                          | **상품유형** | **거래유형** |
| ------------------------------------- | ------------ | ------------ |
| 아파트매매 실거래 상세 자료 조회      | 아파트       | 매매         |
| 아파트 전월세 자료 조회               | 아파트       | 전월세       |
| 아파트 분양권전매 신고 자료 조회      | 분양입주권   | 매매         |
| 오피스텔 매매 신고 조회               | 오피스텔     | 매매         |
| 오피스텔 전월세 신고 조회             | 오피스텔     | 전월세       |
| 연립다세대 매매 실거래자료 조회       | 연립다세대   | 매매         |
| 연립다세대 전월세 실거래자료 조회     | 연립다세대   | 전월세       |
| 단독/다가구 매매 실거래 조회          | 단독다가구   | 매매         |
| 단독/다가구 전월세 자료 조회          | 단독다가구   | 전월세       |
| 토지 매매 신고 조회                   | 토지         | 매매         |
| 상업업무용 부동산 매매 신고 자료 조회 | 상업업무용   | 매매         |


### 2) 국토교통부 건축물대장정보 서비스

| **서비스명**                 | **카테고리명** |
| ---------------------------- | -------------- |
| 건축물대장 기본개요 조회     | 기본개요       |
| 건축물대장 총괄표제부 조회   | 총괄표제부     |
| 건축물대장 표제부 조회       | 표제부         |
| 건축물대장 층별개요 조회     | 층별개요       |
| 건축물대장 부속지번 조회     | 부속지번       |
| 건축물대장 전유공용면적 조회 | 전유공용면적   |
| 건축물대장 오수정화시설 조회 | 오수정화시설   |
| 건축물대장 주택가격 조회     | 주택가격       |
| 건축물대장 전유부 조회       | 전유부         |
| 건축물대장 지역지구구역 조회 | 지역지구구역   |


### 3) 소상공인 상가업소 정보 조회 서비스

| **서비스명**               | **카테고리명** |
| -------------------------- | -------------- |
| 지정 상권조회              | 지정상권       |
| 반경내 상권조회            | 반경상권       |
| 사각형내 상권조회          | 사각형상권     |
| 행정구역 단위 상권조회     | 행정구역상권   |
| 단일 상가업소 조회         | 단일상가       |
| 건물단위 상가업소 조회     | 건물상가       |
| 지번단위 상가업소 조회     | 지번상가       |
| 행정동 단위 상가업소 조회  | 행정동상가     |
| 상권내 상가업소 조회       | 상권상가       |
| 반경내 상가업소 조회       | 반경상가       |
| 사각형내 상가업소 조회     | 사각형상가     |
| 다각형내 상가업소 조회     | 다각형상가     |
| 업종별 상가업소 조회       | 업종별상가     |
| 수정일자기준 상가업소 조회 | 수정일자상가   |
| 상권정보 업종 대분류 조회  | 업종대분류     |
| 상권정보 업종 중분류 조회  | 업종중분류     |
| 상권정보 업종 소분류 조회  | 업종소분류     |


## 서울 열린데이터 광장 서비스 목록

### 1) 서울시 교통 관련 정보 조회 서비스

| **서비스명**                                        | **카테고리명**     |
| ---------------------------------------------------- | ------------------ |
| 서울시 지하철호선별 역별 승하차 인원 정보            | 지하철승하차       |
| 서울시 버스노선별 정류장별 승하차 인원 정보          | 버스승하차         |


## Installation

```bash
pip install --upgrade PublicDataReader
```


## Dependency

```bash
pip install pandas==1.3.4
pip install requests==2.26.0
pip install beautifulsoup4==4.10.0
```


## Quick Start

### 국토교통부 실거래가 정보 조회 서비스

```python
# 1. 라이브러리 임포트하기
import PublicDataReader as pdr
print(pdr.__version__)
print(pdr.__info__)

# 2. 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
serviceKey = "공공 데이터 포털에서 발급받은 서비스 키"

# 3. 국토교통부 실거래가 정보 조회 OpenAPI 세션 정의하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
ts = pdr.Transaction(serviceKey, debug=True)

# 4. 지역코드(시군구코드) 검색하기
sigunguName = "분당구"                                  # 시군구코드: 41135
code = pdr.code_list()
code.loc[(code['시군구명'].str.contains(sigunguName, na=False)) &
         (code['읍면동명'].isna())]

# 5. 지역, 월 별 데이터 프레임 만들기
prod="아파트"                                           # 부동산 상품 종류 (ex. 아파트, 오피스텔, 단독다가구 등)
trans="매매"                                            # 부동산 거래 유형 (ex. 매매, 전월세)
sigunguCode="41135"
yearMonth="202101"

df = ts.read_data(prod, trans, sigunguCode, yearMonth)


# 6. 지역, 기간 별 데이터 프레임 만들기
prod="아파트"                                           # 부동산 상품 종류 (ex. 아파트, 오피스텔, 단독다가구 등)
trans="매매"                                            # 부동산 거래 유형 (ex. 매매, 전월세)
sigunguCode="41135"
startYearMonth="202101"
endYearMonth="202111"

df = ts.collect_data(prod, trans, sigunguCode, startYearMonth, endYearMonth)
```


### 국토교통부 건축물대장정보 서비스

```python
# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
print(pdr.__version__)
print(pdr.__info__)

# 2. 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
serviceKey = "공공 데이터 포털에서 발급받은 서비스 키"

# 3. 국토교통부 건축물대장정보 서비스 OpenAPI 세션 정의하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
bd = pdr.Building(serviceKey, debug=True)

# 4. 지역코드(시군구코드) 검색하기
sigunguName = "분당구"                                  # 시군구코드: 41135
code = pdr.code_list()
code.loc[(code['시군구명'].str.contains(sigunguName, na=False)) &
         (code['읍면동명'].isna())]

# 5. 건축물대장정보 오퍼레이션별 데이터 조회
category = "기본개요"                                   # 건축물대장 종류 (ex. 표제부, 총괄표제부, 전유부 등)
sigunguCd = "41135"                                     # 시군구코드(5)
bjdongCd = "11000"                                      # 읍면동코드(5)
bun = "0541"                                            # 본번(4)
ji = "0000"                                             # 부번(4)

df = bd.read_data(category=category, sigunguCd=sigunguCd, bjdongCd=bjdongCd, bun=bun, ji=ji)
```


### 소상공인 상가업소 정보 조회 서비스

```python
# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
print(pdr.__version__)
print(pdr.__info__)

# 2. 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
serviceKey = "공공 데이터 포털에서 발급받은 서비스 키"

# 3. 소상공인 상가업소 정보 조회 OpenAPI 인스턴스 생성하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
si = pdr.StoreInfo(serviceKey, debug=True)

# 4. 데이터프레임으로 자료 조회하기

# 4-1. 지정상권
category = "지정상권"

key = "9174"

df = si.read_data(category=category, key=key)

# 4-2. 반경상권
category = "반경상권"

radius = 500
cx = 127.03641615737838
cy = 37.50059843782878

df = si.read_data(category=category, radius=radius, cx=cx, cy=cy)

# 4-3. 사각형상권
category = "사각형상권"

minx = 127.0327683531071
miny = 37.495967935149146
maxx = 127.04268179746694
maxy = 37.502402894207286

df = si.read_data(category=category, minx=minx, miny=miny, maxx=maxx, maxy=maxy)

# 4-4. 행정구역상권
category = "행정구역상권"

divId = 'adongCd'
key = '1168058000'

df = si.read_data(category=category,divId=divId, key=key)

# 4-5. 단일상가
category = "단일상가"

key = '11757465'

df = si.read_data(category=category, key=key)

# 4-6. 건물상가
category = "건물상가"

key = '1168011000104940000004966'

df = si.read_data(category=category, key=key)

# 4-7. 지번상가
category = "지번상가"

key = '1165010100108120002'
indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)

# 4-8. 행정동상가
category = "행정동상가"

divId = 'adongCd'
key = '1168064000'
indsLclsCd = 'Q'

df = si.read_data(category=category, divId=divId, key=key, indsLclsCd=indsLclsCd)

# 4-9. 상권상가
category = "상권상가"

key = '9368'
indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)

# 4-10. 반경상가
category = "반경상가"

radius = '500'
cx = 127.03641615737838
cy = 37.50059843782878
indsLclsCd = 'Q'

df = si.read_data(category=category, radius=radius, cx=cx, cy=cy, indsLclsCd=indsLclsCd)

# 4-11. 사각형상가
category = "사각형상가"

minx = 127.0327683531071
miny = 37.495967935149146
maxx = 127.04268179746694
maxy = 37.502402894207286
indsLclsCd = 'Q'

df = si.read_data(category=category, minx=minx, miny=miny, maxx=maxx, maxy=maxy, indsLclsCd=indsLclsCd)

# 4-12. 다각형상가
category = "다각형상가"

key = 'POLYGON((127.02355609555755 37.504264372557095, 127.02496157306963 37.50590702991155, 127.0270858825753 37.50486867039889, 127.02628121988377 37.503489842823114))'
indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)

# 4-13. 업종별상가
category = "업종별상가"

divId = 'indsLclsCd'
key = 'Q'

df = si.read_data(category=category, divId=divId, key=key)

# 4-14. 수정일자상가
category = "수정일자상가"

key = '20200101'
indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)

# 4-15. 업종대분류
category = "업종대분류"

df = si.read_data(category=category, key=key)

# 4-16. 업종중분류
category = "업종중분류"

indsLclsCd = 'Q'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd)

# 4-17. 업종소분류
category = "업종소분류"

indsLclsCd = 'Q'
indsMclsCd = 'Q01'

df = si.read_data(category=category, key=key, indsLclsCd=indsLclsCd, indsMclsCd=indsMclsCd)

```


### 서울 열린데이터 광장 교통 관련 정보 조회 서비스

```python
# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
print(pdr.__version__)
print(pdr.__info__)

# 2. 서울 열린데이터 광장 OpenAPI 서비스 인증키 입력하기
serviceKey = "서울 열린데이터 광장에서 발급받은 서비스 키"

# 3. 국토교통부 건축물대장정보 서비스 OpenAPI 세션 정의하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
tp = pdr.Transportation(serviceKey, debug=True)

# 4. 서울시 지하철호선별 역별 승하차 인원 정보
category = "지하철승하차"
date = "20211001"

df = tp.read_data(category=category, date=date)

# 5. 서울시 버스노선별 정류장별 승하차 인원 정보
category = "버스승하차"
date = "20211001"

df = tp.read_data(category=category, date=date)
```