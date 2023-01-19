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


## 입력 명세

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

| 항목명(국문)         | 항목명(영문)   | 항목크기      | 항목구분   | 샘플데이터                      |
|:---------------------|:---------------|:--------------|:-----------|:--------------------------------|
| 도로명대지위치       | newPlatPlc     | VARCHAR2(200) | 옵         | nan                             |
| 건물명               | bldNm          | VARCHAR2(100) | 옵         | 대치아파트 제217동              |
| 특수지명             | splotNm        | VARCHAR2(200) | 옵         | nan                             |
| 블록                 | block          | VARCHAR2(20)  | 옵         | nan                             |
| 로트                 | lot            | VARCHAR2(20)  | 옵         | nan                             |
| 외필지수             | bylotCnt       | NUMBER(5)     | 옵         | 0                               |
| 새주소도로코드       | naRoadCd       | VARCHAR2(12)  | 옵         | nan                             |
| 새주소법정동코드     | naBjdongCd     | VARCHAR2(5)   | 옵         | nan                             |
| 새주소지상지하코드   | naUgrndCd      | VARCHAR2(1)   | 옵         | 0                               |
| 새주소본번           | naMainBun      | NUMBER(5)     | 옵         | nan                             |
| 새주소부번           | naSubBun       | NUMBER(5)     | 옵         | nan                             |
| 지역코드             | jiyukCd        | VARCHAR2(6)   | 옵         | nan                             |
| 지구코드             | jiguCd         | VARCHAR2(6)   | 옵         | nan                             |
| 구역코드             | guyukCd        | VARCHAR2(6)   | 옵         | nan                             |
| 지역코드명           | jiyukCdNm      | VARCHAR2(100) | 옵         | nan                             |
| 지구코드명           | jiguCdNm       | VARCHAR2(100) | 옵         | nan                             |
| 구역코드명           | guyukCdNm      | VARCHAR2(100) | 옵         | nan                             |
| 생성일자             | crtnDay        | VARCHAR2(8)   | 필         | 20090320                        |
| nan                  | Items          | nan           | 필         | nan                             |
| 순번                 | rnum           | NUMBER(8)     | 옵         | 1                               |
| 대지위치             | platPlc        | VARCHAR2(200) | 필         | 서울특별시 강남구 개포동 12번지 |
| 시군구코드           | sigunguCd      | VARCHAR2(5)   | 필         | 11680                           |
| 법정동코드           | bjdongCd       | VARCHAR2(5)   | 필         | 10300                           |
| 대지구분코드         | platGbCd       | CHAR(1)       | 옵         | 0                               |
| 번                   | bun            | VARCHAR2(4)   | 옵         | 12                              |
| 지                   | ji             | VARCHAR2(4)   | 옵         | 0                               |
| 관리건축물대장PK     | mgmBldrgstPk   | VARCHAR2(33)  | 필         | 11680-8520602                   |
| 관리상위건축물대장PK | mgmUpBldrgstPk | VARCHAR2(33)  | 필         | 11680-91502                     |
| 대장구분코드         | regstrGbCd     | VARCHAR2(1)   | 옵         | 2                               |
| 대장구분코드명       | regstrGbCdNm   | VARCHAR2(100) | 옵         | 집합                            |
| 대장종류코드         | regstrKindCd   | VARCHAR2(1)   | 옵         | 4                               |

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

| 항목명(국문)         | 항목명(영문)       | 항목크기      | 항목구분   | 샘플데이터                      | 항목설명             |
|:---------------------|:-------------------|:--------------|:-----------|:--------------------------------|:---------------------|
| 지능형건축물등급     | itgBldGrade        | CHAR(1)       | 옵         | nan                             | 지능형건축물등급     |
| 지능형건축물인증점수 | itgBldCert         | NUMBER(5)     | 옵         | 0                               | 지능형건축물인증점수 |
| 생성일자             | crtnDay            | VARCHAR2(8)   | 필         | 20120822                        | 생성일자             |
| 새주소법정동코드     | naBjdongCd         | VARCHAR2(5)   | 옵         | 10301                           | 새주소법정동코드     |
| 새주소지상지하코드   | naUgrndCd          | VARCHAR2(1)   | 옵         | 0                               | 새주소지상지하코드   |
| 새주소본번           | naMainBun          | NUMBER(5)     | 옵         | 5                               | 새주소본번           |
| 새주소부번           | naSubBun           | NUMBER(5)     | 옵         | 0                               | 새주소부번           |
| 대지면적(㎡)         | platArea           | NUMBER(19,9)  | 옵         | 0                               | 대지면적(㎡)         |
| 건축면적(㎡)         | archArea           | NUMBER(19,9)  | 옵         | 15324.37                        | 건축면적(㎡)         |
| 건폐율(%)            | bcRat              | NUMBER(19,9)  | 옵         | 0                               | 건폐율(%)            |
| 연면적(㎡)           | totArea            | NUMBER(19,9)  | 옵         | 223939                          | 연면적(㎡)           |
| 용적률산정연면적(㎡) | vlRatEstmTotArea   | NUMBER(19,9)  | 옵         | 211555.54                       | 용적률산정연면적(㎡) |
| 용적률(%)            | vlRat              | NUMBER(19,9)  | 옵         | 0                               | 용적률(%)            |
| 주용도코드           | mainPurpsCd        | VARCHAR2(5)   | 옵         | 2000                            | 주용도코드           |
| 주용도코드명         | mainPurpsCdNm      | VARCHAR2(100) | 옵         | 공동주택                        | 주용도코드명         |
| 기타용도             | etcPurps           | VARCHAR2(500) | 옵         | 주거시설 근린생활시설           | 기타용도             |
| 세대수(세대)         | hhldCnt            | NUMBER(5)     | 옵         | 4199                            | 세대수(세대)         |
| 가구수(가구)         | fmlyCnt            | NUMBER(5)     | 옵         | 0                               | 가구수(가구)         |
| 주건축물수           | mainBldCnt         | NUMBER(5)     | 옵         | 27                              | 주건축물수           |
| 부속건축물수         | atchBldCnt         | NUMBER(5)     | 옵         | 3                               | 부속건축물수         |
| 부속건축물면적(㎡)   | atchBldArea        | NUMBER(19,9)  | 옵         | 64.26                           | 부속건축물면적(㎡)   |
| 총주차수             | totPkngCnt         | NUMBER(7)     | 옵         | 0                               | 총주차수             |
| 옥내기계식대수(대)   | indrMechUtcnt      | NUMBER(6)     | 옵         | 0                               | 옥내기계식대수(대)   |
| 옥내기계식면적(㎡)   | indrMechArea       | NUMBER(19,9)  | 옵         | 0                               | 옥내기계식면적(㎡)   |
| 옥외기계식대수(대)   | oudrMechUtcnt      | NUMBER(6)     | 옵         | 0                               | 옥외기계식대수(대)   |
| 옥외기계식면적(㎡)   | oudrMechArea       | NUMBER(19,9)  | 옵         | 0                               | 옥외기계식면적(㎡)   |
| 옥내자주식대수(대)   | indrAutoUtcnt      | NUMBER(6)     | 옵         | 0                               | 옥내자주식대수(대)   |
| 옥내자주식면적(㎡)   | indrAutoArea       | NUMBER(19,9)  | 옵         | 0                               | 옥내자주식면적(㎡)   |
| 옥외자주식대수(대)   | oudrAutoUtcnt      | NUMBER(6)     | 옵         | 0                               | 옥외자주식대수(대)   |
| 옥외자주식면적(㎡)   | oudrAutoArea       | NUMBER(19,9)  | 옵         | 0                               | 옥외자주식면적(㎡)   |
| 허가일               | pmsDay             | VARCHAR2(8)   | 옵         | nan                             | 허가일               |
| 착공일               | stcnsDay           | VARCHAR2(8)   | 옵         | nan                             | 착공일               |
| 사용승인일           | useAprDay          | VARCHAR2(8)   | 옵         | nan                             | 사용승인일           |
| 허가번호년           | pmsnoYear          | VARCHAR2(4)   | 옵         | nan                             | 허가번호년           |
| 허가번호기관코드     | pmsnoKikCd         | CHAR(7)       | 옵         | nan                             | 허가번호기관코드     |
| 허가번호기관코드명   | pmsnoKikCdNm       | VARCHAR2(100) | 옵         | nan                             | 허가번호기관코드명   |
| 허가번호구분코드     | pmsnoGbCd          | VARCHAR2(4)   | 옵         | nan                             | 허가번호구분코드     |
| 허가번호구분코드명   | pmsnoGbCdNm        | VARCHAR2(100) | 옵         | nan                             | 허가번호구분코드명   |
| 호수(호)             | hoCnt              | NUMBER(5)     | 옵         | 0                               | 호수(호)             |
| 에너지효율등급       | engrGrade          | VARCHAR2(4)   | 옵         | nan                             | 에너지효율등급       |
| 에너지절감율         | engrRat            | NUMBER(19,9)  | 옵         | 0                               | 에너지절감율         |
| EPI점수              | engrEpi            | NUMBER(5)     | 옵         | 0                               | EPI점수              |
| 친환경건축물등급     | gnBldGrade         | CHAR(1)       | 옵         | nan                             | 친환경건축물등급     |
| 친환경건축물인증점수 | gnBldCert          | NUMBER(5)     | 옵         | 0                               | 친환경건축물인증점수 |
| nan                  | Items              | nan           | 필         | nan                             | nan                  |
| 순번                 | rnum               | NUMBER(8)     | 옵         | 1                               | 순번                 |
| 대지위치             | platPlc            | VARCHAR2(200) | 필         | 서울특별시 강남구 개포동 12번지 | 대지위치             |
| 시군구코드           | sigunguCd          | VARCHAR2(5)   | 필         | 11680                           | 행정표준코드         |
| 법정동코드           | bjdongCd           | VARCHAR2(5)   | 필         | 10300                           | 행정표준코드         |
| 대지구분코드         | platGbCd           | CHAR(1)       | 옵         | 0                               | 0:대지 1:산 2:블록   |
| 번                   | bun                | VARCHAR2(4)   | 옵         | 12                              | 번                   |
| 지                   | ji                 | VARCHAR2(4)   | 옵         | 0                               | 지                   |
| 관리건축물대장PK     | mgmBldrgstPk       | VARCHAR2(33)  | 필         | 11680-10302                     | 관리건축물대장PK     |
| 대장구분코드         | regstrGbCd         | VARCHAR2(1)   | 옵         | 2                               | 대장구분코드         |
| 대장구분코드명       | regstrGbCdNm       | VARCHAR2(100) | 옵         | 집합                            | 대장구분코드명       |
| 대장종류코드         | regstrKindCd       | VARCHAR2(1)   | 옵         | 1                               | 대장종류코드         |
| 대장종류코드명       | regstrKindCdNm     | VARCHAR2(100) | 옵         | 총괄표제부                      | 대장종류코드명       |
| 신구대장구분코드     | newOldRegstrGbCd   | CHAR(1)       | 옵         | 0                               | 신구대장구분코드     |
| 신구대장구분코드명   | newOldRegstrGbCdNm | VARCHAR2(100) | 옵         | 구대장                          | 신구대장구분코드명   |
| 도로명대지위치       | newPlatPlc         | VARCHAR2(200) | 옵         | 서울특별시강남구개포로109길5    | 도로명대지위치       |
| 건물명               | bldNm              | VARCHAR2(100) | 옵         | 대치,대청 아파트                | 건물명               |
| 특수지명             | splotNm            | VARCHAR2(200) | 옵         | nan                             | 특수지명             |
| 블록                 | block              | VARCHAR2(20)  | 옵         | nan                             | 블록                 |
| 로트                 | lot                | VARCHAR2(20)  | 옵         | nan                             | 로트                 |
| 외필지수             | bylotCnt           | NUMBER(5)     | 옵         | 0                               | 외필지수             |
| 새주소도로코드       | naRoadCd           | VARCHAR2(12)  | 옵         | 116804166040                    | 새주소도로코드       |

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

| 항목명(국문)         | 항목명(영문)        | 항목크기      | 항목구분   | 샘플데이터                      | 항목설명                         |
|:---------------------|:--------------------|:--------------|:-----------|:--------------------------------|:---------------------------------|
| 주용도코드명         | mainPurpsCdNm       | VARCHAR2(100) | 옵션       | 교육연구시설                    | 주용도코드명                     |
| 기타용도             | etcPurps            | VARCHAR2(500) | 옵션       | 교육연구시설                    | 용도정보(건축물대장 주용도 정보) |
| 지붕코드             | roofCd              | VARCHAR2(2)   | 옵션       | 90                              | 지붕코드                         |
| 지붕코드명           | roofCdNm            | VARCHAR2(100) | 옵션       | 기타지붕                        | 지붕코드명                       |
| 기타지붕             | etcRoof             | VARCHAR2(500) | 옵션       | 아스팔트슁글                    | 지붕정보(건축물대장 지붕 정보)   |
| 세대수(세대)         | hhldCnt             | NUMBER(5)     | 옵션       | 0                               | 세대수(세대)                     |
| 가구수(가구)         | fmlyCnt             | NUMBER(5)     | 옵션       | 0                               | 가구수(가구)                     |
| 높이(m)              | heit                | NUMBER(19,9)  | 옵션       | 0                               | 높이(m)                          |
| 지상층수             | grndFlrCnt          | NUMBER(5)     | 옵션       | 2                               | 지상층수                         |
| 지하층수             | ugrndFlrCnt         | NUMBER(5)     | 옵션       | 0                               | 지하층수                         |
| 승용승강기수         | rideUseElvtCnt      | NUMBER(5)     | 옵션       | 0                               | 승용승강기수                     |
| 비상용승강기수       | emgenUseElvtCnt     | NUMBER(5)     | 옵션       | 0                               | 비상용승강기수                   |
| 부속건축물수         | atchBldCnt          | NUMBER(5)     | 옵션       | 0                               | 부속건축물수                     |
| 부속건축물면적(㎡)   | atchBldArea         | NUMBER(19,9)  | 옵션       | 0                               | 부속건축물면적(㎡)               |
| 총동연면적(㎡)       | totDongTotArea      | NUMBER(19,9)  | 옵션       | 536.06                          | 총동연면적(㎡)                   |
| 옥내기계식대수(대)   | indrMechUtcnt       | NUMBER(6)     | 옵션       | 0                               | 옥내기계식대수(대)               |
| 옥내기계식면적(㎡)   | indrMechArea        | NUMBER(19,9)  | 옵션       | 0                               | 옥내기계식면적(㎡)               |
| 옥외기계식대수(대)   | oudrMechUtcnt       | NUMBER(6)     | 옵션       | 0                               | 옥외기계식대수(대)               |
| 옥외기계식면적(㎡)   | oudrMechArea        | NUMBER(19,9)  | 옵션       | 0                               | 옥외기계식면적(㎡)               |
| 옥내자주식대수(대)   | indrAutoUtcnt       | NUMBER(6)     | 옵션       | 0                               | 옥내자주식대수(대)               |
| 옥내자주식면적(㎡)   | indrAutoArea        | NUMBER(19,9)  | 옵션       | 0                               | 옥내자주식면적(㎡)               |
| 옥외자주식대수(대)   | oudrAutoUtcnt       | NUMBER(6)     | 옵션       | 0                               | 옥외자주식대수(대)               |
| 옥외자주식면적(㎡)   | oudrAutoArea        | NUMBER(19,9)  | 옵션       | 0                               | 옥외자주식면적(㎡)               |
| 허가일               | pmsDay              | VARCHAR2(8)   | 옵션       | 19891226                        | 허가일                           |
| 착공일               | stcnsDay            | VARCHAR2(8)   | 옵션       | nan                             | 착공일                           |
| 사용승인일           | useAprDay           | VARCHAR2(8)   | 옵션       | 19911120                        | 사용승인일                       |
| 허가번호년           | pmsnoYear           | VARCHAR2(4)   | 옵션       | nan                             | 허가번호년                       |
| 허가번호기관코드     | pmsnoKikCd          | CHAR(7)       | 옵션       | nan                             | 허가번호기관코드                 |
| 허가번호기관코드명   | pmsnoKikCdNm        | VARCHAR2(100) | 옵션       | nan                             | 허가번호기관코드명               |
| 허가번호구분코드     | pmsnoGbCd           | VARCHAR2(4)   | 옵션       | nan                             | 허가번호구분코드                 |
| 허가번호구분코드명   | pmsnoGbCdNm         | VARCHAR2(100) | 옵션       | nan                             | 허가번호구분코드명               |
| 호수(호)             | hoCnt               | NUMBER(5)     | 옵션       | 0                               | 호수(호)                         |
| 에너지효율등급       | engrGrade           | VARCHAR2(4)   | 옵션       | nan                             | 에너지효율등급                   |
| 에너지절감율         | engrRat             | NUMBER(19,9)  | 옵션       | 0                               | 에너지절감율                     |
| EPI점수              | engrEpi             | NUMBER(5)     | 옵션       | 0                               | EPI점수                          |
| 친환경건축물등급     | gnBldGrade          | CHAR(1)       | 옵션       | nan                             | 친환경건축물등급                 |
| 친환경건축물인증점수 | gnBldCert           | NUMBER(5)     | 옵션       | 0                               | 친환경건축물인증점수             |
| 지능형건축물등급     | itgBldGrade         | CHAR(1)       | 옵션       | nan                             | 지능형건축물등급                 |
| 지능형건축물인증점수 | itgBldCert          | NUMBER(5)     | 옵션       | 0                               | 지능형건축물인증점수             |
| 생성일자             | crtnDay             | VARCHAR2(8)   | 필수       | 20131207                        | 생성일자                         |
| nan                  | Items               | nan           | 필수       | nan                             | nan                              |
| 순번                 | rnum                | NUMBER(8)     | 옵션       | 1                               | 순번                             |
| 대지위치             | platPlc             | VARCHAR2(200) | 필수       | 서울특별시 강남구 개포동 12번지 | 대지위치                         |
| 시군구코드           | sigunguCd           | VARCHAR2(5)   | 필수       | 11680                           | 행정표준코드                     |
| 법정동코드           | bjdongCd            | VARCHAR2(5)   | 필수       | 10300                           | 행정표준코드                     |
| 대지구분코드         | platGbCd            | CHAR(1)       | 옵션       | 0                               | 0:대지 1:산 2:블록               |
| 번                   | bun                 | VARCHAR2(4)   | 옵션       | 12                              | 번                               |
| 지                   | ji                  | VARCHAR2(4)   | 옵션       | 0                               | 지                               |
| 관리건축물대장PK     | mgmBldrgstPk        | VARCHAR2(33)  | 필수       | 11680-700402                    | 관리건축물대장PK                 |
| 대장구분코드         | regstrGbCd          | VARCHAR2(1)   | 옵션       | 1                               | 대장구분코드                     |
| 대장구분코드명       | regstrGbCdNm        | VARCHAR2(100) | 옵션       | 일반                            | 대장구분코드명                   |
| 대장종류코드         | regstrKindCd        | VARCHAR2(1)   | 옵션       | 2                               | 대장종류코드                     |
| 대장종류코드명       | regstrKindCdNm      | VARCHAR2(100) | 옵션       | 일반건축물                      | 대장종류코드명                   |
| 도로명대지위치       | newPlatPlc          | VARCHAR2(200) | 옵션       | nan                             | 도로명대지위치                   |
| 건물명               | bldNm               | VARCHAR2(100) | 옵션       | nan                             | 건물명                           |
| 특수지명             | splotNm             | VARCHAR2(200) | 옵션       | nan                             | 특수지명                         |
| 블록                 | block               | VARCHAR2(20)  | 옵션       | nan                             | 블록                             |
| 로트                 | lot                 | VARCHAR2(20)  | 옵션       | nan                             | 로트                             |
| 외필지수             | bylotCnt            | NUMBER(5)     | 옵션       | 0                               | 외필지수                         |
| 새주소도로코드       | naRoadCd            | VARCHAR2(12)  | 옵션       | nan                             | 새주소도로코드                   |
| 새주소법정동코드     | naBjdongCd          | VARCHAR2(5)   | 옵션       | nan                             | 새주소법정동코드                 |
| 새주소지상지하코드   | naUgrndCd           | VARCHAR2(1)   | 옵션       | 0                               | 새주소지상지하코드               |
| 새주소본번           | naMainBun           | NUMBER(5)     | 옵션       | nan                             | 새주소본번                       |
| 새주소부번           | naSubBun            | NUMBER(5)     | 옵션       | nan                             | 새주소부번                       |
| 동명칭               | dongNm              | VARCHAR2(100) | 옵션       | nan                             | 동명칭                           |
| 주부속구분코드       | mainAtchGbCd        | CHAR(1)       | 옵션       | 0                               | 주부속구분코드                   |
| 주부속구분코드명     | mainAtchGbCdNm      | VARCHAR2(100) | 옵션       | 주건축물                        | 주부속구분코드명                 |
| 대지면적(㎡)         | platArea            | NUMBER(19,9)  | 옵션       | 0                               | 대지면적(㎡)                     |
| 건축면적(㎡)         | archArea            | NUMBER(19,9)  | 옵션       | 271.63                          | 건축면적(㎡)                     |
| 건폐율(%)            | bcRat               | NUMBER(19,9)  | 옵션       | 0                               | 건폐율(%)                        |
| 연면적(㎡)           | totArea             | NUMBER(19,9)  | 옵션       | 536.06                          | 연면적(㎡)                       |
| 용적률산정연면적(㎡) | vlRatEstmTotArea    | NUMBER(19,9)  | 옵션       | 536.06                          | 용적률산정연면적(㎡)             |
| 용적률(%)            | vlRat               | NUMBER(19,9)  | 옵션       | 0                               | 용적률(%)                        |
| 구조코드             | strctCd             | CHAR(1)       | 옵션       | 11                              | 구조코드                         |
| 구조코드명           | strctCdNm           | VARCHAR2(100) | 옵션       | 벽돌구조                        | 구조코드명                       |
| 기타구조             | etcStrct            | VARCHAR2(500) | 옵션       | 연와조                          | 구조정보(건축물대장 주구조 정보) |
| 주용도코드           | mainPurpsCd         | 25            | 옵션       | 10000                           | 주용도코드                       |
| 내진설계적용여부     | rserthqkDsgnApplyYn | 1             | 옵션       | 1                               | 내진 설계 적용 여부              |
| 내진능력             | rserthqkAblty       | 200           | 옵션       | VII-0.169g                      | 내진 능력                        |

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

| 항목명(국문)       | 항목명(영문)   | 항목크기      | 항목구분   | 샘플데이터                      | 항목설명                  |
|:-------------------|:---------------|:--------------|:-----------|:--------------------------------|:--------------------------|
| 순번               | rnum           | NUMBER(8)     | 옵션       | 1                               | 순번                      |
| 대지위치           | platPlc        | VARCHAR2(200) | 필수       | 서울특별시 강남구 개포동 12번지 | 대지위치                  |
| 시군구코드         | sigunguCd      | VARCHAR2(5)   | 필수       | 11680                           | 행정표준코드              |
| 법정동코드         | bjdongCd       | VARCHAR2(5)   | 필수       | 10300                           | 행정표준코드              |
| 대지구분코드       | platGbCd       | CHAR(1)       | 옵션       | 0                               | 0:대지 1:산 2:블록        |
| 번                 | bun            | VARCHAR2(4)   | 옵션       | 12                              | 번                        |
| 지                 | ji             | VARCHAR2(4)   | 옵션       | 0                               | 지                        |
| 관리건축물대장PK   | mgmBldrgstPk   | VARCHAR2(33)  | 필수       | 11680-700402                    | 관리건축물대장PK          |
| 도로명대지위치     | newPlatPlc     | VARCHAR2(200) | 옵션       | nan                             | 도로명대지위치            |
| 건물명             | bldNm          | VARCHAR2(100) | 옵션       | nan                             | 건물명                    |
| 특수지명           | splotNm        | VARCHAR2(200) | 옵션       | nan                             | 특수지명                  |
| 블록               | block          | VARCHAR2(20)  | 옵션       | nan                             | 블록                      |
| 로트               | lot            | VARCHAR2(20)  | 옵션       | nan                             | 로트                      |
| 새주소도로코드     | naRoadCd       | VARCHAR2(12)  | 옵션       | nan                             | 새주소도로코드            |
| 새주소법정동코드   | naBjdongCd     | VARCHAR2(5)   | 옵션       | nan                             | 새주소법정동코드          |
| 새주소지상지하코드 | naUgrndCd      | VARCHAR2(1)   | 옵션       | 0                               | 새주소지상지하코드        |
| 새주소본번         | naMainBun      | NUMBER(5)     | 옵션       | nan                             | 새주소본번                |
| 새주소부번         | naSubBun       | NUMBER(5)     | 옵션       | nan                             | 새주소부번                |
| 동명칭             | dongNm         | VARCHAR2(100) | 옵션       | nan                             | 동명칭                    |
| 층구분코드         | flrGbCd        | VARCHAR2(2)   | 옵션       | 20                              | 층구분코드                |
| 층구분코드명       | flrGbCdNm      | VARCHAR2(100) | 옵션       | 지상                            | 층구분코드명              |
| 층번호             | flrNo          | NUMBER(4)     | 옵션       | 1                               | 층번호                    |
| 층번호명           | flrNoNm        | VARCHAR2(100) | 옵션       | 1층                             | 층번호명                  |
| 구조코드           | strctCd        | CHAR(1)       | 옵션       | 11                              | 구조코드                  |
| 구조코드명         | strctCdNm      | VARCHAR2(100) | 옵션       | 벽돌구조                        | 구조코드명                |
| 기타구조           | etcStrct       | VARCHAR2(500) | 옵션       | 연와조                          | 구조정보(건축물대장 구조) |
| 주용도코드         | mainPurpsCd    | VARCHAR2(5)   | 옵션       | 10999                           | 주용도코드                |
| 주용도코드명       | mainPurpsCdNm  | VARCHAR2(100) | 옵션       | 기타교육연구시설                | 주용도코드명              |
| 기타용도           | etcPurps       | VARCHAR2(500) | 옵션       | 교육연구및복지시설              | 용도정보(건축물대장 용도) |
| 주부속구분코드     | mainAtchGbCd   | CHAR(1)       | 옵션       | 0                               | 주부속구분코드            |
| 주부속구분코드명   | mainAtchGbCdNm | VARCHAR2(100) | 옵션       | 주건축물                        | 주부속구분코드명          |
| 면적(㎡)           | area           | NUMBER(19,9)  | 옵션       | 271.63                          | 면적(㎡)                  |
| 면적제외여부       | areaExctYn     | VARCHAR2(1)   | 옵션       | nan                             | 0: N 1: Y                 |
| 생성일자           | crtnDay        | VARCHAR2(8)   | 필수       | 20131207                        | 생성일자                  |
| nan                | Items          | nan           | 필수       | nan                             | nan                       |
​

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

| 항목명(국문)       | 항목명(영문)     | 항목크기      | 항목구분   | 샘플데이터                        | 항목설명           |
|:-------------------|:-----------------|:--------------|:-----------|:----------------------------------|:-------------------|
| 대지구분코드       | platGbCd         | CHAR(1)       | 옵         | 0                                 | 0:대지 1:산 2:블록 |
| 번                 | bun              | VARCHAR2(4)   | 옵         | 12                                | 번                 |
| 지                 | ji               | VARCHAR2(4)   | 옵         | 5                                 | 지                 |
| 관리건축물대장PK   | mgmBldrgstPk     | VARCHAR2(33)  | 필         | 11680-1920002                     | 관리건축물대장PK   |
| 대장구분코드       | regstrGbCd       | VARCHAR2(1)   | 옵         | 1                                 | 대장구분코드       |
| 대장구분코드명     | regstrGbCdNm     | VARCHAR2(100) | 옵         | 일반                              | 대장구분코드명     |
| 대장종류코드       | regstrKindCd     | VARCHAR2(1)   | 옵         | 2                                 | 대장종류코드       |
| 대장종류코드명     | regstrKindCdNm   | VARCHAR2(100) | 옵         | 일반건축물                        | 대장종류코드명     |
| 도로명대지위치     | newPlatPlc       | VARCHAR2(200) | 옵         | 서울특별시강남구개포로613         | 도로명대지위치     |
| 건물명             | bldNm            | VARCHAR2(100) | 옵         | nan                               | 건물명             |
| 특수지명           | splotNm          | VARCHAR2(200) | 옵         | nan                               | 특수지명           |
| 블록               | block            | VARCHAR2(20)  | 옵         | nan                               | 블록               |
| 로트               | lot              | VARCHAR2(20)  | 옵         | nan                               | 로트               |
| 새주소도로코드     | naRoadCd         | VARCHAR2(12)  | 옵         | 116803122001                      | 새주소도로코드     |
| 새주소법정동코드   | naBjdongCd       | VARCHAR2(5)   | 옵         | 10301                             | 새주소법정동코드   |
| 새주소지상지하코드 | naUgrndCd        | VARCHAR2(1)   | 옵         | 0                                 | 새주소지상지하코드 |
| 새주소본번         | naMainBun        | NUMBER(5)     | 옵         | 613                               | 새주소본번         |
| 새주소부번         | naSubBun         | NUMBER(5)     | 옵         | 0                                 | 새주소부번         |
| 부속대장구분코드   | atchRegstrGbCd   | CHAR(1)       | 옵         | 1                                 | 부속대장구분코드   |
| 부속대장구분코드명 | atchRegstrGbCdNm | VARCHAR2(100) | 옵         | 일반                              | 부속대장구분코드명 |
| 부속시군구코드     | atchSigunguCd    | VARCHAR2(5)   | 옵         | 11680                             | 부속시군구코드     |
| 부속법정동코드     | atchBjdongCd     | VARCHAR2(5)   | 옵         | 10300                             | 부속법정동코드     |
| 부속대지구분코드   | atchPlatGbCd     | CHAR(1)       | 옵         | 0                                 | 부속대지구분코드   |
| 부속번             | atchBun          | VARCHAR2(4)   | 옵         | 12                                | 부속번             |
| 부속지             | atchJi           | VARCHAR2(4)   | 옵         | 48                                | 부속지             |
| 부속특수지명       | atchSplotNm      | VARCHAR2(200) | 옵         | nan                               | 부속특수지명       |
| 부속블록           | atchBlock        | VARCHAR2(20)  | 옵         | nan                               | 부속블록           |
| 부속로트           | atchLot          | VARCHAR2(20)  | 옵         | nan                               | 부속로트           |
| 부속기타지번명     | atchEtcJibunNm   | VARCHAR2(300) | 옵         | nan                               | 부속기타지번명     |
| 생성일자           | crtnDay          | VARCHAR2(8)   | 필         | 20140325                          | 생성일자           |
| nan                | Items            | nan           | 필         | nan                               | nan                |
| 순번               | rnum             | NUMBER(8)     | 옵         | 1                                 | 순번               |
| 대지위치           | platPlc          | VARCHAR2(200) | 필         | 서울특별시 강남구 개포동 12-5번지 | 대지위치           |
| 시군구코드         | sigunguCd        | VARCHAR2(5)   | 필         | 11680                             | 행정표준코드       |
| 법정동코드         | bjdongCd         | VARCHAR2(5)   | 필         | 10300                             | 행정표준코드       |

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

| 항목명(국문)       | 항목명(영문)      | 항목크기      | 항목구분   | 샘플데이터                      | 항목설명           |
|:-------------------|:------------------|:--------------|:-----------|:--------------------------------|:-------------------|
| 대장구분코드       | regstrGbCd        | VARCHAR2(1)   | 옵         | 2                               | 대장구분코드       |
| 대장구분코드명     | regstrGbCdNm      | VARCHAR2(100) | 옵         | 집합                            | 대장구분코드명     |
| 대장종류코드       | regstrKindCd      | VARCHAR2(1)   | 옵         | 4                               | 대장종류코드       |
| 대장종류코드명     | regstrKindCdNm    | VARCHAR2(100) | 옵         | 전유부                          | 대장종류코드명     |
| 도로명대지위치     | newPlatPlc        | VARCHAR2(200) | 옵         | nan                             | 도로명대지위치     |
| 건물명             | bldNm             | VARCHAR2(100) | 옵         | 대치아파트 제219동              | 건물명             |
| 특수지명           | splotNm           | VARCHAR2(200) | 옵         | nan                             | 특수지명           |
| 블록               | block             | VARCHAR2(20)  | 옵         | nan                             | 블록               |
| 로트               | lot               | VARCHAR2(20)  | 옵         | nan                             | 로트               |
| 새주소도로코드     | naRoadCd          | VARCHAR2(12)  | 옵         | nan                             | 새주소도로코드     |
| 새주소법정동코드   | naBjdongCd        | VARCHAR2(5)   | 옵         | nan                             | 새주소법정동코드   |
| 새주소지상지하코드 | naUgrndCd         | VARCHAR2(1)   | 옵         | 0                               | 새주소지상지하코드 |
| 새주소본번         | naMainBun         | NUMBER(5)     | 옵         | nan                             | 새주소본번         |
| 새주소부번         | naSubBun          | NUMBER(5)     | 옵         | nan                             | 새주소부번         |
| 동명칭             | dongNm            | VARCHAR2(100) | 옵         | 219                             | 동명칭             |
| 호명칭             | hoNm              | VARCHAR2(100) | 옵         | 1502호                          | 호명칭             |
| 층구분코드         | flrGbCd           | VARCHAR2(2)   | 옵         | 20                              | 층구분코드         |
| 층구분코드명       | flrGbCdNm         | VARCHAR2(100) | 옵         | 지상                            | 층구분코드명       |
| 층번호             | flrNo             | NUMBER(4)     | 옵         | 15                              | 층번호             |
| 층번호명           | flrNoNm           | VARCHAR2(100) | 옵         | 15층                            | 층번호명           |
| 전유공용구분코드   | exposPubuseGbCd   | CHAR(1)       | 옵         | 1                               | 전유공용구분코드   |
| 전유공용구분코드명 | exposPubuseGbCdNm | VARCHAR2(100) | 옵         | 전유                            | 전유공용구분코드명 |
| 주부속구분코드     | mainAtchGbCd      | CHAR(1)       | 옵         | 0                               | 주부속구분코드     |
| 주부속구분코드명   | mainAtchGbCdNm    | VARCHAR2(100) | 옵         | 주건축물                        | 주부속구분코드명   |
| 구조코드           | strctCd           | CHAR(1)       | 옵         | 21                              | 구조코드           |
| 구조코드명         | strctCdNm         | VARCHAR2(100) | 옵         | 철근콘크리트구조                | 구조코드명         |
| 기타구조           | etcStrct          | VARCHAR2(500) | 옵         | 철근콘크리트구조                | 기타구조           |
| 주용도코드         | mainPurpsCd       | VARCHAR2(5)   | 옵         | 2001                            | 주용도코드         |
| 주용도코드명       | mainPurpsCdNm     | VARCHAR2(100) | 옵         | 아파트                          | 주용도코드명       |
| 기타용도           | etcPurps          | VARCHAR2(500) | 옵         | 아파트(일부공유면적포함)        | 기타용도           |
| 면적(㎡)           | area              | NUMBER(19,9)  | 옵         | 49.86                           | 면적(㎡)           |
| 생성일자           | crtnDay           | VARCHAR2(8)   | 필         | 20090320                        | 생성일자           |
| nan                | Items             | nan           | 필         | nan                             | nan                |
| 순번               | rnum              | NUMBER(8)     | 옵         | 1                               | 순번               |
| 대지위치           | platPlc           | VARCHAR2(200) | 필         | 서울특별시 강남구 개포동 12번지 | 대지위치           |
| 시군구코드         | sigunguCd         | VARCHAR2(5)   | 필         | 11680                           | 행정표준코드       |
| 법정동코드         | bjdongCd          | VARCHAR2(5)   | 필         | 10300                           | 행정표준코드       |
| 대지구분코드       | platGbCd          | CHAR(1)       | 옵         | 0                               | 0:대지 1:산 2:블록 |
| 번                 | bun               | VARCHAR2(4)   | 옵         | 12                              | 번                 |
| 지                 | ji                | VARCHAR2(4)   | 옵         | 0                               | 지                 |
| 관리건축물대장PK   | mgmBldrgstPk      | VARCHAR2(33)  | 필         | 11680-3609902                   | 관리건축물대장PK   |

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

| 항목명(국문)       | 항목명(영문)   | 항목크기      | 항목구분   | 샘플데이터                      | 항목설명           |
|:-------------------|:---------------|:--------------|:-----------|:--------------------------------|:-------------------|
| 지                 | ji             | VARCHAR2(4)   | 옵         | 0                               | 지                 |
| 관리건축물대장PK   | mgmBldrgstPk   | VARCHAR2(33)  | 필         | 11680-10302                     | 관리건축물대장PK   |
| 대장구분코드       | regstrGbCd     | VARCHAR2(1)   | 옵         | 2                               | 대장구분코드       |
| 대장구분코드명     | regstrGbCdNm   | VARCHAR2(100) | 옵         | 집합                            | 대장구분코드명     |
| 대장종류코드       | regstrKindCd   | VARCHAR2(1)   | 옵         | 1                               | 대장종류코드       |
| 대장종류코드명     | regstrKindCdNm | VARCHAR2(100) | 옵         | 집합                            | 대장종류코드명     |
| 도로명대지위치     | newPlatPlc     | VARCHAR2(200) | 옵         | 서울특별시강남구개포로109길5    | 도로명대지위치     |
| 건물명             | bldNm          | VARCHAR2(100) | 옵         | 대치,대청 아파트                | 건물명             |
| 특수지명           | splotNm        | VARCHAR2(200) | 옵         | nan                             | 특수지명           |
| 블록               | block          | VARCHAR2(20)  | 옵         | nan                             | 블록               |
| 로트               | lot            | VARCHAR2(20)  | 옵         | nan                             | 로트               |
| 새주소도로코드     | naRoadCd       | VARCHAR2(12)  | 옵         | 116804166040                    | 새주소도로코드     |
| 새주소법정동코드   | naBjdongCd     | VARCHAR2(5)   | 옵         | 10301                           | 새주소법정동코드   |
| 새주소지상지하코드 | naUgrndCd      | VARCHAR2(1)   | 옵         | 0                               | 새주소지상지하코드 |
| 새주소본번         | naMainBun      | NUMBER(5)     | 옵         | 5                               | 새주소본번         |
| 새주소부번         | naSubBun       | NUMBER(5)     | 옵         | 0                               | 새주소부번         |
| 형식코드           | modeCd         | VARCHAR2(3)   | 옵         | 299                             | 형식코드           |
| 형식코드명         | modeCdNm       | VARCHAR2(100) | 옵         | 기타단독정화조                  | 형식코드명         |
| 기타형식           | etcMode        | VARCHAR2(200) | 옵         | nan                             | 기타형식           |
| 단위구분코드       | unitGbCd       | CHAR(1)       | 옵         | nan                             | 단위구분코드       |
| 단위구분코드명     | unitGbCdNm     | VARCHAR2(100) | 옵         | nan                             | 단위구분코드명     |
| 용량(인용)         | capaPsper      | NUMBER(19,9)  | 옵         | 300                             | 용량(인용)         |
| 용량(루베)         | capaLube       | NUMBER(19,9)  | 옵         | 0                               | 용량(루베)         |
| 생성일자           | crtnDay        | VARCHAR2(8)   | 필         | 20120822                        | 생성일자           |
| nan                | Items          | nan           | 필         | nan                             | nan                |
| 순번               | rnum           | NUMBER(8)     | 옵         | 1                               | 순번               |
| 대지위치           | platPlc        | VARCHAR2(200) | 필         | 서울특별시 강남구 개포동 12번지 | 대지위치           |
| 시군구코드         | sigunguCd      | VARCHAR2(5)   | 필         | 11680                           | 행정표준코드       |
| 법정동코드         | bjdongCd       | VARCHAR2(5)   | 필         | 10300                           | 행정표준코드       |
| 대지구분코드       | platGbCd       | CHAR(1)       | 옵         | 0                               | 0:대지 1:산 2:블록 |
| 번                 | bun            | VARCHAR2(4)   | 옵         | 12                              | 번                 |

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

| 항목명(국문)       | 항목명(영문)   | 항목크기      | 항목구분   | 샘플데이터                      | 항목설명           |
|:-------------------|:---------------|:--------------|:-----------|:--------------------------------|:-------------------|
| 특수지명           | splotNm        | VARCHAR2(200) | 옵션       | nan                             | 특수지명           |
| 블록               | block          | VARCHAR2(20)  | 옵션       | nan                             | 블록               |
| 로트               | lot            | VARCHAR2(20)  | 옵션       | nan                             | 로트               |
| 외필지수           | bylotCnt       | NUMBER(5)     | 옵션       | 0                               | 외필지수           |
| 새주소도로코드     | naRoadCd       | VARCHAR2(12)  | 옵션       | nan                             | 새주소도로코드     |
| 새주소법정동코드   | naBjdongCd     | VARCHAR2(5)   | 옵션       | nan                             | 새주소법정동코드   |
| 새주소지상지하코드 | naUgrndCd      | VARCHAR2(1)   | 옵션       | 0                               | 새주소지상지하코드 |
| 새주소본번         | naMainBun      | NUMBER(5)     | 옵션       | 0                               | 새주소본번         |
| 새주소부번         | naSubBun       | NUMBER(5)     | 옵션       | 0                               | 새주소부번         |
| 주택가격           | hsprc          | NUMBER(15)    | 옵션       | 381000000                       | 주택가격           |
| 생성일자           | crtnDay        | VARCHAR2(8)   | 필수       | 20090320                        | 생성일자           |
| nan                | Items          | nan           | 필수       | nan                             | nan                |
| 순번               | rnum           | NUMBER(8)     | 옵션       | 1                               | 순번               |
| 대지위치           | platPlc        | VARCHAR2(200) | 필수       | 서울특별시 강남구 개포동 12번지 | 대지위치           |
| 시군구코드         | sigunguCd      | VARCHAR2(5)   | 필수       | 11680                           | 행정표준코드       |
| 법정동코드         | bjdongCd       | VARCHAR2(5)   | 필수       | 10300                           | 행정표준코드       |
| 대지구분코드       | platGbCd       | CHAR(1)       | 옵션       | 0                               | 0:대지 1:산 2:블록 |
| 번                 | bun            | VARCHAR2(4)   | 옵션       | 12                              | 번                 |
| 지                 | ji             | VARCHAR2(4)   | 옵션       | 0                               | 지                 |
| 관리건축물대장PK   | mgmBldrgstPk   | VARCHAR2(33)  | 필수       | 11680-36099                     | 관리건축물대장PK   |
| 대장구분코드       | regstrGbCd     | VARCHAR2(1)   | 옵션       | 2                               | 대장구분코드       |
| 대장구분코드명     | regstrGbCdNm   | VARCHAR2(100) | 옵션       | 집합                            | 대장구분코드명     |
| 대장종류코드       | regstrKindCd   | VARCHAR2(1)   | 옵션       | 4                               | 대장종류코드       |
| 대장종류코드명     | regstrKindCdNm | VARCHAR2(100) | 옵션       | 전유부                          | 대장종류코드명     |
| 도로명대지위치     | newPlatPlc     | VARCHAR2(200) | 옵션       | nan                             | 도로명대지위치     |
| 건물명             | bldNm          | VARCHAR2(100) | 옵션       | 대치아파트 제219동              | 건물명             |

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

| 항목명(국문)       | 항목명(영문)   | 항목크기      | 항목구분   | 샘플데이터                      | 항목설명           |
|:-------------------|:---------------|:--------------|:-----------|:--------------------------------|:-------------------|
| nan                | Items          | nan           | 필         | nan                             | nan                |
| 순번               | rnum           | NUMBER(8)     | 옵         | 1                               | 순번               |
| 대지위치           | platPlc        | VARCHAR2(200) | 필         | 서울특별시 강남구 개포동 12번지 | 대지위치           |
| 시군구코드         | sigunguCd      | VARCHAR2(5)   | 필         | 11680                           | 행정표준코드       |
| 법정동코드         | bjdongCd       | VARCHAR2(5)   | 필         | 10300                           | 행정표준코드       |
| 대지구분코드       | platGbCd       | CHAR(1)       | 옵         | 0                               | 0:대지 1:산 2:블록 |
| 번                 | bun            | VARCHAR2(4)   | 옵         | 12                              | 번                 |
| 지                 | ji             | VARCHAR2(4)   | 옵         | 0                               | 지                 |
| 관리건축물대장PK   | mgmBldrgstPk   | VARCHAR2(33)  | 필         | 11680-3633202                   | 관리건축물대장PK   |
| 대장구분코드       | regstrGbCd     | VARCHAR2(1)   | 옵         | 2                               | 대장구분코드       |
| 대장구분코드명     | regstrGbCdNm   | VARCHAR2(100) | 옵         | 집합                            | 대장구분코드명     |
| 대장종류코드       | regstrKindCd   | VARCHAR2(1)   | 옵         | 4                               | 대장종류코드       |
| 대장종류코드명     | regstrKindCdNm | VARCHAR2(100) | 옵         | 전유부                          | 대장종류코드명     |
| 도로명대지위치     | newPlatPlc     | VARCHAR2(200) | 옵         | nan                             | 도로명대지위치     |
| 건물명             | bldNm          | VARCHAR2(100) | 옵         | 대치아파트 제216동              | 건물명             |
| 특수지명           | splotNm        | VARCHAR2(200) | 옵         | nan                             | 특수지명           |
| 블록               | block          | VARCHAR2(20)  | 옵         | nan                             | 블록               |
| 로트               | lot            | VARCHAR2(20)  | 옵         | nan                             | 로트               |
| 새주소도로코드     | naRoadCd       | VARCHAR2(12)  | 옵         | nan                             | 새주소도로코드     |
| 새주소법정동코드   | naBjdongCd     | VARCHAR2(5)   | 옵         | nan                             | 새주소법정동코드   |
| 새주소지상지하코드 | naUgrndCd      | VARCHAR2(1)   | 옵         | 0                               | 새주소지상지하코드 |
| 새주소본번         | naMainBun      | NUMBER(5)     | 옵         | nan                             | 새주소본번         |
| 새주소부번         | naSubBun       | NUMBER(5)     | 옵         | nan                             | 새주소부번         |
| 동명칭             | dongNm         | VARCHAR2(100) | 옵         | 216                             | 동명칭             |
| 호명칭             | hoNm           | VARCHAR2(100) | 옵         | 303호                           | 호명칭             |
| 층구분코드         | flrGbCd        | VARCHAR2(2)   | 옵         | 20                              | 층구분코드         |
| 층구분코드명       | flrGbCdNm      | VARCHAR2(100) | 옵         | 지상                            | 층구분코드명       |
| 층번호             | flrNo          | NUMBER(4)     | 옵         | 3                               | 층번호             |
| 생성일자           | crtnDay        | VARCHAR2(8)   | 필         | 20090320                        | 생성일자           |

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

| 항목명(국문)           | 항목명(영문)   | 항목크기      | 항목구분   | 샘플데이터                      | 항목설명               |
|:-----------------------|:---------------|:--------------|:-----------|:--------------------------------|:-----------------------|
| 순번                   | rnum           | NUMBER(8)     | 옵         | 1                               | 순번                   |
| 대지위치               | platPlc        | VARCHAR2(200) | 필         | 서울특별시 강남구 개포동 12번지 | 대지위치               |
| 시군구코드             | sigunguCd      | VARCHAR2(5)   | 필         | 11680                           | 행정표준코드           |
| 법정동코드             | bjdongCd       | VARCHAR2(5)   | 필         | 10300                           | 행정표준코드           |
| 대지구분코드           | platGbCd       | CHAR(1)       | 옵         | 0                               | 0:대지 1:산 2:블록     |
| 번                     | bun            | VARCHAR2(4)   | 옵         | 12                              | 번                     |
| 지                     | ji             | VARCHAR2(4)   | 옵         | 0                               | 지                     |
| 관리건축물대장PK       | mgmBldrgstPk   | VARCHAR2(33)  | 필         | 11680-10302                     | 관리건축물대장PK       |
| 도로명대지위치         | newPlatPlc     | VARCHAR2(200) | 옵         | 서울특별시강남구개포로109길5    | 도로명대지위치         |
| 특수지명               | splotNm        | VARCHAR2(200) | 옵         | nan                             | 특수지명               |
| 블록                   | block          | VARCHAR2(20)  | 옵         | nan                             | 블록                   |
| 로트                   | lot            | VARCHAR2(20)  | 옵         | nan                             | 로트                   |
| 지역지구구역구분코드   | jijiguGbCd     | VARCHAR2(1)   | 옵         | 3                               | 지역지구구역구분코드   |
| 지역지구구역구분코드명 | jijiguGbCdNm   | VARCHAR2(100) | 옵         | 용도구역코드                    | 지역지구구역구분코드명 |
| 지역지구구역코드       | jijiguCd       | VARCHAR2(6)   | 옵         | 300                             | 지역지구구역코드       |
| 지역지구구역코드명     | jijiguCdNm     | VARCHAR2(100) | 옵         | 지구단위계획구역                | 지역지구구역코드명     |
| 대표여부               | reprYn         | VARCHAR2(1)   | 옵         | 1                               | 0: 일반 1: 대표        |
| 기타지역지구구역       | etcJijigu      | VARCHAR2(300) | 옵         | 지구단위계획구역                | 기타지역지구구역       |
| 생성일자               | crtnDay        | VARCHAR2(8)   | 필         | 20120822                        | 생성일자               |
| nan                    | Items          | nan           | 필         | nan                             | nan                    |

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
