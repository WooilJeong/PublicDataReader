# 국토교통부 건축물대장정보 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.


## 국토교통부 건축물대장정보 서비스

- [건축물대장정보 서비스 신청 페이지](https://www.data.go.kr/data/15044713/openapi.do)

<div align="center">

| **서비스명**                 | **대장 유형** |
| :---------------------------- | :-------------- |
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

## 국토교통부 건축소유자정보 서비스

- [건축소유자정보 서비스 신청 페이지](https://www.data.go.kr/data/15021136/openapi.do)

<div align="center">

| **서비스명**                 | **대장 유형** |
| :---------------------------- | :-------------- |
| 건축물소유정보 조회           | 소유자       |

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
* [건축물소유정보 조회 서비스](#건축물소유정보-조회-서비스)

<div align="center">

| 이름         | 설명                                                                                                                              | 데이터 타입   | 샘플 데이터   | 항목구분   |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------|:--------------|:-----------|
| ledger_type  | 건축물대장 유형<br>(기본개요, 총괄표제부, 표제부, 층별개요, 부속지번, 전유공용면적, 오수정화시설, 주택가격, 전유부, 지역지구구역, 소유자) | String        | 총괄표제부    | 필수       |
| sigungu_code | 시군구의 5자리 지역코드<br>(서울 서초구: 11650, 경기 성남 분당구: 41135)                                                          | String        | 41135         | 필수       |
| bdong_code   | 읍면동의 5자리 지역코드<br>(서울 서초구 잠원동: 10600, 경기 성남 분당구 백현동: 11000)                                            | String        | 11000         | 필수       |
| plat_code    | 대지구분 코드<br>(대지: 0, 산: 1, 블록: 2)                                                                                        | String        | 540           | 선택       |
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

| 항목명(국문)         | 항목명(영문)   | 샘플데이터                      |
|:---------------------|:---------------|:--------------------------------|
| 도로명대지위치       | newPlatPlc     | nan                             |
| 건물명               | bldNm          | 대치아파트 제217동              |
| 특수지명             | splotNm        | nan                             |
| 블록                 | block          | nan                             |
| 로트                 | lot            | nan                             |
| 외필지수             | bylotCnt       | 0                               |
| 새주소도로코드       | naRoadCd       | nan                             |
| 새주소법정동코드     | naBjdongCd     | nan                             |
| 새주소지상지하코드   | naUgrndCd      | 0                               |
| 새주소본번           | naMainBun      | nan                             |
| 새주소부번           | naSubBun       | nan                             |
| 지역코드             | jiyukCd        | nan                             |
| 지구코드             | jiguCd         | nan                             |
| 구역코드             | guyukCd        | nan                             |
| 지역코드명           | jiyukCdNm      | nan                             |
| 지구코드명           | jiguCdNm       | nan                             |
| 구역코드명           | guyukCdNm      | nan                             |
| 생성일자             | crtnDay        | 20090320                        |
| nan                  | Items          | nan                             |
| 순번                 | rnum           | 1                               |
| 대지위치             | platPlc        | 서울특별시 강남구 개포동 12번지 |
| 시군구코드           | sigunguCd      | 11680                           |
| 법정동코드           | bjdongCd       | 10300                           |
| 대지구분코드         | platGbCd       | 0                               |
| 번                   | bun            | 12                              |
| 지                   | ji             | 0                               |
| 관리건축물대장PK     | mgmBldrgstPk   | 11680-8520602                   |
| 관리상위건축물대장PK | mgmUpBldrgstPk | 11680-91502                     |
| 대장구분코드         | regstrGbCd     | 2                               |
| 대장구분코드명       | regstrGbCdNm   | 집합                            |
| 대장종류코드         | regstrKindCd   | 4                               |

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

| 항목명(국문)         | 항목명(영문)       | 항목설명             | 샘플데이터                      |
|:---------------------|:-------------------|:---------------------|:--------------------------------|
| 지능형건축물등급     | itgBldGrade        | 지능형건축물등급     | nan                             |
| 지능형건축물인증점수 | itgBldCert         | 지능형건축물인증점수 | 0                               |
| 생성일자             | crtnDay            | 생성일자             | 20120822                        |
| 새주소법정동코드     | naBjdongCd         | 새주소법정동코드     | 10301                           |
| 새주소지상지하코드   | naUgrndCd          | 새주소지상지하코드   | 0                               |
| 새주소본번           | naMainBun          | 새주소본번           | 5                               |
| 새주소부번           | naSubBun           | 새주소부번           | 0                               |
| 대지면적(㎡)         | platArea           | 대지면적(㎡)         | 0                               |
| 건축면적(㎡)         | archArea           | 건축면적(㎡)         | 15324.37                        |
| 건폐율(%)            | bcRat              | 건폐율(%)            | 0                               |
| 연면적(㎡)           | totArea            | 연면적(㎡)           | 223939                          |
| 용적률산정연면적(㎡) | vlRatEstmTotArea   | 용적률산정연면적(㎡) | 211555.54                       |
| 용적률(%)            | vlRat              | 용적률(%)            | 0                               |
| 주용도코드           | mainPurpsCd        | 주용도코드           | 2000                            |
| 주용도코드명         | mainPurpsCdNm      | 주용도코드명         | 공동주택                        |
| 기타용도             | etcPurps           | 기타용도             | 주거시설 근린생활시설           |
| 세대수(세대)         | hhldCnt            | 세대수(세대)         | 4199                            |
| 가구수(가구)         | fmlyCnt            | 가구수(가구)         | 0                               |
| 주건축물수           | mainBldCnt         | 주건축물수           | 27                              |
| 부속건축물수         | atchBldCnt         | 부속건축물수         | 3                               |
| 부속건축물면적(㎡)   | atchBldArea        | 부속건축물면적(㎡)   | 64.26                           |
| 총주차수             | totPkngCnt         | 총주차수             | 0                               |
| 옥내기계식대수(대)   | indrMechUtcnt      | 옥내기계식대수(대)   | 0                               |
| 옥내기계식면적(㎡)   | indrMechArea       | 옥내기계식면적(㎡)   | 0                               |
| 옥외기계식대수(대)   | oudrMechUtcnt      | 옥외기계식대수(대)   | 0                               |
| 옥외기계식면적(㎡)   | oudrMechArea       | 옥외기계식면적(㎡)   | 0                               |
| 옥내자주식대수(대)   | indrAutoUtcnt      | 옥내자주식대수(대)   | 0                               |
| 옥내자주식면적(㎡)   | indrAutoArea       | 옥내자주식면적(㎡)   | 0                               |
| 옥외자주식대수(대)   | oudrAutoUtcnt      | 옥외자주식대수(대)   | 0                               |
| 옥외자주식면적(㎡)   | oudrAutoArea       | 옥외자주식면적(㎡)   | 0                               |
| 허가일               | pmsDay             | 허가일               | nan                             |
| 착공일               | stcnsDay           | 착공일               | nan                             |
| 사용승인일           | useAprDay          | 사용승인일           | nan                             |
| 허가번호년           | pmsnoYear          | 허가번호년           | nan                             |
| 허가번호기관코드     | pmsnoKikCd         | 허가번호기관코드     | nan                             |
| 허가번호기관코드명   | pmsnoKikCdNm       | 허가번호기관코드명   | nan                             |
| 허가번호구분코드     | pmsnoGbCd          | 허가번호구분코드     | nan                             |
| 허가번호구분코드명   | pmsnoGbCdNm        | 허가번호구분코드명   | nan                             |
| 호수(호)             | hoCnt              | 호수(호)             | 0                               |
| 에너지효율등급       | engrGrade          | 에너지효율등급       | nan                             |
| 에너지절감율         | engrRat            | 에너지절감율         | 0                               |
| EPI점수              | engrEpi            | EPI점수              | 0                               |
| 친환경건축물등급     | gnBldGrade         | 친환경건축물등급     | nan                             |
| 친환경건축물인증점수 | gnBldCert          | 친환경건축물인증점수 | 0                               |
| nan                  | Items              | nan                  | nan                             |
| 순번                 | rnum               | 순번                 | 1                               |
| 대지위치             | platPlc            | 대지위치             | 서울특별시 강남구 개포동 12번지 |
| 시군구코드           | sigunguCd          | 행정표준코드         | 11680                           |
| 법정동코드           | bjdongCd           | 행정표준코드         | 10300                           |
| 대지구분코드         | platGbCd           | 0:대지 1:산 2:블록   | 0                               |
| 번                   | bun                | 번                   | 12                              |
| 지                   | ji                 | 지                   | 0                               |
| 관리건축물대장PK     | mgmBldrgstPk       | 관리건축물대장PK     | 11680-10302                     |
| 대장구분코드         | regstrGbCd         | 대장구분코드         | 2                               |
| 대장구분코드명       | regstrGbCdNm       | 대장구분코드명       | 집합                            |
| 대장종류코드         | regstrKindCd       | 대장종류코드         | 1                               |
| 대장종류코드명       | regstrKindCdNm     | 대장종류코드명       | 총괄표제부                      |
| 신구대장구분코드     | newOldRegstrGbCd   | 신구대장구분코드     | 0                               |
| 신구대장구분코드명   | newOldRegstrGbCdNm | 신구대장구분코드명   | 구대장                          |
| 도로명대지위치       | newPlatPlc         | 도로명대지위치       | 서울특별시강남구개포로109길5    |
| 건물명               | bldNm              | 건물명               | 대치,대청 아파트                |
| 특수지명             | splotNm            | 특수지명             | nan                             |
| 블록                 | block              | 블록                 | nan                             |
| 로트                 | lot                | 로트                 | nan                             |
| 외필지수             | bylotCnt           | 외필지수             | 0                               |
| 새주소도로코드       | naRoadCd           | 새주소도로코드       | 116804166040                    |

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

| 항목명(국문)         | 항목명(영문)        | 항목설명                         | 샘플데이터                      |
|:---------------------|:--------------------|:---------------------------------|:--------------------------------|
| 주용도코드명         | mainPurpsCdNm       | 주용도코드명                     | 교육연구시설                    |
| 기타용도             | etcPurps            | 용도정보(건축물대장 주용도 정보) | 교육연구시설                    |
| 지붕코드             | roofCd              | 지붕코드                         | 90                              |
| 지붕코드명           | roofCdNm            | 지붕코드명                       | 기타지붕                        |
| 기타지붕             | etcRoof             | 지붕정보(건축물대장 지붕 정보)   | 아스팔트슁글                    |
| 세대수(세대)         | hhldCnt             | 세대수(세대)                     | 0                               |
| 가구수(가구)         | fmlyCnt             | 가구수(가구)                     | 0                               |
| 높이(m)              | heit                | 높이(m)                          | 0                               |
| 지상층수             | grndFlrCnt          | 지상층수                         | 2                               |
| 지하층수             | ugrndFlrCnt         | 지하층수                         | 0                               |
| 승용승강기수         | rideUseElvtCnt      | 승용승강기수                     | 0                               |
| 비상용승강기수       | emgenUseElvtCnt     | 비상용승강기수                   | 0                               |
| 부속건축물수         | atchBldCnt          | 부속건축물수                     | 0                               |
| 부속건축물면적(㎡)   | atchBldArea         | 부속건축물면적(㎡)               | 0                               |
| 총동연면적(㎡)       | totDongTotArea      | 총동연면적(㎡)                   | 536.06                          |
| 옥내기계식대수(대)   | indrMechUtcnt       | 옥내기계식대수(대)               | 0                               |
| 옥내기계식면적(㎡)   | indrMechArea        | 옥내기계식면적(㎡)               | 0                               |
| 옥외기계식대수(대)   | oudrMechUtcnt       | 옥외기계식대수(대)               | 0                               |
| 옥외기계식면적(㎡)   | oudrMechArea        | 옥외기계식면적(㎡)               | 0                               |
| 옥내자주식대수(대)   | indrAutoUtcnt       | 옥내자주식대수(대)               | 0                               |
| 옥내자주식면적(㎡)   | indrAutoArea        | 옥내자주식면적(㎡)               | 0                               |
| 옥외자주식대수(대)   | oudrAutoUtcnt       | 옥외자주식대수(대)               | 0                               |
| 옥외자주식면적(㎡)   | oudrAutoArea        | 옥외자주식면적(㎡)               | 0                               |
| 허가일               | pmsDay              | 허가일                           | 19891226                        |
| 착공일               | stcnsDay            | 착공일                           | nan                             |
| 사용승인일           | useAprDay           | 사용승인일                       | 19911120                        |
| 허가번호년           | pmsnoYear           | 허가번호년                       | nan                             |
| 허가번호기관코드     | pmsnoKikCd          | 허가번호기관코드                 | nan                             |
| 허가번호기관코드명   | pmsnoKikCdNm        | 허가번호기관코드명               | nan                             |
| 허가번호구분코드     | pmsnoGbCd           | 허가번호구분코드                 | nan                             |
| 허가번호구분코드명   | pmsnoGbCdNm         | 허가번호구분코드명               | nan                             |
| 호수(호)             | hoCnt               | 호수(호)                         | 0                               |
| 에너지효율등급       | engrGrade           | 에너지효율등급                   | nan                             |
| 에너지절감율         | engrRat             | 에너지절감율                     | 0                               |
| EPI점수              | engrEpi             | EPI점수                          | 0                               |
| 친환경건축물등급     | gnBldGrade          | 친환경건축물등급                 | nan                             |
| 친환경건축물인증점수 | gnBldCert           | 친환경건축물인증점수             | 0                               |
| 지능형건축물등급     | itgBldGrade         | 지능형건축물등급                 | nan                             |
| 지능형건축물인증점수 | itgBldCert          | 지능형건축물인증점수             | 0                               |
| 생성일자             | crtnDay             | 생성일자                         | 20131207                        |
| nan                  | Items               | nan                              | nan                             |
| 순번                 | rnum                | 순번                             | 1                               |
| 대지위치             | platPlc             | 대지위치                         | 서울특별시 강남구 개포동 12번지 |
| 시군구코드           | sigunguCd           | 행정표준코드                     | 11680                           |
| 법정동코드           | bjdongCd            | 행정표준코드                     | 10300                           |
| 대지구분코드         | platGbCd            | 0:대지 1:산 2:블록               | 0                               |
| 번                   | bun                 | 번                               | 12                              |
| 지                   | ji                  | 지                               | 0                               |
| 관리건축물대장PK     | mgmBldrgstPk        | 관리건축물대장PK                 | 11680-700402                    |
| 대장구분코드         | regstrGbCd          | 대장구분코드                     | 1                               |
| 대장구분코드명       | regstrGbCdNm        | 대장구분코드명                   | 일반                            |
| 대장종류코드         | regstrKindCd        | 대장종류코드                     | 2                               |
| 대장종류코드명       | regstrKindCdNm      | 대장종류코드명                   | 일반건축물                      |
| 도로명대지위치       | newPlatPlc          | 도로명대지위치                   | nan                             |
| 건물명               | bldNm               | 건물명                           | nan                             |
| 특수지명             | splotNm             | 특수지명                         | nan                             |
| 블록                 | block               | 블록                             | nan                             |
| 로트                 | lot                 | 로트                             | nan                             |
| 외필지수             | bylotCnt            | 외필지수                         | 0                               |
| 새주소도로코드       | naRoadCd            | 새주소도로코드                   | nan                             |
| 새주소법정동코드     | naBjdongCd          | 새주소법정동코드                 | nan                             |
| 새주소지상지하코드   | naUgrndCd           | 새주소지상지하코드               | 0                               |
| 새주소본번           | naMainBun           | 새주소본번                       | nan                             |
| 새주소부번           | naSubBun            | 새주소부번                       | nan                             |
| 동명칭               | dongNm              | 동명칭                           | nan                             |
| 주부속구분코드       | mainAtchGbCd        | 주부속구분코드                   | 0                               |
| 주부속구분코드명     | mainAtchGbCdNm      | 주부속구분코드명                 | 주건축물                        |
| 대지면적(㎡)         | platArea            | 대지면적(㎡)                     | 0                               |
| 건축면적(㎡)         | archArea            | 건축면적(㎡)                     | 271.63                          |
| 건폐율(%)            | bcRat               | 건폐율(%)                        | 0                               |
| 연면적(㎡)           | totArea             | 연면적(㎡)                       | 536.06                          |
| 용적률산정연면적(㎡) | vlRatEstmTotArea    | 용적률산정연면적(㎡)             | 536.06                          |
| 용적률(%)            | vlRat               | 용적률(%)                        | 0                               |
| 구조코드             | strctCd             | 구조코드                         | 11                              |
| 구조코드명           | strctCdNm           | 구조코드명                       | 벽돌구조                        |
| 기타구조             | etcStrct            | 구조정보(건축물대장 주구조 정보) | 연와조                          |
| 주용도코드           | mainPurpsCd         | 주용도코드                       | 10000                           |
| 내진설계적용여부     | rserthqkDsgnApplyYn | 내진 설계 적용 여부              | 1                               |
| 내진능력             | rserthqkAblty       | 내진 능력                        | VII-0.169g                      |

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

| 항목명(국문)       | 항목명(영문)   | 항목설명                  | 샘플데이터                      |
|:-------------------|:---------------|:--------------------------|:--------------------------------|
| 순번               | rnum           | 순번                      | 1                               |
| 대지위치           | platPlc        | 대지위치                  | 서울특별시 강남구 개포동 12번지 |
| 시군구코드         | sigunguCd      | 행정표준코드              | 11680                           |
| 법정동코드         | bjdongCd       | 행정표준코드              | 10300                           |
| 대지구분코드       | platGbCd       | 0:대지 1:산 2:블록        | 0                               |
| 번                 | bun            | 번                        | 12                              |
| 지                 | ji             | 지                        | 0                               |
| 관리건축물대장PK   | mgmBldrgstPk   | 관리건축물대장PK          | 11680-700402                    |
| 도로명대지위치     | newPlatPlc     | 도로명대지위치            | nan                             |
| 건물명             | bldNm          | 건물명                    | nan                             |
| 특수지명           | splotNm        | 특수지명                  | nan                             |
| 블록               | block          | 블록                      | nan                             |
| 로트               | lot            | 로트                      | nan                             |
| 새주소도로코드     | naRoadCd       | 새주소도로코드            | nan                             |
| 새주소법정동코드   | naBjdongCd     | 새주소법정동코드          | nan                             |
| 새주소지상지하코드 | naUgrndCd      | 새주소지상지하코드        | 0                               |
| 새주소본번         | naMainBun      | 새주소본번                | nan                             |
| 새주소부번         | naSubBun       | 새주소부번                | nan                             |
| 동명칭             | dongNm         | 동명칭                    | nan                             |
| 층구분코드         | flrGbCd        | 층구분코드                | 20                              |
| 층구분코드명       | flrGbCdNm      | 층구분코드명              | 지상                            |
| 층번호             | flrNo          | 층번호                    | 1                               |
| 층번호명           | flrNoNm        | 층번호명                  | 1층                             |
| 구조코드           | strctCd        | 구조코드                  | 11                              |
| 구조코드명         | strctCdNm      | 구조코드명                | 벽돌구조                        |
| 기타구조           | etcStrct       | 구조정보(건축물대장 구조) | 연와조                          |
| 주용도코드         | mainPurpsCd    | 주용도코드                | 10999                           |
| 주용도코드명       | mainPurpsCdNm  | 주용도코드명              | 기타교육연구시설                |
| 기타용도           | etcPurps       | 용도정보(건축물대장 용도) | 교육연구및복지시설              |
| 주부속구분코드     | mainAtchGbCd   | 주부속구분코드            | 0                               |
| 주부속구분코드명   | mainAtchGbCdNm | 주부속구분코드명          | 주건축물                        |
| 면적(㎡)           | area           | 면적(㎡)                  | 271.63                          |
| 면적제외여부       | areaExctYn     | 0: N 1: Y                 | nan                             |
| 생성일자           | crtnDay        | 생성일자                  | 20131207                        |
| nan                | Items          | nan                       | nan                             |

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

| 항목명(국문)       | 항목명(영문)     | 항목설명           | 샘플데이터                        |
|:-------------------|:-----------------|:-------------------|:----------------------------------|
| 대지구분코드       | platGbCd         | 0:대지 1:산 2:블록 | 0                                 |
| 번                 | bun              | 번                 | 12                                |
| 지                 | ji               | 지                 | 5                                 |
| 관리건축물대장PK   | mgmBldrgstPk     | 관리건축물대장PK   | 11680-1920002                     |
| 대장구분코드       | regstrGbCd       | 대장구분코드       | 1                                 |
| 대장구분코드명     | regstrGbCdNm     | 대장구분코드명     | 일반                              |
| 대장종류코드       | regstrKindCd     | 대장종류코드       | 2                                 |
| 대장종류코드명     | regstrKindCdNm   | 대장종류코드명     | 일반건축물                        |
| 도로명대지위치     | newPlatPlc       | 도로명대지위치     | 서울특별시강남구개포로613         |
| 건물명             | bldNm            | 건물명             | nan                               |
| 특수지명           | splotNm          | 특수지명           | nan                               |
| 블록               | block            | 블록               | nan                               |
| 로트               | lot              | 로트               | nan                               |
| 새주소도로코드     | naRoadCd         | 새주소도로코드     | 116803122001                      |
| 새주소법정동코드   | naBjdongCd       | 새주소법정동코드   | 10301                             |
| 새주소지상지하코드 | naUgrndCd        | 새주소지상지하코드 | 0                                 |
| 새주소본번         | naMainBun        | 새주소본번         | 613                               |
| 새주소부번         | naSubBun         | 새주소부번         | 0                                 |
| 부속대장구분코드   | atchRegstrGbCd   | 부속대장구분코드   | 1                                 |
| 부속대장구분코드명 | atchRegstrGbCdNm | 부속대장구분코드명 | 일반                              |
| 부속시군구코드     | atchSigunguCd    | 부속시군구코드     | 11680                             |
| 부속법정동코드     | atchBjdongCd     | 부속법정동코드     | 10300                             |
| 부속대지구분코드   | atchPlatGbCd     | 부속대지구분코드   | 0                                 |
| 부속번             | atchBun          | 부속번             | 12                                |
| 부속지             | atchJi           | 부속지             | 48                                |
| 부속특수지명       | atchSplotNm      | 부속특수지명       | nan                               |
| 부속블록           | atchBlock        | 부속블록           | nan                               |
| 부속로트           | atchLot          | 부속로트           | nan                               |
| 부속기타지번명     | atchEtcJibunNm   | 부속기타지번명     | nan                               |
| 생성일자           | crtnDay          | 생성일자           | 20140325                          |
| nan                | Items            | nan                | nan                               |
| 순번               | rnum             | 순번               | 1                                 |
| 대지위치           | platPlc          | 대지위치           | 서울특별시 강남구 개포동 12-5번지 |
| 시군구코드         | sigunguCd        | 행정표준코드       | 11680                             |
| 법정동코드         | bjdongCd         | 행정표준코드       | 10300                             |

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

| 항목명(국문)       | 항목명(영문)      | 항목설명           | 샘플데이터                      |
|:-------------------|:------------------|:-------------------|:--------------------------------|
| 대장구분코드       | regstrGbCd        | 대장구분코드       | 2                               |
| 대장구분코드명     | regstrGbCdNm      | 대장구분코드명     | 집합                            |
| 대장종류코드       | regstrKindCd      | 대장종류코드       | 4                               |
| 대장종류코드명     | regstrKindCdNm    | 대장종류코드명     | 전유부                          |
| 도로명대지위치     | newPlatPlc        | 도로명대지위치     | nan                             |
| 건물명             | bldNm             | 건물명             | 대치아파트 제219동              |
| 특수지명           | splotNm           | 특수지명           | nan                             |
| 블록               | block             | 블록               | nan                             |
| 로트               | lot               | 로트               | nan                             |
| 새주소도로코드     | naRoadCd          | 새주소도로코드     | nan                             |
| 새주소법정동코드   | naBjdongCd        | 새주소법정동코드   | nan                             |
| 새주소지상지하코드 | naUgrndCd         | 새주소지상지하코드 | 0                               |
| 새주소본번         | naMainBun         | 새주소본번         | nan                             |
| 새주소부번         | naSubBun          | 새주소부번         | nan                             |
| 동명칭             | dongNm            | 동명칭             | 219                             |
| 호명칭             | hoNm              | 호명칭             | 1502호                          |
| 층구분코드         | flrGbCd           | 층구분코드         | 20                              |
| 층구분코드명       | flrGbCdNm         | 층구분코드명       | 지상                            |
| 층번호             | flrNo             | 층번호             | 15                              |
| 층번호명           | flrNoNm           | 층번호명           | 15층                            |
| 전유공용구분코드   | exposPubuseGbCd   | 전유공용구분코드   | 1                               |
| 전유공용구분코드명 | exposPubuseGbCdNm | 전유공용구분코드명 | 전유                            |
| 주부속구분코드     | mainAtchGbCd      | 주부속구분코드     | 0                               |
| 주부속구분코드명   | mainAtchGbCdNm    | 주부속구분코드명   | 주건축물                        |
| 구조코드           | strctCd           | 구조코드           | 21                              |
| 구조코드명         | strctCdNm         | 구조코드명         | 철근콘크리트구조                |
| 기타구조           | etcStrct          | 기타구조           | 철근콘크리트구조                |
| 주용도코드         | mainPurpsCd       | 주용도코드         | 2001                            |
| 주용도코드명       | mainPurpsCdNm     | 주용도코드명       | 아파트                          |
| 기타용도           | etcPurps          | 기타용도           | 아파트(일부공유면적포함)        |
| 면적(㎡)           | area              | 면적(㎡)           | 49.86                           |
| 생성일자           | crtnDay           | 생성일자           | 20090320                        |
| nan                | Items             | nan                | nan                             |
| 순번               | rnum              | 순번               | 1                               |
| 대지위치           | platPlc           | 대지위치           | 서울특별시 강남구 개포동 12번지 |
| 시군구코드         | sigunguCd         | 행정표준코드       | 11680                           |
| 법정동코드         | bjdongCd          | 행정표준코드       | 10300                           |
| 대지구분코드       | platGbCd          | 0:대지 1:산 2:블록 | 0                               |
| 번                 | bun               | 번                 | 12                              |
| 지                 | ji                | 지                 | 0                               |
| 관리건축물대장PK   | mgmBldrgstPk      | 관리건축물대장PK   | 11680-3609902                   |

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

| 항목명(국문)       | 항목명(영문)   | 항목설명           | 샘플데이터                      |
|:-------------------|:---------------|:-------------------|:--------------------------------|
| 지                 | ji             | 지                 | 0                               |
| 관리건축물대장PK   | mgmBldrgstPk   | 관리건축물대장PK   | 11680-10302                     |
| 대장구분코드       | regstrGbCd     | 대장구분코드       | 2                               |
| 대장구분코드명     | regstrGbCdNm   | 대장구분코드명     | 집합                            |
| 대장종류코드       | regstrKindCd   | 대장종류코드       | 1                               |
| 대장종류코드명     | regstrKindCdNm | 대장종류코드명     | 집합                            |
| 도로명대지위치     | newPlatPlc     | 도로명대지위치     | 서울특별시강남구개포로109길5    |
| 건물명             | bldNm          | 건물명             | 대치,대청 아파트                |
| 특수지명           | splotNm        | 특수지명           | nan                             |
| 블록               | block          | 블록               | nan                             |
| 로트               | lot            | 로트               | nan                             |
| 새주소도로코드     | naRoadCd       | 새주소도로코드     | 116804166040                    |
| 새주소법정동코드   | naBjdongCd     | 새주소법정동코드   | 10301                           |
| 새주소지상지하코드 | naUgrndCd      | 새주소지상지하코드 | 0                               |
| 새주소본번         | naMainBun      | 새주소본번         | 5                               |
| 새주소부번         | naSubBun       | 새주소부번         | 0                               |
| 형식코드           | modeCd         | 형식코드           | 299                             |
| 형식코드명         | modeCdNm       | 형식코드명         | 기타단독정화조                  |
| 기타형식           | etcMode        | 기타형식           | nan                             |
| 단위구분코드       | unitGbCd       | 단위구분코드       | nan                             |
| 단위구분코드명     | unitGbCdNm     | 단위구분코드명     | nan                             |
| 용량(인용)         | capaPsper      | 용량(인용)         | 300                             |
| 용량(루베)         | capaLube       | 용량(루베)         | 0                               |
| 생성일자           | crtnDay        | 생성일자           | 20120822                        |
| nan                | Items          | nan                | nan                             |
| 순번               | rnum           | 순번               | 1                               |
| 대지위치           | platPlc        | 대지위치           | 서울특별시 강남구 개포동 12번지 |
| 시군구코드         | sigunguCd      | 행정표준코드       | 11680                           |
| 법정동코드         | bjdongCd       | 행정표준코드       | 10300                           |
| 대지구분코드       | platGbCd       | 0:대지 1:산 2:블록 | 0                               |
| 번                 | bun            | 번                 | 12                              |

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

| 항목명(국문)       | 항목명(영문)   | 항목설명           | 샘플데이터                      |
|:-------------------|:---------------|:-------------------|:--------------------------------|
| 특수지명           | splotNm        | 특수지명           | nan                             |
| 블록               | block          | 블록               | nan                             |
| 로트               | lot            | 로트               | nan                             |
| 외필지수           | bylotCnt       | 외필지수           | 0                               |
| 새주소도로코드     | naRoadCd       | 새주소도로코드     | nan                             |
| 새주소법정동코드   | naBjdongCd     | 새주소법정동코드   | nan                             |
| 새주소지상지하코드 | naUgrndCd      | 새주소지상지하코드 | 0                               |
| 새주소본번         | naMainBun      | 새주소본번         | 0                               |
| 새주소부번         | naSubBun       | 새주소부번         | 0                               |
| 주택가격           | hsprc          | 주택가격           | 381000000                       |
| 생성일자           | crtnDay        | 생성일자           | 20090320                        |
| nan                | Items          | nan                | nan                             |
| 순번               | rnum           | 순번               | 1                               |
| 대지위치           | platPlc        | 대지위치           | 서울특별시 강남구 개포동 12번지 |
| 시군구코드         | sigunguCd      | 행정표준코드       | 11680                           |
| 법정동코드         | bjdongCd       | 행정표준코드       | 10300                           |
| 대지구분코드       | platGbCd       | 0:대지 1:산 2:블록 | 0                               |
| 번                 | bun            | 번                 | 12                              |
| 지                 | ji             | 지                 | 0                               |
| 관리건축물대장PK   | mgmBldrgstPk   | 관리건축물대장PK   | 11680-36099                     |
| 대장구분코드       | regstrGbCd     | 대장구분코드       | 2                               |
| 대장구분코드명     | regstrGbCdNm   | 대장구분코드명     | 집합                            |
| 대장종류코드       | regstrKindCd   | 대장종류코드       | 4                               |
| 대장종류코드명     | regstrKindCdNm | 대장종류코드명     | 전유부                          |
| 도로명대지위치     | newPlatPlc     | 도로명대지위치     | nan                             |
| 건물명             | bldNm          | 건물명             | 대치아파트 제219동              |

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

| 항목명(국문)       | 항목명(영문)   | 항목설명           | 샘플데이터                      |
|:-------------------|:---------------|:-------------------|:--------------------------------|
| nan                | Items          | nan                | nan                             |
| 순번               | rnum           | 순번               | 1                               |
| 대지위치           | platPlc        | 대지위치           | 서울특별시 강남구 개포동 12번지 |
| 시군구코드         | sigunguCd      | 행정표준코드       | 11680                           |
| 법정동코드         | bjdongCd       | 행정표준코드       | 10300                           |
| 대지구분코드       | platGbCd       | 0:대지 1:산 2:블록 | 0                               |
| 번                 | bun            | 번                 | 12                              |
| 지                 | ji             | 지                 | 0                               |
| 관리건축물대장PK   | mgmBldrgstPk   | 관리건축물대장PK   | 11680-3633202                   |
| 대장구분코드       | regstrGbCd     | 대장구분코드       | 2                               |
| 대장구분코드명     | regstrGbCdNm   | 대장구분코드명     | 집합                            |
| 대장종류코드       | regstrKindCd   | 대장종류코드       | 4                               |
| 대장종류코드명     | regstrKindCdNm | 대장종류코드명     | 전유부                          |
| 도로명대지위치     | newPlatPlc     | 도로명대지위치     | nan                             |
| 건물명             | bldNm          | 건물명             | 대치아파트 제216동              |
| 특수지명           | splotNm        | 특수지명           | nan                             |
| 블록               | block          | 블록               | nan                             |
| 로트               | lot            | 로트               | nan                             |
| 새주소도로코드     | naRoadCd       | 새주소도로코드     | nan                             |
| 새주소법정동코드   | naBjdongCd     | 새주소법정동코드   | nan                             |
| 새주소지상지하코드 | naUgrndCd      | 새주소지상지하코드 | 0                               |
| 새주소본번         | naMainBun      | 새주소본번         | nan                             |
| 새주소부번         | naSubBun       | 새주소부번         | nan                             |
| 동명칭             | dongNm         | 동명칭             | 216                             |
| 호명칭             | hoNm           | 호명칭             | 303호                           |
| 층구분코드         | flrGbCd        | 층구분코드         | 20                              |
| 층구분코드명       | flrGbCdNm      | 층구분코드명       | 지상                            |
| 층번호             | flrNo          | 층번호             | 3                               |
| 생성일자           | crtnDay        | 생성일자           | 20090320                        |

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

| 항목명(국문)           | 항목명(영문)   | 항목설명               | 샘플데이터                      |
|:-----------------------|:---------------|:-----------------------|:--------------------------------|
| 순번                   | rnum           | 순번                   | 1                               |
| 대지위치               | platPlc        | 대지위치               | 서울특별시 강남구 개포동 12번지 |
| 시군구코드             | sigunguCd      | 행정표준코드           | 11680                           |
| 법정동코드             | bjdongCd       | 행정표준코드           | 10300                           |
| 대지구분코드           | platGbCd       | 0:대지 1:산 2:블록     | 0                               |
| 번                     | bun            | 번                     | 12                              |
| 지                     | ji             | 지                     | 0                               |
| 관리건축물대장PK       | mgmBldrgstPk   | 관리건축물대장PK       | 11680-10302                     |
| 도로명대지위치         | newPlatPlc     | 도로명대지위치         | 서울특별시강남구개포로109길5    |
| 특수지명               | splotNm        | 특수지명               | nan                             |
| 블록                   | block          | 블록                   | nan                             |
| 로트                   | lot            | 로트                   | nan                             |
| 지역지구구역구분코드   | jijiguGbCd     | 지역지구구역구분코드   | 3                               |
| 지역지구구역구분코드명 | jijiguGbCdNm   | 지역지구구역구분코드명 | 용도구역코드                    |
| 지역지구구역코드       | jijiguCd       | 지역지구구역코드       | 300                             |
| 지역지구구역코드명     | jijiguCdNm     | 지역지구구역코드명     | 지구단위계획구역                |
| 대표여부               | reprYn         | 0: 일반 1: 대표        | 1                               |
| 기타지역지구구역       | etcJijigu      | 기타지역지구구역       | 지구단위계획구역                |
| 생성일자               | crtnDay        | 생성일자               | 20120822                        |

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


## 건축물소유정보 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)      | 항목명(영문)          | 항목설명         | 샘플데이터              |
| :------------ | :---------------- | :------------ | :------------------ |
| 관리건축물대장PK    | mgm_bldrgst_pk   | 관리건축물대장PK    | 11680-145318       |
| 시군구코드        | sigungu_cd       | 시군구코드        | 11680              |
| 시군구명         | sigungu_nm       | 시군구          | 강남구                |
| 법정동코드        | bjdong_cd        | 법정동          | 10100              |
| 법정동명         | bjdong_nm        | 법정동          | 역삼동                |
| 대지구분코드       | plat_gb_cd       | 대지구분         | 0                  |
| 대지구분명        | plat_gb_nm       | 대지구분         | 대지                 |
| 번            | bun              | 번            | 601                |
| 지            | ji               | 지            | 1                  |
| 특수지명         | splot_nm         | 특수지명         |                    |
| 블록           | block            | 블록           |                    |
| 로트           | lot              | 로트           |                    |
| 새주소대지위치      | na_plat_plc      | 새주소대지위치      | 서울특별시 강남구 봉은사로 110 |
| 새주소도로코드      | na_road_cd       | 새주소도로코드      | 1.16803E+11        |
| 새주소법정동코드     | na_bjdong_cd     | 새주소법정동코드     | 10101              |
| 새주소지상지하코드    | na_ugrnd_cd      | 새주소지상지하코드    | 0                  |
| 새주소지상지하명     | na_ugrnd_nm      | 새주소지상지하      | 지상                 |
| 새주소본번        | na_main_bun      | 새주소본번        | 110                |
| 새주소부번        | na_sub_bun       | 새주소부번        | 0                  |
| 대장구분코드       | regstr_gb_cd     | 대장구분         | 2                  |
| 대장구분명        | regstr_gb_nm     | 대장구분         | 집합                 |
| 대장종류코드       | regstr_kind_cd   | 대장종류         | 4                  |
| 대장종류명        | regstr_kind_nm   | 대장종류         | 전유부                |
| 건물명          | bld_nm           | 건물명          | 연우빌딩               |
| 동명칭          | dong_nm          | 동            | 연우빌딩               |
| 호명칭          | ho_nm            | 호            | 101                |
| 면적           | area             | 면적           | 106.98             |
| 소유구분코드       | own_gb_cd        | 소유구분         | 1                  |
| 소유구분명        | own_gb_nm        | 소유구분         | 개인                 |
| 주민구분코드       | jm_gb_cd         | 주민구분         | 1                  |
| 주민구분명        | jm_gb_nm         | 주민구분         | 내국인                |
| 성명           | nm               | 성명           | 유\*\*              |
| 지분1          | quota1           | 지분1          | 100                |
| 지분2          | quota2           | 지분2          | 100                |
| 소유권지분        | ownsh_quota      | 소유권지분        | 100/100            |
| 변동원인일        | chang_caus_day   | 변동원인일        | 20040823           |
| 소재지시군구코드     | loc_sigungu_cd   | 소재지시군구       |                    |
| 소재지시군구명      | loc_sigungu_nm   | 소재지시군구       |                    |
| 소재지법정동코드     | loc_bjdong_cd    | 소재지법정동       |                    |
| 소재지법정동명      | loc_bjdong_nm    | 소재지법정동       |                    |
| 소재지상세주소      | loc_detl_addr    | 소재지상세주소      |                    |
| 새주소소재지대지위치   | na_loc_plat_plc  | 새주소소재지대지위치   |                    |
| 새주소소재지도로코드   | na_loc_road_cd   | 새주소소재지도로     |                    |
| 새주소소재지법정동코드  | na_loc_bjdong_cd | 새주소소재지법정동    |                    |
| 새주소소재지상세주소   | na_loc_detl_addr | 새주소소재지상세주소   |                    |
| 새주소소재지지상지하코드 | na_loc_ugrnd_cd  | 새주소소재지지상지하코드 |                    |
| 새주소소재지지상지하명  | na_loc_ugrnd_nm  | 새주소소재지지상지하명  |                    |
| 새주소소재지본번     | na_loc_main_bun  | 새주소소재지본번     |                    |
| 주민번호         | jmno             | 사용하지 않음      |                    |
| 새주소소재지부번     | na_loc_sub_bun   | 새주소소재지부번     |                    |

</div>

```python
from PublicDataReader import BuildingLedger

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLedger(service_key)

df = api.get_data(
    ledger_type="소유자", 
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
      <th>관리건축물대장PK</th>
      <th>시군구코드</th>
      <th>시군구명</th>
      <th>법정동코드</th>
      <th>법정동명</th>
      <th>대지구분코드</th>
      <th>대지구분명</th>
      <th>번</th>
      <th>지</th>
      <th>특수지명</th>
      <th>...</th>
      <th>소재지상세주소</th>
      <th>새주소소재지대지위치</th>
      <th>새주소소재지도로코드</th>
      <th>새주소소재지법정동코드</th>
      <th>새주소소재지상세주소</th>
      <th>새주소소재지지상지하코드</th>
      <th>새주소소재지지상지하명</th>
      <th>새주소소재지본번</th>
      <th>주민번호</th>
      <th>새주소소재지부번</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41135-100225802</td>
      <td>41135</td>
      <td>성남시 분당구</td>
      <td>11000</td>
      <td>백현동</td>
      <td>0</td>
      <td>대지</td>
      <td>0542</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>지상</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>41135-100225928</td>
      <td>41135</td>
      <td>성남시 분당구</td>
      <td>11000</td>
      <td>백현동</td>
      <td>0</td>
      <td>대지</td>
      <td>0542</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>지상</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>2</th>
      <td>41135-100225928</td>
      <td>41135</td>
      <td>성남시 분당구</td>
      <td>11000</td>
      <td>백현동</td>
      <td>0</td>
      <td>대지</td>
      <td>0542</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>지상</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>3</th>
      <td>41135-100225976</td>
      <td>41135</td>
      <td>성남시 분당구</td>
      <td>11000</td>
      <td>백현동</td>
      <td>0</td>
      <td>대지</td>
      <td>0542</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>지상</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>4</th>
      <td>41135-100225980</td>
      <td>41135</td>
      <td>성남시 분당구</td>
      <td>11000</td>
      <td>백현동</td>
      <td>0</td>
      <td>대지</td>
      <td>0542</td>
      <td>0000</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>지상</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 50 columns</p>
</div>
