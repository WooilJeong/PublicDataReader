## PublicDataReader 임포트하기

위에서 설치한 **PublicDataReader**를 임포트한 후 발급받은 KOSIS 공유서비스 Open API 사용자 인증키를 `apiKey`의 값으로 할당한다.

```python
import PublicDataReader as pdr
print(pdr.__version__)

# KOSIS 공유서비스 Open API 사용자 인증키
apiKey = "사용자 인증키"
```

    1.0.2


<br>

## KOSIS 통합검색

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| searchNm | String | 검색명 | 필수 |
| orgId | String | 기관코드 | 선택 |
| sort | String | 정렬<br>비고 : 정확도 RANK, 최신순DATE<br>※ 호출 파라미터에 sort 없을 경우에는 자동으로 RANK 로 정렬 | 선택 |
| startCount | String | 페이지 번호 | 선택 |
| resultCount | String | 데이터 출력 개수<br>비고 : <br>resultCount=20, startCount=1 : 1~20번 결과 리턴<br> resultCount=20, startCount=2 : 21~40번 결과 리턴 | 선택 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| ORG_ID | 기관코드 |
| ORG_NM | 기관명 |
| TBL_ID | 통계표ID |
| TBL_NM | 통계표명 |
| STAT_ID | 조사코드 |
| STAT_NM | 조사명 |
| VW_CD | KOSIS 목록구분 |
| MT_ATITLE | KOSIS 통계표 위치 |
| FULL_PATH_ID | 통계표 위치 |
| CONTENTS | 통계표 주요내용 |
| STRT_PRD_DE | 수록기간 시작일 |
| END_PRD_DE | 수록기간 종료일 |
| ITEM03 | 통계표 주석 |
| REC_TBL_SE | 추천통계표 여부 |
| TBL_VIEW_URL | 통계표 이동URL (KOSIS 목록으로 이동) |
| LINK_URL | 통계표 이동URL (KOSIS 통계표로 이동) |
| STAT_DB_CNT | 검색결과 건수 |
| QUERY | 검색어명 |


```python
# KOSIS 공유서비스 Open API 인스턴스 생성
serviceName = "KOSIS통합검색"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
searchNm = "행정구역(시군구)별, 성별 인구수"

# 데이터 조회
df = kosis.get_data(searchNm=searchNm)
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
      <th>ORG_ID</th>
      <th>ORG_NM</th>
      <th>TBL_ID</th>
      <th>TBL_NM</th>
      <th>STAT_ID</th>
      <th>STAT_NM</th>
      <th>VW_CD</th>
      <th>MT_ATITLE</th>
      <th>FULL_PATH_ID</th>
      <th>CONTENTS</th>
      <th>STRT_PRD_DE</th>
      <th>END_PRD_DE</th>
      <th>ITEM03</th>
      <th>REC_TBL_SE</th>
      <th>TBL_VIEW_URL</th>
      <th>LINK_URL</th>
      <th>STAT_DB_CNT</th>
      <th>QUERY</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>101</td>
      <td>행정안전부</td>
      <td>DT_1B040A3</td>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>2008001</td>
      <td>주민등록인구현황</td>
      <td>MT_ZTITLE</td>
      <td>인구 &gt; 주민등록인구현황</td>
      <td>A &gt; A_7</td>
      <td>행정구역(시군구)별 여자인구수 총인구수 남자인구수 전라남도 담양군 여천군 함평군 경...</td>
      <td>1992</td>
      <td>2022</td>
      <td>- 연말기준, 주민등록에 의한 집계, 외국인 제외 - 주민등록법 개정(＇09.10....</td>
      <td>Y</td>
      <td>https://kosis.kr/statisticsList/statisticsList...</td>
      <td>http://kosis.kr/statHtml/statHtml.do?orgId=101...</td>
      <td>176</td>
      <td>행정구역(시군구)별, 성별 인구수</td>
    </tr>
  </tbody>
</table>
</div>



<br>

## 통계설명

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| statId<br>* orgId(기관ID)+tblId(통계표ID)로도 가능 | String | 통계조사 ID | 필수<br>예) &statId=통계조사ID 또는 &orgId=기관ID&tblId=통계표ID |
| metaItm | String | 요청 항목 | 필수<br>전체 - All<br>조사명-statsNm<br>통계종류-statsKind<br>계속여부-statsContinue<br>법적근거-basisLaw<br>조사목적-writingPurps<br>조사주기-statsPeriod<br>조사체계-writingSystem<br>공표범위-pubExtent<br>공표주기-pubPeriod<br>연락처-writingTel<br>통계(활용)분야·실태-statsField<br>조사 대상범위-examinObjrange<br>조사 대상지역-examinObjArea<br>조사단위 및 조사대상규모-josaUnit<br>적용분류-applyGroup<br>조사항목-josaItm<br>공표주기-pubPeriod<br>공표범위-pubExtent<br>공표방법 및 URL-publictMth<br>조사대상기간 및 조사기준시점-examinTrgetPd<br>자료이용자 유의사항 -dataUserNote<br>주요 용어해설-mainTermExpl<br>자료 수집방법-dataCollectMth<br>조사연혁-examinHistory<br>승인번호-confmNo<br>승인일자-confmDt<br>통계종료-statsEnd |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| statsNm | 조사명 |
| statsKind | 통계종류 |
| statsContinue | 계속여부 |
| basisLaw | 법적근거 |
| writingPurps | 조사목적 |
| statsPeriod | 조사주기 |
| writingSystem | 조사체계 |
| pubExtent | 공표범위 |
| pubPeriod | 공표주기 |
| writingTel | 연락처 |
| statsField | 통계(활용)분야·실태 |
| examinObjrange | 조사 대상범위 |
| examinObjArea | 조사 대상지역 |
| josaUnit | 조사단위 및 조사대상규모 |
| applyGroup | 적용분류 |
| josaItm | 조사항목 |
| pubPeriod | 공표주기 |
| pubExtent | 공표범위 |
| publictMth | 공표방법 및 URL |
| examinTrgetPd | 조사대상기간 및 조사기준시점 |
| dataUserNote | 자료이용자 유의사항 |
| mainTermExpl | 주요 용어해설 |
| dataCollectMth | 자료 수집방법 |
| examinHistory | 조사연혁 |
| confmNo | 승인번호 |
| confmDt | 승인일자 |
| statsEnd | 통계종료 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
orgId = "101"
tblId = "DT_1B040A3"
metaItm = "ALL"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, metaItm=metaItm)
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
      <th>writingTel</th>
      <th>statsEnd</th>
      <th>examinObjArea</th>
      <th>statsPeriod</th>
      <th>statsField</th>
      <th>statsNm</th>
      <th>publictMth</th>
      <th>statsKind</th>
      <th>examinHistory</th>
      <th>josaItm</th>
      <th>...</th>
      <th>josaUnit</th>
      <th>confmDt</th>
      <th>writingPurps</th>
      <th>mainTermExpl</th>
      <th>applyGroup</th>
      <th>examinObjrange</th>
      <th>dataUserNote</th>
      <th>writingSystem</th>
      <th>examinTrgetPd</th>
      <th>dataCollectMth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>행정안전부민과 (☎ 044-205-3158)</td>
      <td>일반통계</td>
      <td>전국</td>
      <td>월</td>
      <td>인구</td>
      <td>주민등록인구현황</td>
      <td>전산망(인터넷)미 발 간주민등록 인구통계 홈페이지(https://jumin.mois...</td>
      <td>일반통계 / 보고통계</td>
      <td>ㅇ 최초작성년도 : 2008년 ㅇ 주요연혁 - 2008년 1월 8일 통계작성 승인-...</td>
      <td>ㅇ전국 지방자치단체별 주민등록인구 현황 행정기관별, 연령별, 성별, 세대수, 세대원...</td>
      <td>...</td>
      <td>ㅇ17개 시도, 시군구, 읍면동별 성별, 연령별 인구 및 세대 현황 주민등록기준 읍...</td>
      <td>20080108</td>
      <td>ㅇ“주민등록법”에 의한 주민등록인구 및 세대현황에 대하여 전국단위의 행정기관별(시도...</td>
      <td>주민등록 세대 : 주거 및 생계를 같이하는 사람의 집단인구증감 : 전월인구 대비 금...</td>
      <td>(주) 해당없음</td>
      <td>ㅇ 주민등록 인구 : 주민등록법에 의거 주민등록표에 기재된 인구로 거주자, 거주불명...</td>
      <td>1. 자료내용 : 주민등록(거주자, 거주불명자, 재외국민)이 되어 있는 자의 인구,...</td>
      <td>시·군·구 주민등록시스템(자치행정과, 정보통신담당관실) → 행정안전부 주민등록전산정...</td>
      <td>매월 말일</td>
      <td>행정집계</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 25 columns</p>
</div>



<br>

## 통계표 설명

### 통계표 명칭

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| TBL_NM | 통계표 국문명 |
| TBL_NM_ENG | 통계표 영문명 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "통계표명칭"
orgId = "101"
tblId = "DT_1B040A3"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, detailServiceName=detailServiceName)
df.head()
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
      <th>TBL_NM</th>
      <th>TBL_NM_ENG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>Resident Population by City, County, and District</td>
    </tr>
  </tbody>
</table>
</div>



### 기관 명칭

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| ORG_NM | 기관 국문명 |
| ORG_NM_ENG | 기관 영문명 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "기관명칭"
orgId = "101"

# 데이터 조회
df = kosis.get_data(orgId=orgId, detailServiceName=detailServiceName)
df.head()
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
      <th>ORG_NM</th>
      <th>ORG_NM_ENG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>통계청</td>
      <td>Statistics Korea</td>
    </tr>
  </tbody>
</table>
</div>



### 수록정보

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |
| detail | String | 전체시점 정보 제공 | 선택 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| PRD_SE | 수록주기 |
| PRD_DE | 수록시점 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "통계표명칭"
orgId = "101"
tblId = "DT_1B040A3"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, detailServiceName=detailServiceName)
df.head()
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
      <th>TBL_NM</th>
      <th>TBL_NM_ENG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>Resident Population by City, County, and District</td>
    </tr>
  </tbody>
</table>
</div>



### 분류/항목

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |
| objId | String | 분류코드 | 선택 |
| itmId | String | 분류값코드 | 선택 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| OBJ_ID | 분류 ID |
| OBJ_NM | 분류 국문명 |
| OBJ_NM_ENG | 분류 영문명 |
| ITM_ID | 분류값 ID |
| ITM_NM | 분류값 국문명 |
| ITM_NM_ENG | 분류값 영문명 |
| UP_ITM_ID | 상위 분류값 ID |
| OBJ_ID_SN | 분류값 순번 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "분류항목"
orgId = "101"
tblId = "DT_1B040A3"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, detailServiceName=detailServiceName)
df
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
      <th>ITM_NM</th>
      <th>TBL_ID</th>
      <th>ITM_NM_ENG</th>
      <th>ITM_ID</th>
      <th>OBJ_NM</th>
      <th>OBJ_NM_ENG</th>
      <th>ORG_ID</th>
      <th>OBJ_ID</th>
      <th>OBJ_ID_SN</th>
      <th>UP_ITM_ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>총인구수</td>
      <td>DT_1B040A3</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>항목</td>
      <td>Item code list</td>
      <td>101</td>
      <td>ITEM</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>남자인구수</td>
      <td>DT_1B040A3</td>
      <td>Koreans (Male)</td>
      <td>T21</td>
      <td>항목</td>
      <td>Item code list</td>
      <td>101</td>
      <td>ITEM</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>여자인구수</td>
      <td>DT_1B040A3</td>
      <td>Koreans (Female)</td>
      <td>T22</td>
      <td>항목</td>
      <td>Item code list</td>
      <td>101</td>
      <td>ITEM</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>전국</td>
      <td>DT_1B040A3</td>
      <td>Whole country</td>
      <td>00</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>101</td>
      <td>A</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>서울특별시</td>
      <td>DT_1B040A3</td>
      <td>Seoul</td>
      <td>11</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>101</td>
      <td>A</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>376</th>
      <td>제주특별자치도</td>
      <td>DT_1B040A3</td>
      <td>Jeju-do</td>
      <td>50</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>101</td>
      <td>A</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>377</th>
      <td>제주시</td>
      <td>DT_1B040A3</td>
      <td>Jeju-si</td>
      <td>50110</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>101</td>
      <td>A</td>
      <td>1</td>
      <td>50</td>
    </tr>
    <tr>
      <th>378</th>
      <td>서귀포시</td>
      <td>DT_1B040A3</td>
      <td>Seogwipo-si</td>
      <td>50130</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>101</td>
      <td>A</td>
      <td>1</td>
      <td>50</td>
    </tr>
    <tr>
      <th>379</th>
      <td>북제주군</td>
      <td>DT_1B040A3</td>
      <td>Bukjeju-gun</td>
      <td>50910</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>101</td>
      <td>A</td>
      <td>1</td>
      <td>50</td>
    </tr>
    <tr>
      <th>380</th>
      <td>남제주군</td>
      <td>DT_1B040A3</td>
      <td>Namjeju-gun</td>
      <td>50920</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>101</td>
      <td>A</td>
      <td>1</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
<p>381 rows × 10 columns</p>
</div>



### 주석

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| CMMT_NM | 주석유형 |
| CMMT_DC | 주석 |
| OBJ_ID | 분류 ID |
| OBJ_NM | 분류 명 |
| ITM_ID | 분류값 ID |
| ITM_NM | 분류값 국문명 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "주석"
orgId = "101"
tblId = "DT_1B04006"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, detailServiceName=detailServiceName)
df.head()
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
      <th>CMMT_DC</th>
      <th>CMMT_NM</th>
      <th>ITM_NM</th>
      <th>ITM_ID</th>
      <th>OBJ_NM</th>
      <th>OBJ_ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>* 등록구분의 "전체"는 "거주자", "거주불명자", "재외국민"이 포함된 자료입니다.</td>
      <td>통계표</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>\n  - 거주자: 거주지가 분명한 사람(재외국민 제외)</td>
      <td>통계표</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>\n  - 거주불명자: 거주사실이 불분명하여 거주불명으로 등록된 사람(2010년 1...</td>
      <td>통계표</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>\n  - 재외국민: 외국의 영주권을 취득한(영주목적으로 외국거주 포함) 대한민국 ...</td>
      <td>통계표</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>\n* 주민등록 연령별 인구통계는 주민등록 신고에 따른 것으로 실제 연령과는 차이가...</td>
      <td>통계표</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### 단위

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| UNIT_NM | 단위 국문명 |
| UNIT_NM_ENG | 단위 영문명 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "단위"
orgId = "101"
tblId = "DT_1B040A3"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, detailServiceName=detailServiceName)
df
```

    데이터가 존재하지 않습니다.
    

### 출처

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| JOSA_NM | 조사명 |
| DEPT_NM | 통계표 담당부서 |
| DEPT_PHONE | 통계표 담당부서 전화번호 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "출처"
orgId = "101"
tblId = "DT_1B040A3"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, detailServiceName=detailServiceName)
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
      <th>JOSA_NM</th>
      <th>DEPT_NM</th>
      <th>DEPT_PHONE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>「주민등록인구현황」</td>
      <td>주민과</td>
      <td>044-205-3158</td>
    </tr>
  </tbody>
</table>
</div>



### 가중치

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |
| 분류코드1~분류코드8 | String | 분류코드1~분류코드8 | 선택 |
| ITEM | String | 항목 | 선택 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| C1 ~ C8 | 분류값 ID1 ~ 분류값 ID8 |
| C1_NM ~ C8_NM | 분류값 명1 ~ 분류값 명8 |
| ITM_ID | 항목 ID |
| ITM_NM | 항목명 |
| WGT_CO | 가중치 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "가중치"
orgId = "101"
tblId = "DT_1B040A3"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, detailServiceName=detailServiceName)
df
```

    데이터가 존재하지 않습니다.
    

### 자료갱신일

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |
| prdSe | String | 수록주기 | 선택 [추가정보](https://kosis.kr/openapi/devGuide/devGuide_0601Pop.jsp?type=JSON&gubun=input)<br>(미입력 시 전체주기에 대한 데이터 출력) |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| ORG_NM | 기관명 |
| TBL_NM | 통계표명 |
| PRD_SE | 수록주기 |
| PRD_DE | 수록시점 |
| SEND_DE | 자료갱신일 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계표설명"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
detailServiceName = "자료갱신일"
orgId = "101"
tblId = "DT_1B040A3"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, detailServiceName=detailServiceName)
df.head()
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
      <th>ORG_NM</th>
      <th>TBL_NM</th>
      <th>PRD_SE</th>
      <th>PRD_DE</th>
      <th>SEND_DE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>통계청</td>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>월</td>
      <td>201101</td>
      <td>2022-10-05</td>
    </tr>
    <tr>
      <th>1</th>
      <td>통계청</td>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>월</td>
      <td>201102</td>
      <td>2022-10-05</td>
    </tr>
    <tr>
      <th>2</th>
      <td>통계청</td>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>월</td>
      <td>201103</td>
      <td>2022-10-05</td>
    </tr>
    <tr>
      <th>3</th>
      <td>통계청</td>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>월</td>
      <td>201104</td>
      <td>2022-10-05</td>
    </tr>
    <tr>
      <th>4</th>
      <td>통계청</td>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>월</td>
      <td>201105</td>
      <td>2022-10-05</td>
    </tr>
  </tbody>
</table>
</div>



<br>

## 통계목록

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| vwCd | String | 서비스뷰 코드<br>· MT_ZTITLE : 국내통계 주제별<br>· MT_OTITLE : 국내통계 기관별<br>· MT_GTITLE01 : e-지방지표(주제별)<br>· MT_GTITLE02 : e-지방지표(지역별)<br>· MT_CHOSUN_TITLE : 광복이전통계(1908~1943)<br>· MT_HANKUK_TITLE : 대한민국통계연감<br>· MT_STOP_TITLE : 작성중지통계<br>· MT_RTITLE : 국제통계<br>· MT_BUKHAN : 북한통계<br>· MT_TM1_TITLE : 대상별통계<br>· MT_TM2_TITLE : 이슈별통계<br>· MT_ETITLE : 영문 KOSIS | 필수 |
| parentListId | String | 시작목록 ID | 필수 |

- 출력결과

| 결과변수 | 설명 |
| --- | --- |
| VW_CD | 서비스뷰ID |
| VW_NM | 서비스뷰명 |
| LIST_ID | 목록ID |
| LIST_NM | 목록명 |
| ORG_ID | 기관코드 |
| TBL_ID | 통계표ID |
| TBL_NM | 통계표명 |
| REC_TBL_SE | 추천 통계표 여부 |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계목록"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
vwCd = "MT_OTITLE"
parentListId = "110_20103"

# 데이터 조회
df = kosis.get_data(vwCd=vwCd, parentListId=parentListId)
df
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
      <th>TBL_NM</th>
      <th>TBL_ID</th>
      <th>VW_CD</th>
      <th>VW_NM</th>
      <th>ORG_ID</th>
      <th>REC_TBL_SE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>행정구역(시군구)별 주민등록세대수</td>
      <td>DT_1B040B3</td>
      <td>MT_OTITLE</td>
      <td>국내통계 기관별</td>
      <td>101</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1</th>
      <td>행정구역(시군구)별, 성별 인구수</td>
      <td>DT_1B040A3</td>
      <td>MT_OTITLE</td>
      <td>국내통계 기관별</td>
      <td>101</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2</th>
      <td>행정구역(시군구)별/1세별 주민등록인구</td>
      <td>DT_1B04006</td>
      <td>MT_OTITLE</td>
      <td>국내통계 기관별</td>
      <td>101</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>행정구역(읍면동)별/5세별 주민등록인구(2011년~)</td>
      <td>DT_1B04005N</td>
      <td>MT_OTITLE</td>
      <td>국내통계 기관별</td>
      <td>101</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>행정구역(읍면동)별/5세별 주민등록인구</td>
      <td>DT_1B04005</td>
      <td>MT_OTITLE</td>
      <td>국내통계 기관별</td>
      <td>101</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5</th>
      <td>시군구/성/연령(1세)별 주민등록연앙인구</td>
      <td>DT_1B040M1</td>
      <td>MT_OTITLE</td>
      <td>국내통계 기관별</td>
      <td>101</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>시군구/성/연령(5세)별 주민등록연앙인구</td>
      <td>DT_1B040M5</td>
      <td>MT_OTITLE</td>
      <td>국내통계 기관별</td>
      <td>101</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
</div>


<br>

## 통계자료

- 요청변수

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| apiKey | String | 발급된 인증 key | 필수 |
| orgId | String | 기관 ID | 필수 |
| tblId | String | 통계표 ID | 필수 |
| objL1 | String | 분류1(첫번째 분류코드) | 필수 |
| objL2 ~ objL8 | String | 분류2(두번째 분류코드) ~ 분류8(여덟째 분류코드) | 선택 |
| itmId | String | 항목 | 필수 |
| prdSe | String | 수록주기 | 필수 [추가정보](https://kosis.kr/openapi/devGuide/devGuide_0201Pop.jsp?type=JSON&gubun=input) |
| startPrdDe | String | (시점기준) 시작수록시점 | 선택 [시점정보](https://kosis.kr/openapi/devGuide/devGuide_0202Pop.jsp?gubun=json)<br>(시점기준 또는 최신자료기준 택1)<br>※설정이 없을경우 최근시점1개 조회 |
| endPrdDe | String | (시점기준) 종료수록시점 | 선택 [시점정보](https://kosis.kr/openapi/devGuide/devGuide_0202Pop.jsp?gubun=json)<br>(시점기준 또는 최신자료기준 택1)<br>※설정이 없을경우 최근시점1개 조회 |
| newEstPrdCnt | String | (최신자료기준) 최근수록시점 개수 | 선택 [시점정보](https://kosis.kr/openapi/devGuide/devGuide_0202Pop.jsp?gubun=json)<br>(시점기준 또는 최신자료기준 택1)<br>※설정이 없을경우 최근시점1개 조회 |
| prdInterval | String | (최신자료기준) 수록시점 간격<br>ex) 2019, 2017, 2015 등 2개 시점 간격으로 추출시 [2] 입력 | 선택 [시점정보](https://kosis.kr/openapi/devGuide/devGuide_0202Pop.jsp?gubun=json)<br>(시점기준 또는 최신자료기준 택1)<br>※설정이 없을경우 최근시점1개 조회 |

- 출력결과

| 출력변수 | 설명 | 비고 |
| --- | --- | --- |
| ORG_ID | 기관코드 |  |
| TBL_ID | 통계표ID |  |
| TBL_NM | 통계표명 |  |
| C1 ~ C8 | 분류값 ID1 ~ 분류값 ID8 | 2~8 분류값은 없을 경우 생략 |
| C1_OBJ_NM ~ C8_OBJ_NM | 분류명1 ~ 분류명8 |  |
| C1_OBJ_NM_ENG ~ C8_OBJ_NM_ENG | 분류 영문명1 ~ 분류 영문명8 |  |
| C1_NM ~ C8_NM | 분류값 명1 ~ 분류값 명8 |  |
| C1_NM_ENG ~ C8_NM_ENG | 분류값 영문명1 ~ 분류값 영문명8 |  |
| ITM_ID | 항목 ID |  |
| ITM_NM | 항목명 |  |
| ITM_NM_ENG | 항목영문명 |  |
| UNIT_ID | 단위ID |  |
| UNIT_NM | 단위명 |  |
| UNIT_NM_ENG | 단위영문명 |  |
| PRD_SE | 수록주기 | 추가정보 |
| PRD_DE | 수록시점 |  |
| DT | 수치값 |  |


```python
# KOSIS OPEN API 인스턴스 생성
serviceName = "통계자료"
kosis = pdr.Kosis(apiKey, serviceName)

# 파라미터
orgId = "101"
tblId = "DT_1B040A3"
itmId = "T20"
objL1 = "11 41"
prdSe = "Y"
startPrdDe = "1990"
endPrdDe = "2022"

# 데이터 조회
df = kosis.get_data(orgId=orgId, tblId=tblId, objL1=objL1, itmId=itmId, prdSe=prdSe, startPrdDe=startPrdDe, endPrdDe=endPrdDe)
df
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
      <th>TBL_NM</th>
      <th>PRD_DE</th>
      <th>TBL_ID</th>
      <th>ITM_NM</th>
      <th>ITM_NM_ENG</th>
      <th>ITM_ID</th>
      <th>UNIT_NM</th>
      <th>ORG_ID</th>
      <th>UNIT_NM_ENG</th>
      <th>C1_OBJ_NM</th>
      <th>C1_OBJ_NM_ENG</th>
      <th>DT</th>
      <th>PRD_SE</th>
      <th>C1</th>
      <th>C1_NM</th>
      <th>C1_NM_ENG</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1992</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10935230</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>1</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1993</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10889499</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>2</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1994</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10759454</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>3</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1995</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10550871</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>4</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1996</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10418076</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>5</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1997</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10336134</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>6</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1998</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10270506</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>7</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1999</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10264260</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>8</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2000</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10311314</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>9</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2001</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10263336</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>10</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2002</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10207295</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>11</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2003</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10174086</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>12</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2004</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10173162</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>13</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2005</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10167344</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>14</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2006</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10181166</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>15</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2007</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10192710</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>16</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2008</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10200827</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>17</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2009</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10208302</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>18</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2010</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10312545</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>19</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2011</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10249679</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>20</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2012</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10195318</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>21</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2013</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10143645</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>22</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2014</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10103233</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>23</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2015</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10022181</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>24</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2016</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9930616</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>25</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2017</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9857426</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>26</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2018</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9765623</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>27</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2019</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9729107</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>28</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2020</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9668465</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>29</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2021</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9509458</td>
      <td>A</td>
      <td>11</td>
      <td>서울특별시</td>
      <td>Seoul</td>
    </tr>
    <tr>
      <th>30</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1992</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>6613094</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>31</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1993</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>7005232</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>32</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1994</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>7421823</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>33</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1995</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>7789424</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>34</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1996</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>8155794</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>35</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1997</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>8470594</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>36</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1998</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>8672632</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>37</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>1999</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>8934332</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>38</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2000</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9219343</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>39</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2001</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9544496</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>40</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2002</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>9927473</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>41</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2003</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10206851</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>42</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2004</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10462920</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>43</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2005</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10697215</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>44</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2006</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>10906033</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>45</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2007</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>11106211</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>46</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2008</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>11292264</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>47</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2009</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>11460610</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>48</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2010</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>11786622</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>49</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2011</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>11937415</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>50</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2012</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>12093299</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>51</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2013</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>12234630</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>52</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2014</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>12357830</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>53</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2015</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>12522606</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>54</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2016</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>12716780</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>55</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2017</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>12873895</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>56</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2018</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>13077153</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>57</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2019</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>13239666</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>58</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2020</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>13427014</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
    <tr>
      <th>59</th>
      <td>행정구역(시군구)별 성별 인구수</td>
      <td>2021</td>
      <td>DT_1B040A3</td>
      <td>총인구수</td>
      <td>Koreans (Total)</td>
      <td>T20</td>
      <td>명</td>
      <td>101</td>
      <td>Person</td>
      <td>행정구역(시군구)별</td>
      <td>By Administrative District</td>
      <td>13565450</td>
      <td>A</td>
      <td>41</td>
      <td>경기도</td>
      <td>Gyeonggi-do</td>
    </tr>
  </tbody>
</table>
</div>