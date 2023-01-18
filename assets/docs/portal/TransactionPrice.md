# 국토교통부 부동산 실거래가 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.

## 국토교통부 실거래가 정보 조회 서비스

<div align="center">

| **서비스명**                          | **부동산 유형** | **거래 유형** |
| ------------------------------------- | ------------ | ------------ |
| [아파트매매 실거래 상세 자료 조회](https://www.data.go.kr/data/15057511/openapi.do)      | 아파트       | 매매         |
| [아파트 전월세 자료 조회](https://www.data.go.kr/data/15058017/openapi.do)               | 아파트       | 전월세       |
| [아파트 분양권전매 신고 자료 조회](https://www.data.go.kr/data/15056782/openapi.do)      | 분양입주권   | 매매         |
| [오피스텔 매매 신고 조회](https://www.data.go.kr/data/15058452/openapi.do)               | 오피스텔     | 매매         |
| [오피스텔 전월세 신고 조회](https://www.data.go.kr/data/15059249/openapi.do)             | 오피스텔     | 전월세       |
| [연립다세대 매매 실거래자료 조회](https://www.data.go.kr/data/15058038/openapi.do)       | 연립다세대   | 매매         |
| [연립다세대 전월세 실거래자료 조회](https://www.data.go.kr/data/15058016/openapi.do)     | 연립다세대   | 전월세       |
| [단독/다가구 매매 실거래 조회](https://www.data.go.kr/data/15058022/openapi.do)          | 단독다가구   | 매매         |
| [단독/다가구 전월세 자료 조회](https://www.data.go.kr/data/15058352/openapi.do)          | 단독다가구   | 전월세       |
| [토지 매매 신고 조회](https://www.data.go.kr/data/15056649/openapi.do)                   | 토지         | 매매         |
| [상업업무용 부동산 매매 신고 자료 조회](https://www.data.go.kr/data/15057267/openapi.do) | 상업업무용   | 매매         |
| [공장 및 창고 등 부동산 매매 신고 자료 조회](https://www.data.go.kr/data/15100574/openapi.do) | 공장창고등   | 매매         |

</div>

## 입력 명세

<div align="center">

| 이름             | 설명                                                                                                                               | 데이터 타입   | 샘플 데이터   | 항목구분    |
|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------|:--------------|:--------------|:------------|
| property_type    | 부동산 유형<br>(아파트, 오피스텔, 단독다가구, 연립다세대, 토지, 분양입주권, 공장창고등)                                            | String        | 아파트        | 필수        |
| trade_type       | 거래 유형<br>(매매, 전월세)                                                                                                        | String        | 매매          | 필수        |
| sigungu_code     | 시군구의 5자리 지역코드<br>(서울 서초구: 11650, 경기 성남 분당구: 41135)                                                           | String        | 11650         | 필수        |
| year_month       | 조회 년월 (단일 월 조회 시 필수)<br>(2023년 1월: 202301)<br>※ start_year_month와 end_year_month 모두 입력 시 기간 내 조회가 실행됨 | String        | 202301        | 조건부 필수 |
| start_year_month | 조회 시작 년월 (기간 내 조회 시 필수)<br>(2022년 1월 202201)                                                                       | String        | 202201        | 조건부 필수 |
| end_year_month   | 조회 종료 년월 (기간 내 조회 시 필수)<br>(2022년 12월: 202212)                                                                     | String        | 202212        | 조건부 필수 |
| verbose          | 데이터 조회 진행 상황 메시지 출력 여부<br>(출력: True, 미출력: False)<br>※ 기본값: False                                           | Boolean       | True          | 선택        |

</div>

<br>

```python
# 부동산 실거래가 조회 클래스 임포트하기
from PublicDataReader import TransactionPrice

# 공공 데이터 포털 오픈 API 서비스 인증키 입력하기
service_key = "공공 데이터 포털에서 발급받은 서비스 키"

# 국토교통부 실거래가 조회 API 인스턴스 정의하기
api = TransactionPrice(service_key)

# 특정 년월 자료만 조회하기
df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41135",
    year_month="202212",
    )

# 특정 기간 자료 조회하기
df = api.get_data(
    property_type="아파트",
    trade_type="매매",
    sigungu_code="41135",
    start_year_month="202212",
    end_year_month="202301",
    )
```