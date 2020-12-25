# PublicDataReader

![PNG](./img_logo.png)


## Open Source Project

- **Project Owner: 정우일(Wooil Jeong)**
- **e-mail: wooil@kakao.com**
- **사용 설명서: [PublicDataReader - 부동산 데이터 수집하기](https://wooiljeong.github.io/python/public_data_reader_01/)**
- **코랩 실습 코드: [Colab](https://colab.research.google.com/drive/1pFtMFr_te9T_maHjee8Sd8Yq9rTrE-4F)**

## 소개

- **최신 버전**  
![](https://img.shields.io/badge/PublicDataReader-0.1.2-blue.svg)  

    - v0.1.2 (2020-12): 국토교통부 실거래가 조회 인터페이스 전면 수정


- **요구 사항**  
![](https://img.shields.io/badge/Python-3.7.4-yellow.svg) ![](https://img.shields.io/badge/Pandas-0.25.3-red.svg)

**PublicDataReader**는 [공공데이터포털](https://data.go.kr)에서 제공하는 OpenAPI 서비스를 Python으로 쉽게 이용할 수 있도록 도와주는 **데이터 수집 라이브러리**입니다. 2020년 12월 현재 [국토교통부 실거래가 정보](https://www.data.go.kr/dataset/3050988/openapi.do) 조회 서비스에 대한 인터페이스를 제공하고 있습니다. 추후 수요가 높은 Open API 서비스에 대한 인터페이스도 지속적으로 업데이트할 예정입니다.

## 사용 가능한 서비스

**메서드**              | **서비스 명**
---------------------- | --------------------
CondeFinder | 지역코드 조회
DataCollector | 서비스/기간 별 데이터 조회
AptTrade | 아파트매매 실거래자료 조회
AptTradeDetail | 아파트매매 실거래 상세 자료 조회
AptRent | 아파트 전월세 자료 조회
AptOwnership | 아파트 분양권전매 신고 자료 조회
OffiTrade | 오피스텔 매매 신고 조회
OffiRent | 오피스텔 전월세 신고 조회
RHTrade | 연립다세대 매매 실거래자료 조회
RHRent | 연립다세대 전월세 실거래자료 조회
DHTrade | 단독/다가구 매매 실거래 조회
DHRent | 단독/다가구 전월세 자료 조회
LandTrade | 토지 매매 신고 조회
BizTrade | 상업업무용 부동산 매매 신고 자료 조회



## 설치 방법

```bash
pip install PublicDataReader==0.1.2
```

## 사용 방법
### (예시) 국토교통부 실거래가 정보 조회 서비스

```python
# 1. 라이브러리 임포트 및 버전 확인하기
import PublicDataReader as pdr
print(pdr.__version__)

# 2. 공공 데이터 포털 Open API 서비스 인증키 입력하기
serviceKey = "공공 데이터 포털에서 발급받은 서비스 키"

# 3. 국토교통부(molit) 실거래가 Open API 인스턴스 생성
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
