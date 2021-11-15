# PublicDataReader

![PNG](./img_logo.png)


## Open Source Project

- **Project Owner: 정우일(Wooil Jeong)**
- **e-mail: wooil@kakao.com**
- **사용 설명서**: 
  - [PublicDataReader - 부동산 데이터 수집하기](https://wooiljeong.github.io/python/public_data_reader_01/)
  - [PublicDataReader - 건축물대장 데이터 조회하기](https://wooiljeong.github.io/python/public_data_reader_03/)
  - [PublicDataReader - 상가업소 데이터 수집하기](https://wooiljeong.github.io/python/public_data_reader_02/)
- **[카카오톡 오픈채팅방 링크](https://open.kakao.com/o/gFYXtP2c)**
  - PublicDataReader 사용 관련 Q&A를 위한 오픈채팅방입니다.


## PublicDataReader

- **최신 버전**  
![](https://img.shields.io/badge/PublicDataReader-2021.11.-blue.svg)

- **의존성**  
![](https://img.shields.io/badge/Python-3.8.12-yellow.svg) ![](https://img.shields.io/badge/Pandas-1.3.4-red.svg) ![](https://img.shields.io/badge/beautifulsoup4-4.10.0-green.svg)

**PublicDataReader**는 [공공데이터포털](https://data.go.kr), [서울 열린데이터 광장](https://data.seoul.go.kr/) 등 기관에서 제공하고 있는 데이터 관련 OpenAPI 서비스를 Python으로 쉽게 이용할 수 있도록 도와주는 **데이터 수집 라이브러리**입니다. 

**2021년 11월** 현재 아래 OpenAPI 서비스 각각에 대해 데이터를 Pandas DataFrame 형태로 조회할 수 있습니다.

- [국토교통부 실거래가 정보](https://www.data.go.kr/dataset/3050988/openapi.do)
- [국토교통부 건축물대장정보 서비스](https://www.data.go.kr/data/15044713/openapi.do)
- [소상공인 상가업소 정보](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15012005)
- [서울시 지하철호선별 역별 승하차 인원 정보](https://data.seoul.go.kr/dataList/OA-12914/S/1/datasetView.do)
- [서울시 버스노선별 정류장별 시간대별 승하차 인원 정보](https://data.seoul.go.kr/dataList/OA-12913/S/1/datasetView.do)


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

| **서비스 명**                                        | **메서드**         |
| ---------------------------------------------------- | ------------------ |
| 서울시 지하철호선별 역별 승하차 인원 정보            | CardSubwayStatsNew |
| 서울시 버스노선별 정류장별 시간대별 승하차 인원 정보 | CardBusTimeNew     |


## Installation

```bash
pip install --upgrade PublicDataReader
```


## Quick Start

### (예시1) 국토교통부 실거래가 정보 조회 서비스

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
prod="아파트"
trans="매매"
sigunguCode="41135"
yearMonth="202101"

df = ts.read_data(prod, trans, sigunguCode, yearMonth)


# 6. 지역, 기간 별 데이터 프레임 만들기
prod="아파트"
trans="매매"
sigunguCode="41135"
startYearMonth="202101"
endYearMonth="202111"

df = ts.collect_data(prod, trans, sigunguCode, startYearMonth, endYearMonth)
```


### (예시2) 국토교통부 건축물대장정보 서비스

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
category = "기본개요"                                   # 건축물대장 종류
sigunguCd = "41135"                                     # 시군구코드(5)
bjdongCd = "11000"                                      # 읍면동코드(5)
bun = "0541"                                            # 본번(4)
ji = "0000"                                             # 부번(4)

df = bd.read_data(category=category, sigunguCd=sigunguCd, bjdongCd=bjdongCd, bun=bun, ji=ji)
```


### (예시3) 소상공인 상가업소 정보 조회 서비스

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
