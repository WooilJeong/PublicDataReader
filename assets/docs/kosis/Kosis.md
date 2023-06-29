# KOSIS 통계정보 사용 가이드

[KOSIS 공유서비스](https://kosis.kr/openapi/index/index.jsp)에서 제공하는 오픈 API 서비스를 이용하려면 인증키가 필요합니다. 인증키를 얻기 위해서는 [KOSIS 공유서비스](https://kosis.kr/openapi/index/index.jsp)에 회원가입을 하고 오픈 API 서비스를 신청해야 합니다. KOSIS 공유서비스 오픈 API 신청 방법과 PublicDataReader에서 제공하는 KOSIS 공유서비스 오픈 API의 모든 기능을 살펴보려면 [Python으로 KOSIS 데이터 조회하기](https://wooiljeong.github.io/python/pdr-kosis/) 블로그 글을 참고하세요.

## 라이브러리 임포트하기

```python
from PublicDataReader import Kosis

# KOSIS 공유서비스 Open API 사용자 인증키
service_key = "사용자 인증키"

# 인스턴스 생성하기
api = Kosis(service_key)
```

## KOSIS 통합검색

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| searchNm | String | 검색명 | 필수 |
| orgId | String | 기관코드 | 선택 |
| sort | String | 정렬<br>비고 : 정확도 RANK, 최신순DATE<br>※ 호출 파라미터에 sort 없을 경우에는 자동으로 RANK 로 정렬 | 선택 |
| startCount | String | 페이지 번호 | 선택 |
| resultCount | String | 데이터 출력 개수<br>비고 : <br>resultCount=20, startCount=1 : 1 ~ 20번 결과 리턴<br> resultCount=20, startCount=2 : 21 ~ 40번 결과 리턴 | 선택 |

</div>

- 출력결과

<div align="center">

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

</div>

```python
df1 = api.get_data(
    "KOSIS통합검색",
    searchNm="미분양 현황",
    )
df1.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기관ID</th>
      <th>기관명</th>
      <th>통계표ID</th>
      <th>통계표명</th>
      <th>조사ID</th>
      <th>조사명</th>
      <th>KOSIS목록구분</th>
      <th>KOSIS통계표위치</th>
      <th>통계표위치</th>
      <th>통계표주요내용</th>
      <th>수록기간시작일</th>
      <th>수록기간종료일</th>
      <th>통계표주석</th>
      <th>추천통계표여부</th>
      <th>KOSIS목록URL</th>
      <th>KOSIS통계표URL</th>
      <th>검색결과건수</th>
      <th>검색어명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>116</td>
      <td>국토교통부</td>
      <td>DT_MLTM_2086</td>
      <td>미분양현황_종합</td>
      <td>1998033</td>
      <td>미분양주택현황보고</td>
      <td>MT_ZTITLE</td>
      <td>주거 &gt; 미분양주택현황보고</td>
      <td>I1 &gt; I1_2</td>
      <td>대분류 구분 부문별미분양현황 시도별미분양현황 규모별미분양현황 세종특별자치시 지방 계...</td>
      <td>2001</td>
      <td>2021</td>
      <td>해당연도 12월말 기준 자료 : 국토교통부 주택토지실 주택정책관 주택정책과</td>
      <td>N</td>
      <td>https://kosis.kr/statisticsList/statisticsList...</td>
      <td>http://kosis.kr/statHtml/statHtml.do?orgId=116...</td>
      <td>210</td>
      <td>미분양 현황</td>
    </tr>
  </tbody>
</table>
</div>



<br>

## 통계설명

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| statId<br>* orgId(기관ID)+tblId(통계표ID)로도 가능 | String | 통계조사 ID | 필수<br>예) &statId=통계조사ID 또는 &orgId=기관ID&tblId=통계표ID |
| metaItm | String | 요청 항목 | 필수<br>전체 - All<br>조사명-statsNm<br>통계종류-statsKind<br>계속여부-statsContinue<br>법적근거-basisLaw<br>조사목적-writingPurps<br>조사주기-statsPeriod<br>조사체계-writingSystem<br>공표범위-pubExtent<br>공표주기-pubPeriod<br>연락처-writingTel<br>통계(활용)분야·실태-statsField<br>조사 대상범위-examinObjrange<br>조사 대상지역-examinObjArea<br>조사단위 및 조사대상규모-josaUnit<br>적용분류-applyGroup<br>조사항목-josaItm<br>공표주기-pubPeriod<br>공표범위-pubExtent<br>공표방법 및 URL-publictMth<br>조사대상기간 및 조사기준시점-examinTrgetPd<br>자료이용자 유의사항 -dataUserNote<br>주요 용어해설-mainTermExpl<br>자료 수집방법-dataCollectMth<br>조사연혁-examinHistory<br>승인번호-confmNo<br>승인일자-confmDt<br>통계종료-statsEnd |

</div>

- 출력결과

<div align="center">

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

</div>

```python
df2 = api.get_data(
    "통계설명",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    metaItm = "ALL",
    )
df2.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>조사명</th>
      <th>통계종류</th>
      <th>계속여부</th>
      <th>법적근거</th>
      <th>조사목적</th>
      <th>조사주기</th>
      <th>조사체계</th>
      <th>공표범위</th>
      <th>공표주기</th>
      <th>연락처</th>
      <th>...</th>
      <th>조사단위및조사대상규모</th>
      <th>적용분류</th>
      <th>조사항목</th>
      <th>공표방법및URL</th>
      <th>조사대상기간및조사기준시점</th>
      <th>조사기간</th>
      <th>자료수집방법</th>
      <th>승인번호</th>
      <th>승인일자</th>
      <th>통계종료</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>미분양주택현황보고</td>
      <td>일반통계 / 보고통계</td>
      <td>계속통계</td>
      <td>주택법</td>
      <td>매월 전국 및 지역별 미분양 주택현황을 파악하여 주택공급정책의 기초자료로 활용</td>
      <td>월</td>
      <td>구·시·군→시·도→국토교통부</td>
      <td>시군구</td>
      <td>월</td>
      <td>국토교통부 주택토지실 주택정책관 주택정책과 (☎ 044-201-3336)</td>
      <td>...</td>
      <td>기타전국의 미분양 주택 현황</td>
      <td>(주) 해당없음</td>
      <td>∎ 작성항목(2개 부문 6개항목) - 전체 미분양 현황: 지역별(광역시/시군구) 세...</td>
      <td>전산망(인터넷), 간행물http://stat.molit.go.kr)국토교통통계연보(...</td>
      <td>1월1일~12월31일(매월말)</td>
      <td>매월 1일~15일</td>
      <td>행정집계</td>
      <td>116025</td>
      <td>19981013</td>
      <td>일반통계</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 22 columns</p>
</div>



<br>

## 통계표 설명

### 통계표 명칭

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |

</div>

- 출력결과

<div align="center">

| 결과변수 | 설명 |
| --- | --- |
| TBL_NM | 통계표 국문명 |
| TBL_NM_ENG | 통계표 영문명 |

</div>

```python
df3_1 = api.get_data(
    "통계표설명",
    "통계표명칭",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    )
df3_1.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>통계표명</th>
      <th>통계표영문명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>미분양현황_종합</td>
      <td>Unsold Housings (Total)</td>
    </tr>
  </tbody>
</table>
</div>



### 기관 명칭

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |

</div>

- 출력결과

<div align="center">

| 결과변수 | 설명 |
| --- | --- |
| ORG_NM | 기관 국문명 |
| ORG_NM_ENG | 기관 영문명 |

</div>


```python
df3_2 = api.get_data(
    "통계표설명",
    "기관명칭",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    )
df3_2.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기관명</th>
      <th>기관영문명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>국토교통부</td>
      <td>Ministry of Land, Infrastructure and Transport</td>
    </tr>
  </tbody>
</table>
</div>



### 수록정보

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |
| detail | String | 전체시점 정보 제공 | 선택 |

</div>

- 출력결과

<div align="center">

| 결과변수 | 설명 |
| --- | --- |
| PRD_SE | 수록주기 |
| PRD_DE | 수록시점 |

</div>



```python
df3_3 = api.get_data(
    "통계표설명",
    "수록정보",
    orgId = "101",
    tblId = "DT_1IN0001",
    # detail = "Y",
    )
df3_3.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>수록주기</th>
      <th>수록기간시작일</th>
      <th>수록기간종료일</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5년</td>
      <td>1925</td>
      <td>2010</td>
    </tr>
  </tbody>
</table>
</div>


### 분류/항목

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |
| objId | String | 분류코드 | 선택 |
| itmId | String | 분류값코드 | 선택 |

</div>

- 출력결과

<div align="center">

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

</div>


```python
df3_4 = api.get_data(
    "통계표설명",
    "분류항목",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    )
df3_4.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기관ID</th>
      <th>통계표ID</th>
      <th>코드ID</th>
      <th>코드명</th>
      <th>분류ID</th>
      <th>분류명</th>
      <th>분류영문명</th>
      <th>분류값ID</th>
      <th>분류값명</th>
      <th>분류값영문명</th>
      <th>분류값순번</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>116</td>
      <td>DT_MLTM_2086</td>
      <td>14999116.12월기준</td>
      <td>12월기준</td>
      <td>ITEM</td>
      <td>항목</td>
      <td>Item code list</td>
      <td>13103871014T1</td>
      <td>미분양(12월기준)</td>
      <td>Unsold Housings</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### 주석

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |

</div>

- 출력결과

<div align="center">

| 결과변수 | 설명 |
| --- | --- |
| CMMT_NM | 주석유형 |
| CMMT_DC | 주석 |
| OBJ_ID | 분류 ID |
| OBJ_NM | 분류 명 |
| ITM_ID | 분류값 ID |
| ITM_NM | 분류값 국문명 |

</div>


```python
df3_5 = api.get_data(
    "통계표설명",
    "주석",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    )
df3_5.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>주석유형</th>
      <th>주석</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>통계표</td>
      <td>해당연도 12월말 기준</td>
    </tr>
  </tbody>
</table>
</div>



### 단위

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |

</div>

- 출력결과

<div align="center">

| 결과변수 | 설명 |
| --- | --- |
| UNIT_NM | 단위 국문명 |
| UNIT_NM_ENG | 단위 영문명 |

</div>


```python
df3_6 = api.get_data(
    "통계표설명",
    "단위",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    )
df3_6.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>단위명</th>
      <th>단위영문명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>호</td>
      <td>Apartment Unit</td>
    </tr>
  </tbody>
</table>
</div>

    

### 출처

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |

</div>

- 출력결과

<div align="center">

| 결과변수 | 설명 |
| --- | --- |
| JOSA_NM | 조사명 |
| DEPT_NM | 통계표 담당부서 |
| DEPT_PHONE | 통계표 담당부서 전화번호 |

</div>


```python
df3_7 = api.get_data(
    "통계표설명",
    "출처",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    )
df3_7.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>조사명</th>
      <th>통계표담당부서</th>
      <th>통계표담당부서전화번호</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>「미분양주택현황보고」</td>
      <td>국토교통부 주택토지실 주택정책관 주택정책과</td>
      <td>044-201-3336</td>
    </tr>
  </tbody>
</table>
</div>



### 가중치

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |
| 분류코드1~분류코드8 | String | 분류코드1~분류코드8 | 선택 |
| ITEM | String | 항목 | 선택 |

</div>

- 출력결과

<div align="center">

| 결과변수 | 설명 |
| --- | --- |
| C1 ~ C8 | 분류값 ID1 ~ 분류값 ID8 |
| C1_NM ~ C8_NM | 분류값 명1 ~ 분류값 명8 |
| ITM_ID | 항목 ID |
| ITM_NM | 항목명 |
| WGT_CO | 가중치 |

</div>


```python
df3_8 = api.get_data(
    "통계표설명",
    "가중치",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    )
df3_8
```

    데이터가 존재하지 않습니다.
    

### 자료갱신일

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| orgId | String | 기관코드 | 필수 |
| tblId | String | 통계표ID | 필수 |
| prdSe | String | 수록주기 | 선택 [추가정보](https://kosis.kr/openapi/devGuide/devGuide_0601Pop.jsp?type=JSON&gubun=input)<br>(미입력 시 전체주기에 대한 데이터 출력) |

</div>

- 출력결과

<div align="center">

| 결과변수 | 설명 |
| --- | --- |
| ORG_NM | 기관명 |
| TBL_NM | 통계표명 |
| PRD_SE | 수록주기 |
| PRD_DE | 수록시점 |
| SEND_DE | 자료갱신일 |

</div>



```python
df3_9 = api.get_data(
    "통계표설명",
    "자료갱신일",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    )
df3_9.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기관명</th>
      <th>통계표명</th>
      <th>수록주기</th>
      <th>수록시점</th>
      <th>자료갱신일</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>국토교통부</td>
      <td>미분양현황_종합</td>
      <td>년</td>
      <td>2001</td>
      <td>2022-03-16</td>
    </tr>
  </tbody>
</table>
</div>

<br>

## 통계목록

- 요청변수

<div align="center">

| 요청변수 | 변수타입 | 설명 | 비고 |
| --- | --- | --- | --- |
| vwCd | String | 서비스뷰 코드<br>· MT_ZTITLE : 국내통계 주제별<br>· MT_OTITLE : 국내통계 기관별<br>· MT_GTITLE01 : e-지방지표(주제별)<br>· MT_GTITLE02 : e-지방지표(지역별)<br>· MT_CHOSUN_TITLE : 광복이전통계(1908~1943)<br>· MT_HANKUK_TITLE : 대한민국통계연감<br>· MT_STOP_TITLE : 작성중지통계<br>· MT_RTITLE : 국제통계<br>· MT_BUKHAN : 북한통계<br>· MT_TM1_TITLE : 대상별통계<br>· MT_TM2_TITLE : 이슈별통계<br>· MT_ETITLE : 영문 KOSIS | 필수 |
| parentListId | String | 시작목록 ID | 필수 |

</div>

- 출력결과

<div align="center">

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

</div>


```python
df4 = api.get_data(
    "통계목록",
    vwCd = "MT_OTITLE",
    parentListId = "110_20103",
    )
df4.head(1)
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>서비스뷰ID</th>
      <th>서비스뷰명</th>
      <th>기관ID</th>
      <th>통계표ID</th>
      <th>통계표명</th>
      <th>추천통계표여부</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>MT_OTITLE</td>
      <td>국내통계 기관별</td>
      <td>101</td>
      <td>DT_1B040B3</td>
      <td>행정구역(시군구)별 주민등록세대수</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
</div>


<br>

## 통계자료

- 요청변수

<div align="center">

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

</div>

- 출력결과

<div align="center">

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

</div>


```python
df5 = api.get_data(
    "통계자료",
    orgId = "116",
    tblId = "DT_MLTM_2086",
    itmId = "ALL",
    objL1 = "ALL",
    objL2 = "ALL",
    prdSe = "Y",
    startPrdeDe = "2021",
    endPrdDe = "2021",
    )
df5.head(1)
```



<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기관ID</th>
      <th>통계표ID</th>
      <th>통계표명</th>
      <th>분류명1</th>
      <th>분류영문명1</th>
      <th>분류값명1</th>
      <th>분류값영문명1</th>
      <th>분류값ID1</th>
      <th>분류명2</th>
      <th>분류영문명2</th>
      <th>...</th>
      <th>분류값영문명2</th>
      <th>분류값ID2</th>
      <th>항목ID</th>
      <th>항목명</th>
      <th>항목영문명</th>
      <th>단위명</th>
      <th>단위영문명</th>
      <th>수록주기</th>
      <th>수록시점</th>
      <th>수치값</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>116</td>
      <td>DT_MLTM_2086</td>
      <td>미분양현황_종합</td>
      <td>대분류</td>
      <td>Classification</td>
      <td>부문별미분양현황</td>
      <td>unsold By sector</td>
      <td>13102871014A.0001</td>
      <td>구분</td>
      <td>Classification</td>
      <td>...</td>
      <td>Total</td>
      <td>13102871014B.0001</td>
      <td>13103871014T1</td>
      <td>미분양(12월기준)</td>
      <td>Unsold Housings</td>
      <td>12월기준</td>
      <td>Apartment Unit</td>
      <td>A</td>
      <td>2021</td>
      <td>17710</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 21 columns</p>
</div>
