# 소상공인시장진흥공단 상가(상권)정보 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.


## 소상공인 상가업소 정보 조회 서비스

- [소상공인 상가업소 정보 조회 서비스 신청 페이지](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15012005)

<div align="center">

| **서비스 이름**               | **인자 이름** |
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

<br>


</div>

```python
# 상가업소 정보 조회 클래스 임포트하기
from PublicDataReader import SmallShop

# 공공 데이터 포털 오픈 API 서비스 인증키 입력하기
service_key = "공공 데이터 포털에서 발급받은 서비스 키"

# 데이터 조회 API 인스턴스 만들기
api = SmallShop(service_key)

# 서비스 별 데이터 조회하기

## 지정 상권조회
df = api.get_data(
    service_name = "지정상권",
    key = "9301",
)

## 반경내 상권조회
df = api.get_data(
    service_name = "반경상권",
    cx = 127.042325940821,
    cy = 37.5272105674053,
    radius = 500,
)

## 사각형내 상권조회
df = api.get_data(
    service_name = "사각형상권",
    minx = 127.0327683531071,
    miny = 37.495967935149146,
    maxx = 127.04268179746694,
    maxy = 37.502402894207286
)

## 행정구역 단위 상권조회
df = api.get_data(
    service_name = "행정구역상권",
    divId = 'adongCd',
    key = '1168058000'
)

## 단일 상가업소 조회
df = api.get_data(
    service_name = "단일상가",
    divId = 'adongCd',
    key = '11757465'
)

## 건물단위 상가업소 조회
df = api.get_data(
    service_name = "건물상가",
    key = '1168011000104940000004966'
)

## 지번단위 상가업소 조회
df = api.get_data(
    service_name = "지번상가",
    key = '1165010100108120002'
)

## 행정동 단위 상가업소 조회
df = api.get_data(
    service_name = "행정동상가",
    divId = 'adongCd',
    key = '1168064000',
    indsLclsCd = 'Q'
)

## 상권내 상가업소 조회
df = api.get_data(
    service_name = "상권상가",
    key = '9368',
    indsLclsCd = 'Q'
)

## 반경내 상가업소 조회
df = api.get_data(
    service_name = "반경상가",
    radius = '500',
    cx = 127.03641615737838,
    cy = 37.50059843782878,
    indsLclsCd = 'Q'
)

## 사각형내 상가업소 조회
df = api.get_data(
    service_name = "사각형상가",
    minx = 127.0327683531071,
    miny = 37.495967935149146,
    maxx = 127.04268179746694,
    maxy = 37.502402894207286,
    indsLclsCd = 'Q'
)

## 다각형내 상가업소 조회
df = api.get_data(
    service_name = "다각형상가",
    key = 'POLYGON((127.02355609555755 37.504264372557095, 127.02496157306963 37.50590702991155, 127.0270858825753 37.50486867039889, 127.02628121988377 37.503489842823114))',
    indsLclsCd = 'Q'
)

## 업종별 상가업소 조회
df = api.get_data(
    service_name = "업종별상가",
    divId = 'indsLclsCd',
    key = 'Q'
)

## 수정일자기준 상가업소 조회
df = api.get_data(
    service_name = "수정일자상가",
    key = '20200101',
    indsLclsCd = 'Q'
)

## 상권정보업종 대분류 조회
df = api.get_data(
    service_name = "업종대분류",
)

## 상권정보업종 중분류 조회
df = api.get_data(
    service_name = "업종중분류",
    indsLclsCd = 'Q'
)

## 상권정보업종 소분류 조회
df = api.get_data(
    service_name = "업종소분류",
    indsLclsCd = 'Q',
    indsMclsCd = 'Q01'
)
```