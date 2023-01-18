# 국세청 사업자등록정보 진위확인 및 상태조회 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.

## 국세청 사업자등록정보 진위확인 및 상태조회 서비스

- [국세청 사업자등록정보 진위확인 및 상태조회 서비스 신청 페이지](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15081808)

- 사업자등록정보 진위확인 서비스

```python
import PublicDataReader as pdr
print(pdr.__version__)

# 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
serviceKey = "공공 데이터 포털에서 발급받은 서비스 키"

# OpenAPI 인스턴스 생성
API = pdr.Nts(serviceKey)

# 조회 대상 목록
businesses = [{
  'b_no': '0000000000',
  'start_dt': '20000101',
  'p_nm': '홍길동',
  'p_nm2': '',
  'b_nm': '',
  'corp_no': '',
  'b_sector': '',
  'b_type': ''},
 {'b_no': '1111111111',
  'start_dt': '20100101',
  'p_nm': '홍길동',
  'p_nm2': '',
  'b_nm': '',
  'corp_no': '',
  'b_sector': '',
  'b_type': ''},
 {'b_no': '2222222222',
  'start_dt': '20200101',
  'p_nm': '홍길동',
  'p_nm2': '',
  'b_nm': '',
  'corp_no': '',
  'b_sector': '',
  'b_type': ''
}]

# 진위확인
df = API.validate(businesses)
```

- 사업자등록정보 상태조회 서비스

```python
import PublicDataReader as pdr
print(pdr.__version__)

# 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
serviceKey = "공공 데이터 포털에서 발급받은 서비스 키"

# OpenAPI 인스턴스 생성
API = pdr.Nts(serviceKey)

# 조회 대상 목록 (사업자등록번호 리스트)
b_no = ['0000000000', '1111111111']

# 상태조회
df = API.status(b_no)
```
