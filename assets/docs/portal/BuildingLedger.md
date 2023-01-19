# 국토교통부 건축물대장정보 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.


## 국토교통부 건축물대장정보 서비스

- [건축물대장정보 서비스 신청 페이지](https://www.data.go.kr/data/15044713/openapi.do)

<div align="center">

| **서비스명**                 | **대장 유형** |
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

</div>

## 서비스 목록

* [건축물대장 기본개요 조회 서비스](#건축물대장-기본개요-조회-서비스)
* [건축물대장 총괄표제부 조회 서비스](#건축물대장-총괄표제부-조회-서비스)
* [건축물대장 표제부 조회 서비스](#건축물대장-표제부-조회-서비스)
* [건축물대장 층별개요 조회 서비스](#건축물대장-층별개요-조회-서비스)
* [건축물대장 부속지번 조회 서비스](#건축물대장-부속지번-조회-서비스)
* [건축물대장 전유공용면적 조회 서비스](#건축물대장-전유공용면적-조회-서비스)
* [건축물대장 오수정화시설 조회 서비스](#건축물대장-오수정화시설-조회-서비스)
* [건축물대장 주택가격 조회 서비스](#건축물대장-주택가격-조회-서비스)
* [건축물대장 전유부 조회 서비스](#건축물대장-전유부-조회-서비스)
* [건축물대장 지역지구구역 조회 서비스](#건축물대장-지역지구구역-조회-서비스)


## 입력 명세

<div align="center">

| 이름         | 설명                                                                                                                              | 데이터 타입   | 샘플 데이터   | 항목구분   |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------|:--------------|:-----------|
| ledger_type  | 건축물대장 유형<br>(기본개요, 총괄표제부, 표제부, 층별개요, 부속지번, 전유공용면적, 오수정화시설, 주택가격, 전유부, 지역지구구역) | String        | 총괄표제부    | 필수       |
| sigungu_code | 시군구의 5자리 지역코드<br>(서울 서초구: 11650, 경기 성남 분당구: 41135)                                                          | String        | 41135         | 필수       |
| bdong_code   | 읍면동의 5자리 지역코드<br>(서울 서초구 잠원동: 10600, 경기 성남 분당구 백현동: 11000)                                            | String        | 11000         | 필수       |
| bun          | 주소 번지의 본번<br>(350번지: 350)                                                                                                | String        | 540           | 선택       |
| ji           | 주소 번지의 부번<br>(350-20번지: 20)                                                                                              | String        | nan           | 선택       |
| translate    | 컬럼명 한글 표시 여부<br>(한글 표시: True, 영문 표시: False)<br>※ 기본값: True                                                    | Boolean       | True          | 선택       |
| verbose      | 데이터 조회 진행 상황 메시지 출력 여부<br>(출력: True, 미출력: False)<br>※ 기본값: False                                          | Boolean       | False         | 선택       |
| wait_time    | API 추가 요청 시 대기 시간(초)<br>(30초: 30)<br>※ 기본값: 30                                                                      | Integer       | 30            | 선택       |

</div>

<br>

## 건축물대장 기본개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="기본개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```


<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>법정동코드</th>
      <th>건물명</th>
      <th>블록</th>
      <th>번</th>
      <th>외필지수</th>
      <th>생성일자</th>
      <th>구역코드</th>
      <th>구역코드명</th>
      <th>지</th>
      <th>지구코드</th>
      <th>...</th>
      <th>도로명대지위치</th>
      <th>대지구분코드</th>
      <th>대지위치</th>
      <th>대장구분코드</th>
      <th>대장구분코드명</th>
      <th>대장종류코드</th>
      <th>대장종류코드명</th>
      <th>순번</th>
      <th>시군구코드</th>
      <th>특수지명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>None</td>
      <td>None</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>1</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>None</td>
      <td>None</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>2</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>None</td>
      <td>None</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>3</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>None</td>
      <td>None</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>4</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>None</td>
      <td>None</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>5</td>
      <td>41135</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 31 columns</p>
</div>


## 건축물대장 총괄표제부 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>


```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="총괄표제부", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>건축면적</th>
      <th>부속건축물면적</th>
      <th>부속건축물수</th>
      <th>건폐율</th>
      <th>법정동코드</th>
      <th>건물명</th>
      <th>블록</th>
      <th>번</th>
      <th>외필지수</th>
      <th>생성일자</th>
      <th>...</th>
      <th>대장종류코드명</th>
      <th>순번</th>
      <th>시군구코드</th>
      <th>특수지명</th>
      <th>착공일</th>
      <th>연면적</th>
      <th>총주차수</th>
      <th>사용승인일</th>
      <th>용적률</th>
      <th>용적률산정연면적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10799.671</td>
      <td>72376.6521</td>
      <td>4</td>
      <td>16.39</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20190923</td>
      <td>...</td>
      <td>총괄표제부</td>
      <td>1</td>
      <td>41135</td>
      <td>None</td>
      <td>20081216</td>
      <td>204741.1485</td>
      <td>1718</td>
      <td>20110728</td>
      <td>199.82</td>
      <td>131671.3169</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 65 columns</p>
</div>


## 건축물대장 표제부 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>


```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="표제부", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>건축면적</th>
      <th>부속건축물면적</th>
      <th>부속건축물수</th>
      <th>건폐율</th>
      <th>법정동코드</th>
      <th>건물명</th>
      <th>블록</th>
      <th>번</th>
      <th>외필지수</th>
      <th>생성일자</th>
      <th>...</th>
      <th>특수지명</th>
      <th>착공일</th>
      <th>구조코드</th>
      <th>구조코드명</th>
      <th>연면적</th>
      <th>총동연면적</th>
      <th>지하층수</th>
      <th>사용승인일</th>
      <th>용적률</th>
      <th>용적률산정연면적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>712.3212</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20190817</td>
      <td>...</td>
      <td>None</td>
      <td>20081216</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>12458.5902</td>
      <td>12458.5902</td>
      <td>0</td>
      <td>20110728</td>
      <td>0</td>
      <td>12458.5902</td>
    </tr>
    <tr>
      <th>1</th>
      <td>717.7751</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20200427</td>
      <td>...</td>
      <td>None</td>
      <td>20081216</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>9932.9434</td>
      <td>9932.9434</td>
      <td>0</td>
      <td>20110728</td>
      <td>0</td>
      <td>9932.9434</td>
    </tr>
    <tr>
      <th>2</th>
      <td>508.9298</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20200427</td>
      <td>...</td>
      <td>None</td>
      <td>20081216</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>3281.7024</td>
      <td>3281.7024</td>
      <td>0</td>
      <td>20110728</td>
      <td>0</td>
      <td>3281.7024</td>
    </tr>
    <tr>
      <th>3</th>
      <td>508.9298</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20200427</td>
      <td>...</td>
      <td>None</td>
      <td>20081216</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>3281.7024</td>
      <td>3281.7024</td>
      <td>0</td>
      <td>20110728</td>
      <td>0</td>
      <td>3281.7024</td>
    </tr>
    <tr>
      <th>4</th>
      <td>692.5447</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20200427</td>
      <td>...</td>
      <td>None</td>
      <td>20081216</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>10958.5232</td>
      <td>10958.5232</td>
      <td>0</td>
      <td>20110728</td>
      <td>0</td>
      <td>10958.5232</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 78 columns</p>
</div>


## 건축물대장 층별개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="층별개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>면적</th>
      <th>면적제외여부</th>
      <th>법정동코드</th>
      <th>건물명</th>
      <th>블록</th>
      <th>번</th>
      <th>생성일자</th>
      <th>동명칭</th>
      <th>기타용도</th>
      <th>기타구조</th>
      <th>...</th>
      <th>새주소부번</th>
      <th>새주소지상지하코드</th>
      <th>도로명대지위치</th>
      <th>대지구분코드</th>
      <th>대지위치</th>
      <th>순번</th>
      <th>시군구코드</th>
      <th>특수지명</th>
      <th>구조코드</th>
      <th>구조코드명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>497.7202</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20190817</td>
      <td>109동</td>
      <td>아파트</td>
      <td>철근콘크리트구조</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>1</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
    <tr>
      <th>1</th>
      <td>497.7202</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20190817</td>
      <td>109동</td>
      <td>아파트</td>
      <td>철근콘크리트구조</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
    <tr>
      <th>2</th>
      <td>513.3054</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20190817</td>
      <td>109동</td>
      <td>아파트</td>
      <td>철근콘크리트구조</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>3</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
    <tr>
      <th>3</th>
      <td>497.7202</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20190817</td>
      <td>109동</td>
      <td>아파트</td>
      <td>철근콘크리트구조</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>4</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
    <tr>
      <th>4</th>
      <td>497.7202</td>
      <td>0</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20190817</td>
      <td>109동</td>
      <td>아파트</td>
      <td>철근콘크리트구조</td>
      <td>...</td>
      <td>0.0</td>
      <td>0</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>5</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 34 columns</p>
</div>


## 건축물대장 부속지번 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="부속지번", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>atchBjdongCd</th>
      <th>atchBlock</th>
      <th>atchBun</th>
      <th>atchEtcJibunNm</th>
      <th>atchJi</th>
      <th>atchLot</th>
      <th>atchPlatGbCd</th>
      <th>atchRegstrGbCd</th>
      <th>atchRegstrGbCdNm</th>
      <th>atchSigunguCd</th>
      <th>...</th>
      <th>newPlatPlc</th>
      <th>platGbCd</th>
      <th>platPlc</th>
      <th>regstrGbCd</th>
      <th>regstrGbCdNm</th>
      <th>regstrKindCd</th>
      <th>regstrKindCdNm</th>
      <th>rnum</th>
      <th>sigunguCd</th>
      <th>splotNm</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
<p>0 rows × 34 columns</p>
</div>


## 건축물대장 전유공용면적 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="전유공용면적", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>면적</th>
      <th>법정동코드</th>
      <th>건물명</th>
      <th>블록</th>
      <th>번</th>
      <th>생성일자</th>
      <th>동명칭</th>
      <th>기타용도</th>
      <th>기타구조</th>
      <th>전유공용구분코드</th>
      <th>...</th>
      <th>대지위치</th>
      <th>대장구분코드</th>
      <th>대장구분코드명</th>
      <th>대장종류코드</th>
      <th>대장종류코드명</th>
      <th>순번</th>
      <th>시군구코드</th>
      <th>특수지명</th>
      <th>구조코드</th>
      <th>구조코드명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>117.5193</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20181001</td>
      <td>102동</td>
      <td>아파트</td>
      <td>철근콘크리트구조</td>
      <td>1</td>
      <td>...</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>1</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.1181</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20181001</td>
      <td>102동</td>
      <td>벽체</td>
      <td>철근콘크리트구조</td>
      <td>2</td>
      <td>...</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>2</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18.9066</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20181001</td>
      <td>102동</td>
      <td>계단실</td>
      <td>철근콘크리트구조</td>
      <td>2</td>
      <td>...</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>3</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0634</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20181001</td>
      <td>102동</td>
      <td>지하층 계단실</td>
      <td>철근콘크리트구조</td>
      <td>2</td>
      <td>...</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>4</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
    <tr>
      <th>4</th>
      <td>75.9549</td>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20181001</td>
      <td>102동</td>
      <td>지하주차장(지3~1층)</td>
      <td>철근콘크리트구조</td>
      <td>2</td>
      <td>...</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>5</td>
      <td>41135</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 40 columns</p>
</div>


## 건축물대장 오수정화시설 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="오수정화시설", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>법정동코드</th>
      <th>건물명</th>
      <th>블록</th>
      <th>번</th>
      <th>용량(루베)</th>
      <th>용량(인용)</th>
      <th>생성일자</th>
      <th>기타형식</th>
      <th>지</th>
      <th>로트</th>
      <th>...</th>
      <th>대지위치</th>
      <th>대장구분코드</th>
      <th>대장구분코드명</th>
      <th>대장종류코드</th>
      <th>대장종류코드명</th>
      <th>순번</th>
      <th>시군구코드</th>
      <th>특수지명</th>
      <th>단위구분코드</th>
      <th>단위구분코드명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>20190923</td>
      <td>하수종말처리장연결</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>1</td>
      <td>총괄표제부</td>
      <td>1</td>
      <td>41135</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 30 columns</p>
</div>


## 건축물대장 주택가격 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="주택가격", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>법정동코드</th>
      <th>건물명</th>
      <th>블록</th>
      <th>번</th>
      <th>외필지수</th>
      <th>생성일자</th>
      <th>주택가격</th>
      <th>지</th>
      <th>로트</th>
      <th>관리건축물대장PK</th>
      <th>...</th>
      <th>대지구분코드</th>
      <th>대지위치</th>
      <th>대장구분코드</th>
      <th>대장구분코드명</th>
      <th>대장종류코드</th>
      <th>대장종류코드명</th>
      <th>순번</th>
      <th>시군구코드</th>
      <th>특수지명</th>
      <th>stdDay</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>1008000000</td>
      <td>0000</td>
      <td>None</td>
      <td>41135-100225613</td>
      <td>...</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>1</td>
      <td>41135</td>
      <td>None</td>
      <td>20170101</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>904000000</td>
      <td>0000</td>
      <td>None</td>
      <td>41135-100225195</td>
      <td>...</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>2</td>
      <td>41135</td>
      <td>None</td>
      <td>20170101</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>784000000</td>
      <td>0000</td>
      <td>None</td>
      <td>41135-100225195</td>
      <td>...</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>3</td>
      <td>41135</td>
      <td>None</td>
      <td>20140101</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>896000000</td>
      <td>0000</td>
      <td>None</td>
      <td>41135-100225195</td>
      <td>...</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>4</td>
      <td>41135</td>
      <td>None</td>
      <td>20160101</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>0</td>
      <td>20171205</td>
      <td>718000000</td>
      <td>0000</td>
      <td>None</td>
      <td>41135-100225310</td>
      <td>...</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>5</td>
      <td>41135</td>
      <td>None</td>
      <td>20140101</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 26 columns</p>
</div>


## 건축물대장 전유부 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="전유부", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>법정동코드</th>
      <th>건물명</th>
      <th>블록</th>
      <th>번</th>
      <th>생성일자</th>
      <th>동명칭</th>
      <th>층구분코드</th>
      <th>층구분코드명</th>
      <th>층번호</th>
      <th>호명칭</th>
      <th>...</th>
      <th>도로명대지위치</th>
      <th>대지구분코드</th>
      <th>대지위치</th>
      <th>대장구분코드</th>
      <th>대장구분코드명</th>
      <th>대장종류코드</th>
      <th>대장종류코드명</th>
      <th>순번</th>
      <th>시군구코드</th>
      <th>특수지명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20171205</td>
      <td>112동</td>
      <td>20</td>
      <td>지상</td>
      <td>10.0</td>
      <td>1003</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>1</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20171205</td>
      <td>113동</td>
      <td>20</td>
      <td>지상</td>
      <td>13.0</td>
      <td>1303</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>2</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20171205</td>
      <td>102동</td>
      <td>20</td>
      <td>지상</td>
      <td>10.0</td>
      <td>1001</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>3</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20171205</td>
      <td>107동</td>
      <td>20</td>
      <td>지상</td>
      <td>14.0</td>
      <td>1402</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>4</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11000</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>0542</td>
      <td>20171205</td>
      <td>108동</td>
      <td>20</td>
      <td>지상</td>
      <td>6.0</td>
      <td>602</td>
      <td>...</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>2</td>
      <td>집합</td>
      <td>4</td>
      <td>전유부</td>
      <td>5</td>
      <td>41135</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 28 columns</p>
</div>


## 건축물대장 지역지구구역 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">
</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="지역지구구역", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>법정동코드</th>
      <th>블록</th>
      <th>번</th>
      <th>생성일자</th>
      <th>기타지역지구구역</th>
      <th>지</th>
      <th>지역지구구역코드</th>
      <th>지역지구구역코드명</th>
      <th>지역지구구역구분코드</th>
      <th>지역지구구역구분코드명</th>
      <th>로트</th>
      <th>관리건축물대장PK</th>
      <th>도로명대지위치</th>
      <th>대지구분코드</th>
      <th>대지위치</th>
      <th>대표여부</th>
      <th>순번</th>
      <th>시군구코드</th>
      <th>특수지명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11000</td>
      <td>None</td>
      <td>0542</td>
      <td>20190923</td>
      <td>택지개발지구</td>
      <td>0000</td>
      <td>160</td>
      <td>택지개발지구</td>
      <td>2</td>
      <td>용도지구코드</td>
      <td>None</td>
      <td>41135-100225002</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>1</td>
      <td>1</td>
      <td>41135</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11000</td>
      <td>None</td>
      <td>0542</td>
      <td>20190923</td>
      <td>제3종일반주거지역</td>
      <td>0000</td>
      <td>UQA123</td>
      <td>제3종일반주거지역</td>
      <td>1</td>
      <td>용도지역코드</td>
      <td>None</td>
      <td>41135-100225002</td>
      <td>경기도 성남시 분당구 동판교로 123</td>
      <td>0</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>1</td>
      <td>2</td>
      <td>41135</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
</div>
