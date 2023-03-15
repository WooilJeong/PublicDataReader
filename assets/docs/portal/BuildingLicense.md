# 국토교통부 건축인허가정보 사용 가이드

[공공데이터포털](https://www.data.go.kr)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [공공데이터포털](https://www.data.go.kr)에 회원가입을 하고 원하는 오픈 API 서비스를 신청해야 합니다. 공공데이터포털에서 API를 신청하면 일반적으로 1~2시간 이내에 호출이 가능합니다. 그러나 일부 API의 경우 인증 절차가 24시간 이상 소요될 수 있습니다.


## 국토교통부 건축인허가정보 서비스

- [건축인허가정보 서비스 신청 페이지](https://www.data.go.kr/data/15044678/openapi.do)

<div align="center">

| **서비스명**                 | **대장 유형** |
| :---------------------------- | :-------------- |
| 건축인허가 기본개요 조회     | 기본개요       |
| 건축인허가 동별개요 조회     | 동별개요       |
| 건축인허가 층별개요 조회     | 층별개요       |
| 건축인허가 호별개요 조회     | 호별개요       |
| 건축인허가 대수선 조회     | 대수선       |
| 건축인허가 공작물관리대장 조회     | 공작물관리대장       |
| 건축인허가 철거멸실관리대장 조회     | 철거멸실관리대장       |
| 건축인허가 가설건축물 조회     | 가설건축물       |
| 건축인허가 오수정화시설 조회     | 오수정화시설       |
| 건축인허가 주차장 조회     | 주차장       |
| 건축인허가 부설주차장 조회     | 부설주차장       |
| 건축인허가 전유공용면적 조회     | 전유공용면적       |
| 건축인허가 호별전유공용면적 조회     | 호별전유공용면적       |
| 건축인허가 지역지구구역 조회     | 지역지구구역       |
| 건축인허가 도로명대장 조회     | 도로명대장       |
| 건축인허가 대지위치 조회     | 대지위치       |
| 건축인허가 주택유형 조회     | 주택유형       |

</div>


## 입력 명세

* [건축인허가 기본개요 조회 서비스](#건축인허가-기본개요-조회-서비스)
* [건축인허가 동별개요 조회 서비스](#건축인허가-동별개요-조회-서비스)
* [건축인허가 층별개요 조회 서비스](#건축인허가-층별개요-조회-서비스)
* [건축인허가 호별개요 조회 서비스](#건축인허가-호별개요-조회-서비스)
* [건축인허가 대수선 조회 서비스](#건축인허가-대수선-조회-서비스)
* [건축인허가 공작물관리대장 조회 서비스](#건축인허가-공작물관리대장-조회-서비스)
* [건축인허가 철거멸실관리대장 조회 서비스](#건축인허가-철거멸실관리대장-조회-서비스)
* [건축인허가 가설건축물 조회 서비스](#건축인허가-가설건축물-조회-서비스)
* [건축인허가 오수정화시설 조회 서비스](#건축인허가-오수정화시설-조회-서비스)
* [건축인허가 주차장 조회 서비스](#건축인허가-주차장-조회-서비스)
* [건축인허가 부설주차장 조회 서비스](#건축인허가-부설주차장-조회-서비스)
* [건축인허가 전유공용면적 조회 서비스](#건축인허가-전유공용면적-조회-서비스)
* [건축인허가 호별전유공용면적 조회 서비스](#건축인허가-호별전유공용면적-조회-서비스)
* [건축인허가 지역지구구역 조회 서비스](#건축인허가-지역지구구역-조회-서비스)
* [건축인허가 도로명대장 조회 서비스](#건축인허가-도로명대장-조회-서비스)
* [건축인허가 대지위치 조회 서비스](#건축인허가-대지위치-조회-서비스)
* [건축인허가 주택유형 조회 서비스](#건축인허가-주택유형-조회-서비스)


<div align="center">

| 이름         | 설명                                                                                                                              | 데이터 타입   | 샘플 데이터   | 항목구분   |
|:-------------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------|:--------------|:-----------|
| service_type  | 서비스 유형<br>(기본개요, 동별개요, 층별개요, 호별개요, 대수선, 공작물관리대장, 철거멸실관리대장, 가설건축물, 오수정화시설, 주차장, 부설주차장, 전유공용면적, 호별전유공용면적, 지역지구구역, 도로명대장, 대지위치, 주택유형) | String        | 총괄표제부    | 필수       |
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

## 건축인허가 기본개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)         | 항목명(영문)     | 항목설명             | 샘플데이터                        |
|:---------------------|:-----------------|:---------------------|:----------------------------------|
| 구역코드명           | guyukCdNm        | 구역코드명           | 지구단위계획구역                  |
| 지목코드             | jimokCd          | 지목코드             | 8                                 |
| 지역코드             | jiyukCd          | 지역코드             | UQA123                            |
| 지구코드             | jiguCd           | 지구코드             | nan                               |
| 구역코드             | guyukCd          | 구역코드             | UQQ300                            |
| 건축구분코드         | archGbCdNm       | 건축구분코드         | 700                               |
| 건축구분코드명       | archGbCd         | 건축구분코드명       | 용도변경                          |
| 대지면적(㎡)         | platArea         | 대지면적(㎡)         | 2272                              |
| 건축면적(㎡)         | archArea         | 건축면적(㎡)         | 1152.45                           |
| 건폐율(%)            | bcRat            | 건폐율(%)            | 50.72                             |
| 연면적(㎡)           | totArea          | 연면적(㎡)           | 16074.93                          |
| 용적률산정연면적(㎡) | vlRatEstmTotArea | 용적률산정연면적(㎡) | 9074.07                           |
| 용적률(%)            | vlRat            | 용적률(%)            | 399.38                            |
| 주건축물수           | mainBldCnt       | 주건축물수           | 1                                 |
| 부속건축물동수       | atchBldDongCnt   | 부속건축물동수       | 0                                 |
| 주용도코드           | mainPurpsCd      | 주용도코드           | 4000                              |
| 주용도코드명         | mainPurpsCdNm    | 주용도코드명         | 제2종근린생활시설                 |
| 세대수(세대)         | hhldCnt          | 세대수(세대)         | 96                                |
| 호수(호)             | hoCnt            | 호수(호)             | 0                                 |
| 가구수(가구)         | fmlyCnt          | 가구수(가구)         | 0                                 |
| 총주차수             | totPkngCnt       | 총주차수             | 0                                 |
| 착공예정일           | stcnsSchedDay    | 착공예정일           | nan                               |
| 착공연기일           | stcnsDelayDay    | 착공연기일           | nan                               |
| 실제착공일           | realStcnsDay     | 실제착공일           | nan                               |
| 건축허가일           | archPmsDay       | 건축허가일           | 20110117                          |
| 사용승인일           | useAprDay        | 사용승인일           | 20110214                          |
| 생성일자             | crtnDay          | 생성일자             | 20110215                          |
| 순번                 | rnum             | 순번                 | 1                                 |
| 대지위치             | platPlc          | 대지위치             | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드           | sigunguCd        | 행정표준코드         | 11680                             |
| 법정동코드           | bjdongCd         | 행정표준코드         | 10300                             |
| 대지구분코드         | platGbCd         | 0:대지 1:산 2:블록   | 0                                 |
| 번                   | bun              | 번                   | 12                                |
| 지                   | ji               | 지                   | 4                                 |
| 관리허가대장PK       | mgmPmsrgstPk     | 관리허가대장PK       | 11680-10003070401                 |
| 건물명               | bldNm            | 건물명               | 석탑프라자                        |
| 특수지명             | splotNm          | 특수지명             | nan                               |
| 블록                 | block            | 블록                 | nan                               |
| 로트                 | lot              | 로트                 | nan                               |
| 지목코드명           | jimokCdNm        | 지목코드명           | 대                                |
| 지역코드명           | jiyukCdNm        | 지역코드명           | 제3종일반주거지역                 |
| 지구코드명           | jiguCdNm         | 지구코드명           | nan                               |

</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="기본개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>구역코드명</th>
      <th>지목코드</th>
      <th>지역코드</th>
      <th>지구코드</th>
      <th>구역코드</th>
      <th>건축구분코드</th>
      <th>건축구분코드명</th>
      <th>대지면적(㎡)</th>
      <th>건축면적(㎡)</th>
      <th>건폐율(%)</th>
      <th>...</th>
      <th>번</th>
      <th>지</th>
      <th>관리허가대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>지목코드명</th>
      <th>지역코드명</th>
      <th>지구코드명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>02</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>1682</td>
      <td>45</td>
      <td>0</td>
      <td>...</td>
      <td>0132</td>
      <td>0190</td>
      <td>41135-100059345</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>답</td>
      <td>None</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 42 columns</p>
</div>



## 건축인허가 동별개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)         | 항목명(영문)     | 항목설명             | 샘플데이터                        |
|:---------------------|:-----------------|:---------------------|:----------------------------------|
| 로트                 | lot              | 로트                 | nan                               |
| 주부속구분코드       | mainAtchGbCd     | 주부속구분코드       | 0                                 |
| 주부속구분코드명     | mainAtchGbCdNm   | 주부속구분코드명     | 주건축물                          |
| 주용도코드           | mainPurpsCd      | 주용도코드           | Z8000                             |
| 주용도코드명         | mainPurpsCdNm    | 주용도코드명         | 교육연구및복지시설                |
| 호수(호)             | hoCnt            | 호수(호)             | 0                                 |
| 가구수(가구)         | fmlyCnt          | 가구수(가구)         | 0                                 |
| 세대수(세대)         | hhldCnt          | 세대수(세대)         | 0                                 |
| 구조코드             | strctCd          | 구조코드             | 21                                |
| 구조코드명           | strctCdNm        | 구조코드명           | 철근콘크리트구조                  |
| 지붕코드             | roofCd           | 지붕코드             | 10                                |
| 지붕코드명           | roofCdNm         | 지붕코드명           | (철근)콘크리트                    |
| 건축면적(㎡)         | archArea         | 건축면적(㎡)         | 1152.45                           |
| 연면적(㎡)           | totArea          | 연면적(㎡)           | 16074.93                          |
| 용적률산정연면적(㎡) | vlRatEstmTotArea | 용적률산정연면적(㎡) | 0                                 |
| 생성일자             | crtnDay          | 생성일자             | 20090320                          |
| 순번                 | rnum             | 순번                 | 1                                 |
| 대지위치             | platPlc          | 대지위치             | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드           | sigunguCd        | 행정표준코드         | 11680                             |
| 법정동코드           | bjdongCd         | 행정표준코드         | 10300                             |
| 대지구분코드         | platGbCd         | 0:대지 1:산 2:블록   | 0                                 |
| 번                   | bun              | 번                   | 12                                |
| 지                   | ji               | 지                   | 4                                 |
| 관리동별개요PK       | mgmDongOulnPk    | 관리동별개요PK       | 11680-1304701                     |
| 관리허가대장PK       | mgmPmsrgstPk     | 관리허가대장PK       | 11680-1282301                     |
| 건물명               | bldNm            | 건물명               | 석탑프라자                        |
| 특수지명             | splotNm          | 특수지명             | 석탑프라자 605호                  |
| 블록                 | block            | 블록                 | nan                               |
| 승용승강기수         | rideUseElvtCnt   | 승용승강기수         | 2                                 |
| 비상용승강기수       | emgenUseElvtCnt  | 비상용승강기수       | 1                                 |

    
</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="동별개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>로트</th>
      <th>주부속구분코드</th>
      <th>주부속구분코드명</th>
      <th>주용도코드</th>
      <th>주용도코드명</th>
      <th>호수(호)</th>
      <th>가구수(가구)</th>
      <th>세대수(세대)</th>
      <th>구조코드</th>
      <th>구조코드명</th>
      <th>...</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리동별개요PK</th>
      <th>관리허가대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>승용승강기수</th>
      <th>비상용승강기수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>28000</td>
      <td>가설건축물</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>99</td>
      <td>기타구조</td>
      <td>...</td>
      <td>0</td>
      <td>0132</td>
      <td>0190</td>
      <td>41135-100085858</td>
      <td>41135-100059345</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 30 columns</p>
</div>



## 건축인허가 층별개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)   | 항목명(영문)   | 항목설명           | 샘플데이터                        |
|:---------------|:---------------|:-------------------|:----------------------------------|
| 건축구분코드명 | archGbCd       | 건축구분코드명     | nan                               |
| 생성일자       | crtnDay        | 생성일자           | 20090320                          |
| 순번           | rnum           | 순번               | 1                                 |
| 대지위치       | platPlc        | 대지위치           | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드     | sigunguCd      | 행정표준코드       | 11680                             |
| 법정동코드     | bjdongCd       | 행정표준코드       | 10300                             |
| 대지구분코드   | platGbCd       | 0:대지 1:산 2:블록 | 0                                 |
| 번             | bun            | 번                 | 12                                |
| 지             | ji             | 지                 | 4                                 |
| 관리층별개요PK | mgmFlrOulnPk   | 관리층별개요PK     | 11680-2256201                     |
| 관리동별개요PK | mgmDongOulnPk  | 관리동별개요PK     | 11680-443601                      |
| 관리허가대장PK | mgmPmsrgstPk   | 관리허가대장PK     | 11680-440201                      |
| 건물명         | bldNm          | 건물명             | 2023-12-04 00:00:00               |
| 특수지명       | splotNm        | 특수지명           | nan                               |
| 블록           | block          | 블록               | nan                               |
| 로트           | lot            | 로트               | nan                               |
| 구조코드       | strctCd        | 구조코드           | 21                                |
| 구조코드명     | strctCdNm      | 구조코드명         | 철근콘크리트구조                  |
| 주용도코드     | mainPurpsCd    | 주용도코드         | Z5000                             |
| 주용도코드명   | mainPurpsCdNm  | 주용도코드명       | 문화및집회시설                    |
| 층번호         | flrNo          | 층번호             | 4                                 |
| 층면적(㎡)     | flrArea        | 층면적(㎡)         | 1110.75                           |
| 층구분코드     | flrGbCd        | 층구분코드         | 20                                |
| 층구분코드명   | flrGbCdNm      | 층구분코드명       | 지상                              |
| 건축구분코드   | archGbCdNm     | 건축구분코드       | nan                               |


</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="층별개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>건축구분코드명</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리층별개요PK</th>
      <th>...</th>
      <th>로트</th>
      <th>구조코드</th>
      <th>구조코드명</th>
      <th>주용도코드</th>
      <th>주용도코드명</th>
      <th>층번호</th>
      <th>층면적(㎡)</th>
      <th>층구분코드</th>
      <th>층구분코드명</th>
      <th>건축구분코드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0100</td>
      <td>20220718</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 132-190번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0132</td>
      <td>0190</td>
      <td>41135-100145353</td>
      <td>...</td>
      <td>None</td>
      <td>99</td>
      <td>기타구조</td>
      <td>28004</td>
      <td>공사용가설건축물</td>
      <td>1</td>
      <td>18</td>
      <td>20</td>
      <td>지상</td>
      <td>신축</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 25 columns</p>
</div>



## 건축인허가 호별개요 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)   | 항목명(영문)   | 항목설명           | 샘플데이터                        |
|:---------------|:---------------|:-------------------|:----------------------------------|
| 순번           | rnum           | 순번               | 1                                 |
| 대지위치       | platPlc        | 대지위치           | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드     | sigunguCd      | 행정표준코드       | 11680                             |
| 법정동코드     | bjdongCd       | 행정표준코드       | 10300                             |
| 대지구분코드   | platGbCd       | 0:대지 1:산 2:블록 | 0                                 |
| 번             | bun            | 번                 | 12                                |
| 지             | ji             | 지                 | 4                                 |
| 관리호별명세PK | mgmHoDetlPk    | 관리호별명세PK     | 11680-10000998301                 |
| 관리동별개요PK | mgmDongOulnPk  | 관리동별개요PK     | 11680-10003265101                 |
| 관리허가대장PK | mgmPmsrgstPk   | 관리허가대장PK     | 11680-10003070401                 |
| 특수지명       | splotNm        | 특수지명           | nan                               |
| 블록           | block          | 블록               | nan                               |
| 로트           | lot            | 로트               | nan                               |
| 호번호         | hoNo           | 호번호             | 0                                 |
| 호명칭         | hoNm           | 호명칭             | 701호                             |
| 평형구분명     | pngtypGbNm     | 평형구분명         | 701호                             |
| 층번호         | flrNo          | 층번호             | 7                                 |
| 층구분코드     | flrGbCd        | 층구분코드         | 20                                |
| 층구분코드명   | flrGbCdNm      | 층구분코드명       | 지상                              |
| 변경구분코드   | changGbCd      | 변경구분코드       | nan                               |
| 변경구분코드명 | changGbCdNm    | 변경구분코드명     | nan                               |
| 생성일자       | crtnDay        | 생성일자           | 20110215                          |
    
</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="호별개요", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리허가대장PK</th>
      <th>...</th>
      <th>로트</th>
      <th>호번호</th>
      <th>호명칭</th>
      <th>평형구분명</th>
      <th>층번호</th>
      <th>층구분코드</th>
      <th>층구분코드명</th>
      <th>변경구분코드</th>
      <th>변경구분코드명</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 370번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0370</td>
      <td>0000</td>
      <td>41135-100081707</td>
      <td>41135-100108177</td>
      <td>41135-100065255</td>
      <td>...</td>
      <td>None</td>
      <td>0</td>
      <td>None</td>
      <td>None</td>
      <td>2</td>
      <td>20</td>
      <td>지상</td>
      <td>None</td>
      <td>None</td>
      <td>20220701</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 22 columns</p>
</div>



## 건축인허가 대수선 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">



| 항목명(국문)         | 항목명(영문)      | 항목설명             | 샘플데이터                        |
|:---------------------|:------------------|:---------------------|:----------------------------------|
| 대수선구분코드명     | imprprGbCdNm      | 대수선구분코드명     | 방화구획                          |
| 대수선변경구분코드   | imprprChangGbCd   | 대수선변경구분코드   | 4                                 |
| 대수선변경구분코드명 | imprprChangGbCdNm | 대수선변경구분코드명 | 변경                              |
| 생성일자             | crtnDay           | 생성일자             | 20140313                          |
| 순번                 | rnum              | 순번                 | 1                                 |
| 대지위치             | platPlc           | 대지위치             | 서울특별시 강남구 개포동 13-3번지 |
| 시군구코드           | sigunguCd         | 행정표준코드         | 11680                             |
| 법정동코드           | bjdongCd          | 행정표준코드         | 10300                             |
| 대지구분코드         | platGbCd          | 0:대지 1:산 2:블록   | 0                                 |
| 번                   | bun               | 번                   | 13                                |
| 지                   | ji                | 지                   | 3                                 |
| 관리허가대장PK       | mgmPmsrgstPk      | 관리허가대장PK       | 11680-10003529201                 |
| 건물명               | bldNm             | 건물명               | 대청타워                          |
| 특수지명             | splotNm           | 특수지명             | nan                               |
| 블록                 | block             | 블록                 | nan                               |
| 로트                 | lot               | 로트                 | nan                               |
| 대수선구분코드       | imprprGbCd        | 대수선구분코드       | 6                                 |


</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="대수선", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>대수선구분코드명</th>
      <th>대수선변경구분코드</th>
      <th>대수선변경구분코드명</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리허가대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>대수선구분코드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>주계단</td>
      <td>None</td>
      <td>None</td>
      <td>20090320</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 366-10번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0366</td>
      <td>0010</td>
      <td>41135-13251</td>
      <td>분당로 주유소</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>07</td>
    </tr>
  </tbody>
</table>
</div>



## 건축인허가 공작물관리대장 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)     | 항목명(영문)   | 항목설명           | 샘플데이터                        |
|:-----------------|:---------------|:-------------------|:----------------------------------|
| 순번             | rnum           | 순번               | 1                                 |
| 대지위치         | platPlc        | 대지위치           | 서울특별시 강남구 논현동 6-13번지 |
| 시군구코드       | sigunguCd      | 행정표준코드       | 11680                             |
| 법정동코드       | bjdongCd       | 행정표준코드       | 10800                             |
| 대지구분코드     | platGbCd       | 0:대지 1:산 2:블록 | 0                                 |
| 번               | bun            | 번                 | 6                                 |
| 지               | ji             | 지                 | 13                                |
| 관리허가대장PK   | mgmPmsrgstPk   | 관리허가대장PK     | 11680-1388001                     |
| 건물명           | bldNm          | 건물명             | nan                               |
| 특수지명         | splotNm        | 특수지명           | nan                               |
| 블록             | block          | 블록               | nan                               |
| 로트             | lot            | 로트               | nan                               |
| 지목코드         | jimokCd        | 지목코드           | nan                               |
| 지목코드명       | jimokCdNm      | 지목코드명         | nan                               |
| 지역코드         | jiyukCd        | 지역코드           | 1023                              |
| 지역코드명       | jiyukCdNm      | 지역코드명         | 제3종일반주거지역                 |
| 지구코드         | jiguCd         | 지구코드           | 101                               |
| 지구코드명       | jiguCdNm       | 지구코드명         | 중심지미관지구                    |
| 구역코드         | guyukCd        | 구역코드           | nan                               |
| 구역코드명       | guyukCdNm      | 구역코드명         | nan                               |
| 공작물종류코드   | hdcrKindCd     | 공작물종류코드     | 5                                 |
| 공작물종류코드명 | hdcrKindCdNm   | 공작물종류코드명   | 기계식주차장                      |
| 구조코드         | strctCd        | 구조코드           | 39                                |
| 구조코드명       | strctCdNm      | 구조코드명         | 기타강구조                        |
| 길이(m)          | len            | 길이(m)            | 20.2                              |
| 높이(m)          | heit           | 높이(m)            | 7.93                              |
| 면적(㎡)         | area           | 면적(㎡)           | 134.93                            |
| 건폐율(%)        | bcRat          | 건폐율(%)          | 0                                 |
| 생성일자         | crtnDay        | 생성일자           | 20100325                          |

</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="공작물관리대장", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리허가대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>...</th>
      <th>구역코드명</th>
      <th>공작물종류코드</th>
      <th>공작물종류코드명</th>
      <th>구조코드</th>
      <th>구조코드명</th>
      <th>길이(m)</th>
      <th>높이(m)</th>
      <th>면적(㎡)</th>
      <th>건폐율(%)</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 397번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0397</td>
      <td>0000</td>
      <td>41135-100032915</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>None</td>
      <td>05</td>
      <td>기계식주차장</td>
      <td>39</td>
      <td>기타강구조</td>
      <td>6.2</td>
      <td>7.6</td>
      <td>29.14</td>
      <td>0</td>
      <td>20130718</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 29 columns</p>
</div>



## 건축인허가 철거멸실관리대장 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)       | 항목명(영문)     | 항목설명           | 샘플데이터                          |
|:-------------------|:-----------------|:-------------------|:------------------------------------|
| 대지구분코드       | platGbCd         | 0:대지 1:산 2:블록 | 0                                   |
| 번                 | bun              | 번                 | 660                                 |
| 지                 | ji               | 지                 | 16                                  |
| 관리허가대장PK     | mgmPmsrgstPk     | 관리허가대장PK     | 11680-10002137901                   |
| 건물명             | bldNm            | 건물명             | nan                                 |
| 특수지명           | splotNm          | 특수지명           | nan                                 |
| 블록               | block            | 블록               | nan                                 |
| 로트               | lot              | 로트               | nan                                 |
| 철거멸실구분코드   | demolExtngGbCd   | 철거멸실구분코드   | 3                                   |
| 철거멸실구분코드명 | demolExtngGbCdNm | 철거멸실구분코드명 | 멸실                                |
| 철거시작일         | demolStrtDay     | 철거시작일         | nan                                 |
| 철거종료일         | demolEndDay      | 철거종료일         | nan                                 |
| 철거멸실일         | demolExtngDay    | 철거멸실일         | 20100319                            |
| 연면적(㎡)         | totArea          | 연면적(㎡)         | 248.31                              |
| 건축물수           | bldCnt           | 건축물수           | 1                                   |
| 주용도코드         | mainPurpsCd      | 주용도코드         | 1000                                |
| 주용도코드명       | mainPurpsCdNm    | 주용도코드명       | 단독주택                            |
| 구조코드           | strctCd          | 구조코드           | 11                                  |
| 구조코드명         | strctCdNm        | 구조코드명         | 벽돌구조                            |
| 세대수(세대)       | hhldCnt          | 세대수(세대)       | 0                                   |
| 호수(호)           | hoCnt            | 호수(호)           | 0                                   |
| 가구수(가구)       | fmlyCnt          | 가구수(가구)       | 0                                   |
| 천장재함유유무     | cemaIncYn        | 0: N1: Y           | 0                                   |
| 단열재함유유무     | himaIncYn        | 0: N1: Y           | 0                                   |
| 지붕재함유유무     | rfmaIncYn        | 0: N1: Y           | 0                                   |
| 보온재함유유무     | lgmaIncYn        | 0: N1: Y           | 0                                   |
| 기타함유유무       | etcIncYn         | 0: N1: Y           | nan                                 |
| 해당없음유무       | nabYn            | 0: N1: Y           | 1                                   |
| 기타유무           | etcYn            | 0: N1: Y           | 0                                   |
| 바닥재함유유무     | btmaIncYn        | 0: N1: Y           | nan                                 |
| 생성일자           | crtnDay          | 생성일자           | 20100325                            |
| 순번               | rnum             | 순번               | 1                                   |
| 대지위치           | platPlc          | 대지위치           | 서울특별시 강남구 개포동 660-16번지 |
| 시군구코드         | sigunguCd        | 행정표준코드       | 11680                               |
| 법정동코드         | bjdongCd         | 행정표준코드       | 10300                               |

</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="철거멸실관리대장", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리허가대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>철거멸실구분코드</th>
      <th>철거멸실구분코드명</th>
      <th>...</th>
      <th>보온재함유유무</th>
      <th>기타함유유무</th>
      <th>해당없음유무</th>
      <th>기타유무</th>
      <th>바닥재함유유무</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0366</td>
      <td>0001</td>
      <td>41135-100024080</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>1</td>
      <td>철거</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>20120217</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 366-1번지</td>
      <td>41135</td>
      <td>11000</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 35 columns</p>
</div>



## 건축인허가 가설건축물 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)         | 항목명(영문)     | 항목설명             | 샘플데이터                      |
|:---------------------|:-----------------|:---------------------|:--------------------------------|
| 관리허가대장PK       | mgmPmsrgstPk     | 관리허가대장PK       | 11680-10002408501               |
| 건물명               | bldNm            | 건물명               | nan                             |
| 특수지명             | splotNm          | 특수지명             | nan                             |
| 블록                 | block            | 블록                 | nan                             |
| 로트                 | lot              | 로트                 | nan                             |
| 전체건축면적(㎡)     | sumArchArea      | 전체건축면적(㎡)     | 229.32                          |
| 전체연면적(㎡)       | sumTotArea       | 전체연면적(㎡)       | 0                               |
| 대지면적(㎡)         | platArea         | 대지면적(㎡)         | 121040                          |
| 가설건축물존치만료일 | tmpbldPrsvExpDay | 가설건축물존치만료일 | nan                             |
| 구조코드             | strctCd          | 구조코드             | 39                              |
| 구조코드명           | strctCdNm        | 구조코드명           | 기타강구조                      |
| 주용도코드           | mainPurpsCd      | 주용도코드           | 28000                           |
| 주용도코드명         | mainPurpsCdNm    | 주용도코드명         | 가설건축물                      |
| 건축면적(㎡)         | archArea         | 건축면적(㎡)         | 229.32                          |
| 연면적(㎡)           | totArea          | 연면적(㎡)           | 0                               |
| 지상층수             | grndFlrCnt       | 지상층수             | 1                               |
| 생성일자             | crtnDay          | 생성일자             | 20110723                        |
| 순번                 | rnum             | 순번                 | 1                               |
| 대지위치             | platPlc          | 대지위치             | 서울특별시 강남구 개포동 12번지 |
| 시군구코드           | sigunguCd        | 행정표준코드         | 11680                           |
| 법정동코드           | bjdongCd         | 행정표준코드         | 10300                           |
| 대지구분코드         | platGbCd         | 0:대지 1:산 2:블록   | 0                               |
| 번                   | bun              | 번                   | 12                              |
| 지                   | ji               | 지                   | 0                               |
    
</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="가설건축물", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>관리허가대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>전체건축면적(㎡)</th>
      <th>전체연면적(㎡)</th>
      <th>대지면적(㎡)</th>
      <th>가설건축물존치만료일</th>
      <th>구조코드</th>
      <th>...</th>
      <th>연면적(㎡)</th>
      <th>지상층수</th>
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
      <td>41135-100059345</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>45</td>
      <td>45</td>
      <td>1682</td>
      <td>None</td>
      <td>99</td>
      <td>...</td>
      <td>18</td>
      <td>1</td>
      <td>20220718</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 132-190번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0132</td>
      <td>0190</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 24 columns</p>
</div>



## 건축인허가 오수정화시설 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)           | 항목명(영문)   | 항목설명               | 샘플데이터                        |
|:-----------------------|:---------------|:-----------------------|:----------------------------------|
| 순번                   | rnum           | 순번                   | 1                                 |
| 대지위치               | platPlc        | 대지위치               | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드             | sigunguCd      | 행정표준코드           | 11680                             |
| 법정동코드             | bjdongCd       | 행정표준코드           | 10300                             |
| 대지구분코드           | platGbCd       | 0:대지 1:산 2:블록     | 0                                 |
| 번                     | bun            | 번                     | 12                                |
| 지                     | ji             | 지                     | 4                                 |
| 관리허가대장PK         | mgmPmsrgstPk   | 관리허가대장PK         | 11680-10003070401                 |
| 도로명대지위치         | newPlatPlc     | 도로명대지위치         | nan                               |
| 특수지명               | splotNm        | 특수지명               | nan                               |
| 블록                   | block          | 블록                   | nan                               |
| 로트                   | lot            | 로트                   | nan                               |
| 대표여부               | reprYn         | 0: 일반 1: 대표        | 1                                 |
| 오수정화시설형식코드   | wclfModeCd     | 오수정화시설형식코드   | 300                               |
| 오수정화시설형식코드명 | wclfModeCdNm   | 오수정화시설형식코드명 | 하수종말처리장연결                |
| 주동구분코드           | mainDongGbCd   | 주동구분코드           | 0                                 |
| 주동구분코드명         | mainDongGbCdNm | 주동구분코드명         | 전체                              |
| 용량(인용)             | capaPsper      | 용량(인용)             | 0                                 |
| 용량(루베)             | capaLube       | 용량(루베)             | 0                                 |
| 생성일자               | crtnDay        | 생성일자               | 20110215                          |
    
</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="오수정화시설", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리허가대장PK</th>
      <th>도로명대지위치</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>대표여부</th>
      <th>오수정화시설형식코드</th>
      <th>오수정화시설형식코드명</th>
      <th>주동구분코드</th>
      <th>주동구분코드명</th>
      <th>용량(인용)</th>
      <th>용량(루베)</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 236-4번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0236</td>
      <td>0004</td>
      <td>41135-15766</td>
      <td>NaN</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>1</td>
      <td>117</td>
      <td>접촉폭기방법</td>
      <td>0</td>
      <td>전체</td>
      <td>500</td>
      <td>100</td>
      <td>20130530</td>
    </tr>
  </tbody>
</table>
</div>



## 건축인허가 주차장 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)       | 항목명(영문)   | 항목설명           | 샘플데이터                        |
|:-------------------|:---------------|:-------------------|:----------------------------------|
| 순번               | rnum           | 순번               | 1                                 |
| 대지위치           | platPlc        | 대지위치           | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드         | sigunguCd      | 행정표준코드       | 11680                             |
| 법정동코드         | bjdongCd       | 행정표준코드       | 10300                             |
| 대지구분코드       | platGbCd       | 0:대지 1:산 2:블록 | 0                                 |
| 번                 | bun            | 번                 | 12                                |
| 지                 | ji             | 지                 | 4                                 |
| 관리허가대장PK     | mgmPmsrgstPk   | 관리허가대장PK     | 11680-440201                      |
| 특수지명           | splotNm        | 특수지명           | nan                               |
| 블록               | block          | 블록               | nan                               |
| 로트               | lot            | 로트               | nan                               |
| 옥내자주식대수(대) | indrAutoUtcnt  | 옥내자주식대수(대) | 105                               |
| 옥내자주식면적(㎡) | indrAutoArea   | 옥내자주식면적(㎡) | 4276.96                           |
| 옥외자주식대수(대) | oudrAutoUtcnt  | 옥외자주식대수(대) | 0                                 |
| 옥외자주식면적(㎡) | oudrAutoArea   | 옥외자주식면적(㎡) | 0                                 |
| 옥내기계식대수(대) | indrMechUtcnt  | 옥내기계식대수(대) | 0                                 |
| 옥내기계식면적(㎡) | indrMechArea   | 옥내기계식면적(㎡) | 0                                 |
| 옥외기계식대수(대) | oudrMechUtcnt  | 옥외기계식대수(대) | 0                                 |
| 옥외기계식면적(㎡) | oudrMechArea   | 옥외기계식면적(㎡) | 0                                 |
| 인근자주식대수(대) | neigAutoUtcnt  | 인근자주식대수(대) | 0                                 |
| 인근자주식면적(㎡) | neigAutoArea   | 인근자주식면적(㎡) | 0                                 |
| 인근기계식대수(대) | neigMechUtcnt  | 인근기계식대수(대) | 0                                 |
| 인근기계식면적(㎡) | neigMechArea   | 인근기계식면적(㎡) | 0                                 |
| 면제대수(대)       | exmptUtcnt     | 면제대수(대)       | 0                                 |
| 생성일자           | crtnDay        | 생성일자           | 20090320                          |

</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="주차장", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리허가대장PK</th>
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
      <td>경기도 성남시 분당구 백현동 236-4번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0236</td>
      <td>0004</td>
      <td>41135-15766</td>
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
      <td>20130530</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 25 columns</p>
</div>



## 건축인허가 부설주차장 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)   | 항목명(영문)   | 항목설명           | 샘플데이터                           |
|:---------------|:---------------|:-------------------|:-------------------------------------|
| 순번           | rnum           | 순번               | 1                                    |
| 대지위치       | platPlc        | 대지위치           | 서울특별시 강남구 개포동 1233-22번지 |
| 시군구코드     | sigunguCd      | 행정표준코드       | 11680                                |
| 법정동코드     | bjdongCd       | 행정표준코드       | 10300                                |
| 대지구분코드   | platGbCd       | 0:대지 1:산 2:블록 | 0                                    |
| 번             | bun            | 번                 | 1233                                 |
| 지             | ji             | 지                 | 22                                   |
| 관리허가대장PK | mgmPmsrgstPk   | 관리허가대장PK     | 11680-100064469                      |
| 행정동코드     | hjdongCd       | 행정동코드         | 690                                  |
| 지목코드       | jimokCd        | 지목코드           | 8                                    |
| 지목코드명     | jimokCdNm      | 지목코드명         | 대                                   |
| 관련지번명     | relJibunNm     | 관련지번명         | nan                                  |
| 생성일자       | crtnDay        | 생성일자           | 20150321                             |
    
</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="부설주차장", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리허가대장PK</th>
      <th>행정동코드</th>
      <th>지목코드</th>
      <th>지목코드명</th>
      <th>관련지번명</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 568-7번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0568</td>
      <td>0007</td>
      <td>41135-100037850</td>
      <td>650</td>
      <td>11</td>
      <td>주차장</td>
      <td>None</td>
      <td>20201102</td>
    </tr>
  </tbody>
</table>
</div>



## 건축인허가 전유공용면적 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)       | 항목명(영문)         | 항목설명           | 샘플데이터                        |
|:-------------------|:---------------------|:-------------------|:----------------------------------|
| 순번               | rnum                 | 순번               | 1                                 |
| 대지위치           | platPlc              | 대지위치           | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드         | sigunguCd            | 행정표준코드       | 11680                             |
| 법정동코드         | bjdongCd             | 행정표준코드       | 10300                             |
| 대지구분코드       | platGbCd             | 0:대지 1:산 2:블록 | 0                                 |
| 번                 | bun                  | 번                 | 12                                |
| 지                 | ji                   | 지                 | 4                                 |
| 관리전유공용면적PK | mgmExposPubuseAreaPk | 관리전유공용면적PK | 11680-10001598301                 |
| 관리허가대장PK     | mgmPmsrgstPk         | 관리허가대장PK     | 11680-10003070401                 |
| 특수지명           | splotNm              | 특수지명           | nan                               |
| 블록               | block                | 블록               | nan                               |
| 로트               | lot                  | 로트               | nan                               |
| 평형구분명         | pngtypGbNm           | 평형구분명         | 701호                             |
| 전유공용구분코드   | exposPubuseGbCd      | 전유공용구분코드   | 1                                 |
| 전유공용구분코드명 | exposPubuseGbCdNm    | 전유공용구분코드명 | 전유                              |
| 주부속구분코드     | mainAtchGbCd         | 주부속구분코드     | 0                                 |
| 주부속구분코드명   | mainAtchGbCdNm       | 주부속구분코드명   | 주건축물                          |
| 층구분코드         | flrGbCd              | 층구분코드         | 20                                |
| 층구분코드명       | flrGbCdNm            | 층구분코드명       | 지상                              |
| 층번호             | flrNo                | 층번호             | 7                                 |
| 구조코드           | strctCd              | 구조코드           | 21                                |
| 구조코드명         | strctCdNm            | 구조코드명         | 철근콘크리트구조                  |
| 주용도코드         | mainPurpsCd          | 주용도코드         | 13006                             |
| 주용도코드명       | mainPurpsCdNm        | 주용도코드명       | 체력단련장                        |
| 기타용도           | etcPurps             | 기타용도           | nan                               |
| 면적(㎡)           | area                 | 면적(㎡)           | 675.42                            |
| 생성일자           | crtnDay              | 생성일자           | 20110215                          |

</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="전유공용면적", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리전유공용면적PK</th>
      <th>관리허가대장PK</th>
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
      <td>경기도 성남시 분당구 백현동 370번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0370</td>
      <td>0000</td>
      <td>41135-100145452</td>
      <td>41135-100065255</td>
      <td>None</td>
      <td>...</td>
      <td>40</td>
      <td>각층</td>
      <td>0</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>02003</td>
      <td>다세대주택</td>
      <td>다세대주택</td>
      <td>65.84</td>
      <td>20220701</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 27 columns</p>
</div>



## 건축인허가 호별전유공용면적 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)       | 항목명(영문)         | 항목설명           | 샘플데이터                        |
|:-------------------|:---------------------|:-------------------|:----------------------------------|
| 순번               | rnum                 | 순번               | 1                                 |
| 대지위치           | platPlc              | 대지위치           | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드         | sigunguCd            | 행정표준코드       | 11680                             |
| 법정동코드         | bjdongCd             | 행정표준코드       | 10300                             |
| 대지구분코드       | platGbCd             | 0:대지 1:산 2:블록 | 0                                 |
| 번                 | bun                  | 번                 | 12                                |
| 지                 | ji                   | 지                 | 4                                 |
| 관리전유공용면적PK | mgmExposPubuseAreaPk | 관리전유공용면적PK | 11680-10001598301                 |
| 관리허가대장PK     | mgmPmsrgstPk         | 관리허가대장PK     | 11680-10003070401                 |
| 특수지명           | splotNm              | 특수지명           | nan                               |
| 블록               | block                | 블록               | nan                               |
| 로트               | lot                  | 로트               | nan                               |
| 평형구분명         | pngtypGbNm           | 평형구분명         | 701호                             |
| 전유공용구분코드   | exposPubuseGbCd      | 전유공용구분코드   | 1                                 |
| 전유공용구분코드명 | exposPubuseGbCdNm    | 전유공용구분코드명 | 전유                              |
| 주부속구분코드     | mainAtchGbCd         | 주부속구분코드     | 0                                 |
| 주부속구분코드명   | mainAtchGbCdNm       | 주부속구분코드명   | 주건축물                          |
| 층구분코드         | flrGbCd              | 층구분코드         | 20                                |
| 층구분코드명       | flrGbCdNm            | 층구분코드명       | 지상                              |
| 층번호             | flrNo                | 층번호             | 7                                 |
| 구조코드           | strctCd              | 구조코드           | 21                                |
| 구조코드명         | strctCdNm            | 구조코드명         | 철근콘크리트구조                  |
| 주용도코드         | mainPurpsCd          | 주용도코드         | 13006                             |
| 주용도코드명       | mainPurpsCdNm        | 주용도코드명       | 체력단련장                        |
| 기타용도           | etcPurps             | 기타용도           | nan                               |
| 면적(㎡)           | area                 | 면적(㎡)           | 675.42                            |
| 생성일자           | crtnDay              | 생성일자           | 20110215                          |

</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="호별전유공용면적", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리전유공용면적PK</th>
      <th>관리허가대장PK</th>
      <th>특수지명</th>
      <th>...</th>
      <th>층번호</th>
      <th>구조코드</th>
      <th>구조코드명</th>
      <th>주용도코드</th>
      <th>주용도코드명</th>
      <th>기타용도</th>
      <th>면적(㎡)</th>
      <th>생성일자</th>
      <th>관리호별명세PK</th>
      <th>mgmHoExposPubuseAreaPk</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 370번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0370</td>
      <td>0000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>None</td>
      <td>...</td>
      <td>1</td>
      <td>21</td>
      <td>철근콘크리트구조</td>
      <td>02003</td>
      <td>다세대주택</td>
      <td>다세대주택</td>
      <td>65.84</td>
      <td>20220701</td>
      <td>41135-100081709</td>
      <td>41135-100269757</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 29 columns</p>
</div>



## 건축인허가 지역지구구역 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)           | 항목명(영문)   | 항목설명               | 샘플데이터                        |
|:-----------------------|:---------------|:-----------------------|:----------------------------------|
| 지역지구구역명         | jijiguNm       | 지역지구구역명         | 일반주거지역                      |
| 생성일자               | crtnDay        | 생성일자               | 20090320                          |
| 순번                   | rnum           | 순번                   | 1                                 |
| 대지위치               | platPlc        | 대지위치               | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드             | sigunguCd      | 행정표준코드           | 11680                             |
| 법정동코드             | bjdongCd       | 행정표준코드           | 10300                             |
| 대지구분코드           | platGbCd       | 0:대지 1:산 2:블록     | 0                                 |
| 번                     | bun            | 번                     | 12                                |
| 지                     | ji             | 지                     | 4                                 |
| 관리허가대장PK         | mgmPmsrgstPk   | 관리허가대장PK         | 11680-440201                      |
| 특수지명               | splotNm        | 특수지명               | nan                               |
| 블록                   | block          | 블록                   | nan                               |
| 로트                   | lot            | 로트                   | nan                               |
| 지역지구구역구분코드   | jijiguGbCd     | 지역지구구역구분코드   | 1                                 |
| 지역지구구역구분코드명 | jijiguGbCdNm   | 지역지구구역구분코드명 | 용도지역코드                      |
| 지역지구구역코드       | jijiguCd       | 지역지구구역코드       | 1020                              |
| 지역지구구역코드명     | jijiguCdNm     | 지역지구구역코드명     | 일반주거지역                      |
| 대표여부               | reprYn         | 0: 일반                | 1                                 |
| 주동구분코드           | mainDongGbCd   | 주동구분코드           | 0                                 |
| 주동구분코드명         | mainDongGbCdNm | 주동구분코드명         | 전체                              |

</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="지역지구구역", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역지구구역명</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리허가대장PK</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>지역지구구역구분코드</th>
      <th>지역지구구역구분코드명</th>
      <th>지역지구구역코드</th>
      <th>지역지구구역코드명</th>
      <th>대표여부</th>
      <th>주동구분코드</th>
      <th>주동구분코드명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>제1종일반주거지역</td>
      <td>20120428</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 168-10번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0168</td>
      <td>0010</td>
      <td>41135-100011309</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>1</td>
      <td>용도지역코드</td>
      <td>1021</td>
      <td>제1종일반주거지역</td>
      <td>1</td>
      <td>0</td>
      <td>전체</td>
    </tr>
  </tbody>
</table>
</div>



## 건축인허가 도로명대장 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)         | 항목명(영문)   | 항목설명             | 샘플데이터                         |
|:---------------------|:---------------|:---------------------|:-----------------------------------|
| 순번                 | rnum           | 순번                 | 1                                  |
| 대지위치             | platPlc        | 대지위치             | 서울특별시 강남구 개포동 160-5번지 |
| 시군구코드           | sigunguCd      | 행정표준코드         | 11680                              |
| 법정동코드           | bjdongCd       | 행정표준코드         | 10300                              |
| 대지구분코드         | platGbCd       | 0:대지 1:산 2:블록   | 0                                  |
| 번                   | bun            | 번                   | 160                                |
| 지                   | ji             | 지                   | 5                                  |
| 관리허가대장PK       | mgmPmsrgstPk   | 관리허가대장PK       | 11680-10003432401                  |
| 특수지명             | splotNm        | 특수지명             | nan                                |
| 블록                 | block          | 블록                 | nan                                |
| 로트                 | lot            | 로트                 | nan                                |
| 도로지정번호년       | ranoYear       | 도로지정번호년       | 2011                               |
| 도로지정번호일련번호 | ranoSeqno      | 도로지정번호일련번호 | 16                                 |
| 도로지정구분코드     | rdasnGbCd      | 도로지정구분코드     | 1                                  |
| 도로지정구분코드명   | rdasnGbCdNm    | 도로지정구분코드명   | 지정                               |
| 도로지정일           | rdasnDay       | 도로지정일           | 20110525                           |
| 도로변경일           | roadChangDay   | 도로변경일           | nan                                |
| 도로변경차수         | roadChangOdr   | 도로변경차수         | 0                                  |
| 도로폐지일           | roadCloseDay   | 도로폐지일           | nan                                |
| 관리시군구코드       | mgmSigunguCd   | 관리시군구코드       | 11680                              |
| 도시지정변경일       | rdasnChangDay  | 도시지정변경일       | nan                                |
| 도로길이합계         | roadLenTotal   | 도로길이합계         | 0                                  |
| 도로너비합계         | roadWidthTotal | 도로너비합계         | 0                                  |
| 도로면적합계         | roadAreaTotal  | 도로면적합계         | 0                                  |
| 생성일자             | crtnDay        | 생성일자             | 20111222                           |
    
</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="도로명대장", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리허가대장PK</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>...</th>
      <th>도로지정일</th>
      <th>도로변경일</th>
      <th>도로변경차수</th>
      <th>도로폐지일</th>
      <th>관리시군구코드</th>
      <th>도시지정변경일</th>
      <th>도로길이합계</th>
      <th>도로너비합계</th>
      <th>도로면적합계</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 397번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0397</td>
      <td>0000</td>
      <td>41135-100031060</td>
      <td>None</td>
      <td>None</td>
      <td>...</td>
      <td>20130311</td>
      <td>None</td>
      <td>0</td>
      <td>None</td>
      <td>41135</td>
      <td>None</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>20140905</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 25 columns</p>
</div>



## 건축인허가 대지위치 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)   | 항목명(영문)   | 항목설명           | 샘플데이터                        |
|:---------------|:---------------|:-------------------|:----------------------------------|
| 관리동별개요PK | mgmDongOulnPk  | 관리동별개요PK     | 1                                 |
| 대표여부       | reprYn         | 0: 일반 1: 대표    | 1                                 |
| 주동구분코드   | mainDongGbCd   | 주동구분코드       | 0                                 |
| 주동구분코드명 | mainDongGbCdNm | 주동구분코드명     | 전체                              |
| 행정동코드     | hjdongCd       | 행정동코드         | 740                               |
| 특수지명       | splotNm        | 특수지명           | nan                               |
| 블록           | block          | 블록               | nan                               |
| 로트           | lot            | 로트               | nan                               |
| 지목코드       | jimokCd        | 지목코드           | 8                                 |
| 지목코드명     | jimokCdNm      | 지목코드명         | 대                                |
| 관련지번명     | relJibunNm     | 관련지번명         | nan                               |
| 생성일자       | crtnDay        | 생성일자           | 20090320                          |
| 순번           | rnum           | 순번               | 1                                 |
| 대지위치       | platPlc        | 대지위치           | 서울특별시 강남구 개포동 12-4번지 |
| 시군구코드     | sigunguCd      | 행정표준코드       | 11680                             |
| 법정동코드     | bjdongCd       | 행정표준코드       | 10300                             |
| 대지구분코드   | platGbCd       | 0:대지 1:산 2:블록 | 0                                 |
| 번             | bun            | 번                 | 12                                |
| 지             | ji             | 지                 | 4                                 |
| 관리대지위치PK | mgmPlatPlcPk   | 관리대지위치PK     | 11680-440401                      |
| 관리허가대장PK | mgmPmsrgstPk   | 관리허가대장PK     | 11680-440201                      |

</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="대지위치", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>관리동별개요PK</th>
      <th>대표여부</th>
      <th>주동구분코드</th>
      <th>주동구분코드명</th>
      <th>행정동코드</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>지목코드</th>
      <th>지목코드명</th>
      <th>...</th>
      <th>생성일자</th>
      <th>순번</th>
      <th>대지위치</th>
      <th>시군구코드</th>
      <th>법정동코드</th>
      <th>대지구분코드</th>
      <th>번</th>
      <th>지</th>
      <th>관리대지위치PK</th>
      <th>관리허가대장PK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>None</td>
      <td>0</td>
      <td>0</td>
      <td>전체</td>
      <td>650</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>08</td>
      <td>대</td>
      <td>...</td>
      <td>20090320</td>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0000</td>
      <td>0000</td>
      <td>41135-100005039</td>
      <td>41135-15753</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 21 columns</p>
</div>



## 건축인허가 주택유형 조회 서비스

### 입력 명세

* [입력 명세](#입력-명세)

### 출력 명세

<div align="center">

| 항목명(국문)       | 항목명(영문)   | 항목설명           | 샘플데이터                         |
|:-------------------|:---------------|:-------------------|:-----------------------------------|
| 순번               | rnum           | 순번               | 1                                  |
| 대지위치           | platPlc        | 대지위치           | 서울특별시 강남구 개포동 157-9번지 |
| 시군구코드         | sigunguCd      | 행정표준코드       | 11680                              |
| 법정동코드         | bjdongCd       | 행정표준코드       | 10300                              |
| 대지구분코드       | platGbCd       | 0:대지 1:산 2:블록 | 0                                  |
| 번                 | bun            | 번                 | 157                                |
| 지                 | ji             | 지                 | 9                                  |
| 관리허가대장PK     | mgmPmsrgstPk   | 관리허가대장PK     | 11680-10002663901                  |
| 건물명             | bldNm          | 건물명             | 개포동 157-9 공동주택 (김해옥)     |
| 특수지명           | splotNm        | 특수지명           | nan                                |
| 블록               | block          | 블록               | nan                                |
| 로트               | lot            | 로트               | nan                                |
| 주택유형구분코드   | hstpGbCd       | 주택유형구분코드   | 2                                  |
| 주택유형구분코드명 | hstpGbCdNm     | 주택유형구분코드명 | 준주택(오피스텔)                   |
| 실호세대수(세대)   | silHoHhldCnt   | 실호세대수(세대)   | 4                                  |
| 실호세대수면적(㎡) | silHoHhldArea  | 실호세대수면적(㎡) | 45.22                              |
| 생성일자           | crtnDay        | 생성일자           | 20111117                           |

    
</div>


```python
from PublicDataReader import BuildingLicense

service_key = "공공 데이터 포털에서 발급받은 서비스 키"
api = BuildingLicense(service_key)

df = api.get_data(
    service_type="주택유형", 
    sigungu_code="41135", 
    bdong_code="11000", 
    plat_code=None,
    bun=None,
    ji=None,
)
df.head(1)
```




<div>

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
      <th>관리허가대장PK</th>
      <th>건물명</th>
      <th>특수지명</th>
      <th>블록</th>
      <th>로트</th>
      <th>주택유형구분코드</th>
      <th>주택유형구분코드명</th>
      <th>실호세대수(세대)</th>
      <th>실호세대수면적(㎡)</th>
      <th>생성일자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>경기도 성남시 분당구 백현동 409-5번지</td>
      <td>41135</td>
      <td>11000</td>
      <td>0</td>
      <td>0409</td>
      <td>0005</td>
      <td>41135-100047718</td>
      <td>라비앙스빌(Revien-s Ville)</td>
      <td>None</td>
      <td>None</td>
      <td>None</td>
      <td>4</td>
      <td>도시형생활주택(단지형다세대주택)</td>
      <td>1</td>
      <td>84.86</td>
      <td>20171219</td>
    </tr>
  </tbody>
</table>
</div>


