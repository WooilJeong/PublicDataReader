# 국토교통부 주택인허가정보 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.


## 국토교통부 건축HUB 주택인허가정보 서비스

- [건축HUB_주택인허가정보 서비스 신청 페이지](https://www.data.go.kr/data/15136560/openapi.do)

<div align="center">

| **서비스명**                 | **대장 유형** |
| :---------------------------- | :-------------- |
| 주택인허가 기본개요 조회     | 기본개요       |
| 주택인허가 동별개요 조회     | 동별개요       |
| 주택인허가 층별개요 조회     | 층별개요       |
| 주택인허가 호별개요 조회     | 호별개요       |
| 주택인허가 부대시설 조회     | 부대시설       |
| 주택인허가 오수정화시설 조회     | 오수정화시설       |
| 주택인허가 주차장 조회     | 주차장       |
| 주택인허가 부설주차장 조회     | 부설주차장       |
| 주택인허가 전유공용면적 조회     | 전유공용면적       |
| 주택인허가 행위호전유공용면적 조회     | 행위호전유공용면적       |
| 주택인허가 행위개요 조회     | 행위개요       |
| 주택인허가 관리공동형별개요 조회     | 관리공동형별개요       |
| 주택인허가 관리공동부대복리시설 조회     | 관리공동부대복리시설       |
| 주택인허가 지역지구구역 조회     | 지역지구구역       |
| 주택인허가 복리분양시설 조회     | 복리분양시설       |
| 주택인허가 대지위치 조회     | 대지위치       |


</div>


## 입력 명세

* [주택인허가 기본개요 조회 서비스](#주택인허가-기본개요-조회-서비스)
* [주택인허가 동별개요 조회 서비스](#주택인허가-동별개요-조회-서비스)
* [주택인허가 층별개요 조회 서비스](#주택인허가-층별개요-조회-서비스)
* [주택인허가 호별개요 조회 서비스](#주택인허가-호별개요-조회-서비스)
* [주택인허가 부대시설 조회 서비스](#주택인허가-부대시설-조회-서비스)
* [주택인허가 오수정화시설 조회 서비스](#주택인허가-오수정화시설-조회-서비스)
* [주택인허가 주차장 조회 서비스](#주택인허가-주차장-조회-서비스)
* [주택인허가 부설주차장 조회 서비스](#주택인허가-부설주차장-조회-서비스)
* [주택인허가 전유공용면적 조회 서비스](#주택인허가-전유공용면적-조회-서비스)
* [주택인허가 행위호전유공용면적 조회 서비스](#주택인허가-행위호전유공용면적-조회-서비스)
* [주택인허가 행위개요 조회 서비스](#주택인허가-행위개요-조회-서비스)
* [주택인허가 관리공동형별개요 조회 서비스](#주택인허가-관리공동형별개요-조회-서비스)
* [주택인허가 관리공동부대복리시설 조회 서비스](#주택인허가-관리공동부대복리시설-조회-서비스)
* [주택인허가 지역지구구역 조회 서비스](#주택인허가-지역지구구역-조회-서비스)
* [주택인허가 복리분양시설 조회 서비스](#주택인허가-복리분양시설-조회-서비스)
* [주택인허가 대지위치 조회 서비스](#주택인허가-대지위치-조회-서비스)


<div align="center">

| 이름         | 설명                                                                                                                              | 데이터 타입   | 샘플 데이터   | 항목구분   |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------|:--------------|:-----------|
| service_type  | 서비스 유형<br>(기본개요, 동별개요, 층별개요, 호별개요, 부대시설, 오수정화시설, 주차장, 부설주차장, 전유공용면적, 행위호전유공용면적, 행위개요, 관리공동형별개요, 관리공동부대복리시설, 지역지구구역, 복리분양시설, 대지위치) | String        | 총괄표제부    | 필수       |
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

## 주택인허가 기본개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)   | 항목명(영문)          | 항목설명          | 샘플데이터                |
| :--------- | :---------------- | :------------- | :-------------------- |
| 건물명       | bldNm            | 건물명           | 엘지개포자이               |
| 특수지명      | splotNm          | 특수지명          |                      |
| 블록        | block            | 블록            |                      |
| 로트        | lot              | 로트            |                      |
| 용도코드      | purpsCd          | 용도코드          |                      |
| 용도코드명     | purpsCdNm        | 용도코드명         |                      |
| 구조코드      | strctCd          | 구조코드          |                      |
| 구조코드명     | strctCdNm        | 구조코드명         |                      |
| 주건축물수     | mainBldCnt       | 주건축물수         | 5                    |
| 연면적       | totArea          | 연면적           | 60358.78             |
| 총세대수(세대)  | totHhldCnt       | 총세대수(세대)      | 212                  |
| 철거멸실구분코드  | demolExtngGbCd   | 철거멸실구분코드      |                      |
| 철거멸실구분코드명 | demolExtngGbCdNm | 철거멸실구분코드명     |                      |
| 철거시작일     | demolStrtDay     | 철거시작일         |                      |
| 철거종료일     | demolEndDay      | 철거종료일         |                      |
| 철거멸실일     | demolExtngDay    | 철거멸실일         |                      |
| 건축허가일     | apprvDay         | 건축허가일         | 20040616             |
| 착공예정일     | stcnsSchedDay    | 착공예정일         |                      |
| 착공일       | stcnsDay         | 착공일           |                      |
| 사용검사예정일   | useInsptDay      | 사용검사예정일       |                      |
| 사용검사일     | useInsptSchedDay | 사용검사일         |                      |
| 생성일자      | crtnDay          | 생성일자          | 20100903             |
| 순번        | rnum             | 순번            | 1                    |
| 대지위치      | platPlc          | 대지위치          | 서울특별시 강남구 개포동 12-2번지 |
| 시군구코드     | sigunguCd        | 행정표준코드        | 11680                |
| 법정동코드     | bjdongCd         | 행정표준코드        | 10300                |
| 대지구분코드    | platGbCd         | 0:대지 1:산 2:블록 | 0                    |
| 번         | bun              | 번             | 12                   |
| 지         | ji               | 지             | 2                    |
| 관리주택대장PK  | mgmHsrgstPk      | 관리주택대장PK      | 11680-9103           |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="기본개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>용도코드</th>
      <th>용도코드명</th>
      <th>구조코드</th>
      <th>구조코드명</th>
      <th>주건축물수</th>
      <th>연면적(㎡)</th>
      <th>...</th>
      <th>사용검사예정일</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리주택대장PK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>20110925</td>
      <td>20111014</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41135-100010353</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 30 columns</p>
</div>



## 주택인허가 동별개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)       | 항목명(영문)           | 항목설명          | 샘플데이터                |
| :------------- | :----------------- | :------------- | :-------------------- |
| 주용도코드명        | mainPurpsCdNm     | 주용도코드명        | 공동주택                 |
| 세대수국민임대(세대)   | hhldCntPeplRent   | 세대수국민임대(세대)   | 0                    |
| 세대수공공임대5(세대)  | hhldCntPubRent_5  | 세대수공공임대5(세대)  | 0                    |
| 세대수공공임대10(세대) | hhldCntPubRent_10 | 세대수공공임대10(세대) | 0                    |
| 세대수공공임대기타(세대) | hhldCntPubRentEtc | 세대수공공임대기타(세대) | 0                    |
| 세대수공공임대계(세대)  | hhldCntPubRentTot | 세대수공공임대계(세대)  | 0                    |
| 세대수공공분양(세대)   | hhldCntPubLotou   | 세대수공공분양(세대)   | 0                    |
| 세대수사원임대(세대)   | hhldCntEmplRent   | 세대수사원임대(세대)   | 0                    |
| 세대수근로복지(세대)   | hhldCntLaborWlfar | 세대수근로복지(세대)   | 0                    |
| 세대수민간임대(세대)   | hhldCntCvlRent    | 세대수민간임대(세대)   | 0                    |
| 세대수민간분양(세대)   | hhldCntCvlLotou   | 세대수민간분양(세대)   | 0                    |
| 구조코드          | strctCd           | 구조코드          | 21                   |
| 구조코드명         | strctCdNm         | 구조코드명         | 철근콘크리트구조             |
| 지붕코드          | roofCd            | 지붕코드          | 10                   |
| 지붕코드명         | roofCdNm          | 지붕코드명         | (철근)콘크리트             |
| 건축면적(㎡)       | archArea          | 건축면적(㎡)       | 522.89               |
| 연면적(㎡)        | totArea           | 연면적(㎡)        | 21382.26             |
| 지하면적(㎡)       | ugrndArea         | 지하면적(㎡)       | 21382.26             |
| 용적률산정연면적(㎡)   | vlRatEstmTotArea  | 용적률산정연면적(㎡)   | 0                    |
| 지하층수          | ugrndFlrCnt       | 지하층수          | 2                    |
| 지상층수          | grndFlrCnt        | 지상층수          | 0                    |
| 높이(m)         | heit              | 높이(m)         | 0                    |
| 승용승강기수        | rideUseElvtCnt    | 승용승강기수        | 0                    |
| 비상용승강기수       | emgenUseElvtCnt   | 비상용승강기수       | 0                    |
| 층고FROM        | flrhFrom          | 층고FROM        | 0                    |
| 반자높이(m)       | ceilHeit          | 반자높이(m)       |                      |
| 계단유효폭         | stairValidWidth   | 계단유효폭         | 0                    |
| 복도너비          | hwayWidth         | 복도너비          | 0                    |
| 외벽두께          | ouwlThick         | 외벽두께          | 0                    |
| 인접세대벽두께       | adjHhldWallThick  | 인접세대벽두께       | 0                    |
| 생성일자          | crtnDay           | 생성일자          | 20100903             |
| 순번            | rnum              | 순번            | 1                    |
| 대지위치          | platPlc           | 대지위치          | 서울특별시 강남구 개포동 12-2번지 |
| 시군구코드         | sigunguCd         | 행정표준코드        | 11680                |
| 법정동코드         | bjdongCd          | 행정표준코드        | 10300                |
| 대지구분코드        | platGbCd          | 0:대지 1:산 2:블록 | 0                    |
| 번             | bun               | 번             | 12                   |
| 지             | ji                | 지             | 2                    |
| 관리동별개요PK      | mgmDongOulnPk     | 관리동별개요PK      | 11680-24903          |
| 관리주택대장PK      | mgmHsrgstPk       | 관리주택대장PK      | 11680-9103           |
| 건물명           | bldNm             | 건물명           | 엘지개포자이               |
| 특수지명          | splotNm           | 특수지명          |                      |
| 블록            | block             | 블록            |                      |
| 로트            | lot               | 로트            |                      |
| 주부속구분코드       | mainAtchGbCd      | 주부속구분코드       | 1                    |
| 주부속구분코드명      | mainAtchGbCdNm    | 주부속구분코드명      | 부속건축물                |
| 동명칭           | dongNm            | 동명칭           | 주차장                  |
| 주용도코드         | mainPurpsCd       | 주용도코드         | 2000                 |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="동별개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>주용도코드명</th>
      <th>세대수국민임대(세대)</th>
      <th>세대수공공임대5(세대)</th>
      <th>세대수공공임대10(세대)</th>
      <th>세대수공공임대기타(세대)</th>
      <th>세대수공공임대계(세대)</th>
      <th>세대수공공분양(세대)</th>
      <th>세대수사원임대(세대)</th>
      <th>세대수근로복지(세대)</th>
      <th>세대수민간임대(세대)</th>
      <th>...</th>
      <th>관리동별개요PK</th>
      <th>관리주택대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>주부속구분코드</th>
      <th>주부속구분코드명</th>
      <th>동명칭</th>
      <th>주용도코드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>제2종근린생활시설</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>41135-100005729</td>
      <td>41135-100010913</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>주건축물</td>
      <td>203동</td>
      <td>04000</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 48 columns</p>
</div>



## 주택인허가 층별개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)  | 항목명(영문)       | 항목설명          | 샘플데이터                |
| :-------- | :------------- | :------------- | :-------------------- |
| 관리층별개요PK | mgmFlrOulnPk  | 관리층별개요PK      | 11680-128503         |
| 관리동별개요PK | mgmDongOulnPk | 관리동별개요PK      | 11680-183            |
| 건물명      | bldNm         | 건물명           | 엘지개포자이               |
| 특수지명     | splotNm       | 특수지명          |                      |
| 블록       | block         | 블록            |                      |
| 로트       | lot           | 로트            |                      |
| 동명칭      | dongNm        | 동명칭           | 주차장                  |
| 층번호      | flrNo         | 층번호           | \-1                  |
| 층구분코드    | flrGbCd       | 층구분코드         | 10                   |
| 층구분코드명   | flrGbCdNm     | 층구분코드명        | 지하                   |
| 층면적(㎡)   | flrArea       | 층면적(㎡)        | 10492.76             |
| 용도코드     | purpsCd       | 용도코드          | 2001                 |
| 용도코드명    | purpsCdNm     | 용도코드명         | 아파트                  |
| 생성일자     | crtnDay       | 생성일자          | 20100903             |
| 순번       | rnum          | 순번            | 1                    |
| 대지위치     | platPlc       | 대지위치          | 서울특별시 강남구 개포동 12-2번지 |
| 시군구코드    | sigunguCd     | 행정표준코드        | 11680                |
| 법정동코드    | bjdongCd      | 행정표준코드        | 10300                |
| 대지구분코드   | platGbCd      | 0:대지 1:산 2:블록 | 0                    |
| 번        | bun           | 번             | 12                   |
| 지        | ji            | 지             | 2                    |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="층별개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>관리층별개요PK</th>
      <th>관리동별개요PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>동명칭</th>
      <th>층번호</th>
      <th>층구분코드</th>
      <th>층구분코드명</th>
      <th>...</th>
      <th>용도코드</th>
      <th>용도코드명</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41130-100018136</td>
      <td>41130-637</td>
      <td>판교 푸르지오그랑블</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>101동</td>
      <td>20</td>
      <td>20</td>
      <td>지상</td>
      <td>...</td>
      <td>02001</td>
      <td>아파트</td>
      <td>20180913</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 21 columns</p>
</div>



## 주택인허가 호별개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)  | 항목명(영문)       | 항목설명          | 샘플데이터                |
| :-------- | :------------- | :------------- | :-------------------- |
| 순번       | rnum          | 순번            | 1                    |
| 대지위치     | platPlc       | 대지위치          | 서울특별시 강남구 개포동 12-2번지 |
| 시군구코드    | sigunguCd     | 행정표준코드        | 11680                |
| 법정동코드    | bjdongCd      | 행정표준코드        | 10300                |
| 대지구분코드   | platGbCd      | 0:대지 1:산 2:블록 | 0                    |
| 번        | bun           | 번             | 12                   |
| 지        | ji            | 지             | 2                    |
| 관리호별명세PK | mgmHoDetlPk   | 관리호별명세PK      | 11680-393103         |
| 관리동별개요PK | mgmDongOulnPk | 관리동별개요PK      | 11680-24503          |
| 건물명      | bldNm         | 건물명           | 엘지개포자이               |
| 특수지명     | splotNm       | 특수지명          |                      |
| 블록       | block         | 블록            |                      |
| 로트       | lot           | 로트            |                      |
| 동명칭      | dongNm        | 동명칭           | 104동                 |
| 층번호      | flrNo         | 층번호           | 12                   |
| 층구분코드    | flrGbCd       | 층구분코드         | 20                   |
| 층구분코드명   | flrGbCdNm     | 층구분코드명        | 지상                   |
| 호번호      | hoNo          | 호번호           | 22                   |
| 호명칭      | hoNm          | 호명칭           | 1201                 |
| 평형구분명    | pngtypGbNm    | 평형구분명         | 48p                  |
| 변경구분코드   | changGbCd     | 변경구분코드        |                      |
| 변경구분코드명  | changGbCdNm   | 변경구분코드명       |                      |
| 생성일자     | crtnDay       | 생성일자          | 20100903             |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="호별개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리호별명세PK</th>
      <th>관리동별개요PK</th>
      <th>건물명</th>
      <th>...</th>
      <th>동명칭</th>
      <th>층번호</th>
      <th>층구분코드</th>
      <th>층구분코드명</th>
      <th>호번호</th>
      <th>호명칭</th>
      <th>평형구분명</th>
      <th>변경구분코드</th>
      <th>변경구분코드명</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41130-100039051</td>
      <td>41130-648</td>
      <td>판교 푸르지오그랑블</td>
      <td>...</td>
      <td>112동</td>
      <td>1</td>
      <td>20</td>
      <td>지상</td>
      <td>1</td>
      <td>101</td>
      <td>128</td>
      <td>None</td>
      <td>None</td>
      <td>20180913</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 23 columns</p>
</div>



## 주택인허가 부대시설 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)   | 항목명(영문)                | 항목설명          | 샘플데이터                                    |
| :--------- | :---------------------- | :------------- | :---------------------------------------- |
| 대지위치      | platPlc                | 대지위치          | 서울특별시 강남구 개포동 12-2번지                     |
| 시군구코드     | sigunguCd              | 행정표준코드        | 11680                                    |
| 법정동코드     | bjdongCd               | 행정표준코드        | 10300                                    |
| 대지구분코드    | platGbCd               | 0:대지 1:산 2:블록 | 0                                        |
| 번         | bun                    | 번             | 12                                       |
| 지         | ji                     | 지             | 2                                        |
| 관리주택대장PK  | mgmHsrgstPk            | 관리주택대장PK      | 11680-9103                               |
| 건물명       | bldNm                  | 건물명           | 엘지개포자이                                   |
| 특수지명      | splotNm                | 특수지명          |                                          |
| 블록        | block                  | 블록            |                                          |
| 로트        | lot                    | 로트            |                                          |
| 부대시설종류코드  | sbsdfcKindCd           | 부대시설종류코드      | 11                                       |
| 부대시설종류코드명 | sbsdfcKindCdNm         | 부대시설종류코드명     | 전기                                       |
| 기타시설종류    | etcFcKind              | 기타시설종류        |                                          |
| 설치현황      | instalCurst            | 설치현황          | 전용 60M2이하 3Kw, 60M2초과시 10M2당 0.3Kw가산     |
| 단지내현황     | cmplxinCurst           | 단지내현황         | 48평형:8Kw, 55평형:8Kw, 61A평형:9Kw, 61B평형:9Kw |
| 단지외현황     | cmplxbyndCurst         | 단지외현황         |                                          |
| 변경전설치현황   | changbefInstalCurst    | 변경전설치현황       |                                          |
| 변경전단지내현황  | changbefCmplxinCurst   | 변경전단지내현황      |                                          |
| 변경전단지외현황  | changbefCmplxbyndCurst | 변경전단지외현황      |                                          |
| 전부대종류코드   | befSbsdKindCd          | 전부대종류코드       |                                          |
| 전부대종류코드명  | befSbsdKindCdNm        | 전부대종류코드명      |                                          |
| 전기타시설종류   | befEtcFcKind           | 전기타시설종류       |                                          |
| 생성일자      | crtnDay                | 생성일자          | 20100903                                 |
| 순번        | rnum                   | 순번            | 1                                        |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="부대시설", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리주택대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>...</th>
      <th>단지내현황</th>
      <th>단지외현황</th>
      <th>변경전설치현황</th>
      <th>변경전단지내현황</th>
      <th>변경전단지외현황</th>
      <th>전부대종류코드</th>
      <th>전부대종류코드명</th>
      <th>전기타시설종류</th>
      <th>생성일자</th>
      <th>순번</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41135-100043730</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>주차차단기</td>
      <td>None</td>
      <td>None</td>
      <td>25</td>
      <td>기타시설</td>
      <td>주차차단기</td>
      <td>20211217</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 25 columns</p>
</div>



## 주택인허가 오수정화시설 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)     | 항목명(영문)      | 항목설명          | 샘플데이터                |
| :----------- | :------------ | :------------- | :-------------------- |
| 오수정화시설형식코드  | wclfModeCd   | 오수정화시설형식코드    | 300                  |
| 오수정화시설형식코드명 | wclfModeCdNm | 오수정화시설형식코드명   | 하수종말처리장연결            |
| 기타오수정화시설    | etcWclf      | 기타오수정화시설      |                      |
| 용량(인용)      | capaPsper    | 용량(인용)        | 0                    |
| 용량(루베)      | capaLube     | 용량(루베)        | 0                    |
| 동별관계구분      | dongRelGb    | 동별관계구분        |                      |
| 동별관계구분명     | dongRelGbNm  | 동별관계구분명       |                      |
| 생성일자        | crtnDay      | 생성일자          | 20100903             |
| 순번          | rnum         | 순번            | 1                    |
| 대지위치        | platPlc      | 대지위치          | 서울특별시 강남구 개포동 12-2번지 |
| 시군구코드       | sigunguCd    | 행정표준코드        | 11680                |
| 법정동코드       | bjdongCd     | 행정표준코드        | 10300                |
| 대지구분코드      | platGbCd     | 0:대지 1:산 2:블록 | 0                    |
| 번           | bun          | 번             | 12                   |
| 지           | ji           | 지             | 2                    |
| 관리주택대장PK    | mgmHsrgstPk  | 관리주택대장PK      | 11680-8703           |
| 행정동코드       | hjdongCd     | 행정동코드         | 660                  |
| 특수지명        | splotNm      | 특수지명          |                      |
| 블록          | block        | 블록            |                      |
| 로트          | lot          | 로트            |                      |
| 대표여부        | reprYn       | 0: 일반 1: 대표   | 1                    |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="오수정화시설", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>오수정화시설형식코드</th>
      <th>오수정화시설형식코드명</th>
      <th>기타오수정화시설</th>
      <th>용량(인용)</th>
      <th>용량(루베)</th>
      <th>동별관계구분</th>
      <th>동별관계구분명</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>...</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리주택대장PK</th>
      <th>행정동코드</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>대표여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>300</td>
      <td>하수종말처리장연결</td>
      <td>None</td>
      <td>0</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>20190919</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>...</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41135-100034612</td>
      <td>650</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 21 columns</p>
</div>



## 주택인허가 주차장 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)    | 항목명(영문)       | 항목설명          | 샘플데이터                |
| :---------- | :------------- | :------------- | :-------------------- |
| 순번         | rnum          | 순번            | 1                    |
| 대지위치       | platPlc       | 대지위치          | 서울특별시 강남구 개포동 12-2번지 |
| 시군구코드      | sigunguCd     | 행정표준코드        | 11680                |
| 법정동코드      | bjdongCd      | 행정표준코드        | 10300                |
| 대지구분코드     | platGbCd      | 0:대지 1:산 2:블록 | 0                    |
| 번          | bun           | 번             | 12                   |
| 지          | ji            | 지             | 2                    |
| 관리주택대장PK   | mgmHsrgstPk   | 관리주택대장PK      | 11680-9103           |
| 특수지명       | splotNm       | 특수지명          |                      |
| 블록         | block         | 블록            |                      |
| 로트         | lot           | 로트            |                      |
| 옥내자주식대수(대) | indrAutoUtcnt | 옥내자주식대수(대)    | 483                  |
| 옥내자주식면적(㎡) | indrAutoArea  | 옥내자주식면적(㎡)    | 20945.12             |
| 옥외자주식대수(대) | oudrAutoUtcnt | 옥외자주식대수(대)    | 19                   |
| 옥외자주식면적(㎡) | oudrAutoArea  | 옥외자주식면적(㎡)    | 278.5                |
| 옥내기계식대수(대) | indrMechUtcnt | 옥내기계식대수(대)    | 0                    |
| 옥내기계식면적(㎡) | indrMechArea  | 옥내기계식면적(㎡)    | 0                    |
| 옥외기계식대수(대) | oudrMechUtcnt | 옥외기계식대수(대)    | 0                    |
| 옥외기계식면적(㎡) | oudrMechArea  | 옥외기계식면적(㎡)    | 0                    |
| 인근자주식대수(대) | neigAutoUtcnt | 인근자주식대수(대)    | 0                    |
| 인근자주식면적(㎡) | neigAutoArea  | 인근자주식면적(㎡)    | 0                    |
| 인근기계식대수(대) | neigMechUtcnt | 인근기계식대수(대)    | 0                    |
| 인근기계식면적(㎡) | neigMechArea  | 인근기계식면적(㎡)    | 0                    |
| 면제대수(대)    | exmptUtcnt    | 면제대수(대)       | 0                    |
| 생성일자       | crtnDay       | 생성일자          | 20100903             |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="주차장", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리주택대장PK</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>...</th>
      <th>옥내기계식대수(대)</th>
      <th>옥내기계식면적(㎡)</th>
      <th>옥외기계식대수(대)</th>
      <th>옥외기계식면적(㎡)</th>
      <th>인근자주식대수(대)</th>
      <th>인근자주식면적(㎡)</th>
      <th>인근기계식대수(대)</th>
      <th>인근기계식면적(㎡)</th>
      <th>면제대수(대)</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41135-100034612</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>20190919</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 25 columns</p>
</div>



## 주택인허가 부설주차장 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)  | 항목명(영문)     | 항목설명          | 샘플데이터                  |
| :-------- | :----------- | :------------- | :---------------------- |
| 대지구분코드   | platGbCd    | 0:대지 1:산 2:블록 | 0                      |
| 번        | bun         | 번             | 1494                   |
| 지        | ji          | 지             | 3                      |
| 관리주택대장PK | mgmHsrgstPk | 관리주택대장PK      | 11500-100005805        |
| 행정동코드    | hjdongCd    | 행정동코드         | 605                    |
| 특수지명     | splotNm     | 특수지명          |                        |
| 블록       | block       | 블록            |                        |
| 로트       | lot         | 로트            |                        |
| 지목코드     | jimokCd     | 지목코드          | 11                     |
| 지목코드명    | jimokCdNm   | 지목코드명         | 주차장                    |
| 관련지번명    | relJibunNm  | 관련지번명         |                        |
| 생성일자     | crtnDay     | 생성일자          | 20140923               |
| 순번       | rnum        | 순번            | 1                      |
| 대지위치     | platPlc     | 대지위치          | 서울특별시 강서구 가양동 1494-3번지 |
| 시군구코드    | sigunguCd   | 행정표준코드        | 11500                  |
| 법정동코드    | bjdongCd    | 행정표준코드        | 10400                  |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="부설주차장", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리주택대장PK</th>
      <th>행정동코드</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>지목코드</th>
      <th>지목코드명</th>
      <th>관련지번명</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
</div>



## 주택인허가 전유공용면적 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)   | 항목명(영문)           | 항목설명          | 샘플데이터                 |
| :--------- | :----------------- | :------------- | :--------------------- |
| 순번        | rnum              | 순번            | 1                     |
| 대지위치      | platPlc           | 대지위치          | 서울특별시 강남구 논현동 221-7번지 |
| 시군구코드     | sigunguCd         | 행정표준코드        | 11680                 |
| 법정동코드     | bjdongCd          | 행정표준코드        | 10800                 |
| 대지구분코드    | platGbCd          | 0:대지 1:산 2:블록 | 0                     |
| 번         | bun               | 번             | 221                   |
| 지         | ji                | 지             | 7                     |
| 관리전유공용PK  | mgmExposPubusePk  | 관리전유공용PK      | 11680-10000193903     |
| 관리형별개요PK  | mgmTypeOulnPk     | 관리형별개요PK      | 11680-10000192103     |
| 전유공용구분코드  | exposPubuseGbCd   | 전유공용구분코드      | 2                     |
| 전유공용구분코드명 | exposPubuseGbCdNm | 전유공용구분코드명     | 공용                    |
| 주부속구분코드   | mainAtchGbCd      | 주부속구분코드       | 1                     |
| 주부속구분코드명  | mainAtchGbCdNm    | 주부속구분코드명      | 부속건축물                 |
| 층구분코드     | flrGbCd           | 층구분코드         | 10                    |
| 층구분코드명    | flrGbCdNm         | 층구분코드명        | 지하                    |
| 층번호       | flrNo             | 층번호           | 1                     |
| 층번호명      | flrNoNm           | 층번호명          |                       |
| 구조코드      | strctCd           | 구조코드          | 21                    |
| 구조코드명     | strctCdNm         | 구조코드명         | 철근콘크리트구조              |
| 기타구조      | etcStrct          | 기타구조          | 철근콘크리트구조              |
| 용도코드      | purpsCd           | 용도코드          | 4001                  |
| 용도코드명     | purpsCdNm         | 용도코드명         | 일반음식점                 |
| 기타용도      | etcPurps          | 기타용도          | 주차장                   |
| 면적(㎡)     | area              | 면적(㎡)         | 41.63                 |
| 생성일자      | crtnDay           | 생성일자          | 20130627              |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="전유공용면적", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리전유공용PK</th>
      <th>관리형별개요PK</th>
      <th>전유공용구분코드</th>
      <th>...</th>
      <th>층번호</th>
      <th>층번호명</th>
      <th>구조코드</th>
      <th>구조코드명</th>
      <th>기타구조</th>
      <th>용도코드</th>
      <th>용도코드명</th>
      <th>기타용도</th>
      <th>면적(㎡)</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41130-100007027</td>
      <td>41130-100002714</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>None</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>철근콘크리트구조</td>
      <td>04999</td>
      <td>기타제2종근린생활시설</td>
      <td>근린생활시설</td>
      <td>34.22</td>
      <td>20180913</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 25 columns</p>
</div>



## 주택인허가 행위호전유공용면적 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)     | 항목명(영문)               | 항목설명          | 샘플데이터               |
| :----------- | :--------------------- | :------------- | :------------------- |
| 순번          | rnum                  | 순번            | 1                   |
| 대지위치        | platPlc               | 대지위치          | 서울특별시 강남구 대치동 985번지 |
| 시군구코드       | sigunguCd             | 행정표준코드        | 11680               |
| 법정동코드       | bjdongCd              | 행정표준코드        | 10600               |
| 대지구분코드      | platGbCd              | 0:대지 1:산 2:블록 | 0                   |
| 번           | bun                   | 번             | 985                 |
| 지           | ji                    | 지             | 0                   |
| 관리행위호전유공용PK | mgmActHoExposPubusePk | 관리행위호전유공용PK   | 11680-10000796603   |
| 관리호별명세PK    | mgmHoDetlPk           | 관리호별명세PK      | 11680-10003927703   |
| 특수지명        | splotNm               | 특수지명          |                     |
| 블록          | block                 | 블록            |                     |
| 로트          | lot                   | 로트            |                     |
| 평형구분명       | pngtypGbNm            | 평형구분명         |                     |
| 전유공용구분코드    | exposPubuseGbCd       | 전유공용구분코드      | 1                   |
| 전유공용구분코드명   | exposPubuseGbCdNm     | 전유공용구분코드명     | 전유                  |
| 주부속구분코드     | mainAtchGbCd          | 주부속구분코드       | 0                   |
| 주부속구분코드명    | mainAtchGbCdNm        | 주부속구분코드명      | 주건축물                |
| 층구분코드       | flrGbCd               | 층구분코드         | 20                  |
| 층구분코드명      | flrGbCdNm             | 층구분코드명        | 지상                  |
| 층번호         | flrNo                 | 층번호           | 1                   |
| 구조코드        | strctCd               | 구조코드          | 21                  |
| 구조코드명       | strctCdNm             | 구조코드명         | 철근콘크리트구조            |
| 주용도코드       | mainPurpsCd           | 주용도코드         | 3000                |
| 주용도코드명      | mainPurpsCdNm         | 주용도코드명        | 제1종근린생활시설           |
| 기타용도        | etcPurps              | 기타용도          | 복덕방                 |
| 면적(㎡)       | area                  | 면적(㎡)         | 23.43               |
| 생성일자        | crtnDay               | 생성일자          | 20140604            |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="행위호전유공용면적", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리행위호전유공용PK</th>
      <th>관리호별명세PK</th>
      <th>특수지명</th>
      <th>...</th>
      <th>층구분코드</th>
      <th>층구분코드명</th>
      <th>층번호</th>
      <th>구조코드</th>
      <th>구조코드명</th>
      <th>주용도코드</th>
      <th>주용도코드명</th>
      <th>기타용도</th>
      <th>면적(㎡)</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41135-100001897</td>
      <td>41135-100039865</td>
      <td>None</td>
      <td>...</td>
      <td>10</td>
      <td>지하</td>
      <td>0</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>04000</td>
      <td>제2종근린생활시설</td>
      <td>복도,주차장</td>
      <td>22.71</td>
      <td>20180927</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 27 columns</p>
</div>



## 주택인허가 행위개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)  | 항목명(영문)            | 항목설명          | 샘플데이터                |
| :-------- | :------------------ | :------------- | :-------------------- |
| 특수지명     | splotNm            | 특수지명          |                      |
| 블록       | block              | 블록            |                      |
| 로트       | lot                | 로트            |                      |
| 행위구분     | actGb              | 행위구분          | 1                    |
| 행위구분코드   | actGbCd            | 행위구분코드        | 12                   |
| 행위구분코드명  | actGbCdNm          | 행위구분코드명       | 발코니확장                |
| 단지명      | cmplxNm            | 단지명           | 엘지개포자이               |
| 건축물여부    | bldYn              | 0: N 1: Y     | 1                    |
| 시설종류     | fcKind             | 시설종류          | 1                    |
| 건축면적(㎡)  | archArea           | 건축면적(㎡)       | 355.8                |
| 연면적(㎡)   | totArea            | 연면적(㎡)        | 7347.76              |
| 바닥면적(㎡)  | btmArea            | 바닥면적(㎡)       | 0                    |
| 주용도코드    | mainPurpsCd        | 주용도코드         | 2000                 |
| 주용도코드명   | mainPurpsCdNm      | 주용도코드명        | 공동주택                 |
| 기타용도     | etcPurps           | 기타용도          | 아파트                  |
| 공사면적(㎡)  | constArea          | 공사면적(㎡)       | 5.2                  |
| 지하층수     | ugrndFlrCnt        | 지하층수          | 2                    |
| 지상층수     | grndFlrCnt         | 지상층수          | 22                   |
| 총사업비     | totWkp             | 총사업비          | 0                    |
| 착공예정일    | stcnsSchedDay      | 착공예정일         | 20150430             |
| 사용검사예정일  | useInsptSchedDay   | 사용검사예정일       |                      |
| 세대수(세대)  | hhldCnt            | 세대수(세대)       | 43                   |
| 단지층수동수   | cmplxFlrCntDongCnt | 단지층수동수        | 103동-1601호           |
| 대장구분코드   | regstrGbCd         | 대장구분코드        | 2                    |
| 대장구분코드명  | regstrGbCdNm       | 대장구분코드명       | 집합                   |
| 행위전용도코드  | actBefPurpsCd      | 행위전용도코드       |                      |
| 행위전용도코드명 | actBefPurpsCdNm    | 행위전용도코드명      |                      |
| 행위전면적(㎡) | actBefArea         | 행위전면적(㎡)      |                      |
| 행위후용도코드  | actAftPurpsCd      | 행위후용도코드       |                      |
| 행위후용도코드명 | actAftPurpsCdNm    | 행위후용도코드명      |                      |
| 행위후면적(㎡) | actAftArea         | 행위후면적(㎡)      |                      |
| 시설명      | fcNm               | 시설명           |                      |
| 행위이전기타용도 | actBefEtcPurps     | 행위이전기타용도      |                      |
| 행위이후기타용도 | actAftEtcPurps     | 행위이후기타용도      |                      |
| 생성일자     | crtnDay            | 생성일자          | 20150505             |
| 순번       | rnum               | 순번            | 1                    |
| 대지위치     | platPlc            | 대지위치          | 서울특별시 강남구 개포동 12-2번지 |
| 시군구코드    | sigunguCd          | 행정표준코드        | 11680                |
| 법정동코드    | bjdongCd           | 행정표준코드        | 10300                |
| 대지구분코드   | platGbCd           | 0:대지 1:산 2:블록 | 0                    |
| 번        | bun                | 번             | 12                   |
| 지        | ji                 | 지             | 2                    |
| 관리주택대장PK | mgmHsrgstPk        | 관리주택대장PK      | 11680-10002028303    |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="행위개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>행위구분</th>
      <th>행위구분코드</th>
      <th>행위구분코드명</th>
      <th>단지명</th>
      <th>건축물여부</th>
      <th>시설종류</th>
      <th>건축면적(㎡)</th>
      <th>...</th>
      <th>행위이후기타용도</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리주택대장PK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>1</td>
      <td>10</td>
      <td>비내력벽 철거</td>
      <td>판교 푸르지오그랑블</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>...</td>
      <td>None</td>
      <td>20220224</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41135-100044663</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 43 columns</p>
</div>



## 주택인허가 관리공동형별개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)    | 항목명(영문)         | 항목설명          | 샘플데이터              |
| :---------- | :--------------- | :------------- | :------------------ |
| 관리시군구코드    | mgmSigunguCd    | 관리시군구코드       | 11680              |
| 생성일자       | crtnDay         | 생성일자          | 20100725           |
| 대지구분코드     | platGbCd        | 0:대지 1:산 2:블록 | 0                  |
| 번          | bun             | 번             | 12                 |
| 지          | ji              | 지             |                    |
| 관리공동주택대장PK | mgmCoophsrgstPk | 관리공동주택대장PK    | 11680-17903        |
| 특수지명       | splotNm         | 특수지명          |                    |
| 블록         | block           | 블록            |                    |
| 로트         | lot             | 로트            |                    |
| 형별구분       | typeGb          | 형별구분          | 14                 |
| 기타형별       | etcType         | 기타형별          |                    |
| 전용면적(㎡)    | exuseArea       | 전용면적(㎡)       | 0                  |
| 단지명        | cmplxNm         | 단지명           | 대치2단지              |
| 사업주체명      | bizBodyNm       | 사업주체명         | 서울시도시개발공사          |
| 사업승인일      | bizApprvDay     | 사업승인일         | 19911020           |
| 사용검사일      | useInsptDay     | 사용검사일         | 19921014           |
| 주건축물수      | mainBldCnt      | 주건축물수         | 0                  |
| 최고층수       | maxFlrCnt       | 최고층수          | 15                 |
| 세대수(세대)    | hhldCnt         | 세대수(세대)       | 298                |
| 구조코드       | strctCd         | 구조코드          | 22                 |
| 구조코드명      | strctCdNm       | 구조코드명         | 프리케스트콘크리트구조        |
| 승강기승용      | elvtRideUse     | 승강기승용         | 0                  |
| 승강기비상      | elvtEmgen       | 승강기비상         | 0                  |
| 대지면적(㎡)    | platArea        | 대지면적(㎡)       | 55976.6            |
| 연면적(㎡)     | totArea         | 연면적(㎡)        | 0                  |
| 건축면적(㎡)    | archArea        | 건축면적(㎡)       | 0                  |
| 복도형식코드     | hwayModeCd      | 복도형식코드        |                    |
| 복도형식코드명    | hwayModeCdNm    | 복도형식코드명       |                    |
| 수도코드       | wtspCd          | 수도코드          | 2                  |
| 수도코드명      | wtspCdNm        | 수도코드명         | 상수도                |
| 관리방식코드     | mgmMthdCd       | 관리방식코드        | 2                  |
| 관리방식코드명    | mgmMthdCdNm     | 관리방식코드명       | 위탁관리               |
| 자치관리개시일    | sfgvMgmStrtDay  | 자치관리개시일       |                    |
| 난방방식코드     | heatMthdCd      | 난방방식코드        | 2                  |
| 난방방식코드명    | heatMthdCdNm    | 난방방식코드명       | 지역난방               |
| 사용연료       | useFuel         | 사용연료          | 도시가스               |
| 주택유형구분코드   | hsStyleGbCd     | 주택유형구분코드      | 13                 |
| 주택유형구분코드명  | hsStyleGbCdNm   | 주택유형구분코드명     | 공공임대(10년)          |
| 주택형별구분코드   | hsTypeGbCd      | 주택형별구분코드      | 3                  |
| 주택형별구분코드명  | hsTypeGbCdNm    | 주택형별구분코드명     | 아파트                |
| 순번         | rnum            | 순번            | 1                  |
| 대지위치       | platPlc         | 대지위치          | 서울특별시 강남구 개포동 12번지 |
| 시군구코드      | sigunguCd       | 행정표준코드        | 11680              |
| 법정동코드      | bjdongCd        | 행정표준코드        | 10300              |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="관리공동형별개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>관리시군구코드</th>
      <th>생성일자</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리공동주택대장PK</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>형별구분</th>
      <th>...</th>
      <th>난방방식코드명</th>
      <th>사용연료</th>
      <th>주택유형구분코드</th>
      <th>주택유형구분코드명</th>
      <th>주택형별구분코드</th>
      <th>주택형별구분코드명</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41130</td>
      <td>20110818</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41130-100001909</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>130</td>
      <td>...</td>
      <td>지역난방</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>3</td>
      <td>아파트</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 44 columns</p>
</div>



## 주택인허가 관리공동부대복리시설 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)     | 항목명(영문)         | 항목설명          | 샘플데이터              |
| :----------- | :--------------- | :------------- | :------------------ |
| 순번          | rnum            | 순번            | 1                  |
| 대지위치        | platPlc         | 대지위치          | 서울특별시 강남구 개포동 12번지 |
| 시군구코드       | sigunguCd       | 행정표준코드        | 11680              |
| 법정동코드       | bjdongCd        | 행정표준코드        | 10300              |
| 대지구분코드      | platGbCd        | 0:대지 1:산 2:블록 | 0                  |
| 번           | bun             | 번             | 12                 |
| 지           | ji              | 지             |                    |
| 관리공동주택대장PK  | mgmCoophsrgstPk | 관리공동주택대장PK    | 11680-17903        |
| 특수지명        | splotNm         | 특수지명          |                    |
| 블록          | block           | 블록            |                    |
| 로트          | lot             | 로트            |                    |
| 지상주차장대수(대)  | grndPklotUtcnt  | 지상주차장대수(대)    | 440                |
| 지하주차장대수(대)  | ugrndPklotUtcnt | 지하주차장대수(대)    | 71                 |
| 총주차장대수(대)   | totPklotUtcnt   | 총주차장대수(대)     | 511                |
| 주차CCTV수     | pkngCctvCnt     | 주차CCTV수       | 0                  |
| 대표회의실면적(㎡)  | reprMtrmArea    | 대표회의실면적(㎡)    | 0                  |
| 관리소면적(㎡)    | mgmOffcArea     | 관리소면적(㎡)      | 135                |
| 놀이터CCTV수    | plgndCctvCnt    | 놀이터CCTV수      | 0                  |
| 저수조용량       | wttnkCapa       | 저수조용량         | 4940               |
| 조경면적(㎡)     | lndscArea       | 조경면적(㎡)       | 1043.4             |
| 경비실개소       | guardrmCnt      | 경비실개소         | 14                 |
| 노인정면적(㎡)    | hsoldArea       | 노인정면적(㎡)      | 254.2              |
| 생활편익시설면적(㎡) | lifeConvFcArea  | 생활편익시설면적(㎡)   | 0                  |
| 보육시설면적(㎡)   | nturFcArea      | 보육시설면적(㎡)     | 197.53             |
| 주민운동시설개소    | jmExcsFcCnt     | 주민운동시설개소      | 1                  |
| 유치원층수       | kgtFlrCnt       | 유치원층수         | 0                  |
| 유치원부지면적(㎡)  | kgtLotArea      | 유치원부지면적(㎡)    | 0                  |
| 유치원용도       | kgtPurps        | 유치원용도         |                    |
| 의료시설면적(㎡)   | mediFcArea      | 의료시설면적(㎡)     | 0                  |
| 놀이터개소       | plgndCnt        | 놀이터개소         | 5                  |
| 생성일자        | crtnDay         | 생성일자          | 20100725           |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="관리공동부대복리시설", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리공동주택대장PK</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>...</th>
      <th>노인정면적(㎡)</th>
      <th>생활편익시설면적(㎡)</th>
      <th>보육시설면적(㎡)</th>
      <th>주민운동시설개소</th>
      <th>유치원층수</th>
      <th>유치원부지면적(㎡)</th>
      <th>유치원용도</th>
      <th>의료시설면적(㎡)</th>
      <th>놀이터개소</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
  </tbody>
</table>
<p>0 rows × 31 columns</p>
</div>



## 주택인허가 지역지구구역 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)     | 항목명(영문)      | 항목설명          | 샘플데이터              |
| :----------- | :------------ | :------------- | :------------------ |
| 시군구코드       | sigunguCd    | 행정표준코드        | 11680              |
| 법정동코드       | bjdongCd     | 행정표준코드        | 10300              |
| 대지구분코드      | platGbCd     | 0:대지 1:산 2:블록 | 0                  |
| 번           | bun          | 번             | 12                 |
| 지           | ji           | 지             | 2                  |
| 관리주택대장PK    | mgmHsrgstPk  | 관리주택대장PK      | 11680-9103         |
| 특수지명        | splotNm      | 특수지명          |                    |
| 블록          | block        | 블록            |                    |
| 로트          | lot          | 로트            |                    |
| 지역지구구역구분코드  | jijiguGbCd   | 지역지구구역구분코드    | 3                  |
| 지역지구구역구분코드명 | jijiguGbCdNm | 지역지구구역구분코드명   | 용도구역코드             |
| 지역지구구역코드    | jijiguCd     | 지역지구구역코드      | 50                 |
| 지역지구구역코드명   | jijiguCdNm   | 지역지구구역코드명     | 상세계획구역             |
| 대표여부        | reprYn       | 0: 일반 1: 대표   | 1                  |
| 지역지구구역명     | jijiguNm     | 지역지구구역명       | 상세계획구역             |
| 동별관계구분      | dongRelGb    | 동별관계구분        |                    |
| 동별관계구분명     | dongRelGbNm  | 동별관계구분명       |                    |
| 생성일자        | crtnDay      | 생성일자          | 20100903           |
| 순번          | rnum         | 순번            | 1                  |
| 대지위치        | platPlc      | 대지위치          | 서울특별시 강남구 개포동 12번지 |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="지역지구구역", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리주택대장PK</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>지역지구구역구분코드</th>
      <th>지역지구구역구분코드명</th>
      <th>지역지구구역코드</th>
      <th>지역지구구역코드명</th>
      <th>대표여부</th>
      <th>지역지구구역명</th>
      <th>동별관계구분</th>
      <th>동별관계구분명</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41130-303</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>2</td>
      <td>용도지구코드</td>
      <td>160</td>
      <td>택지개발지구</td>
      <td>1</td>
      <td>택지개발지구</td>
      <td>None</td>
      <td>None</td>
      <td>20180913</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
    </tr>
  </tbody>
</table>
</div>



## 주택인허가 복리분양시설 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)     | 항목명(영문)              | 항목설명          | 샘플데이터              |
| :----------- | :-------------------- | :------------- | :------------------ |
| 변경전용도코드     | changbefPurpsCd      | 변경전용도코드       |                    |
| 변경전용도코드명    | changbefPurpsCdNm    | 변경전용도코드명      |                    |
| 변경전기타용도     | changbefEtcPurps     | 변경전기타용도       |                    |
| 변경전면적(㎡)    | changbefArea         | 변경전면적(㎡)      | 0                  |
| 변경전개소       | changbefCnt          | 변경전개소         | 0                  |
| 변경전기타현황     | changbefEtcCurst     | 변경전기타현황       |                    |
| 전복리시설종류코드   | befWlfarFcKindCd     | 전복리시설종류코드     |                    |
| 전복리시설종류코드명  | befWlfarFcKindCdNm   | 전복리시설종류코드명    |                    |
| 전기타시설       | befEtcFc             | 전기타시설         |                    |
| 생성일자        | crtnDay              | 생성일자          | 20100903           |
| 순번          | rnum                 | 순번            | 1                  |
| 대지위치        | platPlc              | 대지위치          | 서울특별시 강남구 개포동 12번지 |
| 시군구코드       | sigunguCd            | 행정표준코드        | 11680              |
| 법정동코드       | bjdongCd             | 행정표준코드        | 10300              |
| 대지구분코드      | platGbCd             | 0:대지 1:산 2:블록 | 0                  |
| 번           | bun                  | 번             | 12                 |
| 지           | ji                   | 지             | 2                  |
| 관리주택대장PK    | mgmHsrgstPk          | 관리주택대장PK      | 11680-9103         |
| 건물명         | bldNm                | 건물명           | 엘지개포자이             |
| 특수지명        | splotNm              | 특수지명          |                    |
| 블록          | block                | 블록            |                    |
| 로트          | lot                  | 로트            |                    |
| 복리분양시설종류코드  | wlfarLotouFcKindCd   | 복리분양시설종류코드    | 1000               |
| 복리분양시설종류코드명 | wlfarLotouFcKindCdNm | 복리분양시설종류코드명   | 어린이놀이터             |
| 기타시설        | etcFc                | 기타시설          |                    |
| 용도코드        | purpsCd              | 용도코드          | 1000               |
| 용도코드명       | purpsCdNm            | 용도코드명         | 단독주택               |
| 기타용도        | etcPurps             | 기타용도          |                    |
| 면적(㎡)       | area                 | 면적(㎡)         | 473.23             |
| 개소          | openCnt              | 개소            | 1                  |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="복리분양시설", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>변경전용도코드</th>
      <th>변경전용도코드명</th>
      <th>변경전기타용도</th>
      <th>변경전면적(㎡)</th>
      <th>변경전개소</th>
      <th>변경전기타현황</th>
      <th>전복리시설종류코드</th>
      <th>전복리시설종류코드명</th>
      <th>전기타시설</th>
      <th>생성일자</th>
      <th>...</th>
      <th>블록</th>
      <th>로트</th>
      <th>복리분양시설종류코드</th>
      <th>복리분양시설종류코드명</th>
      <th>기타시설</th>
      <th>용도코드</th>
      <th>용도코드명</th>
      <th>기타용도</th>
      <th>면적(㎡)</th>
      <th>개소</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>20180913</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>90000</td>
      <td>기타복리시설</td>
      <td>주민공동시설</td>
      <td>02006</td>
      <td>복리시설</td>
      <td>None</td>
      <td>2197.0139</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 30 columns</p>
</div>



## 주택인허가 대지위치 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)  | 항목명(영문)      | 항목설명          | 샘플데이터              |
| :-------- | :------------ | :------------- | :------------------ |
| 순번       | rnum         | 순번            | 1                  |
| 대지위치     | platPlc      | 대지위치          | 서울특별시 강남구 개포동 12번지 |
| 시군구코드    | sigunguCd    | 행정표준코드        | 11680              |
| 법정동코드    | bjdongCd     | 행정표준코드        | 10300              |
| 대지구분코드   | platGbCd     | 0:대지 1:산 2:블록 | 0                  |
| 번        | bun          | 번             | 12                 |
| 지        | ji           | 지             | 2                  |
| 관리주택대장PK | mgmHsrgstPk  | 관리주택대장PK      | 11680-9103         |
| 대표여부     | reprYn       | 0: 일반 1: 대표   | 1                  |
| 행정동코드    | hjdongCd     | 행정동코드         | 660                |
| 특수지명     | splotNm      | 특수지명          |                    |
| 블록       | block        | 블록            |                    |
| 로트       | lot          | 로트            |                    |
| 지목코드     | jimokCd      | 지목코드          |                    |
| 지목코드명    | jimokCdNm    | 지목코드명         |                    |
| 관련지번명    | relJibunNm   | 관련지번명         |                    |
| 대지면적(㎡)  | platArea     | 대지면적(㎡)       | 15487.3            |
| 최저대지폭    | minPlatWidth | 최저대지폭         | 0                  |
| 최고대지폭    | maxPlatWidth | 최고대지폭         | 0                  |
| 동별관계구분   | dongRelGb    | 동별관계구분        |                    |
| 동별관계구분명  | dongRelGbNm  | 동별관계구분명       |                    |
| 생성일자     | crtnDay      | 생성일자          | 20100903           |

</div>


```python
from PublicDataReader import HousingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = HousingLicense(service_key)

df = api.get_data(
    service_type="대지위치", 
    sigungu_code="41135", 
    bdong_code="11000", 
    bun="542", 
    ji="",
)
df.head(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리주택대장PK</th>
      <th>대표여부</th>
      <th>행정동코드</th>
      <th>...</th>
      <th>로트</th>
      <th>지목코드</th>
      <th>지목코드명</th>
      <th>관련지번명</th>
      <th>대지면적(㎡)</th>
      <th>최저대지폭</th>
      <th>최고대지폭</th>
      <th>동별관계구분</th>
      <th>동별관계구분명</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 542번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0542</td>
      <td>0000</td>
      <td>41135-100026626</td>
      <td>1</td>
      <td>610</td>
      <td>...</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>20170114</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 22 columns</p>
</div>


